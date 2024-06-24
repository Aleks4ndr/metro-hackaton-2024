// src/components/TabsComponent.tsx

import React from 'react';
import { Tabs, TabList, TabPanels, Tab, TabPanel, Box, Text } from '@chakra-ui/react';

interface TabsComponentProps {
    layersData: { [key: string]: any[] };
}

const TabsComponent: React.FC<TabsComponentProps> = ({ layersData }) => {
    return (
        <Tabs>
            <TabList>
                {Object.keys(layersData).map((layerName, index) => (
                    <Tab key={index}>{layerName}</Tab>
                ))}
            </TabList>
            <TabPanels>
                {Object.keys(layersData).map((layerName, index) => (
                    <TabPanel key={index}>
                        <Text fontWeight="bold">{layerName}</Text>
                        <Box>
                            {/* Render layer data as a table or list */}
                            {layersData[layerName].map((feature, featureIndex) => (
                                <Box key={featureIndex} mb={2}>
                                    <Text>{JSON.stringify(feature.properties)}</Text>
                                </Box>
                            ))}
                        </Box>
                    </TabPanel>
                ))}
            </TabPanels>
        </Tabs>
    );
};

export default TabsComponent;
