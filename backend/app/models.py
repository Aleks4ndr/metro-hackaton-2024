from sqlmodel import Field, Relationship, SQLModel, Column
from decimal import Decimal
from geoalchemy2 import Geometry
from pydantic import ConfigDict

from typing import List

from sqlalchemy import Numeric, DateTime, ARRAY, BigInteger, Boolean, CHAR, CheckConstraint, Column, Date, Double, ForeignKeyConstraint, Index, Integer, Numeric, PrimaryKeyConstraint, String, Table, Text, UniqueConstraint, text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from sqlalchemy.sql.sqltypes import NullType
from datetime import datetime

Base = declarative_base()
metadata = Base.metadata

# Shared properties
# TODO replace email str with EmailStr when sqlmodel supports it
class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str


# TODO replace email str with EmailStr when sqlmodel supports it
class UserRegister(SQLModel):
    email: str
    password: str
    full_name: str | None = None


# Properties to receive via API on update, all are optional
# TODO replace email str with EmailStr when sqlmodel supports it
class UserUpdate(UserBase):
    email: str | None = None  # type: ignore
    password: str | None = None


# TODO replace email str with EmailStr when sqlmodel supports it
class UserUpdateMe(SQLModel):
    full_name: str | None = None
    email: str | None = None


class UpdatePassword(SQLModel):
    current_password: str
    new_password: str


# Database model, database table inferred from class name
class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str
    items: list["Item"] = Relationship(back_populates="owner")
    comments: list["Comment"] = Relationship(back_populates="owner")


# Properties to return via API, id is always required
class UserPublic(UserBase):
    id: int


class UsersPublic(SQLModel):
    data: list[UserPublic]
    count: int


# Shared properties
class ItemBase(SQLModel):
    title: str
    description: str | None = None


# Properties to receive on item creation
class ItemCreate(ItemBase):
    title: str


# Properties to receive on item update
class ItemUpdate(ItemBase):
    title: str | None = None  # type: ignore


# Database model, database table inferred from class name
class Item(ItemBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
    owner: User | None = Relationship(back_populates="items")


# Properties to return via API, id is always required
class ItemPublic(ItemBase):
    id: int
    owner_id: int


class ItemsPublic(SQLModel):
    data: list[ItemPublic]
    count: int


# Generic message
class Message(SQLModel):
    message: str


# JSON payload containing access token
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    sub: int | None = None


class NewPassword(SQLModel):
    token: str
    new_password: str

# from pydantic import BaseModel

# class GeometryType:
#     def __init__(self, geometry_type: str):
#         self.geometry_type = geometry_type

# class GeometryModel(BaseModel):
#     geom: GeometryType

#     class Config:
#         arbitrary_types_allowed = True

class Okrug(SQLModel, table=True):
    __tablename__ = 'okrug'
    gid: int | None = Field(default=None, primary_key=True)
    name: str | None
    label: str | None
    shape_area: Decimal = Field(default=0, max_digits=10, decimal_places=2)
    geom: any = Field(sa_column = Column(sa_column=Geometry('MULTIPOLYGON')))
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
    
class Zu(SQLModel, table=True):
    __tablename__ = 'zu'

    gid: int | None = Field(default=None, primary_key=True)
    cadastra2: str | None = Field(max_length=80)
    address: str | None = Field(max_length=254)
    hasvalid5: str | None = Field(max_length=80)
    hascadas6: str | None = Field(max_length=80)
    isdraft: str | None = Field(max_length=80)
    ownershi8: str | None = Field(max_length=80)
    is_stroy: str | None = Field(max_length=80)
    # is_nonca20: Decimal | None = Field(sa_column=Numeric(10, 2))
    area: Decimal = Field(default=0, max_digits=10, decimal_places=2)
    geom: any = Field(sa_column = Column(sa_column=Geometry('MULTIPOLYGON')))
    comments: list["Comment"] = Relationship(back_populates="zu")
    
    # cadastra2: int | None 
    # address: int | None 
    # hasvalid5: int | None 
    # hascadas6: int | None 
    # isdraft: int | None 
    # ownershi8: int | None 
    # is_stroy: int | None 
    is_nonca20: Decimal = Field(default=0, max_digits=10, decimal_places=2)
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
    # geom: GeometryModel = Field(sa_column=Geometry('MULTIPOLYGON'))
    
#     class Config:
#         arbitrary_types_allowed = True
        
# class Zu(Base):
#     __tablename__ = 'zu'
#     __table_args__ = (
#         PrimaryKeyConstraint('gid', name='zu_pkey'),
#         Index('zu_geom_idx', 'geom')
#     )

#     gid = mapped_column(Integer)
#     cadastra2 = mapped_column(String(80))
#     address = mapped_column(String(254))
#     hasvalid5 = mapped_column(String(80))
#     hascadas6 = mapped_column(String(80))
#     isdraft = mapped_column(String(80))
#     ownershi8 = mapped_column(Numeric)
#     is_stroy = mapped_column(String(80))
#     is_nonca20 = mapped_column(Numeric)
#     area = mapped_column(Numeric)
#     geom = mapped_column(Geometry('MULTIPOLYGON'))

class CommentCreate(SQLModel):
    text: str 
    zu_id: int = Field(default=None, foreign_key="zu.gid", nullable=False)
     
    
class CommentPublic(CommentCreate):
    gid: int | None = Field(default=None, primary_key=True)
    date: datetime = Field(default_factory=datetime.utcnow)
    owner_id: int = Field(default=None, foreign_key="user.id", nullable=False)
    
    
class Comment(CommentPublic, table=True):
    zu: Zu = Relationship(back_populates="comments")
    owner: User = Relationship(back_populates="comments")
    
from typing import Generic, TypeVar, List, Optional
from pydantic.generics import GenericModel
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Field, Session, create_engine, select

# Define a type variable for the generic model
T = TypeVar("T")

# Define the generic response model
class PagedResponse(GenericModel, Generic[T]):
    page: int
    items: List[T]
    has_more: bool

    
class Mkd(SQLModel, table=True):
    gid: int  | None = Field(default=None, primary_key=True)
    address: str | None
    cadastra3: str | None
    shape_area: Decimal
    geom: any = Field(sa_column = Column(sa_column=Geometry('MULTIPOLYGON')))
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
    
class Oozt(SQLModel, table=True):
    gid: int  | None = Field(default=None, primary_key=True)
    status: str | None
    zoneid: str | None
    docnum: str | None
    zoneid: str | None
    docdate: str | None
    doclist: str | None
    geom: any = Field(sa_column = Column(sa_column=Geometry('MULTIPOLYGON')))
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
    
class Pp_gaz(SQLModel, table=True):
    gid: int | None = Field(default=None, primary_key=True)
    reg_num: str | None
    vid_ppt: str | None
    name: str | None
    vid_doc_ra: str | None
    num_doc_ra: str | None
    data_doc_r: str | None
    zakazchik: str | None
    ispolnitel: str | None
    istoch_fin: str | None
    otvetst_mk: str | None
    num_kontra: str | None
    data_kontr: str | None
    vid_doc_ut: str | None
    num_doc_ut: str | None
    data_doc_u: str | None
    priostanov: str | None
    zaversheni: str | None
    otmena: str | None
    status: str | None
    grup1: str | None
    grup2: str | None
    oasi: str | None
    us_ppt: str | None
    shape_area: Decimal
    geom: any = Field(sa_column = Column(sa_column=Geometry('MULTIPOLYGON')))
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
    
class Pp_metro_all(SQLModel, table=True):
    gid: int  | None = Field(default=None, primary_key=True)
    reg_num: str | None
    vid_ppt: str | None
    name: str | None
    vid_doc_ra: str | None
    num_doc_ra: str | None
    data_doc_r: str | None
    zakazchik: str | None
    ispolnitel: str | None
    istoch_fin: str | None
    otvetst_mk: str | None
    num_kontra: str | None
    data_kontr: str | None
    vid_doc_ut: str | None
    num_doc_ut: str | None
    data_doc_u: str | None
    priostanov: str | None
    zaversheni: str | None
    otmena: str | None
    status: str | None
    grup1: str | None
    grup2: str | None
    oasi: str | None
    us_ppt: str | None
    shape_area: Decimal
    geom: any = Field(sa_column = Column(sa_column=Geometry('MULTIPOLYGON')))
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
    
class Ppt_all(SQLModel, table=True):
    gid: int | None = Field(default=None, primary_key=True)
    reg_num: str | None
    vid_ppt: str | None
    name: str | None
    vid_doc_ra: str | None
    num_doc_ra: str | None
    data_doc_r: str | None
    zakazchik: str | None
    ispolnitel: str | None
    istoch_fin: str | None
    otvetst_mk: str | None
    num_kontra: str | None
    data_kontr: str | None
    vid_doc_ut: str | None
    num_doc_ut: str | None
    data_doc_u: str | None
    priostanov: str | None
    zaversheni: str | None
    otmena: str | None
    status: str | None
    grup1: str | None
    grup2: str | None
    oasi: str | None
    us_ppt: str | None
    shape_area: Decimal
    geom: any = Field(sa_column = Column(sa_column=Geometry('MULTIPOLYGON')))  
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
    
class Ppt_uds(SQLModel, table=True):
    gid: int | None = Field(default=None, primary_key=True)
    reg_num: str | None
    vid_ppt: str | None
    name: str | None
    vid_doc_ra: str | None
    num_doc_ra: str | None
    data_doc_r: str | None
    zakazchik: str | None
    ispolnitel: str | None
    istoch_fin: str | None
    otvetst_mk: str | None
    num_kontra: str | None
    data_kontr: str | None
    vid_doc_ut: str | None
    num_doc_ut: str | None
    data_doc_u: str | None
    priostanov: str | None
    zaversheni: str | None
    otmena: str | None
    status: str | None
    grup1: str | None
    grup2: str | None
    oasi: str | None
    us_ppt: str | None
    shape_area: Decimal
    geom: any = Field(sa_column = Column(sa_column=Geometry('MULTIPOLYGON')))    
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
    
class Rayon(SQLModel, table=True):
    gid: int | None = Field(default=None, primary_key=True)
    name: str | None
    shape_area: Decimal
    shape_len: Decimal
    geom: any = Field(sa_column = Column(sa_column=Geometry('MULTIPOLYGON')))
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
      
class Rsp(SQLModel, table=True):
    gid: int | None = Field(default=None, primary_key=True)
    okrug: str | None
    rayon: str | None
    address: str | None
    area: str | None
    prim: str | None
    plotnost: str | None
    vysota: str | None
    spp: str | None
    total_area: str | None
    flat_area: str | None
    osnovanie: str | None
    arg: str | None
    objectid: str | None
    geom: any = Field(sa_column = Column(sa_column=Geometry('MULTIPOLYGON')))
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
       
class SpritZones(SQLModel, table=True):
    __tablename__ = 'spritzones_2024_04_18_12_16_48'
    gid: int | None = Field(default=None, primary_key=True)
    linecode: str | None
    name: str | None
    doc: str | None
    comment: str | None
    area: Decimal
    geom: any = Field(sa_column = Column(sa_column=Geometry('MULTIPOLYGON')))
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
    
class Oks(SQLModel, table=True):
    gid: int | None = Field(default=None, primary_key=True)
    address: str
    cadastra3: str
    shape_area: Decimal
    geom: any = Field(sa_column = Column(sa_column=Geometry('MULTIPOLYGON')))
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
    
class Tpz_new(SQLModel, table=True):
    gid: int | None = Field(default=None, primary_key=True)
    podzone_nu: str | None
    num_pp: str | None
    doc_date: datetime | None
    type: str | None
    plotnost: str | None
    vysota: str | None
    proczastro: str | None
    area: Decimal | None
    geom: any = Field(sa_column = Column(sa_column=Geometry('MULTIPOLYGON'))) 
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
    
class Tz_new(SQLModel, table=True):
    gid: int | None = Field(default=None, primary_key=True)
    zone_num: str
    num_pp: str
    doc_date: datetime
    type: str | None
    index_: str | None
    area: Decimal
    geom: any = Field(sa_column = Column(sa_column=Geometry('MULTIPOLYGON')))
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
    
class Uchastrki_megevania(SQLModel, table=True):
    gid: int | None = Field(default=None, primary_key=True)
    numberarea: int
    dscr: str
    klass: str | None
    func_use: str | None
    n_kvar: str | None
    n_park: str | None
    year: str | None
    area: Decimal
    geom: any = Field(sa_column = Column(sa_column=Geometry('MULTIPOLYGON')))
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
    
class Uds_bridges(SQLModel, table=True):
    gid: int | None = Field(default=None, primary_key=True)
    vid: str | None
    name: str | None
    shape_leng: Decimal
    shape_area: Decimal
    geom: any = Field(sa_column = Column(sa_column=Geometry('MULTIPOLYGON'))) 
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
    
class Uds_roads(SQLModel, table=True):
    gid: int | None = Field(default=None, primary_key=True)
    name_str: str | None
    vid_road: str | None
    ext_name: str | None
    shape_leng: Decimal
    shape_area: Decimal
    geom: any = Field(sa_column = Column(sa_column=Geometry('MULTIPOLYGON'))) 
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
        
class Zouit(SQLModel, table=True):
    __tablename__ = 'zouit'
    gid: int | None = Field(default=None, primary_key=True)
    cad_num: str | None
    okrug: str | None
    rayon_pos: str | None
    vid_zouit: str | None
    type_zone: str | None
    name: str | None
    organ: str | None
    doc: str | None
    shape_leng: Decimal
    shape_area: Decimal
    geom: any = Field(sa_column = Column(sa_column=Geometry('MULTIPOLYGON'))) 
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
           
class ZuDetails(SQLModel):
    zu: Zu
    okrug: List[Okrug]
    mkd: List[Mkd]
    oozt: List[Oozt]
    pp_metro_allkrug: List[Pp_metro_all]
    ppt_all: List[Ppt_all]
    ppt_uds: List[Ppt_uds]
    spritzones: List[SpritZones]
    oks: List[Oks]
    tpz_new: List[Tpz_new]
    uchastrki_megevania: List[Uchastrki_megevania]
    uds_bridges: List[Uds_bridges]
    uds_roads: List[Uds_roads]

    
    