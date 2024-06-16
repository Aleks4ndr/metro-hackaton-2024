import React, { useState } from 'react';
import { Button, Input, Select } from '@chakra-ui/react';

interface SearchFormProps {
  onSearch: (conditions: any) => void;
}

const SearchForm: React.FC<SearchFormProps> = ({ onSearch }) => {
  const [conditions, setConditions] = useState<any>({});

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setConditions({ ...conditions, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSearch(conditions);
  };

  return (
    <form onSubmit={handleSubmit}>
      <Input name="attribute" placeholder="Attribute" onChange={handleChange} />
      <Select name="layer" onChange={handleChange}>
        <option value="layer1">Layer 1</option>
        <option value="layer2">Layer 2</option>
      </Select>
      <Button type="submit" colorScheme="blue" mt={2}>Search</Button>
    </form>
  );
};

export default SearchForm;
