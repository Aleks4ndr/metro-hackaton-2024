import React, { useState } from 'react';
import { Button, Input, Textarea } from '@chakra-ui/react';

interface CommentFormProps {
  onSubmit: (comment: { text: string }) => void;
}

const CommentForm: React.FC<CommentFormProps> = ({ onSubmit }) => {
  const [text, setText] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit({ text });
    setText('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <Textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Add a comment"
      />
      <Button type="submit" colorScheme="blue" mt={2}>Submit</Button>
    </form>
  );
};

export default CommentForm;
