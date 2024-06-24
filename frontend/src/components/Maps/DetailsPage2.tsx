// src/App.tsx

import React, { useEffect, useState } from 'react';
import { Container, Grid, Box } from '@chakra-ui/react';
import MapComponent from './DetailsMap';
import DetailsComponent from './DetailsComponent';
import TabsComponent from './TabsComponent';
import axios from 'axios';

const App: React.FC = () => {
    const [parcelData, setParcelData] = useState<any>(null);
    const [layersData, setLayersData] = useState<{ [key: string]: any[] }>({});

    useEffect(() => {
        // Fetch the land parcel data
        axios.get('/path-to-your-geojson-file').then(response => {
            setParcelData(response.data);
        });

        // Fetch the other layers data
        const layerNames = ['layer1', 'layer2', 'layer3']; // Replace with your actual layer names
        layerNames.forEach(layerName => {
            axios.get(`/path-to-${layerName}-geojson-file`).then(response => {
                setLayersData(prevData => ({
                    ...prevData,
                    [layerName]: response.data.features
                }));
            });
        });
    }, []);

    return (
        <Container maxW="container.xl">
            <Grid templateColumns="repeat(2, 1fr)" gap={4}>
                <Box>
                    <MapComponent parcelData={parcelData} layersData={Object.values(layersData).flat()} />
                </Box>
                <Box>
                    <DetailsComponent parcelData={parcelData} />
                </Box>
            </Grid>
            <Box mt={4}>
                <TabsComponent layersData={layersData} />
            </Box>
        </Container>
    );
};

export default App;
