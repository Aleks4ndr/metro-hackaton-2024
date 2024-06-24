// src/components/DetailsComponent.tsx

import React from 'react';
import { Box, Heading, Text } from '@chakra-ui/react';

interface DetailsComponentProps {
    parcelData: any;
}

const DetailsComponent: React.FC<DetailsComponentProps> = ({ parcelData }) => {
    return (
        <Box>
            <Heading size="md" mb={4}>Land Parcel Details</Heading>
            {parcelData && (
                <Box>
                    {/* Render details of the parcel */}
                    <Text>Parcel ID: {parcelData.id}</Text>
                    <Text>Name: {parcelData.properties.name}</Text>
                    {/* Add more fields as required */}
                </Box>
            )}
        </Box>
    );
};

export default DetailsComponent;
