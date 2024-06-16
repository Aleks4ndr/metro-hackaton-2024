// pages/Details.tsx
import React from 'react';
import { useParams } from '@tanstack/react-router';
import { Button } from '@chakra-ui/react';
import { useNavigate } from '@tanstack/react-router';

const Details: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();

  // Fetch or use passed data based on id
  return (
    <div>
      <h1>Details Page</h1>
      <p>Item ID: {id}</p>
      {/* Add more details about the item here */}
      <Button onClick={() => navigate('../map')}>Back to Map</Button>
    </div>
  );
};

export default Details;
