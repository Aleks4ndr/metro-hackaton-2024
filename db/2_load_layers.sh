#!/bin/bash

shp2pgsql -d -D -I -s 998001:4326 /data/_1_ZU/ZU.shp ZU | psql -h "$POSTGRES_SERVER" -U "$POSTGRES_USER" -d "$POSTGRES_DB"
echo "step 1"
shp2pgsql -d -D -I -W "UTF8" -s 998001:4326 /data/_2_OKS/OKS.shp OKS | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 2 -"
shp2pgsql -d -D -I -s 998001:4326 /data/_3_ZOUIT/ZOUIT.shp ZOUIT | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 3"
shp2pgsql -d -D -I -s 998002:4326 /data/_4_SPRIT/spritzones_2024_04_18_12_16_48.shp spritzones_2024_04_18_12_16_48 | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 4"
shp2pgsql -d -D -I -W "WINDOWS-1251" -s 998001:4326 /data/_5_UDS/UDS_bridges.shp UDS_bridges | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 5"
shp2pgsql -d -D -I -W "WINDOWS-1251" -s 998001:4326 /data/_5_UDS/UDS_roads.shp UDS_roads | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 6"
shp2pgsql -d -D -I -s 998001:4326 /data/_6_RSP/RSP.shp RSP | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 7"
shp2pgsql -d -D -I -s 998001:4326 /data/_7_PZZ_ZONES/TZ_new.shp TZ_new | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 8"
shp2pgsql -d -D -I -s 998001:4326 /data/_7_PZZ_ZONES/TZ_old.shp TZ_old | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 9"
shp2pgsql -d -D -I -s 998001:4326 /data/_8_PZZ_SUBZONES/TPZ_new.shp TPZ_new | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 10"
shp2pgsql -d -D -I -s 998001:4326 /data/_8_PZZ_SUBZONES/TPZ_old.shp TPZ_old | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 11"
shp2pgsql -d -D -I -s 998001:4326 /data/_9_KRT/KRT.shp KRT | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 12"
shp2pgsql -d -D -I -W "WINDOWS-1251" -s 998001:4326 /data/_10_Okrug_Rayon/okrug.shp okrug | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 13"
shp2pgsql -d -D -I -W "WINDOWS-1251" -s 998001:4326 /data/_10_Okrug_Rayon/rayon.shp rayon | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 14"
shp2pgsql -d -D -I -W "WINDOWS-1251" -s 998001:4326 /data/_11_Uchastki_megevania_kvartalov/uchastki_megevania.shp uchastki_megevania | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 15"
shp2pgsql -d -D -I -s 998001:4326 /data/_12_OOZT/OOZT.shp OOZT | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 16"
shp2pgsql -d -D -I -W "WINDOWS-1251" -s 998001:4326 /data/_13_PPT/kvartal_region.shp kvartal_region | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 17"
shp2pgsql -d -D -I -W "WINDOWS-1251" -s 998001:4326 /data/_13_PPT/PP_GAZ.shp PP_GAZ | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 18"
shp2pgsql -d -D -I -W "WINDOWS-1251" -s 998001:4326 /data/_13_PPT/PP_METRO_ALL.shp PP_METRO_ALL | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 19"
shp2pgsql -d -D -I -W "WINDOWS-1251" -s 998001:4326 /data/_13_PPT/PPT_ALL.shp PPT_ALL | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 20"
shp2pgsql -d -D -I -W "WINDOWS-1251" -s 998001:4326 /data/_13_PPT/PPT_UDS.shp PPT_UDS | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 21"
shp2pgsql -d -D -I -W "WINDOWS-1251" -s 998001:4326 /data/_13_PPT/TPU_RV_METRO_Polygon.shp TPU_RV_METRO_Polygon | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 22"
shp2pgsql -d -D -I -s 998001:4326 /data/_14_Kadastr_delenie/Kadastr_delenie.shp Kadastr_delenie | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "step 23"
shp2pgsql -d -D -I -W "KOI8R" -s 998001:4326 /data/_15_MKD/MKD.shp MKD | psql -U $POSTGRES_USER -d $POSTGRES_DB
echo "done"
