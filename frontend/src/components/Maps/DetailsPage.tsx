import React from 'react';
import { useEffect, useState } from 'react';
import { Box, Flex } from '@chakra-ui/react';
import { useParams } from '@tanstack/react-router';
import MapHeader from './DetailsHeader';
import ParcelProperties from './ParcelProperties';
import BodyTabs from './ParcelBodyTabs';
import { ZuDetails, ZuService } from "../../client";
import { convertFeatures, swapCoordinates } from '../../utils.ts';
import { Feature, Geometry, FeatureCollection } from 'geojson';

import { ZuDetailsData } from './types.ts';



const DetailsPage: React.FC = () => {
  const { gid } = useParams<{ gid: string }>();
  const [ data, setData ] = useState<ZuDetailsData>({});
  useEffect(() => {
    // declare the data fetching function
    const fetchData = async () => {
      const zuData = await ZuService.readZu(gid);
      const zu = convertFeatures([zuData.zu]);
      const rayon = convertFeatures(zuData.rayon ?? []);
      const okrug = convertFeatures(zuData.okrug ?? []);
      const bridges = convertFeatures(zuData.bidges ?? []);
      const krt = convertFeatures(zuData.krt ?? []);
      const mkd = convertFeatures(zuData.mkd ?? []);
      const oks = convertFeatures(zuData.oks ?? []);
      const oozt = convertFeatures(zuData.oozt ?? []);
      const pzz_tpz = convertFeatures(zuData.pzz_tpz ?? []);
      const pzz_tz = convertFeatures(zuData.pzz_tz ?? []);
      const roads = convertFeatures(zuData.roads ?? []);
      const rsp = convertFeatures(zuData.rsp ?? []);
      const sprit = convertFeatures(zuData.sprit ?? []);
      const zouit = convertFeatures(zuData.zouit ?? []);
      
      setData({zu, rayon, okrug, bridges, krt, mkd, oks, oozt, pzz_tpz, pzz_tz, roads, rsp, sprit, zouit});
    }

    // call the function
    fetchData()
      // make sure to catch any error
      .catch(console.error);
  }, [])
  console.log("gid: ", gid);

  const isObjectFilled = (objectName: any) => {
    return Object.keys(objectName).length > 0
  }

  return ( 
    <Box p={4}> 
    { isObjectFilled(data) && (<>
      <Flex mb={4}>
        <Box flex="1">
          <MapHeader ZuDetails={data} />
        </Box>
        <Box flex="1" ml={4}>
          <ParcelProperties properties={data.zu} />
        </Box>
      </Flex>
      <Box>
        <BodyTabs zuDetails={data} />
      </Box> </>)}
    </Box>
  );
};

export default DetailsPage;
