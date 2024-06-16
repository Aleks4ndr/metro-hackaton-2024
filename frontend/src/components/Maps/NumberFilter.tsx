import React, { useState } from 'react';
import {
  Box,
  Checkbox,
  FormControl,
  FormLabel,
  NumberInput,
  NumberInputField,
  VStack,
} from '@chakra-ui/react';

interface NumberFilterProps {
  label: string;
  onChange: (from: number | null, to: number | null, isEnabled: boolean) => void;
}

const NumberFilter: React.FC<NumberFilterProps> = React.memo(({ label, onChange }) => {
  const [from, setFrom] = useState<number | null>(null);
  const [to, setTo] = useState<number | null>(null);
  const [isEnabled, setIsEnabled] = useState(false);

  const handleCheckboxChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setIsEnabled(e.target.checked);
    onChange(from, to, e.target.checked);
  };

  const handleFromChange = (valueAsString: string, valueAsNumber: number) => {
    setFrom(valueAsNumber);
    onChange(valueAsNumber, to, isEnabled);
  };

  const handleToChange = (valueAsString: string, valueAsNumber: number) => {
    setTo(valueAsNumber);
    onChange(from, valueAsNumber, isEnabled);
  };

  return (
    <VStack align="start" spacing={2}>
      <Checkbox isChecked={isEnabled} onChange={handleCheckboxChange}>
        {label}
      </Checkbox>
      <Box pl={4}>
        <FormControl>
          <FormLabel>From</FormLabel>
          <NumberInput
            value={from ?? ""}
            onChange={handleFromChange}
            isDisabled={!isEnabled}
            min={0}
          >
            <NumberInputField />
          </NumberInput>
        </FormControl>
        <FormControl mt={2}>
          <FormLabel>To</FormLabel>
          <NumberInput
            value={to ?? ""}
            onChange={handleToChange}
            isDisabled={!isEnabled}
            min={0}
          >
            <NumberInputField />
          </NumberInput>
        </FormControl>
      </Box>
    </VStack>
  );
});

export default NumberFilter;
