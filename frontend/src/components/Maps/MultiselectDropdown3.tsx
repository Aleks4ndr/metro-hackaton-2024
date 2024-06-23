import React from 'react';
import Select from 'react-select';
import { useFormContext, Controller } from 'react-hook-form';
import { FormControl, FormLabel } from '@chakra-ui/react';

interface Option {
    value: string | number;
    label: string;
}

interface MultiselectDropdownProps {
    name: string;
    label: string;
    options: Option[];
}

// const customStyles = {
//     container: (provided: any) => ({
//         ...provided,
//         width: '100%',
//     }),
//     menu: (provided: any) => ({
//         ...provided,
//         zIndex: 1000,
//         width: 'max-content',
//         minWidth: '100%',
//     }),
//     option: (provided: any) => ({
//         ...provided,
//         whiteSpace: 'nowrap',
//     }),
// };

const customStyles = {
    container: (provided: any) => ({
      ...provided,
      width: '100%',
    }),
    control: (provided: any) => ({
      ...provided,
      minWidth: '300px', // Minimum width of the control
      maxWidth: '100%', // Ensure it doesn't exceed the container's width
    }),
    menu: (provided: any) => ({
      ...provided,
      zIndex: 1000,
      width: '100%',
      minWidth: '300px',
    }),
    option: (provided: any) => ({
      ...provided,
      whiteSpace: 'nowrap',
      overflow: 'hidden',
      textOverflow: 'ellipsis',
      maxWidth: '100%',
    }),
    multiValue: (provided: any) => ({
      ...provided,
      whiteSpace: 'nowrap',
      overflow: 'hidden',
      textOverflow: 'ellipsis',
      maxWidth: '100%',
    }),
  };

const MultiselectDropdown: React.FC<MultiselectDropdownProps> = ({ name, label, options }) => {
    const { control } = useFormContext();

    const filterOption = (candidate: Option, input: string) => {
        return candidate.label.toLowerCase().includes(input.toLowerCase());
    };

    return (
        <FormControl>
            <FormLabel>{label}</FormLabel>
            <Controller
                name={name}
                control={control}
                render={({ field }) => (
                    <Select
                        {...field}
                        isMulti
                        options={options}
                        filterOption={filterOption}
                        onChange={(selectedOptions) => field.onChange(selectedOptions)}
                        styles={customStyles}
                    />
                )}
            />
        </FormControl>
    );
};

export default MultiselectDropdown;
