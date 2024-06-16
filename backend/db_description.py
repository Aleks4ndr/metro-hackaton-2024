from typing import List

from sqlalchemy import ARRAY, BigInteger, Boolean, CHAR, CheckConstraint, Column, Date, Double, ForeignKeyConstraint, Index, Integer, Numeric, PrimaryKeyConstraint, String, Table, Text, UniqueConstraint, text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from sqlalchemy.sql.sqltypes import NullType

Base = declarative_base()
metadata = Base.metadata


class Addr(Base):
    __tablename__ = 'addr'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='addr_pkey'),
        Index('idx_tiger_addr_tlid_statefp', 'tlid', 'statefp'),
        Index('idx_tiger_addr_zip', 'zip')
    )

    gid = mapped_column(Integer)
    tlid = mapped_column(BigInteger)
    fromhn = mapped_column(String(12))
    tohn = mapped_column(String(12))
    side = mapped_column(String(1))
    zip = mapped_column(String(5))
    plus4 = mapped_column(String(4))
    fromtyp = mapped_column(String(1))
    totyp = mapped_column(String(1))
    fromarmid = mapped_column(Integer)
    toarmid = mapped_column(Integer)
    arid = mapped_column(String(22))
    mtfcc = mapped_column(String(5))
    statefp = mapped_column(String(2))


class Addrfeat(Base):
    __tablename__ = 'addrfeat'
    __table_args__ = (
        CheckConstraint("geometrytype(the_geom) = 'LINESTRING'::text OR the_geom IS NULL", name='enforce_geotype_the_geom'),
        CheckConstraint('st_ndims(the_geom) = 2', name='enforce_dims_the_geom'),
        CheckConstraint('st_srid(the_geom) = 4269', name='enforce_srid_the_geom'),
        PrimaryKeyConstraint('gid', name='addrfeat_pkey'),
        Index('idx_addrfeat_geom_gist', 'the_geom'),
        Index('idx_addrfeat_tlid', 'tlid'),
        Index('idx_addrfeat_zipl', 'zipl'),
        Index('idx_addrfeat_zipr', 'zipr')
    )

    gid = mapped_column(Integer)
    statefp = mapped_column(String(2), nullable=False)
    tlid = mapped_column(BigInteger)
    aridl = mapped_column(String(22))
    aridr = mapped_column(String(22))
    linearid = mapped_column(String(22))
    fullname = mapped_column(String(100))
    lfromhn = mapped_column(String(12))
    ltohn = mapped_column(String(12))
    rfromhn = mapped_column(String(12))
    rtohn = mapped_column(String(12))
    zipl = mapped_column(String(5))
    zipr = mapped_column(String(5))
    edge_mtfcc = mapped_column(String(5))
    parityl = mapped_column(String(1))
    parityr = mapped_column(String(1))
    plus4l = mapped_column(String(4))
    plus4r = mapped_column(String(4))
    lfromtyp = mapped_column(String(1))
    ltotyp = mapped_column(String(1))
    rfromtyp = mapped_column(String(1))
    rtotyp = mapped_column(String(1))
    offsetl = mapped_column(String(1))
    offsetr = mapped_column(String(1))
    the_geom = mapped_column(NullType)


class Bg(Base):
    __tablename__ = 'bg'
    __table_args__ = (
        CheckConstraint("geometrytype(the_geom) = 'MULTIPOLYGON'::text OR the_geom IS NULL", name='enforce_geotype_geom'),
        CheckConstraint('st_ndims(the_geom) = 2', name='enforce_dims_geom'),
        CheckConstraint('st_srid(the_geom) = 4269', name='enforce_srid_geom'),
        PrimaryKeyConstraint('bg_id', name='bg_pkey'),
        {'comment': 'block groups'}
    )

    gid = mapped_column(Integer, nullable=False)
    bg_id = mapped_column(String(12))
    statefp = mapped_column(String(2))
    countyfp = mapped_column(String(3))
    tractce = mapped_column(String(6))
    blkgrpce = mapped_column(String(1))
    namelsad = mapped_column(String(13))
    mtfcc = mapped_column(String(5))
    funcstat = mapped_column(String(1))
    aland = mapped_column(Double(53))
    awater = mapped_column(Double(53))
    intptlat = mapped_column(String(11))
    intptlon = mapped_column(String(12))
    the_geom = mapped_column(NullType)


class County(Base):
    __tablename__ = 'county'
    __table_args__ = (
        CheckConstraint("geometrytype(the_geom) = 'MULTIPOLYGON'::text OR the_geom IS NULL", name='enforce_geotype_geom'),
        CheckConstraint('st_ndims(the_geom) = 2', name='enforce_dims_geom'),
        CheckConstraint('st_srid(the_geom) = 4269', name='enforce_srid_geom'),
        PrimaryKeyConstraint('cntyidfp', name='pk_tiger_county'),
        UniqueConstraint('gid', name='uidx_county_gid'),
        Index('idx_tiger_county', 'countyfp')
    )

    gid = mapped_column(Integer, nullable=False)
    cntyidfp = mapped_column(String(5))
    statefp = mapped_column(String(2))
    countyfp = mapped_column(String(3))
    countyns = mapped_column(String(8))
    name = mapped_column(String(100))
    namelsad = mapped_column(String(100))
    lsad = mapped_column(String(2))
    classfp = mapped_column(String(2))
    mtfcc = mapped_column(String(5))
    csafp = mapped_column(String(3))
    cbsafp = mapped_column(String(5))
    metdivfp = mapped_column(String(5))
    funcstat = mapped_column(String(1))
    aland = mapped_column(BigInteger)
    awater = mapped_column(Double(53))
    intptlat = mapped_column(String(11))
    intptlon = mapped_column(String(12))
    the_geom = mapped_column(NullType)


class CountyLookup(Base):
    __tablename__ = 'county_lookup'
    __table_args__ = (
        PrimaryKeyConstraint('st_code', 'co_code', name='county_lookup_pkey'),
        Index('county_lookup_name_idx'),
        Index('county_lookup_state_idx', 'state')
    )

    st_code = mapped_column(Integer, nullable=False)
    co_code = mapped_column(Integer, nullable=False)
    state = mapped_column(String(2))
    name = mapped_column(String(90))


class CountysubLookup(Base):
    __tablename__ = 'countysub_lookup'
    __table_args__ = (
        PrimaryKeyConstraint('st_code', 'co_code', 'cs_code', name='countysub_lookup_pkey'),
        Index('countysub_lookup_name_idx'),
        Index('countysub_lookup_state_idx', 'state')
    )

    st_code = mapped_column(Integer, nullable=False)
    co_code = mapped_column(Integer, nullable=False)
    cs_code = mapped_column(Integer, nullable=False)
    state = mapped_column(String(2))
    county = mapped_column(String(90))
    name = mapped_column(String(90))


class Cousub(Base):
    __tablename__ = 'cousub'
    __table_args__ = (
        CheckConstraint("geometrytype(the_geom) = 'MULTIPOLYGON'::text OR the_geom IS NULL", name='enforce_geotype_the_geom'),
        CheckConstraint('st_ndims(the_geom) = 2', name='enforce_dims_the_geom'),
        CheckConstraint('st_srid(the_geom) = 4269', name='enforce_srid_the_geom'),
        PrimaryKeyConstraint('cosbidfp', name='cousub_pkey'),
        UniqueConstraint('gid', name='uidx_cousub_gid'),
        Index('tige_cousub_the_geom_gist', 'the_geom')
    )

    gid = mapped_column(Integer, nullable=False)
    cosbidfp = mapped_column(String(10))
    statefp = mapped_column(String(2))
    countyfp = mapped_column(String(3))
    cousubfp = mapped_column(String(5))
    cousubns = mapped_column(String(8))
    name = mapped_column(String(100))
    namelsad = mapped_column(String(100))
    lsad = mapped_column(String(2))
    classfp = mapped_column(String(2))
    mtfcc = mapped_column(String(5))
    cnectafp = mapped_column(String(3))
    nectafp = mapped_column(String(5))
    nctadvfp = mapped_column(String(5))
    funcstat = mapped_column(String(1))
    aland = mapped_column(Numeric(14, 0))
    awater = mapped_column(Numeric(14, 0))
    intptlat = mapped_column(String(11))
    intptlon = mapped_column(String(12))
    the_geom = mapped_column(NullType)


class DirectionLookup(Base):
    __tablename__ = 'direction_lookup'
    __table_args__ = (
        PrimaryKeyConstraint('name', name='direction_lookup_pkey'),
        Index('direction_lookup_abbrev_idx', 'abbrev')
    )

    name = mapped_column(String(20))
    abbrev = mapped_column(String(3))


class Edges(Base):
    __tablename__ = 'edges'
    __table_args__ = (
        CheckConstraint("geometrytype(the_geom) = 'MULTILINESTRING'::text OR the_geom IS NULL", name='enforce_geotype_the_geom'),
        CheckConstraint('st_ndims(the_geom) = 2', name='enforce_dims_the_geom'),
        CheckConstraint('st_srid(the_geom) = 4269', name='enforce_srid_the_geom'),
        PrimaryKeyConstraint('gid', name='edges_pkey'),
        Index('idx_edges_tlid', 'tlid'),
        Index('idx_tiger_edges_countyfp', 'countyfp'),
        Index('idx_tiger_edges_the_geom_gist', 'the_geom')
    )

    gid = mapped_column(Integer)
    statefp = mapped_column(String(2))
    countyfp = mapped_column(String(3))
    tlid = mapped_column(BigInteger)
    tfidl = mapped_column(Numeric(10, 0))
    tfidr = mapped_column(Numeric(10, 0))
    mtfcc = mapped_column(String(5))
    fullname = mapped_column(String(100))
    smid = mapped_column(String(22))
    lfromadd = mapped_column(String(12))
    ltoadd = mapped_column(String(12))
    rfromadd = mapped_column(String(12))
    rtoadd = mapped_column(String(12))
    zipl = mapped_column(String(5))
    zipr = mapped_column(String(5))
    featcat = mapped_column(String(1))
    hydroflg = mapped_column(String(1))
    railflg = mapped_column(String(1))
    roadflg = mapped_column(String(1))
    olfflg = mapped_column(String(1))
    passflg = mapped_column(String(1))
    divroad = mapped_column(String(1))
    exttyp = mapped_column(String(1))
    ttyp = mapped_column(String(1))
    deckedroad = mapped_column(String(1))
    artpath = mapped_column(String(1))
    persist = mapped_column(String(1))
    gcseflg = mapped_column(String(1))
    offsetl = mapped_column(String(1))
    offsetr = mapped_column(String(1))
    tnidf = mapped_column(Numeric(10, 0))
    tnidt = mapped_column(Numeric(10, 0))
    the_geom = mapped_column(NullType)


class Faces(Base):
    __tablename__ = 'faces'
    __table_args__ = (
        CheckConstraint("geometrytype(the_geom) = 'MULTIPOLYGON'::text OR the_geom IS NULL", name='enforce_geotype_the_geom'),
        CheckConstraint('st_ndims(the_geom) = 2', name='enforce_dims_the_geom'),
        CheckConstraint('st_srid(the_geom) = 4269', name='enforce_srid_the_geom'),
        PrimaryKeyConstraint('gid', name='faces_pkey'),
        Index('idx_tiger_faces_countyfp', 'countyfp'),
        Index('idx_tiger_faces_tfid', 'tfid'),
        Index('tiger_faces_the_geom_gist', 'the_geom')
    )

    gid = mapped_column(Integer)
    tfid = mapped_column(Numeric(10, 0))
    statefp00 = mapped_column(String(2))
    countyfp00 = mapped_column(String(3))
    tractce00 = mapped_column(String(6))
    blkgrpce00 = mapped_column(String(1))
    blockce00 = mapped_column(String(4))
    cousubfp00 = mapped_column(String(5))
    submcdfp00 = mapped_column(String(5))
    conctyfp00 = mapped_column(String(5))
    placefp00 = mapped_column(String(5))
    aiannhfp00 = mapped_column(String(5))
    aiannhce00 = mapped_column(String(4))
    comptyp00 = mapped_column(String(1))
    trsubfp00 = mapped_column(String(5))
    trsubce00 = mapped_column(String(3))
    anrcfp00 = mapped_column(String(5))
    elsdlea00 = mapped_column(String(5))
    scsdlea00 = mapped_column(String(5))
    unsdlea00 = mapped_column(String(5))
    uace00 = mapped_column(String(5))
    cd108fp = mapped_column(String(2))
    sldust00 = mapped_column(String(3))
    sldlst00 = mapped_column(String(3))
    vtdst00 = mapped_column(String(6))
    zcta5ce00 = mapped_column(String(5))
    tazce00 = mapped_column(String(6))
    ugace00 = mapped_column(String(5))
    puma5ce00 = mapped_column(String(5))
    statefp = mapped_column(String(2))
    countyfp = mapped_column(String(3))
    tractce = mapped_column(String(6))
    blkgrpce = mapped_column(String(1))
    blockce = mapped_column(String(4))
    cousubfp = mapped_column(String(5))
    submcdfp = mapped_column(String(5))
    conctyfp = mapped_column(String(5))
    placefp = mapped_column(String(5))
    aiannhfp = mapped_column(String(5))
    aiannhce = mapped_column(String(4))
    comptyp = mapped_column(String(1))
    trsubfp = mapped_column(String(5))
    trsubce = mapped_column(String(3))
    anrcfp = mapped_column(String(5))
    ttractce = mapped_column(String(6))
    tblkgpce = mapped_column(String(1))
    elsdlea = mapped_column(String(5))
    scsdlea = mapped_column(String(5))
    unsdlea = mapped_column(String(5))
    uace = mapped_column(String(5))
    cd111fp = mapped_column(String(2))
    sldust = mapped_column(String(3))
    sldlst = mapped_column(String(3))
    vtdst = mapped_column(String(6))
    zcta5ce = mapped_column(String(5))
    tazce = mapped_column(String(6))
    ugace = mapped_column(String(5))
    puma5ce = mapped_column(String(5))
    csafp = mapped_column(String(3))
    cbsafp = mapped_column(String(5))
    metdivfp = mapped_column(String(5))
    cnectafp = mapped_column(String(3))
    nectafp = mapped_column(String(5))
    nctadvfp = mapped_column(String(5))
    lwflag = mapped_column(String(1))
    offset = mapped_column(String(1))
    atotal = mapped_column(Double(53))
    intptlat = mapped_column(String(11))
    intptlon = mapped_column(String(12))
    the_geom = mapped_column(NullType)
    tractce20 = mapped_column(String(6))
    blkgrpce20 = mapped_column(String(1))
    blockce20 = mapped_column(String(4))
    countyfp20 = mapped_column(String(3))
    statefp20 = mapped_column(String(2))


class Featnames(Base):
    __tablename__ = 'featnames'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='featnames_pkey'),
        Index('idx_tiger_featnames_lname'),
        Index('idx_tiger_featnames_snd_name'),
        Index('idx_tiger_featnames_tlid_statefp', 'tlid', 'statefp')
    )

    gid = mapped_column(Integer)
    tlid = mapped_column(BigInteger)
    fullname = mapped_column(String(100))
    name = mapped_column(String(100))
    predirabrv = mapped_column(String(15))
    pretypabrv = mapped_column(String(50))
    prequalabr = mapped_column(String(15))
    sufdirabrv = mapped_column(String(15))
    suftypabrv = mapped_column(String(50))
    sufqualabr = mapped_column(String(15))
    predir = mapped_column(String(2))
    pretyp = mapped_column(String(3))
    prequal = mapped_column(String(2))
    sufdir = mapped_column(String(2))
    suftyp = mapped_column(String(3))
    sufqual = mapped_column(String(2))
    linearid = mapped_column(String(22))
    mtfcc = mapped_column(String(5))
    paflag = mapped_column(String(1))
    statefp = mapped_column(String(2))


class GeocodeSettings(Base):
    __tablename__ = 'geocode_settings'
    __table_args__ = (
        PrimaryKeyConstraint('name', name='geocode_settings_pkey'),
    )

    name = mapped_column(Text)
    setting = mapped_column(Text)
    unit = mapped_column(Text)
    category = mapped_column(Text)
    short_desc = mapped_column(Text)


class GeocodeSettingsDefault(Base):
    __tablename__ = 'geocode_settings_default'
    __table_args__ = (
        PrimaryKeyConstraint('name', name='geocode_settings_default_pkey'),
    )

    name = mapped_column(Text)
    setting = mapped_column(Text)
    unit = mapped_column(Text)
    category = mapped_column(Text)
    short_desc = mapped_column(Text)


t_geography_columns = Table(
    'geography_columns', metadata,
    Column('f_table_catalog', String),
    Column('f_table_schema', String),
    Column('f_table_name', String),
    Column('f_geography_column', String),
    Column('coord_dimension', Integer),
    Column('srid', Integer),
    Column('type', Text)
)


t_geometry_columns = Table(
    'geometry_columns', metadata,
    Column('f_table_catalog', String(256)),
    Column('f_table_schema', String),
    Column('f_table_name', String),
    Column('f_geometry_column', String),
    Column('coord_dimension', Integer),
    Column('srid', Integer),
    Column('type', String(30))
)


class KadastrDelenie(Base):
    __tablename__ = 'kadastr_delenie'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='kadastr_delenie_pkey'),
        Index('kadastr_delenie_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    cadastra1 = mapped_column(String(80))
    objectid = mapped_column(String(80))
    geom = mapped_column(NullType)


class Krt(Base):
    __tablename__ = 'krt'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='krt_pkey'),
        Index('krt_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    name = mapped_column(String(254))
    area_krt = mapped_column(Numeric)
    type_krt = mapped_column(String(80))
    geom = mapped_column(NullType)


class KvartalRegion(Base):
    __tablename__ = 'kvartal_region'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='kvartal_region_pkey'),
        Index('kvartal_region_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    objectid = mapped_column(Double(53))
    num_doc_ut = mapped_column(String(20))
    data_doc_u = mapped_column(Date)
    name_ppt = mapped_column(String(254))
    okrug = mapped_column(String(10))
    rayon = mapped_column(String(254))
    area = mapped_column(Numeric)
    prim = mapped_column(String(254))
    uslov = mapped_column(Integer)
    db2gse_st_ = mapped_column(Numeric)
    db2gse_sde = mapped_column(Numeric)
    geom = mapped_column(NullType)


class LoaderLookuptables(Base):
    __tablename__ = 'loader_lookuptables'
    __table_args__ = (
        PrimaryKeyConstraint('lookup_name', name='loader_lookuptables_pkey'),
    )

    process_order = mapped_column(Integer, nullable=False, server_default=text('1000'))
    lookup_name = mapped_column(Text, comment='This is the table name to inherit from and suffix of resulting output table -- how the table will be named --  edges here would mean -- ma_edges , pa_edges etc. except in the case of national tables. national level tables have no prefix')
    single_mode = mapped_column(Boolean, nullable=False, server_default=text('true'))
    load = mapped_column(Boolean, nullable=False, server_default=text('true'), comment="Whether or not to load the table.  For states and zcta5 (you may just want to download states10, zcta510 nationwide file manually) load your own into a single table that inherits from tiger.states, tiger.zcta5.  You'll get improved performance for some geocoding cases.")
    level_county = mapped_column(Boolean, nullable=False, server_default=text('false'))
    level_state = mapped_column(Boolean, nullable=False, server_default=text('false'))
    level_nation = mapped_column(Boolean, nullable=False, server_default=text('false'), comment='These are tables that contain all data for the whole US so there is just a single file')
    insert_mode = mapped_column(CHAR(1), nullable=False, server_default=text("'c'::bpchar"))
    table_name = mapped_column(Text, comment='suffix of the tables to load e.g.  edges would load all tables like *edges.dbf(shp)  -- so tl_2010_42129_edges.dbf .  ')
    post_load_process = mapped_column(Text)
    single_geom_mode = mapped_column(Boolean, server_default=text('false'))
    pre_load_process = mapped_column(Text)
    columns_exclude = mapped_column(ARRAY(Text()), comment='List of columns to exclude as an array. This is excluded from both input table and output table and rest of columns remaining are assumed to be in same order in both tables. gid, geoid,cpi,suffix1ce are excluded if no columns are specified.')
    website_root_override = mapped_column(Text, comment='Path to use for wget instead of that specified in year table.  Needed currently for zcta where they release that only for 2000 and 2010')


class LoaderPlatform(Base):
    __tablename__ = 'loader_platform'
    __table_args__ = (
        PrimaryKeyConstraint('os', name='loader_platform_pkey'),
    )

    os = mapped_column(String(50))
    declare_sect = mapped_column(Text)
    pgbin = mapped_column(Text)
    wget = mapped_column(Text)
    unzip_command = mapped_column(Text)
    psql = mapped_column(Text)
    path_sep = mapped_column(Text)
    loader = mapped_column(Text)
    environ_set_command = mapped_column(Text)
    county_process_command = mapped_column(Text)


class LoaderVariables(Base):
    __tablename__ = 'loader_variables'
    __table_args__ = (
        PrimaryKeyConstraint('tiger_year', name='loader_variables_pkey'),
    )

    tiger_year = mapped_column(String(4))
    website_root = mapped_column(Text)
    staging_fold = mapped_column(Text)
    data_schema = mapped_column(Text)
    staging_schema = mapped_column(Text)


class Mkd(Base):
    __tablename__ = 'mkd'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='mkd_pkey'),
        Index('mkd_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    unom = mapped_column(Numeric)
    address = mapped_column(String(254))
    cadastra3 = mapped_column(String(80))
    hascadas4 = mapped_column(String(80))
    hasbti = mapped_column(String(80))
    hascontr6 = mapped_column(Numeric)
    hasownrf = mapped_column(String(80))
    hasownmo8 = mapped_column(String(80))
    hasownot9 = mapped_column(String(80))
    shape_area = mapped_column(Numeric)
    geom = mapped_column(NullType)


class Okrug(Base):
    __tablename__ = 'okrug'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='okrug_pkey'),
        Index('okrug_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    objectid = mapped_column(Double(53))
    uidnftn = mapped_column(Double(53))
    name = mapped_column(String(254))
    label = mapped_column(String(254))
    address = mapped_column(String(254))
    x = mapped_column(Numeric)
    y = mapped_column(Numeric)
    bui_no_bti = mapped_column(Double(53))
    cad_no = mapped_column(String(254))
    street_bti = mapped_column(String(254))
    house_bti = mapped_column(String(254))
    hadd_bti = mapped_column(String(254))
    moddate = mapped_column(Date)
    moduser = mapped_column(String(100))
    torzid = mapped_column(Numeric)
    exclude_gr = mapped_column(Numeric)
    shape_area = mapped_column(Numeric)
    shape_len = mapped_column(Numeric)
    geom = mapped_column(NullType)


class Oks(Base):
    __tablename__ = 'oks'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='oks_pkey'),
        Index('oks_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    unom = mapped_column(Numeric)
    address = mapped_column(String(254))
    cadastra3 = mapped_column(String(80))
    hascadas4 = mapped_column(String(80))
    hasbti = mapped_column(String(80))
    hascontr6 = mapped_column(Numeric)
    hasownrf = mapped_column(String(80))
    hasownmo8 = mapped_column(String(80))
    hasownot9 = mapped_column(String(80))
    shape_area = mapped_column(Numeric)
    geom = mapped_column(NullType)


class Oozt(Base):
    __tablename__ = 'oozt'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='oozt_pkey'),
        Index('oozt_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    objectid = mapped_column(String(80))
    status = mapped_column(String(80))
    zoneid = mapped_column(String(80))
    docnum = mapped_column(String(80))
    docdate = mapped_column(String(80))
    doclist = mapped_column(String(254))
    geom = mapped_column(NullType)


class PagcGaz(Base):
    __tablename__ = 'pagc_gaz'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pagc_gaz_pkey'),
    )

    id = mapped_column(Integer)
    is_custom = mapped_column(Boolean, nullable=False, server_default=text('true'))
    seq = mapped_column(Integer)
    word = mapped_column(Text)
    stdword = mapped_column(Text)
    token = mapped_column(Integer)


class PagcLex(Base):
    __tablename__ = 'pagc_lex'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pagc_lex_pkey'),
    )

    id = mapped_column(Integer)
    is_custom = mapped_column(Boolean, nullable=False, server_default=text('true'))
    seq = mapped_column(Integer)
    word = mapped_column(Text)
    stdword = mapped_column(Text)
    token = mapped_column(Integer)


class PagcRules(Base):
    __tablename__ = 'pagc_rules'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pagc_rules_pkey'),
    )

    id = mapped_column(Integer)
    rule = mapped_column(Text)
    is_custom = mapped_column(Boolean, server_default=text('true'))


class Place(Base):
    __tablename__ = 'place'
    __table_args__ = (
        CheckConstraint("geometrytype(the_geom) = 'MULTIPOLYGON'::text OR the_geom IS NULL", name='enforce_geotype_the_geom'),
        CheckConstraint('st_ndims(the_geom) = 2', name='enforce_dims_the_geom'),
        CheckConstraint('st_srid(the_geom) = 4269', name='enforce_srid_the_geom'),
        PrimaryKeyConstraint('plcidfp', name='place_pkey'),
        UniqueConstraint('gid', name='uidx_tiger_place_gid'),
        Index('tiger_place_the_geom_gist', 'the_geom')
    )

    gid = mapped_column(Integer, nullable=False)
    plcidfp = mapped_column(String(7))
    statefp = mapped_column(String(2))
    placefp = mapped_column(String(5))
    placens = mapped_column(String(8))
    name = mapped_column(String(100))
    namelsad = mapped_column(String(100))
    lsad = mapped_column(String(2))
    classfp = mapped_column(String(2))
    cpi = mapped_column(String(1))
    pcicbsa = mapped_column(String(1))
    pcinecta = mapped_column(String(1))
    mtfcc = mapped_column(String(5))
    funcstat = mapped_column(String(1))
    aland = mapped_column(BigInteger)
    awater = mapped_column(BigInteger)
    intptlat = mapped_column(String(11))
    intptlon = mapped_column(String(12))
    the_geom = mapped_column(NullType)


class PlaceLookup(Base):
    __tablename__ = 'place_lookup'
    __table_args__ = (
        PrimaryKeyConstraint('st_code', 'pl_code', name='place_lookup_pkey'),
        Index('place_lookup_name_idx'),
        Index('place_lookup_state_idx', 'state')
    )

    st_code = mapped_column(Integer, nullable=False)
    pl_code = mapped_column(Integer, nullable=False)
    state = mapped_column(String(2))
    name = mapped_column(String(90))


class PpGaz(Base):
    __tablename__ = 'pp_gaz'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='pp_gaz_pkey'),
        Index('pp_gaz_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    reg_num = mapped_column(String(10))
    vid_ppt = mapped_column(String(100))
    name = mapped_column(String(254))
    vid_doc_ra = mapped_column(String(100))
    num_doc_ra = mapped_column(String(100))
    data_doc_r = mapped_column(Date)
    zakazchik = mapped_column(String(100))
    ispolnitel = mapped_column(String(100))
    istoch_fin = mapped_column(String(100))
    otvetst_mk = mapped_column(String(50))
    num_kontra = mapped_column(String(50))
    data_kontr = mapped_column(Date)
    vid_doc_ut = mapped_column(String(100))
    num_doc_ut = mapped_column(String(50))
    data_doc_u = mapped_column(Date)
    priostanov = mapped_column(String(100))
    zaversheni = mapped_column(String(100))
    otmena = mapped_column(String(100))
    status = mapped_column(String(50))
    grup1 = mapped_column(String(100))
    grup2 = mapped_column(String(100))
    oasi = mapped_column(String(20))
    us_ppt = mapped_column(String(10))
    shape_area = mapped_column(Numeric)
    geom = mapped_column(NullType)


class PpMetroAll(Base):
    __tablename__ = 'pp_metro_all'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='pp_metro_all_pkey'),
        Index('pp_metro_all_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    reg_num = mapped_column(String(10))
    vid_ppt = mapped_column(String(100))
    name = mapped_column(String(254))
    vid_doc_ra = mapped_column(String(100))
    num_doc_ra = mapped_column(String(100))
    data_doc_r = mapped_column(Date)
    zakazchik = mapped_column(String(100))
    ispolnitel = mapped_column(String(100))
    istoch_fin = mapped_column(String(100))
    otvetst_mk = mapped_column(String(50))
    num_kontra = mapped_column(String(50))
    data_kontr = mapped_column(Date)
    vid_doc_ut = mapped_column(String(100))
    num_doc_ut = mapped_column(String(50))
    data_doc_u = mapped_column(Date)
    priostanov = mapped_column(String(100))
    zaversheni = mapped_column(String(100))
    otmena = mapped_column(String(100))
    status = mapped_column(String(50))
    grup1 = mapped_column(String(100))
    grup2 = mapped_column(String(100))
    oasi = mapped_column(String(20))
    us_ppt = mapped_column(String(10))
    shape_area = mapped_column(Numeric)
    geom = mapped_column(NullType)


class PptAll(Base):
    __tablename__ = 'ppt_all'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='ppt_all_pkey'),
        Index('ppt_all_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    reg_num = mapped_column(String(10))
    vid_ppt = mapped_column(String(100))
    name = mapped_column(String(254))
    vid_doc_ra = mapped_column(String(100))
    num_doc_ra = mapped_column(String(50))
    data_doc_r = mapped_column(Date)
    zakazchik = mapped_column(String(100))
    ispolnitel = mapped_column(String(100))
    istoch_fin = mapped_column(String(100))
    otvetst_mk = mapped_column(String(50))
    num_kontra = mapped_column(String(50))
    data_kontr = mapped_column(Date)
    vid_doc_ut = mapped_column(String(100))
    num_doc_ut = mapped_column(String(50))
    data_doc_u = mapped_column(Date)
    priostanov = mapped_column(String(100))
    zaversheni = mapped_column(String(100))
    otmena = mapped_column(String(100))
    status = mapped_column(String(40))
    grup1 = mapped_column(String(100))
    grup2 = mapped_column(String(100))
    oasi = mapped_column(String(20))
    us_ppt = mapped_column(String(10))
    sppgns_obs = mapped_column(String(100))
    sppgns_jil = mapped_column(String(100))
    sppgns_nej = mapped_column(String(100))
    shape_area = mapped_column(Numeric)
    geom = mapped_column(NullType)


class PptUds(Base):
    __tablename__ = 'ppt_uds'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='ppt_uds_pkey'),
        Index('ppt_uds_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    reg_num = mapped_column(String(10))
    vid_ppt = mapped_column(String(100))
    name = mapped_column(String(254))
    vid_doc_ra = mapped_column(String(100))
    num_doc_ra = mapped_column(String(100))
    data_doc_r = mapped_column(Date)
    zakazchik = mapped_column(String(100))
    ispolnitel = mapped_column(String(100))
    istoch_fin = mapped_column(String(100))
    otvetst_mk = mapped_column(String(50))
    num_kontra = mapped_column(String(50))
    data_kontr = mapped_column(Date)
    vid_doc_ut = mapped_column(String(100))
    num_doc_ut = mapped_column(String(50))
    data_doc_u = mapped_column(Date)
    priostanov = mapped_column(String(100))
    zaversheni = mapped_column(String(100))
    otmena = mapped_column(String(100))
    status = mapped_column(String(50))
    grup1 = mapped_column(String(100))
    grup2 = mapped_column(String(100))
    oasi = mapped_column(String(20))
    us_ppt = mapped_column(String(10))
    shape_area = mapped_column(Numeric)
    geom = mapped_column(NullType)


class Rayon(Base):
    __tablename__ = 'rayon'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='rayon_pkey'),
        Index('rayon_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    objectid = mapped_column(Double(53))
    uidnftn = mapped_column(Double(53))
    name = mapped_column(String(254))
    label = mapped_column(String(254))
    address = mapped_column(String(254))
    x = mapped_column(Numeric)
    y = mapped_column(Numeric)
    bui_no_bti = mapped_column(Double(53))
    cad_no = mapped_column(String(254))
    street_bti = mapped_column(String(254))
    house_bti = mapped_column(String(254))
    hadd_bti = mapped_column(String(254))
    mun_obr = mapped_column(String(200))
    moddate = mapped_column(Date)
    moduser = mapped_column(String(100))
    exclude_gr = mapped_column(Numeric)
    shape_area = mapped_column(Numeric)
    shape_len = mapped_column(Numeric)
    geom = mapped_column(NullType)


class Rsp(Base):
    __tablename__ = 'rsp'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='rsp_pkey'),
        Index('rsp_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    okrug = mapped_column(String(80))
    rayon = mapped_column(String(80))
    address = mapped_column(String(254))
    area = mapped_column(String(80))
    prim = mapped_column(String(115))
    plotnost = mapped_column(String(80))
    vysota = mapped_column(String(80))
    spp = mapped_column(String(80))
    total_area = mapped_column(String(80))
    flat_area = mapped_column(String(80))
    osnovanie = mapped_column(String(254))
    agr = mapped_column(String(254))
    objectid = mapped_column(String(80))
    geom = mapped_column(NullType)


class SecondaryUnitLookup(Base):
    __tablename__ = 'secondary_unit_lookup'
    __table_args__ = (
        PrimaryKeyConstraint('name', name='secondary_unit_lookup_pkey'),
        Index('secondary_unit_lookup_abbrev_idx', 'abbrev')
    )

    name = mapped_column(String(20))
    abbrev = mapped_column(String(5))


class SpatialRefSys(Base):
    __tablename__ = 'spatial_ref_sys'
    __table_args__ = (
        CheckConstraint('srid > 0 AND srid <= 998999', name='spatial_ref_sys_srid_check'),
        PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
    )

    srid = mapped_column(Integer)
    auth_name = mapped_column(String(256))
    auth_srid = mapped_column(Integer)
    srtext = mapped_column(String(2048))
    proj4text = mapped_column(String(2048))


class Spritzones20240418121648(Base):
    __tablename__ = 'spritzones_2024_04_18_12_16_48'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='spritzones_2024_04_18_12_16_48_pkey'),
        Index('spritzones_2024_04_18_12_16_48_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    linecode = mapped_column(String(254))
    name = mapped_column(String(254))
    doc = mapped_column(String(254))
    comment = mapped_column(String(254))
    area = mapped_column(Numeric)
    geom = mapped_column(NullType)


class State(Base):
    __tablename__ = 'state'
    __table_args__ = (
        CheckConstraint("geometrytype(the_geom) = 'MULTIPOLYGON'::text OR the_geom IS NULL", name='enforce_geotype_the_geom'),
        CheckConstraint('st_ndims(the_geom) = 2', name='enforce_dims_the_geom'),
        CheckConstraint('st_srid(the_geom) = 4269', name='enforce_srid_the_geom'),
        PrimaryKeyConstraint('statefp', name='pk_tiger_state'),
        UniqueConstraint('gid', name='uidx_tiger_state_gid'),
        UniqueConstraint('stusps', name='uidx_tiger_state_stusps'),
        Index('idx_tiger_state_the_geom_gist', 'the_geom')
    )

    gid = mapped_column(Integer, nullable=False)
    statefp = mapped_column(String(2))
    stusps = mapped_column(String(2), nullable=False)
    region = mapped_column(String(2))
    division = mapped_column(String(2))
    statens = mapped_column(String(8))
    name = mapped_column(String(100))
    lsad = mapped_column(String(2))
    mtfcc = mapped_column(String(5))
    funcstat = mapped_column(String(1))
    aland = mapped_column(BigInteger)
    awater = mapped_column(BigInteger)
    intptlat = mapped_column(String(11))
    intptlon = mapped_column(String(12))
    the_geom = mapped_column(NullType)


class StateLookup(Base):
    __tablename__ = 'state_lookup'
    __table_args__ = (
        PrimaryKeyConstraint('st_code', name='state_lookup_pkey'),
        UniqueConstraint('abbrev', name='state_lookup_abbrev_key'),
        UniqueConstraint('name', name='state_lookup_name_key'),
        UniqueConstraint('statefp', name='state_lookup_statefp_key')
    )

    st_code = mapped_column(Integer)
    name = mapped_column(String(40))
    abbrev = mapped_column(String(3))
    statefp = mapped_column(CHAR(2))


class StreetTypeLookup(Base):
    __tablename__ = 'street_type_lookup'
    __table_args__ = (
        PrimaryKeyConstraint('name', name='street_type_lookup_pkey'),
        Index('street_type_lookup_abbrev_idx', 'abbrev')
    )

    name = mapped_column(String(50))
    is_hw = mapped_column(Boolean, nullable=False, server_default=text('false'))
    abbrev = mapped_column(String(50))


class Tabblock(Base):
    __tablename__ = 'tabblock'
    __table_args__ = (
        CheckConstraint("geometrytype(the_geom) = 'MULTIPOLYGON'::text OR the_geom IS NULL", name='enforce_geotype_geom'),
        CheckConstraint('st_ndims(the_geom) = 2', name='enforce_dims_geom'),
        CheckConstraint('st_srid(the_geom) = 4269', name='enforce_srid_geom'),
        PrimaryKeyConstraint('tabblock_id', name='tabblock_pkey')
    )

    gid = mapped_column(Integer, nullable=False)
    tabblock_id = mapped_column(String(16))
    statefp = mapped_column(String(2))
    countyfp = mapped_column(String(3))
    tractce = mapped_column(String(6))
    blockce = mapped_column(String(4))
    name = mapped_column(String(20))
    mtfcc = mapped_column(String(5))
    ur = mapped_column(String(1))
    uace = mapped_column(String(5))
    funcstat = mapped_column(String(1))
    aland = mapped_column(Double(53))
    awater = mapped_column(Double(53))
    intptlat = mapped_column(String(11))
    intptlon = mapped_column(String(12))
    the_geom = mapped_column(NullType)


class Tabblock20(Base):
    __tablename__ = 'tabblock20'
    __table_args__ = (
        PrimaryKeyConstraint('geoid', name='pk_tabblock20'),
    )

    geoid = mapped_column(String(15))
    statefp = mapped_column(String(2))
    countyfp = mapped_column(String(3))
    tractce = mapped_column(String(6))
    blockce = mapped_column(String(4))
    name = mapped_column(String(10))
    mtfcc = mapped_column(String(5))
    ur = mapped_column(String(1))
    uace = mapped_column(String(5))
    uatype = mapped_column(String(1))
    funcstat = mapped_column(String(1))
    aland = mapped_column(Double(53))
    awater = mapped_column(Double(53))
    intptlat = mapped_column(String(11))
    intptlon = mapped_column(String(12))
    the_geom = mapped_column(NullType)
    housing = mapped_column(Double(53))
    pop = mapped_column(Double(53))


class Topology(Base):
    __tablename__ = 'topology'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='topology_pkey'),
        UniqueConstraint('name', name='topology_name_key')
    )

    id = mapped_column(Integer)
    name = mapped_column(String, nullable=False)
    srid = mapped_column(Integer, nullable=False)
    precision = mapped_column(Double(53), nullable=False)
    hasz = mapped_column(Boolean, nullable=False, server_default=text('false'))

    layer: Mapped[List['Layer']] = relationship('Layer', uselist=True, back_populates='topology')


class TpuRvMetroPolygon(Base):
    __tablename__ = 'tpu_rv_metro_polygon'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='tpu_rv_metro_polygon_pkey'),
        Index('tpu_rv_metro_polygon_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    reg_num = mapped_column(String(10))
    vid_ppt = mapped_column(String(100))
    name = mapped_column(String(254))
    vid_doc_ra = mapped_column(String(100))
    num_doc_ra = mapped_column(String(100))
    data_doc_r = mapped_column(Date)
    zakazchik = mapped_column(String(100))
    ispolnitel = mapped_column(String(100))
    istoch_fin = mapped_column(String(100))
    otvetst_mk = mapped_column(String(50))
    num_kontra = mapped_column(String(50))
    data_kontr = mapped_column(Date)
    vid_doc_ut = mapped_column(String(100))
    num_doc_ut = mapped_column(String(50))
    data_doc_u = mapped_column(Date)
    priostanov = mapped_column(String(100))
    zaversheni = mapped_column(String(100))
    otmena = mapped_column(String(100))
    status = mapped_column(String(50))
    grup1 = mapped_column(String(100))
    grup2 = mapped_column(String(100))
    oasi = mapped_column(String(20))
    us_ppt = mapped_column(String(10))
    sppgns_obs = mapped_column(String(100))
    sppgns_jil = mapped_column(String(100))
    sppgns_nej = mapped_column(String(100))
    shape_area = mapped_column(Numeric)
    geom = mapped_column(NullType)


class TpzNew(Base):
    __tablename__ = 'tpz_new'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='tpz_new_pkey'),
        Index('tpz_new_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    podzone_nu = mapped_column(String(25))
    num_pp = mapped_column(String(50))
    doc_date = mapped_column(Date)
    type = mapped_column(String(50))
    plotnost = mapped_column(String(50))
    vysota = mapped_column(String(50))
    proczastro = mapped_column(String(50))
    area = mapped_column(Numeric)
    geom = mapped_column(NullType)


class TpzOld(Base):
    __tablename__ = 'tpz_old'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='tpz_old_pkey'),
        Index('tpz_old_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    plotnost = mapped_column(String(50))
    vysota = mapped_column(String(50))
    proczastro = mapped_column(String(50))
    podzone_nu = mapped_column(String(25))
    num_pp = mapped_column(String(50))
    doc_date = mapped_column(Date)
    type = mapped_column(String(50))
    area = mapped_column(Numeric)
    geom = mapped_column(NullType)


class Tract(Base):
    __tablename__ = 'tract'
    __table_args__ = (
        CheckConstraint("geometrytype(the_geom) = 'MULTIPOLYGON'::text OR the_geom IS NULL", name='enforce_geotype_geom'),
        CheckConstraint('st_ndims(the_geom) = 2', name='enforce_dims_geom'),
        CheckConstraint('st_srid(the_geom) = 4269', name='enforce_srid_geom'),
        PrimaryKeyConstraint('tract_id', name='tract_pkey')
    )

    gid = mapped_column(Integer, nullable=False)
    tract_id = mapped_column(String(11))
    statefp = mapped_column(String(2))
    countyfp = mapped_column(String(3))
    tractce = mapped_column(String(6))
    name = mapped_column(String(7))
    namelsad = mapped_column(String(20))
    mtfcc = mapped_column(String(5))
    funcstat = mapped_column(String(1))
    aland = mapped_column(Double(53))
    awater = mapped_column(Double(53))
    intptlat = mapped_column(String(11))
    intptlon = mapped_column(String(12))
    the_geom = mapped_column(NullType)


class TzNew(Base):
    __tablename__ = 'tz_new'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='tz_new_pkey'),
        Index('tz_new_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    zone_num = mapped_column(String(20))
    num_pp = mapped_column(String(50))
    doc_date = mapped_column(Date)
    type = mapped_column(String(50))
    index_ = mapped_column(String(254))
    vri_540 = mapped_column(String(254))
    area = mapped_column(Numeric)
    geom = mapped_column(NullType)


class TzOld(Base):
    __tablename__ = 'tz_old'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='tz_old_pkey'),
        Index('tz_old_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    zone_num = mapped_column(String(20))
    num_pp = mapped_column(String(50))
    doc_date = mapped_column(Date)
    type = mapped_column(String(50))
    index_ = mapped_column(String(254))
    vri_540 = mapped_column(String(254))
    area = mapped_column(Numeric)
    geom = mapped_column(NullType)


class UchastkiMegevania(Base):
    __tablename__ = 'uchastki_megevania'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='uchastki_megevania_pkey'),
        Index('uchastki_megevania_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    numberarea = mapped_column(Integer)
    descr = mapped_column(String(254))
    klass = mapped_column(String(254))
    func_use = mapped_column(String(254))
    n_kvar = mapped_column(String(50))
    n_parc = mapped_column(String(50))
    year = mapped_column(String(50))
    area = mapped_column(Numeric)
    shape_area = mapped_column(Numeric)
    geom = mapped_column(NullType)


class UdsBridges(Base):
    __tablename__ = 'uds_bridges'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='uds_bridges_pkey'),
        Index('uds_bridges_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    name_obj = mapped_column(String(6))
    state = mapped_column(String(254))
    vid = mapped_column(String(254))
    name = mapped_column(String(80))
    shape_leng = mapped_column(Numeric)
    shape_area = mapped_column(Numeric)
    geom = mapped_column(NullType)


class UdsRoads(Base):
    __tablename__ = 'uds_roads'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='uds_roads_pkey'),
        Index('uds_roads_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    name_obj = mapped_column(String(4))
    name_str = mapped_column(String(254))
    vid_road = mapped_column(String(254))
    ext_name = mapped_column(String(254))
    shape_leng = mapped_column(Numeric)
    shape_area = mapped_column(Numeric)
    geom = mapped_column(NullType)


class User(Base):
    __tablename__ = 'user'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='user_pkey'),
        Index('ix_user_email', 'email', unique=True)
    )

    email = mapped_column(String, nullable=False)
    is_active = mapped_column(Boolean, nullable=False)
    is_superuser = mapped_column(Boolean, nullable=False)
    id = mapped_column(Integer)
    hashed_password = mapped_column(String, nullable=False)
    full_name = mapped_column(String)

    item: Mapped[List['Item']] = relationship('Item', uselist=True, back_populates='owner')


class Zcta5(Base):
    __tablename__ = 'zcta5'
    __table_args__ = (
        CheckConstraint("geometrytype(the_geom) = 'MULTIPOLYGON'::text OR the_geom IS NULL", name='enforce_geotype_the_geom'),
        CheckConstraint('st_ndims(the_geom) = 2', name='enforce_dims_the_geom'),
        CheckConstraint('st_srid(the_geom) = 4269', name='enforce_srid_the_geom'),
        PrimaryKeyConstraint('zcta5ce', 'statefp', name='pk_tiger_zcta5_zcta5ce'),
        UniqueConstraint('gid', name='uidx_tiger_zcta5_gid')
    )

    gid = mapped_column(Integer, nullable=False)
    statefp = mapped_column(String(2), nullable=False)
    zcta5ce = mapped_column(String(5), nullable=False)
    classfp = mapped_column(String(2))
    mtfcc = mapped_column(String(5))
    funcstat = mapped_column(String(1))
    aland = mapped_column(Double(53))
    awater = mapped_column(Double(53))
    intptlat = mapped_column(String(11))
    intptlon = mapped_column(String(12))
    partflg = mapped_column(String(1))
    the_geom = mapped_column(NullType)


class ZipLookup(Base):
    __tablename__ = 'zip_lookup'
    __table_args__ = (
        PrimaryKeyConstraint('zip', name='zip_lookup_pkey'),
    )

    zip = mapped_column(Integer)
    st_code = mapped_column(Integer)
    state = mapped_column(String(2))
    co_code = mapped_column(Integer)
    county = mapped_column(String(90))
    cs_code = mapped_column(Integer)
    cousub = mapped_column(String(90))
    pl_code = mapped_column(Integer)
    place = mapped_column(String(90))
    cnt = mapped_column(Integer)


t_zip_lookup_all = Table(
    'zip_lookup_all', metadata,
    Column('zip', Integer),
    Column('st_code', Integer),
    Column('state', String(2)),
    Column('co_code', Integer),
    Column('county', String(90)),
    Column('cs_code', Integer),
    Column('cousub', String(90)),
    Column('pl_code', Integer),
    Column('place', String(90)),
    Column('cnt', Integer)
)


class ZipLookupBase(Base):
    __tablename__ = 'zip_lookup_base'
    __table_args__ = (
        PrimaryKeyConstraint('zip', name='zip_lookup_base_pkey'),
    )

    zip = mapped_column(String(5))
    state = mapped_column(String(40))
    county = mapped_column(String(90))
    city = mapped_column(String(90))
    statefp = mapped_column(String(2))


class ZipState(Base):
    __tablename__ = 'zip_state'
    __table_args__ = (
        PrimaryKeyConstraint('zip', 'stusps', name='zip_state_pkey'),
    )

    zip = mapped_column(String(5), nullable=False)
    stusps = mapped_column(String(2), nullable=False)
    statefp = mapped_column(String(2))


class ZipStateLoc(Base):
    __tablename__ = 'zip_state_loc'
    __table_args__ = (
        PrimaryKeyConstraint('zip', 'stusps', 'place', name='zip_state_loc_pkey'),
    )

    zip = mapped_column(String(5), nullable=False)
    stusps = mapped_column(String(2), nullable=False)
    place = mapped_column(String(100), nullable=False)
    statefp = mapped_column(String(2))


class Zouit(Base):
    __tablename__ = 'zouit'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='zouit_pkey'),
        Index('zouit_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    cad_num = mapped_column(String(254))
    okrug = mapped_column(String(254))
    raion_pos = mapped_column(String(254))
    vid_zouit = mapped_column(String(254))
    type_zone = mapped_column(String(254))
    name = mapped_column(String(254))
    ogran = mapped_column(String(254))
    doc = mapped_column(String(254))
    area = mapped_column(Numeric)
    geom = mapped_column(NullType)


class Zu(Base):
    __tablename__ = 'zu'
    __table_args__ = (
        PrimaryKeyConstraint('gid', name='zu_pkey'),
        Index('zu_geom_idx', 'geom')
    )

    gid = mapped_column(Integer)
    cadastra2 = mapped_column(String(80))
    address = mapped_column(String(254))
    hasvalid5 = mapped_column(String(80))
    hascadas6 = mapped_column(String(80))
    isdraft = mapped_column(String(80))
    ownershi8 = mapped_column(Numeric)
    is_stroy = mapped_column(String(80))
    is_nonca20 = mapped_column(Numeric)
    area = mapped_column(Numeric)
    geom = mapped_column(NullType)


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


class Item(Base):
    __tablename__ = 'item'
    __table_args__ = (
        ForeignKeyConstraint(['owner_id'], ['user.id'], name='item_owner_id_fkey'),
        PrimaryKeyConstraint('id', name='item_pkey')
    )

    id = mapped_column(Integer)
    title = mapped_column(String, nullable=False)
    owner_id = mapped_column(Integer, nullable=False)
    description = mapped_column(String)

    owner: Mapped['User'] = relationship('User', back_populates='item')


class Layer(Base):
    __tablename__ = 'layer'
    __table_args__ = (
        ForeignKeyConstraint(['topology_id'], ['topology.id'], name='layer_topology_id_fkey'),
        PrimaryKeyConstraint('topology_id', 'layer_id', name='layer_pkey'),
        UniqueConstraint('schema_name', 'table_name', 'feature_column', name='layer_schema_name_table_name_feature_column_key')
    )

    topology_id = mapped_column(Integer, nullable=False)
    layer_id = mapped_column(Integer, nullable=False)
    schema_name = mapped_column(String, nullable=False)
    table_name = mapped_column(String, nullable=False)
    feature_column = mapped_column(String, nullable=False)
    feature_type = mapped_column(Integer, nullable=False)
    level = mapped_column(Integer, nullable=False, server_default=text('0'))
    child_id = mapped_column(Integer)

    topology: Mapped['Topology'] = relationship('Topology', back_populates='layer')
