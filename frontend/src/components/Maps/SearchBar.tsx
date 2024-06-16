import React, { useState } from 'react';
import {
    Box,
    Button,
    Checkbox,
    FormControl,
    FormLabel,
    HStack,
    Input,
    Select,
    Stack,
    VStack,
    Menu,
    MenuList,
    MenuItem,
    MenuButton,

} from '@chakra-ui/react';

import {
    ChevronDownIcon
} from '@chakra-ui/icons';

interface SearchFormProps {
    onSearch: (params: any) => void;
}

const SearchForm: React.FC<SearchFormProps> = ({ onSearch }) => {
    const [formValues, setFormValues] = useState({
        area_from: '',
        area_to: '',
        type: '',
        region: '',
        district: '',
        location: '',
        properties: {
            singleChoice: '',
            multipleChoice: [] as string[],
            exclude: [] as string[],
        },
    });

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
        const { name, value } = e.target;
        setFormValues((prevValues) => ({
            ...prevValues,
            [name]: value,
        }));
    };

    const handleCheckboxChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value, checked } = e.target;
        setFormValues((prevValues) => ({
            ...prevValues,
            properties: {
                ...prevValues.properties,
                [name]: checked
                    ? [...prevValues.properties[name as keyof typeof formValues.properties], value]
                    : prevValues.properties[name as keyof typeof formValues.properties].filter(
                        (v) => v !== value
                    ),
            },
        }));
    };

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        onSearch(formValues);
    };

    return (
        <Box as="form" onSubmit={handleSubmit} p={4} bg="gray.100" borderRadius="md">
            <VStack spacing={4} align="stretch">

                <HStack>
                    <FormControl id="area">
                        <FormLabel>Площадь:</FormLabel>
                        <Input
                            name="area_from"
                            value={formValues.area_from}
                            onChange={handleInputChange}
                            placeholder="от"
                        />
                        <Input
                            name="area_to"
                            value={formValues.area_to}
                            onChange={handleInputChange}
                            placeholder="до"
                        />
                    </FormControl>
                </HStack>

                <FormControl id="district">
                    <Menu>
                        <MenuButton as={Button} rightIcon={<ChevronDownIcon />}>
                            Округ:
                        </MenuButton>
                        <Box>
                            <MenuList>
                            <MenuItem>
                                <Checkbox
                                    name="district_cao"
                                    value="district_cao"
                                    onChange={handleCheckboxChange}
                                    isChecked={formValues.properties.multipleChoice.includes('district_cao')}
                                >
                                    ЦАО
                                </Checkbox>
                                </MenuItem>
                                <MenuItem>
                                <Checkbox
                                    name="district_zao"
                                    value="district_zao"
                                    onChange={handleCheckboxChange}
                                    isChecked={formValues.properties.multipleChoice.includes('district_zao')}
                                >
                                    ЗАО
                                </Checkbox>
                                </MenuItem>

                                {/* <Select name="type" value={formValues.type} onChange={handleInputChange}>

                                    <MenuItem><option value="district_cao">ЦАО</option></MenuItem>
                                    <MenuItem><option value="district_zao">ЗАО</option></MenuItem>
                                    <MenuItem><option value="district_uao">ЮАО</option></MenuItem>
                                    <MenuItem><option value="district_nao">НАО</option></MenuItem>
                                    <MenuItem><option value="district_sao">САО</option></MenuItem>
                                    <MenuItem><option value="district_vao">ВАО</option></MenuItem>
                                </Select> */}

                            </MenuList>
                        </Box>



                    </Menu>
                    <FormLabel>Округ:</FormLabel>
                    <Select name="type" value={formValues.type} onChange={handleInputChange}>
                        <option value="">Select type</option>
                        <option value="type1">Type 1</option>
                        <option value="type2">Type 2</option>
                    </Select>
                </FormControl>

                <FormControl id="type">
                    <FormLabel>Type</FormLabel>
                    <Select name="type" value={formValues.type} onChange={handleInputChange}>
                        <option value="">Select type</option>
                        <option value="type1">Type 1</option>
                        <option value="type2">Type 2</option>
                    </Select>
                </FormControl>
                <FormControl id="region">
                    <FormLabel>Region</FormLabel>
                    <Input
                        name="region"
                        value={formValues.region}
                        onChange={handleInputChange}
                        placeholder="Enter region"
                    />
                </FormControl>
                <FormControl id="district">
                    <FormLabel>District</FormLabel>
                    <Input
                        name="district"
                        value={formValues.district}
                        onChange={handleInputChange}
                        placeholder="Enter district"
                    />
                </FormControl>
                <FormControl id="location">
                    <FormLabel>Location</FormLabel>
                    <Input
                        name="location"
                        value={formValues.location}
                        onChange={handleInputChange}
                        placeholder="Enter location"
                    />
                </FormControl>
                <FormControl id="properties">
                    <FormLabel>Properties</FormLabel>
                    <Stack spacing={2}>
                        <FormLabel>Single Choice</FormLabel>
                        <Select
                            name="singleChoice"
                            value={formValues.properties.singleChoice}
                            onChange={handleInputChange}
                        >
                            <option value="">Select</option>
                            <option value="property1">Property 1</option>
                            <option value="property2">Property 2</option>
                        </Select>
                        <FormLabel>Multiple Choice</FormLabel>
                        <Stack spacing={1}>
                            <Checkbox
                                name="multipleChoice"
                                value="property1"
                                onChange={handleCheckboxChange}
                                isChecked={formValues.properties.multipleChoice.includes('property1')}
                            >
                                Property 1
                            </Checkbox>
                            <Checkbox
                                name="multipleChoice"
                                value="property2"
                                onChange={handleCheckboxChange}
                                isChecked={formValues.properties.multipleChoice.includes('property2')}
                            >
                                Property 2
                            </Checkbox>
                        </Stack>
                        <FormLabel>Exclude</FormLabel>
                        <Stack spacing={1}>
                            <Checkbox
                                name="exclude"
                                value="property1"
                                onChange={handleCheckboxChange}
                                isChecked={formValues.properties.exclude.includes('property1')}
                            >
                                Property 1
                            </Checkbox>
                            <Checkbox
                                name="exclude"
                                value="property2"
                                onChange={handleCheckboxChange}
                                isChecked={formValues.properties.exclude.includes('property2')}
                            >
                                Property 2
                            </Checkbox>
                        </Stack>
                    </Stack>
                </FormControl>
                <Button type="submit" colorScheme="blue">
                    Search
                </Button>
            </VStack>
        </Box>
    );
};

export default SearchForm;
