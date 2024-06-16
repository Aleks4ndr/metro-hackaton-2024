import React from 'react';
import { Box, Heading, Text } from '@chakra-ui/react';

interface ParcelPropertiesProps {
  properties: any;
}

const ParcelProperties: React.FC<ParcelPropertiesProps> = ({ properties }) => {
  return (
    <Box p={4}>
      <Heading size="md">Parcel Properties</Heading>
      <Text><strong>Address:</strong> {properties.address}</Text>
      <Text><strong>Area:</strong> {properties.area}</Text>
      <Text><strong>gid:</strong> {properties.gid}</Text>
      {/* Add more properties as needed */}
    </Box>
  );
};

export default ParcelProperties;
