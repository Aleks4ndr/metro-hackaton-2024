import React from 'react';
import { useForm, FormProvider } from 'react-hook-form';
import { Box, Button, HStack, VStack, FormControl, FormLabel, NumberInput, NumberInputField } from '@chakra-ui/react';

interface SearchFormValues {
    searchTerm: string;
    categories: { value: string, label: string }[];
}

interface SearchPanelProps {
    onSearch: (data: SearchFormValues) => void;
}

import MultiSelectDropdown from './MultiselectDropdown3.tsx';

import rayonOptions from './RAYON.ts';
import districtOptions from './DISTRICT.ts';
import vriOptions from './VRI.ts';
import { ZuPublic, ZuService } from "../../client";

// type SearchPanelProps = {
//     onSearch: ((data: ZuPublic[]) => void);
// }

const SearchPanel: React.FC<SearchPanelProps> = ({ onSearch }: SearchPanelProps) => {
    // const [formValues, setFormValues] = useState({
    //     areaFrom: '',
    //     areaTo: '',
    //     districts: [] as number[],
    //     rayon: [] as number[],
    //     vri: [] as string[],
    //     regions: [] as string[],
    //     usageTypes: [] as string[],
    //     ownership: '',
    //     ZPO: [] as string[],
    //     density: '',
    //     height: '',
    //     buildPercent: '',
    //     inPMT: false,
    //     inOOZT: false,
    //     inPPT: false,
    //     KRT: [] as string[],
    //     usageKinds: [] as string[],
    //     minWidth: '',
    //     minLength: '',
    // });

    // const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    //     const { name, value, type, checked } = e.target;
    //     const val = type === 'checkbox' ? checked : value;
    //     setFormValues((prevValues) => ({
    //         ...prevValues,
    //         [name]: val,
    //     }));
    // };

    // const handleMultiSelectChange = (key: string, values: string[]) => {
    //     setFormValues((prevValues) => ({
    //         ...prevValues,
    //         [key]: values,
    //     }));
    // };

    const methods = useForm<SearchFormValues>();
    const { handleSubmit, register, formState } = methods;

    const onSubmit = (data: SearchFormValues) => {
        onSearch(data);
    };

    // const  handleSubmit = async (e: React.FormEvent) => {
    //     e.preventDefault();
    //     console.log('Search parameters:', formValues);

    //     const data = await ZuService.readItems();
    //     onSearch(data.items);



    // };

    return (
        <FormProvider {...methods}>
            <Box as="form" onSubmit={handleSubmit(onSubmit)}>
            <VStack width="100%" spacing={4} align="center">
                {/* <Heading size="lg" textAlign={{ base: "center", md: "left" }} pt={12}>
                    Панель поиска
                </Heading> */}
                <Box p={4} bg="gray.100" borderRadius="md" as="form" onSubmit={handleSubmit}>
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
        </Box>
        </FormProvider>
    );
};

export default SearchPanel;
