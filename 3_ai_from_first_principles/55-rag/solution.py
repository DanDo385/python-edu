"""Project 46: RAG - SOLUTION"""

class RAGSystem:
    """RAG system combining retrieval and generation."""
    
    def __init__(self, retriever, generator):
        self.retriever = retriever
        self.generator = generator
    
    def retrieve(self, query, top_k=5):
        """Retrieve relevant documents."""
        return self.retriever.retrieve(query, top_k)
    
    def generate(self, query, context):
        """Generate answer with context."""
        prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
        return self.generator.generate(prompt)
