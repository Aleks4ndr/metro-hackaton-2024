import React from 'react';
import { Table, Thead, Tbody, Tr, Th, Td, Box } from '@chakra-ui/react';

interface TableComponentProps<T> {
  data: T[];
  headers: Array<keyof T>;
}

const TableComponent = <T extends object>({ data, headers }: TableComponentProps<T>) => {
  if (!data || data.length === 0) {
    return <Box>No data available</Box>;
  }

  return (
    <Box overflowX="auto">
      <Table variant="simple">
        <Thead>
          <Tr>
            {headers.map((header) => (
              <Th key={header as string}>{header as string}</Th>
            ))}
          </Tr>
        </Thead>
        <Tbody>
          {data.map((row, rowIndex) => (
            <Tr key={rowIndex}>
              {headers.map((header) => (
                <Td key={header as string}>{(row as any).properties[header]}</Td>
              ))}
            </Tr>
          ))}
        </Tbody>
      </Table>
    </Box>
  );
};

export default TableComponent;
