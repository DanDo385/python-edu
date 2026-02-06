"""Project 45: Tokenization - SOLUTION"""

class SimpleTokenizer:
    """Simple tokenizer implementation."""
    
    def __init__(self, vocab):
        self.vocab = vocab
        self.id_to_token = {v: k for k, v in vocab.items()}
    
    def encode(self, text):
        """Convert text to token IDs."""
        tokens = text.lower().split()
        return [self.vocab.get(token, self.vocab.get('<unk>', 0)) for token in tokens]
    
    def decode(self, token_ids):
        """Convert token IDs to text."""
        tokens = [self.id_to_token.get(id, '<unk>') for id in token_ids]
        return ' '.join(tokens)
