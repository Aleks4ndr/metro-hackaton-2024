export const emailPattern = {
  value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
  message: "Invalid email address",
}

export const namePattern = {
  value: /^[A-Za-z\s\u00C0-\u017F]{1,30}$/,
  message: "Invalid name",
}

export const passwordRules = (isRequired = true) => {
  const rules: any = {
    minLength: {
      value: 8,
      message: "Password must be at least 8 characters",
    },
  }

  if (isRequired) {
    rules.required = "Password is required"
  }

  return rules
}

export const confirmPasswordRules = (
  getValues: () => any,
  isRequired = true,
) => {
  const rules: any = {
    validate: (value: string) => {
      const password = getValues().password || getValues().new_password
      return value === password ? true : "The passwords do not match"
    },
  }

  if (isRequired) {
    rules.required = "Password confirmation is required";
  }

  return rules;
}

// utils/ewktToGeoJSON.ts
import { wktToGeoJSON } from '@terraformer/wkt';
import { Feature, Geometry, FeatureCollection } from 'geojson';

export const ewktToGeoJSON = (ewkt: string): Feature => {
  const wktWithoutSrid = ewkt.replace(/SRID=\d+;/, ''); // Remove the SRID part if present
  const geojsonFeature = wktToGeoJSON(wktWithoutSrid) as Feature;

  return {
    type: 'Feature',
    geometry: geojsonFeature.geometry as Geometry,
    properties: {}
  };
};


export const convertFeatures = (data: any[]): FeatureCollection => {
  return {
    type: 'FeatureCollection',
    features: data.map(item => ({
      ...ewkbToGeoJSON(item.geom),
      properties: {
        ...item,
        // gid: item.gid,
        // cadastra: item.cadastra2,
        // address: item.address,
        // ownership: item.ownershi8,
        // area: item.area,
        // Add other properties as needed
      },
    })),
  };
};


// import { Feature, Geometry } from 'geojson';
import wkx from 'wkx';

// Function to convert EWKB to GeoJSON
export const ewkbToGeoJSON = (ewkb: string): Feature => {
  // Decode the EWKB string to a Buffer
  const ewkbBuffer = Buffer.from(ewkb, 'hex');
  
  // Parse the EWKB buffer to a geometry object
  const geometry = wkx.Geometry.parse(ewkbBuffer);
  
  // Convert the geometry object to GeoJSON
  const geojson = geometry.toGeoJSON();

  return {
    type: 'Feature',
    geometry: geojson as Geometry,
    properties: {},
  };
};

export const swapCoordinates = (geojson: any) => {
  if (geojson.type === 'FeatureCollection') {
    geojson.features = geojson.features.map((feature: any) => {
      feature.geometry = swapCoordinatesInGeometry(feature.geometry);
      return feature;
    });
  } else if (geojson.type === 'Feature') {
    geojson.geometry = swapCoordinatesInGeometry(geojson.geometry);
  }
  return geojson;
};

const swapCoordinatesInGeometry = (geometry: any) => {
  if (geometry.type === 'Point') {
    geometry.coordinates = swapCoordinatesInArray(geometry.coordinates);
  } else if (geometry.type === 'LineString' || geometry.type === 'MultiPoint') {
    geometry.coordinates = geometry.coordinates.map(swapCoordinatesInArray);
  } else if (geometry.type === 'Polygon' || geometry.type === 'MultiLineString') {
    geometry.coordinates = geometry.coordinates.map((ring: any) => ring.map(swapCoordinatesInArray));
  } else if (geometry.type === 'MultiPolygon') {
    geometry.coordinates = geometry.coordinates.map((polygon: any) =>
      polygon.map((ring: any) => ring.map(swapCoordinatesInArray))
    );
  }
  return geometry;
};

const swapCoordinatesInArray = (coords: number[]) => [coords[1], coords[0]];
