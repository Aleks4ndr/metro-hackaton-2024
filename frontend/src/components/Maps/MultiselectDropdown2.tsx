import React, { useState, useEffect } from 'react';
import {
  Box,
  Checkbox,
  CheckboxGroup,
  Input,
  VStack,
  Menu,
  MenuButton,
  MenuList,
  MenuItem,
  Button,
  Portal,
} from '@chakra-ui/react';
import { ChevronDownIcon } from '@chakra-ui/icons';

interface MultiSelectDropdownProps<T> {
  label: string;
  options: Array<{ value: T; label: string }>;
  onChange: (selected: T[]) => void;
  selectedOptions: T[];
}

const MultiSelectDropdown = <T,>({ label, options, onChange, selectedOptions }: MultiSelectDropdownProps<T>) => {
  const [isOpen, setIsOpen] = useState(false);
  const [filter, setFilter] = useState('');

  const filteredOptions = options.filter(option =>
    option.label.toLowerCase().includes(filter.toLowerCase())
  );

  const handleCheckboxChange = (value: T) => {
    if (selectedOptions.includes(value)) {
      onChange(selectedOptions.filter(item => item !== value));
    } else {
      onChange([...selectedOptions, value]);
    }
  };

  return (
    <Menu isOpen={isOpen} onClose={() => setIsOpen(false)}>
      <MenuButton as={Button} rightIcon={<ChevronDownIcon />} onClick={() => setIsOpen(!isOpen)}>
        {label}
      </MenuButton>
      <Portal>
        <MenuList zIndex="popover">
          <Box p={2}>
            <Input
              placeholder="Search..."
              value={filter}
              onChange={(e) => setFilter(e.target.value)}
              mb={2}
            />
            <CheckboxGroup value={selectedOptions as unknown as string[]}>
              <VStack align="start" spacing={2}>
                {filteredOptions.map((option) => (
                  <Checkbox
                    key={option.value as unknown as string}
                    onChange={() => handleCheckboxChange(option.value)}
                    isChecked={selectedOptions.includes(option.value)}
                  >
                    {option.label}
                  </Checkbox>
                ))}
              </VStack>
            </CheckboxGroup>
          </Box>
        </MenuList>
      </Portal>
    </Menu>
  );
};

export default MultiSelectDropdown;
