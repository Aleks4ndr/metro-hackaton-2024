// PopupContent.tsx
import React from 'react';
import { Box, Heading, Text, Link } from '@chakra-ui/react';

interface PopupContentProps {
  data: any;
}

const PopupContent: React.FC<PopupContentProps> = ({ data }) => {
  return (
    <Box bg="white" width="100%" p={4} maxW="md">
      <Heading size="md" mb={2}>Details</Heading>
      <Text><strong>GID:</strong> {data.gid}</Text>
      <Text><strong>Address:</strong> {data.address}</Text>
      <Text><strong>Area:</strong> {data.area}</Text>
      {/* Add more fields as needed */}
      <Link href={`/details/${data.gid}`} color="teal.500" mt={2} display="block">
        View Details
      </Link>
    </Box>
  );
};

export default PopupContent;
