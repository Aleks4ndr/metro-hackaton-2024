import React from 'react';
import { MapContainer, TileLayer, Marker, Popup, useMapEvents } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

interface MapComponentProps {
  data: { id: number, lat: number, lng: number, name: string, description: string }[];
  onMapClick: (latlng: { lat: number, lng: number }) => void;
}

const MapComponent: React.FC<MapComponentProps> = ({ data, onMapClick }) => {
  useMapEvents({
    click: (e) => {
      onMapClick(e.latlng);
    },
  });

  return (
    <MapContainer center={[51.505, -0.09]} zoom={13} style={{ height: "100vh", width: "100%" }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      {data.map((obj) => (
        <Marker key={obj.id} position={[obj.lat, obj.lng]}>
          <Popup>
            {obj.name} <br /> {obj.description}
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
};

export default MapComponent;
