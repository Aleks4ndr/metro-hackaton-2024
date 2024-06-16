import {
  Box,
  Button,
  Checkbox,
  CheckboxGroup,
  Menu,
  MenuButton,
  MenuList,
  MenuItem,
} from '@chakra-ui/react';
import { ChevronDownIcon } from '@chakra-ui/icons';

interface MultiSelectDropdownProps<T> {
  options: { value: T, label: string }[];
  selectedOptions: T[];
  onChange: (selected: T[]) => void;
  buttonText?: string;
}

const MultiSelectDropdown = <T extends unknown>({ options, selectedOptions, onChange, buttonText = "Select Options" }: MultiSelectDropdownProps<T>) => {

  const handleCheckboxChange = (values: T[]) => {
    onChange(values);
  };

  return (
    <Menu closeOnSelect={false}>
      <MenuButton as={Button} rightIcon={<ChevronDownIcon />}>
        {buttonText}
      </MenuButton>
      <MenuList>
        <CheckboxGroup value={selectedOptions} onChange={(values) => handleCheckboxChange(values as T[])}>
          {options.map((option) => (
            <MenuItem key={String(option.value)}>
              <Checkbox value={String(option.value)}>{option.label}</Checkbox>
            </MenuItem>
          ))}
        </CheckboxGroup>
      </MenuList>
    </Menu>
  );
};

export default MultiSelectDropdown;
