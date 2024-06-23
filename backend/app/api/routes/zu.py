from typing import Any, Annotated, List, Union

from fastapi import APIRouter, HTTPException, Query
from sqlmodel import func, select, text

from app.api.deps import CurrentUser, SessionDep
from app.models import Zu, ZuDetails, Message, PagedResponse, Okrug, Mkd, Oozt, Pp_gaz, Pp_metro_all, Ppt_all, Ppt_uds, Rayon, Rsp, SpritZones, Oks, Tpz_new, Tz_new, Uchastrki_megevania, Uds_bridges, Uds_roads, Zouit
from math import ceil 

import uuid

router = APIRouter()


@router.get("/", response_model=PagedResponse[Zu])
def read_zu(
    session: SessionDep, 
    areaFrom: float | None = None,
    areaTo: float | None = None,
    rectangleWidth: float | None = None,
    rectangleHeight: float | None = None,
    vri: Annotated[List[str], Query()] = None,
    okrug: Annotated[List[int], Query()] = None,
    rayon: Annotated[List[int], Query()] = None,
    offset: int = 0,
    limit: int = 100
    # current_user: CurrentUser, 
    # page: int = 0, page_size: int = 100
) -> Any:
    """
    Retrieve ZU.
    """
    
    # base_query = "SELECT DISTINCT zu.gid, zu.cadastra2, zu.address, zu.hasvalid5, zu.hascadas6, zu.isdraft, zu.ownershi8, zu.is_stroy, zu.area, zu.geom FROM zu"
    
    unique_table_name = f"temp_zu_{uuid.uuid4().hex}"
    
    base_query = f"""
    CREATE TEMPORARY TABLE {unique_table_name} AS
    SELECT DISTINCT zu.gid, zu.cadastra2, zu.address, zu.hasvalid5, zu.hascadas6, 
                    zu.isdraft, zu.ownershi8, zu.is_stroy, zu.area, zu.geom 
    FROM zu
    """
    
    joins = ""
    conditions = " WHERE 1=1"
    parameters = {}
    
    if areaFrom is not None:
        conditions += " AND zu.area >= :areaFrom"
        parameters['areaFrom'] = areaFrom
    if areaTo is not None:
        conditions += " AND zu.area <= :areaTo"
        parameters['areaTo'] = areaTo
    if okrug is not None:
        joins += " join zu_okrug on zu.gid = zu_okrug.zu_gid "
        conditions += " AND zu_okrug.okrug_gid = ANY(:okrug)"
        parameters['okrug'] = list(okrug)
    if rayon is not None:
        joins += " join zu_rayon on zu.gid = zu_rayon.zu_gid "
        conditions += " AND zu_rayon.rayon_gid = ANY(:rayon)"
        parameters['rayon'] = list(rayon)
    if vri is not None:
        joins += " join zu_tz on zu.gid = zu_tz.zu_gid join tz_vri on zu_tz.tz_gid = tz_vri.tz_gid "
        conditions += " AND tz_vri.vri_540 = ANY(:vri)"
        parameters['vri'] = list(vri)
    
    
    
    temp_table_query = f"""
    {base_query} {joins} {conditions} ORDER BY zu.gid;
    """
    
    data_query = f"""
    SELECT * FROM {unique_table_name}
    ORDER BY gid
    LIMIT :limit OFFSET :offset;
    """
    
    count_query = f"""
    SELECT COUNT(*) AS total_count FROM {unique_table_name};
    """
    
    drop_temp_table_query = f"""
    DROP TABLE {unique_table_name};
    """
    
    final_query = f"""
    {temp_table_query}
    {data_query}
    {count_query}
    {drop_temp_table_query}
    """
    
    parameters['limit'] = limit
    parameters['offset'] = offset
    
    # result = session.execute(text(final_query), parameters)
    
    # Begin a transaction
    with session.begin():
        # Execute the create temporary table query
        session.execute(text(temp_table_query), parameters)
        
        # Execute the data query
        result = session.execute(text(data_query), parameters)
        rows = result.all()
        
        # Execute the count query
        count_result = session.execute(text(count_query), parameters)
        total_count = count_result.scalar()
        
        # Execute the drop temporary table query
        # session.execute(text(drop_temp_table_query))
        session.rollback()
    

    # total_count = count_row['total_count']
    keys = result.keys()
    records = [dict(zip(keys, row)) for row in rows]
    
    # Transform dictionaries to list of Zu models
    zu_list = [Zu(**record) for record in records]
    
    # Determine if there are more results
    more_results = offset + limit < total_count
    
    return PagedResponse(items=zu_list, has_more=more_results)

@router.get("/{id}", response_model=ZuDetails)
def read_item(
    session: SessionDep, 
    # current_user: CurrentUser, 
    id: int) -> Any:
    """
    Get item by ID.
    """
    
    zu = session.get(Zu, id)
    
    return ZuDetails(
        zu = zu,
        okrug = run_query("okrug", Okrug, session, id),
        mkd = run_query("mkd", Okrug, session, id)
    )
        
        

    
    query_template = "select t.* from {table} t join zu_{table} zt on t.gid = zt.{table}_gid where zt.zu_gid = :id"
    
    # krt_query = "select krt.* from krt join zu_krt on krt.gid = zu_rkt.krt_gid where zu_krt.zu_gid = :id"
    krt_query = query_template.format(table = "krt")
    
    
def run_query(table, type, session, id):
    query = "select t.* from {table} t join zu_{table} zt on t.gid = zt.{table}_gid where zt.zu_gid = :id".format(table = table)
    result = session.execute(text(query), {"id": id})
    rows = result.all()
    keys = result.keys()
    records = [dict(zip(keys, row)) for row in rows]
    data = [type(**record) for record in records]
    return data
    
    
   


# @router.post("/", response_model=ItemPublic)
# def create_item(
#     *, session: SessionDep, current_user: CurrentUser, item_in: ItemCreate
# ) -> Any:
#     """
#     Create new item.
#     """
#     item = Item.model_validate(item_in, update={"owner_id": current_user.id})
#     session.add(item)
#     session.commit()
#     session.refresh(item)
#     return item


# @router.put("/{id}", response_model=ItemPublic)
# def update_item(
#     *, session: SessionDep, current_user: CurrentUser, id: int, item_in: ItemUpdate
# ) -> Any:
#     """
#     Update an item.
#     """
#     item = session.get(Item, id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not current_user.is_superuser and (item.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     update_dict = item_in.model_dump(exclude_unset=True)
#     item.sqlmodel_update(update_dict)
#     session.add(item)
#     session.commit()
#     session.refresh(item)
#     return item


# @router.delete("/{id}")
# def delete_item(session: SessionDep, current_user: CurrentUser, id: int) -> Message:
#     """
#     Delete an item.
#     """
#     item = session.get(Item, id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not current_user.is_superuser and (item.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     session.delete(item)
#     session.commit()
#     return Message(message="Item deleted successfully")
