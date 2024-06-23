import {
  Container,
  Heading,
  Box,
  HStack,
  VStack,
  Button,
  Flex
} from "@chakra-ui/react"
import { createFileRoute } from "@tanstack/react-router"
import 'leaflet/dist/leaflet.css';
export const Route = createFileRoute("/_layout/map")({
  component: Page,
})

import React, { useEffect, useRef } from 'react';
import SearchForm from '../../components/Maps/SearchPanel';
import { useState } from 'react'
import { MapContainer, Marker, Popup, TileLayer, useMap, GeoJSON } from 'react-leaflet'
import { ZuPublic } from "../../client";
import { FeatureCollection } from 'geojson';
import { convertFeatures, swapCoordinates } from '../../utils.ts';
import PopupContent from '../../components/Maps/PopupContent';
import L from 'leaflet';
import ReactDOM from 'react-dom';
import { useRouter } from '@tanstack/react-router';

type mapProps = {
  mapData: ZuPublic[];
}
function Map({ mapData = [] }: mapProps) {
  const geoJsonData: FeatureCollection = convertFeatures(mapData);
  const geoJsonRef = useRef<L.GeoJSON>();
  const router = useRouter();

  useEffect(() => {
    if (geoJsonRef.current) {
      geoJsonRef.current.clearLayers();
      geoJsonRef.current.addData(convertFeatures(mapData));
    }
  }, [mapData]);

  const onEachFeature = (feature: any, layer: L.Layer) => {
    layer.on({
      click: () => {
        const popup = L.popup()
          .setLatLng(layer.getBounds().getCenter())
          .setContent(
            `<div style="width: 300px;" id="popup-${feature.properties.gid}"></div>`
          )
          .openOn(layer._map);

        setTimeout(() => {
          const popupElement = document.getElementById(`popup-${feature.properties.gid}`);
          if (popupElement) {
            ReactDOM.render(
              <PopupContent data={feature.properties} onDetailsClick={() => router.navigate(`/details/${feature.properties.gid}`)} />,
              popupElement
            );
          }
        }, 0);
      },
    });
  };


  console.log('Rendering Map: ', mapData);
  return (
    <Box height="80vh" width="100%">
      <MapContainer center={[55.751244, 37.618423]} zoom={13} scrollWheelZoom={true} style={{ height: "100%", width: "100%" }} attributionControl={false}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        <GeoJSON data={geoJsonData} onEachFeature={onEachFeature} ref={geoJsonRef} />
      </MapContainer>
    </Box>
  )
}

import testData from '../../components/Maps/Zu.ts';

function Page() {

  const [view, setView] = useState<'map' | 'list'>('map');

  const [mapData, setMapData] = useState<ZuPublic[]>([]);

  const handleSearch = (data: any) => {
    console.log('Search parameters:', data);
    setMapData(data);
    // Implement search logic here, e.g., API call to fetch filtered data
  };

  // const toggleView = () => {
  //   setView((prevView) => (prevView === 'map' ? 'list' : 'map'));
  // };

  return (

    <HStack width="100%" spacing={4}>
      {/* <Flex width="100%" justify="space-between" align="center"> */}
        <Box  width="20%">
        <SearchForm  onSearch={handleSearch} />
        </Box>
        {/* <Button onClick={toggleView} mb={4}>
          {view === 'map' ? 'Switch to List View' : 'Switch to Map View'}
        </Button> */}
      {/* </Flex> */}
      <Box position="relative" width="100%" height="100%">
        {view === 'map' ? <Map mapData={mapData} /> : <p>List</p>}
      </Box>
    </HStack>
  )
}