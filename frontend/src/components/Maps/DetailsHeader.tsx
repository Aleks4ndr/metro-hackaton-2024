import React, { useEffect, useRef } from 'react';
import { MapContainer, TileLayer, GeoJSON } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import { Feature } from 'geojson';

interface MapHeaderProps {
  geometry: Feature['geometry'];
}

const MapHeader: React.FC<MapHeaderProps> = ({ geometry }) => {
  const mapRef = useRef<L.Map>(null);

  useEffect(() => {
    if (mapRef.current) {
      mapRef.current.fitBounds(L.geoJSON(geometry).getBounds());
    }
  }, [geometry]);

  return (
    <MapContainer ref={mapRef} center={[55.751244, 37.618423]} zoom={13} style={{ height: '300px', width: '100%' }} attributionControl={false}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
      <GeoJSON data={geometry} />
    </MapContainer>
  );
};

export default MapHeader;
