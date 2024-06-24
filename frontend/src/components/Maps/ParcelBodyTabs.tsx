import React from 'react';
import { Tabs, TabList, TabPanels, Tab, TabPanel, Box } from '@chakra-ui/react';
import { ZuDetailsData } from './types.ts';
import TableComponent from './TableComponent.tsx';


const BodyTabs: React.FC = (zuDetails: ZuDetailsData) => {
  return (
    <Tabs>
      <TabList>
        <Tab>Округ</Tab>
        <Tab>Район</Tab>
        <Tab>ЗОУИТ</Tab>
        <Tab>ООЗТ</Tab>
        <Tab>МКД</Tab>
        <Tab>ОКС</Tab>
        <Tab>СПРИТ</Tab>
        <Tab>КРТ</Tab>
        <Tab>ПЗЗ (ТЗ)</Tab>
        <Tab>ПЗЗ (ТПЗ)</Tab>
        <Tab>Реновация</Tab>
        <Tab>Мосты</Tab>
        <Tab>Дороги</Tab>
      </TabList>
      <TabPanels>
        <TabPanel>
          <TableComponent data={zuDetails.okrug} headers={['gid', 'name', 'label', 'address']}></TableComponent>
          <Box>
            {/* Content for Округ */}
          </Box>
        </TabPanel>
        <TabPanel>
          <Box>
            {/* Content for Район */}
          </Box>
        </TabPanel>
        <TabPanel>
          <Box>
            {/* Content for ЗОУИТ */}
          </Box>
        </TabPanel>
        <TabPanel>
          <Box>
            {/* Content for ООЗТ */}
          </Box>
        </TabPanel>
        <TabPanel>
          <Box>
            {/* Content for МКД */}
          </Box>
        </TabPanel>
        <TabPanel>
          <Box>
            {/* Content for ОКС */}
          </Box>
        </TabPanel>
        <TabPanel>
          <Box>
            {/* Content for СПРИТ */}
          </Box>
        </TabPanel>
        <TabPanel>
          <Box>
            {/* Content for КРТ */}
          </Box>
        </TabPanel>
        <TabPanel>
          <Box>
            {/* Content for ПЗЗ (ТЗ) */}
          </Box>
        </TabPanel>
        <TabPanel>
          <Box>
            {/* Content for ПЗЗ (ТПЗ) */}
          </Box>
        </TabPanel>
        <TabPanel>
          <Box>
            {/* Content for Реновация */}
          </Box>
        </TabPanel>
        <TabPanel>
          <Box>
            {/* Content for Мосты */}
          </Box>
        </TabPanel>
        <TabPanel>
          <Box>
            {/* Content for Дороги */}
          </Box>
        </TabPanel>
      </TabPanels>
    </Tabs>
  );
};

export default BodyTabs;
