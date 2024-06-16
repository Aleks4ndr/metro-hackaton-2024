create table zu_tpz as (
select z.gid as zu_gid, tn.gid as tpz_gid from zu z join tpz_new tn on ST_intersects(z.geom, tn.geom) 

);

CREATE INDEX zu_tpz_zu_gid ON zu_tpz(zu_gid) INCLUDE (tpz_gid);
CREATE INDEX zu_tpz_tpz_gid ON zu_tpz(tpz_gid) INCLUDE (zu_gid);

create table zu_tz as (
select z.gid as zu_gid, tn.gid as tz_gid from zu z join tz_new tn on ST_intersects(z.geom, tn.geom) 

);

CREATE INDEX zu_tz_zu_gid ON zu_tz(zu_gid) INCLUDE (tz_gid);
CREATE INDEX zu_tz_tz_gid ON zu_tz(tz_gid) INCLUDE (zu_gid);

create table zu_zouit as (
select z.gid as zu_gid, tn.gid as zouit_gid from zu z join zouit tn on ST_intersects(z.geom, tn.geom) 

);

CREATE INDEX zu_zouit_zu_gid ON zu_zouit(zu_gid) INCLUDE (zouit_gid);
CREATE INDEX zu_zouit_zouit_gid ON zu_zouit(zouit_gid) INCLUDE (zu_gid);

create table zu_uchastki_megevania as (
select z.gid as zu_gid, tn.gid as uchastok_megevania_gid from zu z join uchastki_megevania tn on ST_intersects(z.geom, tn.geom) 

);

CREATE INDEX zu_uchastki_megevania_zu_gid ON zu_uchastki_megevania(zu_gid) INCLUDE (uchastok_megevania_gid);
CREATE INDEX zu_uchastki_megevania_uchastok_megevania_gid ON zu_uchastki_megevania(uchastok_megevania_gid) INCLUDE (zu_gid);

create table zu_tpu_rv_metro_polygon as (
select z.gid as zu_gid, tn.gid as tpu_rv_metro_gid from zu z join tpu_rv_metro_polygon tn on ST_intersects(z.geom, tn.geom) 

);

CREATE INDEX zu_tpu_rv_metro_polygon_zu_gid ON zu_tpu_rv_metro_polygon(zu_gid) INCLUDE (tpu_rv_metro_gid);
CREATE INDEX zu_tpu_rv_metro_polygon_tpu_rv_metro_gid ON zu_tpu_rv_metro_polygon(tpu_rv_metro_gid) INCLUDE (zu_gid);

create table zu_spritzones as (
select z.gid as zu_gid, tn.gid as spritzone_gid from zu z join spritzones_2024_04_18_12_16_48 tn on ST_intersects(z.geom, tn.geom) 

);

CREATE INDEX zu_spritzones_zu_gid ON zu_spritzones(zu_gid) INCLUDE (spritzone_gid);
CREATE INDEX zu_spritzones_spritzone_gid ON zu_spritzones(spritzone_gid) INCLUDE (zu_gid);

create table zu_rsp as (
select z.gid as zu_gid, tn.gid as rsp_gid from zu z join rsp tn on ST_intersects(z.geom, tn.geom) 

);

CREATE INDEX zu_rsp_zu_gid ON zu_rsp(zu_gid) INCLUDE (rsp_gid);
CREATE INDEX zu_rsp_spritzone_rsp_gid ON zu_rsp(rsp_gid) INCLUDE (zu_gid);

create table zu_rayon as (
select z.gid as zu_gid, tn.gid as rayon_gid from zu z join rayon tn on ST_intersects(z.geom, tn.geom) 

);

CREATE INDEX zu_rayon_zu_gid ON zu_rayon(zu_gid) INCLUDE (rayon_gid);
CREATE INDEX zu_rayon_rayon_gid ON zu_rayon(rayon_gid) INCLUDE (zu_gid);

create table zu_ppt_uds as (
select z.gid as zu_gid, tn.gid as ppt_uds_gid from zu z join ppt_uds tn on ST_intersects(z.geom, tn.geom) 

);

CREATE INDEX zu_ppt_uds_zu_gid ON zu_ppt_uds(zu_gid) INCLUDE (ppt_uds_gid);
CREATE INDEX zu_ppt_uds_ppt_uds_gid ON zu_ppt_uds(ppt_uds_gid) INCLUDE (zu_gid);

create table zu_ppt_all as (
select z.gid as zu_gid, tn.gid as ppt_all_gid from zu z join ppt_all tn on ST_intersects(z.geom, tn.geom) 

);

CREATE INDEX zu_ppt_all_zu_gid ON zu_ppt_all(zu_gid) INCLUDE (ppt_all_gid);
CREATE INDEX zu_ppt_all_ppt_all_gid ON zu_ppt_all(ppt_all_gid) INCLUDE (zu_gid);

create table zu_pp_metro_all as (
select z.gid as zu_gid, tn.gid as pp_metro_gid from zu z join pp_metro_all tn on ST_intersects(z.geom, tn.geom) 

);

CREATE INDEX zu_pp_metro_all_zu_gid ON zu_pp_metro_all(zu_gid) INCLUDE (pp_metro_gid);
CREATE INDEX zu_pp_metro_all_gid ON zu_pp_metro_all(pp_metro_gid) INCLUDE (zu_gid);

create table zu_pp_gaz as (
select z.gid as zu_gid, tn.gid as pp_gaz_gid from zu z join pp_gaz tn on ST_intersects(z.geom, tn.geom) 

);

CREATE INDEX zu_pp_gaz_zu_gid ON zu_pp_gaz(zu_gid) INCLUDE (pp_gaz_gid);
CREATE INDEX zu_pp_gaz_pp_gaz_gid ON zu_pp_gaz(pp_gaz_gid) INCLUDE (zu_gid);

create table zu_oozt as (
select z.gid as zu_gid, tn.gid as oozt_gid from zu z join oozt tn on ST_intersects(z.geom, tn.geom) 

);

CREATE INDEX zu_oozt_zu_gid ON zu_oozt(zu_gid) INCLUDE (oozt_gid);
CREATE INDEX zu_oozt_oozt_gid ON zu_oozt(oozt_gid) INCLUDE (zu_gid);

create table zu_oks as (
select z.gid as zu_gid, tn.gid as oks_gid from zu z join oks tn on ST_intersects(z.geom, st_makevalid(tn.geom)) 

);

CREATE INDEX zu_oks_zu_gid ON zu_oks(zu_gid) INCLUDE (oks_gid);
CREATE INDEX zu_oks_oks_gid ON zu_oks(oks_gid) INCLUDE (zu_gid);

create table zu_okrug as (
select z.gid as zu_gid, tn.gid as okrug_gid from zu z join okrug tn on ST_intersects(z.geom, tn.geom) 

);

CREATE INDEX zu_okrug_zu_gid ON zu_okrug(zu_gid) INCLUDE (okrug_gid);
CREATE INDEX zu_oks_okrug_gid ON zu_okrug(okrug_gid) INCLUDE (zu_gid);

create table zu_mkd as (
select z.gid as zu_gid, tn.gid as mkd_gid from zu z join mkd tn on ST_intersects(z.geom, st_makevalid(tn.geom)) 

);

CREATE INDEX zu_mkd_zu_gid ON zu_mkd(zu_gid) INCLUDE (mkd_gid);
CREATE INDEX zu_mkd_mkd_gid ON zu_mkd(mkd_gid) INCLUDE (zu_gid);

create table zu_kvartal_region as (
select z.gid as zu_gid, tn.gid as kvartal_region_gid from zu z join kvartal_region tn on ST_intersects(z.geom, tn.geom) 

);

CREATE INDEX zu_kvartal_region_zu_gid ON zu_kvartal_region(zu_gid) INCLUDE (kvartal_region_gid);
CREATE INDEX zu_kvartal_region_kvartal_region_gid ON zu_kvartal_region(kvartal_region_gid) INCLUDE (zu_gid);

create table zu_krt as (
select z.gid as zu_gid, tn.gid as krt_gid from zu z join krt tn on ST_intersects(z.geom, tn.geom) 

);

CREATE INDEX zu_krt_zu_gid ON zu_krt(zu_gid) INCLUDE (krt_gid);
CREATE INDEX zu_krt_krt_gid ON zu_krt(krt_gid) INCLUDE (zu_gid);

create table zu_kadastr_delenie as (
select z.gid as zu_gid, tn.gid as kadastr_delenie_gid from zu z join kadastr_delenie tn on ST_intersects(z.geom, tn.geom) 

);

CREATE INDEX zu_kadastr_delenie_zu_gid ON zu_kadastr_delenie(zu_gid) INCLUDE (kadastr_delenie_gid);
CREATE INDEX zu_kadastr_delenie_kadastr_delenie_gid ON zu_kadastr_delenie(kadastr_delenie_gid) INCLUDE (zu_gid);