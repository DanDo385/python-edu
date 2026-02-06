"""Project 50: LLM Deployment - SOLUTION"""

class ModelServer:
    """Simple model server for LLM deployment."""
    
    def __init__(self, model):
        self.model = model
        self.request_queue = []
    
    def predict(self, text):
        """Generate prediction for input text."""
        return self.model.generate(text)
    
    def batch_predict(self, texts):
        """Batch prediction for multiple texts."""
        return [self.model.generate(text) for text in texts]
