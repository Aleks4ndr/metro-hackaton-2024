import React, { useEffect, useRef, useState } from 'react';
import { MapContainer, TileLayer, GeoJSON, LayersControl } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import { ZuDetailsData } from './types.ts';

const layerColors = [
  '#FF5733', '#33FF57', '#3357FF', '#F333FF',
  '#FF33A1', '#33FFA1', '#A133FF', '#FFD700',
  '#FF5733', '#33FF57', '#3357FF', '#F333FF',
  '#FF33A1', '#33FFA1'
];

const layerStyle = (ind: number) => {
  return {
    color: layerColors[ind],
    weight: 2,
    fillColor: layerColors[ind],
    fillOpacity: 0.5,
  }
}

interface MapHeaderProps {
  ZuDetails: ZuDetailsData;
}

const MapHeader: React.FC<MapHeaderProps> = ({ ZuDetails }) => {
  


  const mapRef = useRef<L.Map>(null);
  const ZuRef = useRef<L.GeoJSON>();
  const RayonRef = useRef<L.GeoJSON>();
  const OkrugRef = useRef<L.GeoJSON>();
  const BridgesRef = useRef<L.GeoJSON>();
  const KrtRef = useRef<L.GeoJSON>();
  const MkdRef = useRef<L.GeoJSON>();
  const OksRef = useRef<L.GeoJSON>();
  const OoztRef = useRef<L.GeoJSON>();
  const Pzz_tpzRef = useRef<L.GeoJSON>();
  const Pzz_tzRef = useRef<L.GeoJSON>();
  const RoadsRef = useRef<L.GeoJSON>();
  const RspRef = useRef<L.GeoJSON>();
  const SpritRef = useRef<L.GeoJSON>();
  const ZouitRef = useRef<L.GeoJSON>();

  const updateGeoJSONData = (Ref, Data) => {
    if (Ref.current) {
      Ref.current.clearLayers();
      Ref.current.addData(Data);
    }
  };

  const [isInitialized, setIsInitialized ] = useState(false);
  useEffect(() => {
    setIsInitialized(true);
  }, []);

  useEffect(() => {
    if (mapRef.current) {
      mapRef.current.fitBounds(L.geoJSON(ZuDetails.zu).getBounds());
      updateGeoJSONData(ZuRef, ZuDetails.zu!);
      updateGeoJSONData(RayonRef, ZuDetails.rayon!);
      updateGeoJSONData(OkrugRef, ZuDetails.okrug!);
      updateGeoJSONData(BridgesRef, ZuDetails.bridges!);
      updateGeoJSONData(KrtRef, ZuDetails.krt!);
      updateGeoJSONData(MkdRef, ZuDetails.mkd!);
      updateGeoJSONData(OksRef, ZuDetails.oks!);
      updateGeoJSONData(OoztRef, ZuDetails.oozt!);
      updateGeoJSONData(Pzz_tpzRef, ZuDetails.pzz_tpz!);
      updateGeoJSONData(Pzz_tzRef, ZuDetails.pzz_tz!);
      updateGeoJSONData(RoadsRef, ZuDetails.roads!);
      updateGeoJSONData(RspRef, ZuDetails.rsp!);
      updateGeoJSONData(SpritRef, ZuDetails.sprit!);
      updateGeoJSONData(ZouitRef, ZuDetails.zouit!);
    }
  }, [isInitialized, ZuDetails]);

  return (
    <MapContainer ref={mapRef} style={{ height: '300px', width: '100%' }} attributionControl={false}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
      <LayersControl position="topright">
        <LayersControl.Overlay name="Земельный участок" checked>
          <GeoJSON data={ZuDetails.zu!} ref={ZuRef} style={layerStyle(0)} /> 
        </LayersControl.Overlay>
        <LayersControl.Overlay name="ОКС">
          <GeoJSON data={ZuDetails.oks!} ref={OksRef} style={layerStyle(1)} /> 
        </LayersControl.Overlay>
        <LayersControl.Overlay name="Округ">
          <GeoJSON data={ZuDetails.okrug!} ref={OkrugRef} style={layerStyle(2)}/> 
        </LayersControl.Overlay>
        <LayersControl.Overlay name="Район">
          <GeoJSON data={ZuDetails.rayon!} ref={RayonRef} style={layerStyle(3)}/> 
        </LayersControl.Overlay>
        <LayersControl.Overlay name="КРТ" >
          <GeoJSON data={ZuDetails.krt!} ref={KrtRef} style={layerStyle(4)}/> 
        </LayersControl.Overlay>
        <LayersControl.Overlay name="Мосты">
          <GeoJSON data={ZuDetails.bridges!} ref={BridgesRef} style={layerStyle(5)}/> 
        </LayersControl.Overlay>
        <LayersControl.Overlay name="МКД">
          <GeoJSON data={ZuDetails.mkd!} ref={MkdRef} style={layerStyle(6)}/> 
        </LayersControl.Overlay>
        <LayersControl.Overlay name="ООЗТ">
          <GeoJSON data={ZuDetails.oozt!} ref={OoztRef} style={layerStyle(7)}/> 
        </LayersControl.Overlay>
        <LayersControl.Overlay name="Дороги" >
          <GeoJSON data={ZuDetails.roads!} ref={RoadsRef} style={layerStyle(8)}/> 
        </LayersControl.Overlay>
        <LayersControl.Overlay name="Стартовые площадки реновации">
          <GeoJSON data={ZuDetails.rsp!} ref={RspRef} style={layerStyle(9)}/> 
        </LayersControl.Overlay>
        <LayersControl.Overlay name="СПРИТ">
          <GeoJSON data={ZuDetails.sprit!} ref={SpritRef} style={layerStyle(10)}/> 
        </LayersControl.Overlay>
        <LayersControl.Overlay name="ЗОУИТ">
          <GeoJSON data={ZuDetails.zouit!} ref={ZouitRef} style={layerStyle(11)}/> 
        </LayersControl.Overlay>
        <LayersControl.Overlay name="ПЗЗ (ТЗ)">
          <GeoJSON data={ZuDetails.pzz_tz!} ref={Pzz_tzRef} style={layerStyle(12)}/> 
        </LayersControl.Overlay>
        <LayersControl.Overlay name="ПЗЗ (ТПЗ)">
          <GeoJSON data={ZuDetails.pzz_tz!} ref={Pzz_tpzRef} style={layerStyle(13)}/> 
        </LayersControl.Overlay>
      </LayersControl>
      
    </MapContainer>
  );
};

export default MapHeader;
