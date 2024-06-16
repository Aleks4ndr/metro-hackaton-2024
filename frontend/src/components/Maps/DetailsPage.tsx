import React from 'react';
import { Box, Flex } from '@chakra-ui/react';
import { useParams } from '@tanstack/react-router';
import MapHeader from './DetailsHeader';
import ParcelProperties from './ParcelProperties';
import BodyTabs from './ParcelBodyTabs';

const DetailsPage: React.FC = () => {
  const { gid } = useParams<{ gid: string }>();

  console.log("gid: ", gid);
  
  // Fetch or use passed data based on id
  // Example data structure:
  const exampleData = {
    geometry: {
      type: "Polygon",
      coordinates: [
        [
          [37.618423, 55.751244],
          [37.628453, 55.751244],
          [37.628453, 55.765244],
          [37.618423, 55.765244],
          [37.618423, 55.751244]
        ]
      ]
    },
    properties: {
      address: "г. Москва, пос. Внуковское, п. Внуково, ул. Зеленая, влд. 14А",
      area: "1065.15195000",
      gid: gid,
      // Add more properties as needed
    }
  };

  return (
    <Box p={4}>
      <Flex mb={4}>
        <Box flex="1">
          <MapHeader geometry={exampleData.geometry} />
        </Box>
        <Box flex="1" ml={4}>
          <ParcelProperties properties={exampleData.properties} />
        </Box>
      </Flex>
      <Box>
        <BodyTabs />
      </Box>
    </Box>
  );
};

export default DetailsPage;
