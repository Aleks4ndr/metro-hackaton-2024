// src/components/MapComponent.tsx

import React, { useEffect } from 'react';
import { MapContainer, TileLayer, GeoJSON, useMap } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

interface MapComponentProps {
    parcelData: any;
    layersData: any[];
}

const MapComponent: React.FC<MapComponentProps> = ({ parcelData, layersData }) => {
    const center = parcelData?.geometry?.coordinates ? 
        [parcelData.geometry.coordinates[1], parcelData.geometry.coordinates[0]] : [0, 0];

    const CenterMap = () => {
        const map = useMap();
        useEffect(() => {
            if (parcelData) {
                map.setView(center, 13);
            }
        }, [map, parcelData]);
        return null;
    };

    return (
        <MapContainer center={center} zoom={13} style={{ height: "400px", width: "100%" }}>
            <CenterMap />
            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            {parcelData && <GeoJSON data={parcelData} />}
            {layersData.map((layer, index) => (
                <GeoJSON key={index} data={layer} />
            ))}
        </MapContainer>
    );
};

export default MapComponent;
