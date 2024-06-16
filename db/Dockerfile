FROM postgis/postgis:16-3.4

# Environment variables for PostgreSQL connection
# ENV PGUSER=pg_admin
# ENV PGPASSWORD=pg_password
# ENV PGDATABASE=lct_2024_4
# ENV PGHOST=localhost
# ENV PGPORT=5432

RUN apt update && apt install -y postgis gdal-bin

COPY ./data /data
# COPY ./initscipts/* /docker-entrypoint-initdb.d/

# # Copy the entrypoint script
# COPY entrypoint.sh /docker-entrypoint-initdb.d/entrypoint.sh

# # Make the entrypoint script executable
# RUN chmod +x /docker-entrypoint-initdb.d/entrypoint.sh

# Use the default entrypoint from the PostGIS image
# ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
# CMD ["postgres"]



# RUN shp2pgsql -I -s 4326 your_shapefile.shp your_table_name | psql -d your_database
# RUN shp2pgsql -I -s 32637:4326 data/_1_ZU/ZU.shp ZU | psql -d lct_2024_4
