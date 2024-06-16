from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import Zu, Message, PagedResponse, Okrug, Mkd, Oozt, Pp_gaz, Pp_metro_all, Ppt_all, Ppt_uds, Rayon, Rsp, SpritZones, Ppt_uds, Oks, Tpz_new, Tz_new, Uchastrki_megevania, Uds_bridges, Uds_roads, Zouit
from math import ceil 

router = APIRouter()


@router.get("/", response_model=PagedResponse[Zu])
def read_zu(
    session: SessionDep, 
    # current_user: CurrentUser, 
    page: int = 0, page_size: int = 100
) -> Any:
    """
    Retrieve ZU.
    """

    # if current_user.is_superuser:
    count_statement = select(func.count()).select_from(Zu)
    count = session.exec(count_statement).one()
    pages_count = ceil(count / page_size)
    statement = select(Zu).offset(page * page_size).limit(page_size)
    items = session.exec(statement).all()
    # else:
    #     count_statement = (
    #         select(func.count())
    #         .select_from(Zu)
    #         .where(Zu.owner_id == current_user.id)
    #     )
    #     count = session.exec(count_statement).one()
    #     statement = (
    #         select(Zu)
    #         .where(Zu.owner_id == current_user.id)
    #         .offset(skip)
    #         .limit(limit)
    #     )
    #     items = session.exec(statement).all()
    has_more = page < pages_count
    return PagedResponse(page=page, items=items, has_more=has_more)


@router.get("/{id}", response_model=Zu)
def read_item(session: SessionDep, current_user: CurrentUser, id: int) -> Any:
    """
    Get item by ID.
    """
    
    statement = select(Zu).offset(10).limit(3)
    
    item = session.get(Zu, id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not current_user.is_superuser and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return item


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
