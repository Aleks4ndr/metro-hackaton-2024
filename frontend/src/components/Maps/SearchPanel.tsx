import React from 'react';
import { useForm, FormProvider } from 'react-hook-form';
import { Box, Button, HStack, VStack, FormControl, FormLabel, NumberInput, NumberInputField } from '@chakra-ui/react';

interface SearchFormValues {
    areaFrom: number;
    areaTo: number;

    vri: { value: string, label: string }[];
    okrug: { value: string, label: number }[];
    rayon: { value: string, label: number }[];
}

interface SearchPanelProps {
    onSearch: (data: SearchFormValues) => void;
}

import MultiSelectDropdown from './MultiselectDropdown4.tsx';

import rayonOptions from './RAYON.ts';
import districtOptions from './DISTRICT.ts';
import vriOptions from './VRI.ts';
import { ZuService } from "../../client";

// type SearchPanelProps = {
//     onSearch: ((data: ZuPublic[]) => void);
// }

const SearchPanel: React.FC<SearchPanelProps> = ({ onSearch }: SearchPanelProps) => {
    const methods = useForm<SearchFormValues>();
    const { handleSubmit, register, control } = methods;

    const onSubmit = async (searchParameters: SearchFormValues) => {
        const data = await ZuService.readItems(searchParameters);
        onSearch(data.items);
    };

    // const  handleSubmit = async (e: React.FormEvent) => {
    //     e.preventDefault();
    //     console.log('Search parameters:', formValues);
    //     const data = await ZuService.readItems();
    //     onSearch(data.items);
    // };

    return (
        <FormProvider {...methods}>
            <VStack width="100%" spacing={4} align="center">
                {/* <Heading size="lg" textAlign={{ base: "center", md: "left" }} pt={12}>
                    Панель поиска
                </Heading> */}
                <Box p={4} bg="gray.100" borderRadius="md" as="form" onSubmit={handleSubmit(onSubmit)}>
                    <VStack spacing={4} align="stretch">
                        <FormControl id="areaFrom">
                            <FormLabel>Площадь от</FormLabel>
                            <NumberInput min={0} {...register('areaFrom')}>
                                <NumberInputField name="areaFrom" />
                            </NumberInput>
                        </FormControl>
                        <FormControl id="areaTo">
                            <FormLabel>Площадь до</FormLabel>
                            <NumberInput min={0} {...register('areaTo')}>
                                <NumberInputField name="areaTo" />
                            </NumberInput>
                        </FormControl>
                        <FormControl id="districts">
                            {/* <FormLabel>Округ</FormLabel> */}
                            <MultiSelectDropdown
                                label="Округ"
                                name="districts"
                                options={districtOptions}
                                control={control}
                                // selectedOptions={formValues.districts}
                                // onChange={(values) => handleMultiSelectChange('districts', values)}
                            />
                        </FormControl>

                        <FormControl id="rayon">
                            {/* <FormLabel>Округ</FormLabel> */}
                            <MultiSelectDropdown
                                label="Район"
                                name="rayon"
                                options={rayonOptions}
                                control={control}
                                // selectedOptions={formValues.rayon}
                                // onChange={(values) => handleMultiSelectChange('rayon', values)}
                            />
                        </FormControl>

                        <FormControl id="vri">
                            {/* <FormLabel>Округ</FormLabel> */}
                            <MultiSelectDropdown
                                label="ВРИ"
                                name="vri"
                                options={vriOptions}
                                control={control}
                                // selectedOptions={formValues.vri}
                                // onChange={(values) => handleMultiSelectChange('vri', values)}
                            />
                        </FormControl>

                        <FormControl id="perimeterToArea">
                            <FormLabel>Мин. ширина:</FormLabel>
                            <NumberInput min={0} {...register('perimeterToArea')}>
                                <NumberInputField name="perimeterToArea" />
                            </NumberInput>
                        </FormControl>
                        <FormControl id="innerCircleRadius">
                            <FormLabel>Мин. длина:</FormLabel>
                            <NumberInput min={0} {...register('innerCircleRadius')}>
                                <NumberInputField name="innerCircleRadius" />
                            </NumberInput>
                        </FormControl>

                        <Button width="100%" margin="10px" padding="10px" type="submit" colorScheme="blue">
                            Поиск
                        </Button>
                    </VStack>
                </Box>
            </VStack>
        </FormProvider>
    );
};

export default SearchPanel;
