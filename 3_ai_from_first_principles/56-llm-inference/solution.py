"""Project 47: LLM Inference - SOLUTION"""

class KVCache:
    """KV cache for efficient inference."""
    
    def __init__(self):
        self.cache = {}
    
    def get(self, layer_id, position):
        key = (layer_id, position)
        return self.cache.get(key)
    
    def set(self, layer_id, position, k, v):
        key = (layer_id, position)
        self.cache[key] = (k, v)
