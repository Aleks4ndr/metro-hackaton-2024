import React from 'react';
import { Box, Heading, Text } from '@chakra-ui/react';
import { FeatureCollection } from 'geojson';
interface ParcelPropertiesProps {
  properties: any;
}

const ParcelProperties: React.FC<ParcelPropertiesProps> = ({ properties: FeatureCollection }) => {

  // const zu = properties.properties ?? {};


  return (
    <Box p={4}>
      <Heading size="md">Parcel Properties</Heading>
      <Text><strong>Address:</strong> {properties.address2}</Text>
      <Text><strong>Area:</strong> {properties.area}</Text>
      <Text><strong>gid:</strong> {properties.gid}</Text>
      {/* Add more properties as needed */}
    </Box>
  );
};

export default ParcelProperties;
