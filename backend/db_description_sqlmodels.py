from datetime import date
from decimal import Decimal
from typing import Any, List, Optional

from sqlalchemy import ARRAY, BigInteger, Boolean, CHAR, CheckConstraint, Column, Date, Double, ForeignKeyConstraint, Index, Integer, Numeric, PrimaryKeyConstraint, String, Table, Text, UniqueConstraint, text
from sqlalchemy.orm.base import Mapped
from sqlalchemy.sql.sqltypes import NullType
from sqlmodel import Field, Relationship, SQLModel

from geoalchemy2 import Geometry

metadata = SQLModel.metadata

class KadastrDelenie(SQLModel, table=True):
    __tablename__ = 'kadastr_delenie'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='kadastr_delenie_pkey'),
        Index('kadastr_delenie_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    cadastra1: Optional[str] = Field(default=None, sa_column=mapped_column('cadastra1', String(80)))
    objectid: Optional[str] = Field(default=None, sa_column=mapped_column('objectid', String(80)))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


class Krt(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='krt_pkey'),
        Index('krt_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    name: Optional[str] = Field(default=None, sa_column=mapped_column('name', String(254)))
    area_krt: Optional[Decimal] = Field(default=None, sa_column=mapped_column('area_krt', Numeric))
    type_krt: Optional[str] = Field(default=None, sa_column=mapped_column('type_krt', String(80)))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


class KvartalRegion(SQLModel, table=True):
    __tablename__ = 'kvartal_region'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='kvartal_region_pkey'),
        Index('kvartal_region_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    objectid: Optional[float] = Field(default=None, sa_column=mapped_column('objectid', Double(53)))
    num_doc_ut: Optional[str] = Field(default=None, sa_column=mapped_column('num_doc_ut', String(20)))
    data_doc_u: Optional[date] = Field(default=None, sa_column=mapped_column('data_doc_u', Date))
    name_ppt: Optional[str] = Field(default=None, sa_column=mapped_column('name_ppt', String(254)))
    okrug: Optional[str] = Field(default=None, sa_column=mapped_column('okrug', String(10)))
    rayon: Optional[str] = Field(default=None, sa_column=mapped_column('rayon', String(254)))
    area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('area', Numeric))
    prim: Optional[str] = Field(default=None, sa_column=mapped_column('prim', String(254)))
    uslov: Optional[int] = Field(default=None, sa_column=mapped_column('uslov', Integer))
    db2gse_st_: Optional[Decimal] = Field(default=None, sa_column=mapped_column('db2gse_st_', Numeric))
    db2gse_sde: Optional[Decimal] = Field(default=None, sa_column=mapped_column('db2gse_sde', Numeric))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))

class Mkd(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='mkd_pkey'),
        Index('mkd_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    unom: Optional[Decimal] = Field(default=None, sa_column=mapped_column('unom', Numeric))
    address: Optional[str] = Field(default=None, sa_column=mapped_column('address', String(254)))
    cadastra3: Optional[str] = Field(default=None, sa_column=mapped_column('cadastra3', String(80)))
    hascadas4: Optional[str] = Field(default=None, sa_column=mapped_column('hascadas4', String(80)))
    hasbti: Optional[str] = Field(default=None, sa_column=mapped_column('hasbti', String(80)))
    hascontr6: Optional[Decimal] = Field(default=None, sa_column=mapped_column('hascontr6', Numeric))
    hasownrf: Optional[str] = Field(default=None, sa_column=mapped_column('hasownrf', String(80)))
    hasownmo8: Optional[str] = Field(default=None, sa_column=mapped_column('hasownmo8', String(80)))
    hasownot9: Optional[str] = Field(default=None, sa_column=mapped_column('hasownot9', String(80)))
    shape_area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('shape_area', Numeric))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


class Okrug(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='okrug_pkey'),
        Index('okrug_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    objectid: Optional[float] = Field(default=None, sa_column=mapped_column('objectid', Double(53)))
    uidnftn: Optional[float] = Field(default=None, sa_column=mapped_column('uidnftn', Double(53)))
    name: Optional[str] = Field(default=None, sa_column=mapped_column('name', String(254)))
    label: Optional[str] = Field(default=None, sa_column=mapped_column('label', String(254)))
    address: Optional[str] = Field(default=None, sa_column=mapped_column('address', String(254)))
    x: Optional[Decimal] = Field(default=None, sa_column=mapped_column('x', Numeric))
    y: Optional[Decimal] = Field(default=None, sa_column=mapped_column('y', Numeric))
    bui_no_bti: Optional[float] = Field(default=None, sa_column=mapped_column('bui_no_bti', Double(53)))
    cad_no: Optional[str] = Field(default=None, sa_column=mapped_column('cad_no', String(254)))
    street_bti: Optional[str] = Field(default=None, sa_column=mapped_column('street_bti', String(254)))
    house_bti: Optional[str] = Field(default=None, sa_column=mapped_column('house_bti', String(254)))
    hadd_bti: Optional[str] = Field(default=None, sa_column=mapped_column('hadd_bti', String(254)))
    moddate: Optional[date] = Field(default=None, sa_column=mapped_column('moddate', Date))
    moduser: Optional[str] = Field(default=None, sa_column=mapped_column('moduser', String(100)))
    torzid: Optional[Decimal] = Field(default=None, sa_column=mapped_column('torzid', Numeric))
    exclude_gr: Optional[Decimal] = Field(default=None, sa_column=mapped_column('exclude_gr', Numeric))
    shape_area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('shape_area', Numeric))
    shape_len: Optional[Decimal] = Field(default=None, sa_column=mapped_column('shape_len', Numeric))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


class Oks(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='oks_pkey'),
        Index('oks_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    unom: Optional[Decimal] = Field(default=None, sa_column=mapped_column('unom', Numeric))
    address: Optional[str] = Field(default=None, sa_column=mapped_column('address', String(254)))
    cadastra3: Optional[str] = Field(default=None, sa_column=mapped_column('cadastra3', String(80)))
    hascadas4: Optional[str] = Field(default=None, sa_column=mapped_column('hascadas4', String(80)))
    hasbti: Optional[str] = Field(default=None, sa_column=mapped_column('hasbti', String(80)))
    hascontr6: Optional[Decimal] = Field(default=None, sa_column=mapped_column('hascontr6', Numeric))
    hasownrf: Optional[str] = Field(default=None, sa_column=mapped_column('hasownrf', String(80)))
    hasownmo8: Optional[str] = Field(default=None, sa_column=mapped_column('hasownmo8', String(80)))
    hasownot9: Optional[str] = Field(default=None, sa_column=mapped_column('hasownot9', String(80)))
    shape_area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('shape_area', Numeric))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


class Oozt(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='oozt_pkey'),
        Index('oozt_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    objectid: Optional[str] = Field(default=None, sa_column=mapped_column('objectid', String(80)))
    status: Optional[str] = Field(default=None, sa_column=mapped_column('status', String(80)))
    zoneid: Optional[str] = Field(default=None, sa_column=mapped_column('zoneid', String(80)))
    docnum: Optional[str] = Field(default=None, sa_column=mapped_column('docnum', String(80)))
    docdate: Optional[str] = Field(default=None, sa_column=mapped_column('docdate', String(80)))
    doclist: Optional[str] = Field(default=None, sa_column=mapped_column('doclist', String(254)))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


class PagcGaz(SQLModel, table=True):
    __tablename__ = 'pagc_gaz'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pagc_gaz_pkey'),
    )

    id: Optional[int] = Field(default=None, sa_column=mapped_column('id', Integer))
    is_custom: bool = Field(sa_column=mapped_column('is_custom', Boolean, nullable=False, server_default=text('true')))
    seq: Optional[int] = Field(default=None, sa_column=mapped_column('seq', Integer))
    word: Optional[str] = Field(default=None, sa_column=mapped_column('word', Text))
    stdword: Optional[str] = Field(default=None, sa_column=mapped_column('stdword', Text))
    token: Optional[int] = Field(default=None, sa_column=mapped_column('token', Integer))


class PagcLex(SQLModel, table=True):
    __tablename__ = 'pagc_lex'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pagc_lex_pkey'),
    )

    id: Optional[int] = Field(default=None, sa_column=mapped_column('id', Integer))
    is_custom: bool = Field(sa_column=mapped_column('is_custom', Boolean, nullable=False, server_default=text('true')))
    seq: Optional[int] = Field(default=None, sa_column=mapped_column('seq', Integer))
    word: Optional[str] = Field(default=None, sa_column=mapped_column('word', Text))
    stdword: Optional[str] = Field(default=None, sa_column=mapped_column('stdword', Text))
    token: Optional[int] = Field(default=None, sa_column=mapped_column('token', Integer))


class PagcRules(SQLModel, table=True):
    __tablename__ = 'pagc_rules'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pagc_rules_pkey'),
    )

    id: Optional[int] = Field(default=None, sa_column=mapped_column('id', Integer))
    rule: Optional[str] = Field(default=None, sa_column=mapped_column('rule', Text))
    is_custom: Optional[bool] = Field(default=None, sa_column=mapped_column('is_custom', Boolean, server_default=text('true')))


class Place(SQLModel, table=True):
    __table_args__ = (
        CheckConstraint("geometrytype(the_geom) = 'MULTIPOLYGON'::text OR the_geom IS NULL", name='enforce_geotype_the_geom'),
        CheckConstraint('st_ndims(the_geom) = 2', name='enforce_dims_the_geom'),
        CheckConstraint('st_srid(the_geom) = 4269', name='enforce_srid_the_geom'),
        PrimaryKeyConstraint('plcidfp', name='place_pkey'),
        UniqueConstraint('gid', name='uidx_tiger_place_gid'),
        Index('tiger_place_the_geom_gist', 'the_geom')
    )

    gid: int = Field(sa_column=mapped_column('gid', Integer, nullable=False))
    plcidfp: str = Field(sa_column=mapped_column('plcidfp', String(7)))
    statefp: Optional[str] = Field(default=None, sa_column=mapped_column('statefp', String(2)))
    placefp: Optional[str] = Field(default=None, sa_column=mapped_column('placefp', String(5)))
    placens: Optional[str] = Field(default=None, sa_column=mapped_column('placens', String(8)))
    name: Optional[str] = Field(default=None, sa_column=mapped_column('name', String(100)))
    namelsad: Optional[str] = Field(default=None, sa_column=mapped_column('namelsad', String(100)))
    lsad: Optional[str] = Field(default=None, sa_column=mapped_column('lsad', String(2)))
    classfp: Optional[str] = Field(default=None, sa_column=mapped_column('classfp', String(2)))
    cpi: Optional[str] = Field(default=None, sa_column=mapped_column('cpi', String(1)))
    pcicbsa: Optional[str] = Field(default=None, sa_column=mapped_column('pcicbsa', String(1)))
    pcinecta: Optional[str] = Field(default=None, sa_column=mapped_column('pcinecta', String(1)))
    mtfcc: Optional[str] = Field(default=None, sa_column=mapped_column('mtfcc', String(5)))
    funcstat: Optional[str] = Field(default=None, sa_column=mapped_column('funcstat', String(1)))
    aland: Optional[int] = Field(default=None, sa_column=mapped_column('aland', BigInteger))
    awater: Optional[int] = Field(default=None, sa_column=mapped_column('awater', BigInteger))
    intptlat: Optional[str] = Field(default=None, sa_column=mapped_column('intptlat', String(11)))
    intptlon: Optional[str] = Field(default=None, sa_column=mapped_column('intptlon', String(12)))
    the_geom: Optional[Any] = Field(default=None, sa_column=mapped_column('the_geom', NullType))


class PlaceLookup(SQLModel, table=True):
    __tablename__ = 'place_lookup'
    __table_args__ = (
        PrimaryKeyConstraint('st_code', 'pl_code', name='place_lookup_pkey'),
        Index('place_lookup_name_idx'),
        Index('place_lookup_state_idx', 'state')
    )

    st_code: int = Field(sa_column=mapped_column('st_code', Integer, nullable=False))
    pl_code: int = Field(sa_column=mapped_column('pl_code', Integer, nullable=False))
    state: Optional[str] = Field(default=None, sa_column=mapped_column('state', String(2)))
    name: Optional[str] = Field(default=None, sa_column=mapped_column('name', String(90)))


class PpGaz(SQLModel, table=True):
    __tablename__ = 'pp_gaz'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='pp_gaz_pkey'),
        Index('pp_gaz_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    reg_num: Optional[str] = Field(default=None, sa_column=mapped_column('reg_num', String(10)))
    vid_ppt: Optional[str] = Field(default=None, sa_column=mapped_column('vid_ppt', String(100)))
    name: Optional[str] = Field(default=None, sa_column=mapped_column('name', String(254)))
    vid_doc_ra: Optional[str] = Field(default=None, sa_column=mapped_column('vid_doc_ra', String(100)))
    num_doc_ra: Optional[str] = Field(default=None, sa_column=mapped_column('num_doc_ra', String(100)))
    data_doc_r: Optional[date] = Field(default=None, sa_column=mapped_column('data_doc_r', Date))
    zakazchik: Optional[str] = Field(default=None, sa_column=mapped_column('zakazchik', String(100)))
    ispolnitel: Optional[str] = Field(default=None, sa_column=mapped_column('ispolnitel', String(100)))
    istoch_fin: Optional[str] = Field(default=None, sa_column=mapped_column('istoch_fin', String(100)))
    otvetst_mk: Optional[str] = Field(default=None, sa_column=mapped_column('otvetst_mk', String(50)))
    num_kontra: Optional[str] = Field(default=None, sa_column=mapped_column('num_kontra', String(50)))
    data_kontr: Optional[date] = Field(default=None, sa_column=mapped_column('data_kontr', Date))
    vid_doc_ut: Optional[str] = Field(default=None, sa_column=mapped_column('vid_doc_ut', String(100)))
    num_doc_ut: Optional[str] = Field(default=None, sa_column=mapped_column('num_doc_ut', String(50)))
    data_doc_u: Optional[date] = Field(default=None, sa_column=mapped_column('data_doc_u', Date))
    priostanov: Optional[str] = Field(default=None, sa_column=mapped_column('priostanov', String(100)))
    zaversheni: Optional[str] = Field(default=None, sa_column=mapped_column('zaversheni', String(100)))
    otmena: Optional[str] = Field(default=None, sa_column=mapped_column('otmena', String(100)))
    status: Optional[str] = Field(default=None, sa_column=mapped_column('status', String(50)))
    grup1: Optional[str] = Field(default=None, sa_column=mapped_column('grup1', String(100)))
    grup2: Optional[str] = Field(default=None, sa_column=mapped_column('grup2', String(100)))
    oasi: Optional[str] = Field(default=None, sa_column=mapped_column('oasi', String(20)))
    us_ppt: Optional[str] = Field(default=None, sa_column=mapped_column('us_ppt', String(10)))
    shape_area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('shape_area', Numeric))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


class PpMetroAll(SQLModel, table=True):
    __tablename__ = 'pp_metro_all'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='pp_metro_all_pkey'),
        Index('pp_metro_all_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    reg_num: Optional[str] = Field(default=None, sa_column=mapped_column('reg_num', String(10)))
    vid_ppt: Optional[str] = Field(default=None, sa_column=mapped_column('vid_ppt', String(100)))
    name: Optional[str] = Field(default=None, sa_column=mapped_column('name', String(254)))
    vid_doc_ra: Optional[str] = Field(default=None, sa_column=mapped_column('vid_doc_ra', String(100)))
    num_doc_ra: Optional[str] = Field(default=None, sa_column=mapped_column('num_doc_ra', String(100)))
    data_doc_r: Optional[date] = Field(default=None, sa_column=mapped_column('data_doc_r', Date))
    zakazchik: Optional[str] = Field(default=None, sa_column=mapped_column('zakazchik', String(100)))
    ispolnitel: Optional[str] = Field(default=None, sa_column=mapped_column('ispolnitel', String(100)))
    istoch_fin: Optional[str] = Field(default=None, sa_column=mapped_column('istoch_fin', String(100)))
    otvetst_mk: Optional[str] = Field(default=None, sa_column=mapped_column('otvetst_mk', String(50)))
    num_kontra: Optional[str] = Field(default=None, sa_column=mapped_column('num_kontra', String(50)))
    data_kontr: Optional[date] = Field(default=None, sa_column=mapped_column('data_kontr', Date))
    vid_doc_ut: Optional[str] = Field(default=None, sa_column=mapped_column('vid_doc_ut', String(100)))
    num_doc_ut: Optional[str] = Field(default=None, sa_column=mapped_column('num_doc_ut', String(50)))
    data_doc_u: Optional[date] = Field(default=None, sa_column=mapped_column('data_doc_u', Date))
    priostanov: Optional[str] = Field(default=None, sa_column=mapped_column('priostanov', String(100)))
    zaversheni: Optional[str] = Field(default=None, sa_column=mapped_column('zaversheni', String(100)))
    otmena: Optional[str] = Field(default=None, sa_column=mapped_column('otmena', String(100)))
    status: Optional[str] = Field(default=None, sa_column=mapped_column('status', String(50)))
    grup1: Optional[str] = Field(default=None, sa_column=mapped_column('grup1', String(100)))
    grup2: Optional[str] = Field(default=None, sa_column=mapped_column('grup2', String(100)))
    oasi: Optional[str] = Field(default=None, sa_column=mapped_column('oasi', String(20)))
    us_ppt: Optional[str] = Field(default=None, sa_column=mapped_column('us_ppt', String(10)))
    shape_area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('shape_area', Numeric))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


class PptAll(SQLModel, table=True):
    __tablename__ = 'ppt_all'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='ppt_all_pkey'),
        Index('ppt_all_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    reg_num: Optional[str] = Field(default=None, sa_column=mapped_column('reg_num', String(10)))
    vid_ppt: Optional[str] = Field(default=None, sa_column=mapped_column('vid_ppt', String(100)))
    name: Optional[str] = Field(default=None, sa_column=mapped_column('name', String(254)))
    vid_doc_ra: Optional[str] = Field(default=None, sa_column=mapped_column('vid_doc_ra', String(100)))
    num_doc_ra: Optional[str] = Field(default=None, sa_column=mapped_column('num_doc_ra', String(50)))
    data_doc_r: Optional[date] = Field(default=None, sa_column=mapped_column('data_doc_r', Date))
    zakazchik: Optional[str] = Field(default=None, sa_column=mapped_column('zakazchik', String(100)))
    ispolnitel: Optional[str] = Field(default=None, sa_column=mapped_column('ispolnitel', String(100)))
    istoch_fin: Optional[str] = Field(default=None, sa_column=mapped_column('istoch_fin', String(100)))
    otvetst_mk: Optional[str] = Field(default=None, sa_column=mapped_column('otvetst_mk', String(50)))
    num_kontra: Optional[str] = Field(default=None, sa_column=mapped_column('num_kontra', String(50)))
    data_kontr: Optional[date] = Field(default=None, sa_column=mapped_column('data_kontr', Date))
    vid_doc_ut: Optional[str] = Field(default=None, sa_column=mapped_column('vid_doc_ut', String(100)))
    num_doc_ut: Optional[str] = Field(default=None, sa_column=mapped_column('num_doc_ut', String(50)))
    data_doc_u: Optional[date] = Field(default=None, sa_column=mapped_column('data_doc_u', Date))
    priostanov: Optional[str] = Field(default=None, sa_column=mapped_column('priostanov', String(100)))
    zaversheni: Optional[str] = Field(default=None, sa_column=mapped_column('zaversheni', String(100)))
    otmena: Optional[str] = Field(default=None, sa_column=mapped_column('otmena', String(100)))
    status: Optional[str] = Field(default=None, sa_column=mapped_column('status', String(40)))
    grup1: Optional[str] = Field(default=None, sa_column=mapped_column('grup1', String(100)))
    grup2: Optional[str] = Field(default=None, sa_column=mapped_column('grup2', String(100)))
    oasi: Optional[str] = Field(default=None, sa_column=mapped_column('oasi', String(20)))
    us_ppt: Optional[str] = Field(default=None, sa_column=mapped_column('us_ppt', String(10)))
    sppgns_obs: Optional[str] = Field(default=None, sa_column=mapped_column('sppgns_obs', String(100)))
    sppgns_jil: Optional[str] = Field(default=None, sa_column=mapped_column('sppgns_jil', String(100)))
    sppgns_nej: Optional[str] = Field(default=None, sa_column=mapped_column('sppgns_nej', String(100)))
    shape_area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('shape_area', Numeric))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


class PptUds(SQLModel, table=True):
    __tablename__ = 'ppt_uds'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='ppt_uds_pkey'),
        Index('ppt_uds_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    reg_num: Optional[str] = Field(default=None, sa_column=mapped_column('reg_num', String(10)))
    vid_ppt: Optional[str] = Field(default=None, sa_column=mapped_column('vid_ppt', String(100)))
    name: Optional[str] = Field(default=None, sa_column=mapped_column('name', String(254)))
    vid_doc_ra: Optional[str] = Field(default=None, sa_column=mapped_column('vid_doc_ra', String(100)))
    num_doc_ra: Optional[str] = Field(default=None, sa_column=mapped_column('num_doc_ra', String(100)))
    data_doc_r: Optional[date] = Field(default=None, sa_column=mapped_column('data_doc_r', Date))
    zakazchik: Optional[str] = Field(default=None, sa_column=mapped_column('zakazchik', String(100)))
    ispolnitel: Optional[str] = Field(default=None, sa_column=mapped_column('ispolnitel', String(100)))
    istoch_fin: Optional[str] = Field(default=None, sa_column=mapped_column('istoch_fin', String(100)))
    otvetst_mk: Optional[str] = Field(default=None, sa_column=mapped_column('otvetst_mk', String(50)))
    num_kontra: Optional[str] = Field(default=None, sa_column=mapped_column('num_kontra', String(50)))
    data_kontr: Optional[date] = Field(default=None, sa_column=mapped_column('data_kontr', Date))
    vid_doc_ut: Optional[str] = Field(default=None, sa_column=mapped_column('vid_doc_ut', String(100)))
    num_doc_ut: Optional[str] = Field(default=None, sa_column=mapped_column('num_doc_ut', String(50)))
    data_doc_u: Optional[date] = Field(default=None, sa_column=mapped_column('data_doc_u', Date))
    priostanov: Optional[str] = Field(default=None, sa_column=mapped_column('priostanov', String(100)))
    zaversheni: Optional[str] = Field(default=None, sa_column=mapped_column('zaversheni', String(100)))
    otmena: Optional[str] = Field(default=None, sa_column=mapped_column('otmena', String(100)))
    status: Optional[str] = Field(default=None, sa_column=mapped_column('status', String(50)))
    grup1: Optional[str] = Field(default=None, sa_column=mapped_column('grup1', String(100)))
    grup2: Optional[str] = Field(default=None, sa_column=mapped_column('grup2', String(100)))
    oasi: Optional[str] = Field(default=None, sa_column=mapped_column('oasi', String(20)))
    us_ppt: Optional[str] = Field(default=None, sa_column=mapped_column('us_ppt', String(10)))
    shape_area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('shape_area', Numeric))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


class Rayon(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='rayon_pkey'),
        Index('rayon_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    objectid: Optional[float] = Field(default=None, sa_column=mapped_column('objectid', Double(53)))
    uidnftn: Optional[float] = Field(default=None, sa_column=mapped_column('uidnftn', Double(53)))
    name: Optional[str] = Field(default=None, sa_column=mapped_column('name', String(254)))
    label: Optional[str] = Field(default=None, sa_column=mapped_column('label', String(254)))
    address: Optional[str] = Field(default=None, sa_column=mapped_column('address', String(254)))
    x: Optional[Decimal] = Field(default=None, sa_column=mapped_column('x', Numeric))
    y: Optional[Decimal] = Field(default=None, sa_column=mapped_column('y', Numeric))
    bui_no_bti: Optional[float] = Field(default=None, sa_column=mapped_column('bui_no_bti', Double(53)))
    cad_no: Optional[str] = Field(default=None, sa_column=mapped_column('cad_no', String(254)))
    street_bti: Optional[str] = Field(default=None, sa_column=mapped_column('street_bti', String(254)))
    house_bti: Optional[str] = Field(default=None, sa_column=mapped_column('house_bti', String(254)))
    hadd_bti: Optional[str] = Field(default=None, sa_column=mapped_column('hadd_bti', String(254)))
    mun_obr: Optional[str] = Field(default=None, sa_column=mapped_column('mun_obr', String(200)))
    moddate: Optional[date] = Field(default=None, sa_column=mapped_column('moddate', Date))
    moduser: Optional[str] = Field(default=None, sa_column=mapped_column('moduser', String(100)))
    exclude_gr: Optional[Decimal] = Field(default=None, sa_column=mapped_column('exclude_gr', Numeric))
    shape_area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('shape_area', Numeric))
    shape_len: Optional[Decimal] = Field(default=None, sa_column=mapped_column('shape_len', Numeric))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


class Rsp(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='rsp_pkey'),
        Index('rsp_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    okrug: Optional[str] = Field(default=None, sa_column=mapped_column('okrug', String(80)))
    rayon: Optional[str] = Field(default=None, sa_column=mapped_column('rayon', String(80)))
    address: Optional[str] = Field(default=None, sa_column=mapped_column('address', String(254)))
    area: Optional[str] = Field(default=None, sa_column=mapped_column('area', String(80)))
    prim: Optional[str] = Field(default=None, sa_column=mapped_column('prim', String(115)))
    plotnost: Optional[str] = Field(default=None, sa_column=mapped_column('plotnost', String(80)))
    vysota: Optional[str] = Field(default=None, sa_column=mapped_column('vysota', String(80)))
    spp: Optional[str] = Field(default=None, sa_column=mapped_column('spp', String(80)))
    total_area: Optional[str] = Field(default=None, sa_column=mapped_column('total_area', String(80)))
    flat_area: Optional[str] = Field(default=None, sa_column=mapped_column('flat_area', String(80)))
    osnovanie: Optional[str] = Field(default=None, sa_column=mapped_column('osnovanie', String(254)))
    agr: Optional[str] = Field(default=None, sa_column=mapped_column('agr', String(254)))
    objectid: Optional[str] = Field(default=None, sa_column=mapped_column('objectid', String(80)))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


class Spritzones20240418121648(SQLModel, table=True):
    __tablename__ = 'spritzones_2024_04_18_12_16_48'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='spritzones_2024_04_18_12_16_48_pkey'),
        Index('spritzones_2024_04_18_12_16_48_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    linecode: Optional[str] = Field(default=None, sa_column=mapped_column('linecode', String(254)))
    name: Optional[str] = Field(default=None, sa_column=mapped_column('name', String(254)))
    doc: Optional[str] = Field(default=None, sa_column=mapped_column('doc', String(254)))
    comment: Optional[str] = Field(default=None, sa_column=mapped_column('comment', String(254)))
    area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('area', Numeric))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))

class TpuRvMetroPolygon(SQLModel, table=True):
    __tablename__ = 'tpu_rv_metro_polygon'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='tpu_rv_metro_polygon_pkey'),
        Index('tpu_rv_metro_polygon_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    reg_num: Optional[str] = Field(default=None, sa_column=mapped_column('reg_num', String(10)))
    vid_ppt: Optional[str] = Field(default=None, sa_column=mapped_column('vid_ppt', String(100)))
    name: Optional[str] = Field(default=None, sa_column=mapped_column('name', String(254)))
    vid_doc_ra: Optional[str] = Field(default=None, sa_column=mapped_column('vid_doc_ra', String(100)))
    num_doc_ra: Optional[str] = Field(default=None, sa_column=mapped_column('num_doc_ra', String(100)))
    data_doc_r: Optional[date] = Field(default=None, sa_column=mapped_column('data_doc_r', Date))
    zakazchik: Optional[str] = Field(default=None, sa_column=mapped_column('zakazchik', String(100)))
    ispolnitel: Optional[str] = Field(default=None, sa_column=mapped_column('ispolnitel', String(100)))
    istoch_fin: Optional[str] = Field(default=None, sa_column=mapped_column('istoch_fin', String(100)))
    otvetst_mk: Optional[str] = Field(default=None, sa_column=mapped_column('otvetst_mk', String(50)))
    num_kontra: Optional[str] = Field(default=None, sa_column=mapped_column('num_kontra', String(50)))
    data_kontr: Optional[date] = Field(default=None, sa_column=mapped_column('data_kontr', Date))
    vid_doc_ut: Optional[str] = Field(default=None, sa_column=mapped_column('vid_doc_ut', String(100)))
    num_doc_ut: Optional[str] = Field(default=None, sa_column=mapped_column('num_doc_ut', String(50)))
    data_doc_u: Optional[date] = Field(default=None, sa_column=mapped_column('data_doc_u', Date))
    priostanov: Optional[str] = Field(default=None, sa_column=mapped_column('priostanov', String(100)))
    zaversheni: Optional[str] = Field(default=None, sa_column=mapped_column('zaversheni', String(100)))
    otmena: Optional[str] = Field(default=None, sa_column=mapped_column('otmena', String(100)))
    status: Optional[str] = Field(default=None, sa_column=mapped_column('status', String(50)))
    grup1: Optional[str] = Field(default=None, sa_column=mapped_column('grup1', String(100)))
    grup2: Optional[str] = Field(default=None, sa_column=mapped_column('grup2', String(100)))
    oasi: Optional[str] = Field(default=None, sa_column=mapped_column('oasi', String(20)))
    us_ppt: Optional[str] = Field(default=None, sa_column=mapped_column('us_ppt', String(10)))
    sppgns_obs: Optional[str] = Field(default=None, sa_column=mapped_column('sppgns_obs', String(100)))
    sppgns_jil: Optional[str] = Field(default=None, sa_column=mapped_column('sppgns_jil', String(100)))
    sppgns_nej: Optional[str] = Field(default=None, sa_column=mapped_column('sppgns_nej', String(100)))
    shape_area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('shape_area', Numeric))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


class TpzNew(SQLModel, table=True):
    __tablename__ = 'tpz_new'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='tpz_new_pkey'),
        Index('tpz_new_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    podzone_nu: Optional[str] = Field(default=None, sa_column=mapped_column('podzone_nu', String(25)))
    num_pp: Optional[str] = Field(default=None, sa_column=mapped_column('num_pp', String(50)))
    doc_date: Optional[date] = Field(default=None, sa_column=mapped_column('doc_date', Date))
    type: Optional[str] = Field(default=None, sa_column=mapped_column('type', String(50)))
    plotnost: Optional[str] = Field(default=None, sa_column=mapped_column('plotnost', String(50)))
    vysota: Optional[str] = Field(default=None, sa_column=mapped_column('vysota', String(50)))
    proczastro: Optional[str] = Field(default=None, sa_column=mapped_column('proczastro', String(50)))
    area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('area', Numeric))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


class TpzOld(SQLModel, table=True):
    __tablename__ = 'tpz_old'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='tpz_old_pkey'),
        Index('tpz_old_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    plotnost: Optional[str] = Field(default=None, sa_column=mapped_column('plotnost', String(50)))
    vysota: Optional[str] = Field(default=None, sa_column=mapped_column('vysota', String(50)))
    proczastro: Optional[str] = Field(default=None, sa_column=mapped_column('proczastro', String(50)))
    podzone_nu: Optional[str] = Field(default=None, sa_column=mapped_column('podzone_nu', String(25)))
    num_pp: Optional[str] = Field(default=None, sa_column=mapped_column('num_pp', String(50)))
    doc_date: Optional[date] = Field(default=None, sa_column=mapped_column('doc_date', Date))
    type: Optional[str] = Field(default=None, sa_column=mapped_column('type', String(50)))
    area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('area', Numeric))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))

class TzNew(SQLModel, table=True):
    __tablename__ = 'tz_new'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='tz_new_pkey'),
        Index('tz_new_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    zone_num: Optional[str] = Field(default=None, sa_column=mapped_column('zone_num', String(20)))
    num_pp: Optional[str] = Field(default=None, sa_column=mapped_column('num_pp', String(50)))
    doc_date: Optional[date] = Field(default=None, sa_column=mapped_column('doc_date', Date))
    type: Optional[str] = Field(default=None, sa_column=mapped_column('type', String(50)))
    index_: Optional[str] = Field(default=None, sa_column=mapped_column('index_', String(254)))
    vri_540: Optional[str] = Field(default=None, sa_column=mapped_column('vri_540', String(254)))
    area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('area', Numeric))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


class TzOld(SQLModel, table=True):
    __tablename__ = 'tz_old'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='tz_old_pkey'),
        Index('tz_old_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    zone_num: Optional[str] = Field(default=None, sa_column=mapped_column('zone_num', String(20)))
    num_pp: Optional[str] = Field(default=None, sa_column=mapped_column('num_pp', String(50)))
    doc_date: Optional[date] = Field(default=None, sa_column=mapped_column('doc_date', Date))
    type: Optional[str] = Field(default=None, sa_column=mapped_column('type', String(50)))
    index_: Optional[str] = Field(default=None, sa_column=mapped_column('index_', String(254)))
    vri_540: Optional[str] = Field(default=None, sa_column=mapped_column('vri_540', String(254)))
    area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('area', Numeric))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


class UchastkiMegevania(SQLModel, table=True):
    __tablename__ = 'uchastki_megevania'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='uchastki_megevania_pkey'),
        Index('uchastki_megevania_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    numberarea: Optional[int] = Field(default=None, sa_column=mapped_column('numberarea', Integer))
    descr: Optional[str] = Field(default=None, sa_column=mapped_column('descr', String(254)))
    klass: Optional[str] = Field(default=None, sa_column=mapped_column('klass', String(254)))
    func_use: Optional[str] = Field(default=None, sa_column=mapped_column('func_use', String(254)))
    n_kvar: Optional[str] = Field(default=None, sa_column=mapped_column('n_kvar', String(50)))
    n_parc: Optional[str] = Field(default=None, sa_column=mapped_column('n_parc', String(50)))
    year: Optional[str] = Field(default=None, sa_column=mapped_column('year', String(50)))
    area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('area', Numeric))
    shape_area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('shape_area', Numeric))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


class UdsBridges(SQLModel, table=True):
    __tablename__ = 'uds_bridges'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='uds_bridges_pkey'),
        Index('uds_bridges_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    name_obj: Optional[str] = Field(default=None, sa_column=mapped_column('name_obj', String(6)))
    state: Optional[str] = Field(default=None, sa_column=mapped_column('state', String(254)))
    vid: Optional[str] = Field(default=None, sa_column=mapped_column('vid', String(254)))
    name: Optional[str] = Field(default=None, sa_column=mapped_column('name', String(80)))
    shape_leng: Optional[Decimal] = Field(default=None, sa_column=mapped_column('shape_leng', Numeric))
    shape_area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('shape_area', Numeric))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


class UdsRoads(SQLModel, table=True):
    __tablename__ = 'uds_roads'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='uds_roads_pkey'),
        Index('uds_roads_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    name_obj: Optional[str] = Field(default=None, sa_column=mapped_column('name_obj', String(4)))
    name_str: Optional[str] = Field(default=None, sa_column=mapped_column('name_str', String(254)))
    vid_road: Optional[str] = Field(default=None, sa_column=mapped_column('vid_road', String(254)))
    ext_name: Optional[str] = Field(default=None, sa_column=mapped_column('ext_name', String(254)))
    shape_leng: Optional[Decimal] = Field(default=None, sa_column=mapped_column('shape_leng', Numeric))
    shape_area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('shape_area', Numeric))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


class Zouit(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='zouit_pkey'),
        Index('zouit_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    cad_num: Optional[str] = Field(default=None, sa_column=mapped_column('cad_num', String(254)))
    okrug: Optional[str] = Field(default=None, sa_column=mapped_column('okrug', String(254)))
    raion_pos: Optional[str] = Field(default=None, sa_column=mapped_column('raion_pos', String(254)))
    vid_zouit: Optional[str] = Field(default=None, sa_column=mapped_column('vid_zouit', String(254)))
    type_zone: Optional[str] = Field(default=None, sa_column=mapped_column('type_zone', String(254)))
    name: Optional[str] = Field(default=None, sa_column=mapped_column('name', String(254)))
    ogran: Optional[str] = Field(default=None, sa_column=mapped_column('ogran', String(254)))
    doc: Optional[str] = Field(default=None, sa_column=mapped_column('doc', String(254)))
    area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('area', Numeric))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


class Zu(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='zu_pkey'),
        Index('zu_geom_idx', 'geom')
    )

    gid: Optional[int] = Field(default=None, sa_column=mapped_column('gid', Integer))
    cadastra2: Optional[str] = Field(default=None, sa_column=mapped_column('cadastra2', String(80)))
    address: Optional[str] = Field(default=None, sa_column=mapped_column('address', String(254)))
    hasvalid5: Optional[str] = Field(default=None, sa_column=mapped_column('hasvalid5', String(80)))
    hascadas6: Optional[str] = Field(default=None, sa_column=mapped_column('hascadas6', String(80)))
    isdraft: Optional[str] = Field(default=None, sa_column=mapped_column('isdraft', String(80)))
    ownershi8: Optional[Decimal] = Field(default=None, sa_column=mapped_column('ownershi8', Numeric))
    is_stroy: Optional[str] = Field(default=None, sa_column=mapped_column('is_stroy', String(80)))
    is_nonca20: Optional[Decimal] = Field(default=None, sa_column=mapped_column('is_nonca20', Numeric))
    area: Optional[Decimal] = Field(default=None, sa_column=mapped_column('area', Numeric))
    geom: Optional[Any] = Field(default=None, sa_column=mapped_column('geom', Geometry('MULTIPOLYGON')))


t_zu_kadastr_delenie = Table(
    'zu_kadastr_delenie', metadata,
    Column('zu_gid', Integer),
    Column('kadastr_delenie_gid', Integer),
    Index('zu_kadastr_delenie_kadastr_delenie_gid', 'kadastr_delenie_gid'),
    Index('zu_kadastr_delenie_zu_gid', 'zu_gid')
)


t_zu_krt = Table(
    'zu_krt', metadata,
    Column('zu_gid', Integer),
    Column('krt_gid', Integer),
    Index('zu_krt_krt_gid', 'krt_gid'),
    Index('zu_krt_zu_gid', 'zu_gid')
)


t_zu_kvartal_region = Table(
    'zu_kvartal_region', metadata,
    Column('zu_gid', Integer),
    Column('kvartal_region_gid', Integer),
    Index('zu_kvartal_region_kvartal_region_gid', 'kvartal_region_gid'),
    Index('zu_kvartal_region_zu_gid', 'zu_gid')
)


t_zu_mkd = Table(
    'zu_mkd', metadata,
    Column('zu_gid', Integer),
    Column('mkd_gid', Integer),
    Index('zu_mkd_gid', 'mkd_gid'),
    Index('zu_mkd_zu_gid', 'zu_gid')
)


t_zu_okrug = Table(
    'zu_okrug', metadata,
    Column('zu_gid', Integer),
    Column('okrug_gid', Integer),
    Index('zu_okrug_zu_gid', 'zu_gid'),
    Index('zu_oks_okrug_gid', 'okrug_gid')
)


t_zu_oks = Table(
    'zu_oks', metadata,
    Column('zu_gid', Integer),
    Column('oks_gid', Integer),
    Index('zu_oks_oks_gid', 'oks_gid'),
    Index('zu_oks_zu_gid', 'zu_gid')
)


t_zu_oozt = Table(
    'zu_oozt', metadata,
    Column('zu_gid', Integer),
    Column('oozt_gid', Integer),
    Index('zu_oozt_oozt_gid', 'oozt_gid'),
    Index('zu_oozt_zu_gid', 'zu_gid')
)


t_zu_pp_gaz = Table(
    'zu_pp_gaz', metadata,
    Column('zu_gid', Integer),
    Column('pp_gaz_gid', Integer),
    Index('zu_pp_gaz_pp_gaz_gid', 'pp_gaz_gid'),
    Index('zu_pp_gaz_zu_gid', 'zu_gid')
)


t_zu_pp_metro_all = Table(
    'zu_pp_metro_all', metadata,
    Column('zu_gid', Integer),
    Column('pp_metro_gid', Integer),
    Index('zu_pp_metro_all_gid', 'pp_metro_gid'),
    Index('zu_pp_metro_all_zu_gid', 'zu_gid')
)


t_zu_ppt_all = Table(
    'zu_ppt_all', metadata,
    Column('zu_gid', Integer),
    Column('ppt_all_gid', Integer),
    Index('zu_ppt_all_ppt_all_gid', 'ppt_all_gid'),
    Index('zu_ppt_all_zu_gid', 'zu_gid')
)


t_zu_ppt_uds = Table(
    'zu_ppt_uds', metadata,
    Column('zu_gid', Integer),
    Column('ppt_uds_gid', Integer),
    Index('zu_ppt_uds_ppt_uds_gid', 'ppt_uds_gid'),
    Index('zu_ppt_uds_zu_gid', 'zu_gid')
)


t_zu_rayon = Table(
    'zu_rayon', metadata,
    Column('zu_gid', Integer),
    Column('rayon_gid', Integer),
    Index('zu_rayon_rayon_gid', 'rayon_gid'),
    Index('zu_rayon_zu_gid', 'zu_gid')
)


t_zu_rsp = Table(
    'zu_rsp', metadata,
    Column('zu_gid', Integer),
    Column('rsp_gid', Integer),
    Index('zu_rsp_spritzone_rsp_gid', 'rsp_gid'),
    Index('zu_rsp_zu_gid', 'zu_gid')
)


t_zu_spritzones = Table(
    'zu_spritzones', metadata,
    Column('zu_gid', Integer),
    Column('spritzone_gid', Integer),
    Index('zu_spritzones_spritzone_gid', 'spritzone_gid'),
    Index('zu_spritzones_zu_gid', 'zu_gid')
)


t_zu_tpu_rv_metro_polygon = Table(
    'zu_tpu_rv_metro_polygon', metadata,
    Column('zu_gid', Integer),
    Column('tpu_rv_metro_gid', Integer),
    Index('zu_tpu_rv_metro_polygon_tpu_rv_metro_gid', 'tpu_rv_metro_gid'),
    Index('zu_tpu_rv_metro_polygon_zu_gid', 'zu_gid')
)


t_zu_tpz = Table(
    'zu_tpz', metadata,
    Column('zu_gid', Integer),
    Column('tpz_gid', Integer),
    Index('zu_tpz_tpz_gid', 'tpz_gid'),
    Index('zu_tpz_zu_gid', 'zu_gid')
)


t_zu_tz = Table(
    'zu_tz', metadata,
    Column('zu_gid', Integer),
    Column('tz_gid', Integer),
    Index('zu_tz_tz_gid', 'tz_gid'),
    Index('zu_tz_zu_gid', 'zu_gid')
)


t_zu_uchastki_megevania = Table(
    'zu_uchastki_megevania', metadata,
    Column('zu_gid', Integer),
    Column('uchastok_megevania_gid', Integer),
    Index('zu_uchastki_megevania_uchastok_megevania_gid', 'uchastok_megevania_gid'),
    Index('zu_uchastki_megevania_zu_gid', 'zu_gid')
)


t_zu_zouit = Table(
    'zu_zouit', metadata,
    Column('zu_gid', Integer),
    Column('zouit_gid', Integer),
    Index('zu_zouit_zouit_gid', 'zouit_gid'),
    Index('zu_zouit_zu_gid', 'zu_gid')
)
