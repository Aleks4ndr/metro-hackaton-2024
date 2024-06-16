import React, { useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup, useMapEvents } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import CommentForm from './CommentForm';

interface MapComponentProps {
  data: { id: number, lat: number, lng: number, name: string, description: string }[];
  onMapClick: (latlng: { lat: number, lng: number }) => void;
}

const MapComponent: React.FC<MapComponentProps> = ({ data, onMapClick }) => {
  const [selectedObject, setSelectedObject] = useState<{ id: number } | null>(null);

  useMapEvents({
    click: (e) => {
      onMapClick(e.latlng);
    },
  });

  const handleCommentSubmit = (comment: { text: string }) => {
    console.log('Comment submitted:', comment);
    // Handle comment submission (e.g., send to backend)
  };

  return (
    <MapContainer center={[51.505, -0.09]} zoom={13} style={{ height: "100vh", width: "100%" }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      {data.map((obj) => (
        <Marker key={obj.id} position={[obj.lat, obj.lng]} eventHandlers={{
          click: () => setSelectedObject(obj),
        }}>
          <Popup>
            {obj.name} <br /> {obj.description}
            {selectedObject?.id === obj.id && <CommentForm onSubmit={handleCommentSubmit} />}
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
};

export default MapComponent;
