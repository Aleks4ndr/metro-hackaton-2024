import React from 'react';
import {useState} from 'react';
import {
    AsyncCreatableSelect,
    AsyncSelect,
    CreatableSelect,
    Select,
    StylesConfig,
    chakraComponents, 
    ChakraStylesConfig,
    
  } from "chakra-react-select";
import { useFormContext, Controller, useController, Control } from 'react-hook-form';
import { FormControl, FormLabel, Box, Text, Checkbox } from '@chakra-ui/react';

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
    multiValue: (base) => ({
      ...base,
      maxWidth: '300px',  // Limit the width of each selected value
      display: 'flex',
      alignItems: 'center',
    }),
    multiValueLabel: (base) => ({
      ...base,
      whiteSpace: 'nowrap',
      overflow: 'hidden',
      textOverflow: 'ellipsis',
    }),
    menu: (base) => ({
      ...base,
      zIndex: 9999,
      width: 'auto',
    }),
    option: (base) => ({
      ...base,
      whiteSpace: 'nowrap',
      overflow: 'hidden',
      textOverflow: 'ellipsis',
    }),
  };
  
  const CustomMultiValue = (props: any) => (
    <chakraComponents.MultiValue {...props}>
      <Box maxW="100%" display="flex" alignItems="center">
        <Text isTruncated>{props.children}</Text>
      </Box>
    </chakraComponents.MultiValue>
  );

  const CustomOption = (props) => (
    <chakraComponents.Option {...props}>
      <Checkbox
        isChecked={props.isSelected}
        mr={2}
        pointerEvents="none"
      />
      {props.label}
    </chakraComponents.Option>
  );

// const customStyles = {
//     container: (provided: any) => ({
//       ...provided,
//     //   width: '100%',
//       width: '300px',
//     }),
//     control: (provided: any) => ({
//       ...provided,
//     //   minWidth: '300px', // Minimum width of the control
//     //   maxWidth: '100%', // Ensure it doesn't exceed the container's width
//       width: '300px',
//     }),
//     menu: (provided: any) => ({
//       ...provided,
//       zIndex: 1000,
//       width: '100%',
//       minWidth: '300px',
//       maxWidth: '350px%',
//     }),
//     option: (provided: any) => ({
//       ...provided,
//       whiteSpace: 'nowrap',
//       overflow: 'hidden',
//       textOverflow: 'ellipsis',
//       maxWidth: '100%',
//     }),
//     multiValue: (provided: any) => ({
//       ...provided,
//       whiteSpace: 'nowrap',
//       overflow: 'hidden',
//       textOverflow: 'ellipsis',
//       maxWidth: '150px%',
//       display: 'flex',
//       alignItems: 'center'
//     }),
//     multiValueLabel: (provided: any) => ({
//         ...provided,
//         whiteSpace: 'nowrap',
//         overflow: 'hidden',
//         textOverflow: 'ellipsis',
//         maxWidth: '150px',
//       }),
//   };

const MultiselectDropdown: React.FC<MultiselectDropdownProps> = ({ name, label, options }) => {
    const { control } = useFormContext();
    const { field } = useController({ name, control });

    const filterOption = (candidate: Option, input: string) => {
        return candidate.label.toLowerCase().includes(input.toLowerCase());
    };

    const [selectedOptions, setSelectedOptions] = useState([]);

    const handleChange = (selected) => {
      setSelectedOptions(selected || []);
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
                        // onChange={handleChange}
                        onChange={(selectedOptions) => field.onChange(selectedOptions)}
                        // value={selectedOptions}
                        components={{ MultiValue: CustomMultiValue, Option: CustomOption }}
                        chakraStyles={customStyles}
                        placeholder="Select options"
                        closeMenuOnSelect={false}
                        onBlur={field.onBlur}
                        value={field.value}

                    />
                )}
            />
        </FormControl>
    );
};

export default MultiselectDropdown;
