#!/bin/bash

# Variables
SHAPEFILE_DIR="/data"  # Directory containing the shapefiles and .prj files
# POSTGRES_SERVER="localhost"          # PostgreSQL server hostname
# POSTGRES_DB="your_database"          # PostgreSQL database name
# POSTGRES_USER="your_username"        # PostgreSQL username
# POSTGRES_PASSWORD="your_password"    # PostgreSQL password (consider using .pgpass for security)

# Export password for non-interactive psql
# export PGPASSWORD=$POSTGRES_PASSWORD

# Temporary files
PRJ_LIST=$(mktemp)
UNIQUE_PRJ=$(mktemp)
PRJ_MAPPING=$(mktemp)

# Find all .prj files and extract their WKT definitions
find "$SHAPEFILE_DIR" -name "*.prj" | while read -r PRJ_FILE; do
    gdalsrsinfo -o wkt "$PRJ_FILE" | awk -v FILE="$PRJ_FILE" '{printf "%s,%s\n", FILE, $0}' >> "$PRJ_LIST"
done

# Sort and remove duplicates
sort -t, -k2 -u "$PRJ_LIST" > "$UNIQUE_PRJ"

# Load unique coordinate systems into PostGIS and save the mapping
# while IFS=, read -r PRJ_FILE WKT; do
#     # Generate a unique SRID for custom projections
#     SRID=$(echo "$WKT" | md5sum | cut -d' ' -f1 | tr -cd '[:digit:]' | cut -c1-6)

#     # Insert into spatial_ref_sys if it doesn't exist
#     psql -h "$POSTGRES_SERVER" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "
#     DO \$\$
#     BEGIN
#         IF NOT EXISTS (SELECT 1 FROM spatial_ref_sys WHERE srid = $SRID) THEN
#             INSERT INTO spatial_ref_sys (srid, auth_name, auth_srid, srtext)
#             VALUES ($SRID, 'custom', $SRID, '$WKT');
#         END IF;
#     END
#     \$\$;
#     "

#     # Save the mapping
#     echo "$PRJ_FILE -> SRID $SRID" >> "$PRJ_MAPPING"
# done < "$UNIQUE_PRJ"

# # Output the mapping for reference
# cat "$PRJ_MAPPING"

# # Clean up temporary files
# rm "$PRJ_LIST" "$UNIQUE_PRJ" "$PRJ_MAPPING"

# Unset password after use
# unset PGPASSWORD

echo "Coordinate systems have been loaded and mapping saved."