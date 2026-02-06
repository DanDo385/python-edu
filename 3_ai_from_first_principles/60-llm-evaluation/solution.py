"""Project 49: LLM Evaluation - SOLUTION"""

import torch
import math
from collections import Counter


def compute_bleu(reference, candidate, n=4):
    """Compute BLEU score."""
    if len(candidate) == 0:
        return 0.0
    
    # Precision for each n-gram order
    precisions = []
    for i in range(1, n + 1):
        ref_ngrams = Counter(zip(*[reference[j:] for j in range(i)]))
        cand_ngrams = Counter(zip(*[candidate[j:] for j in range(i)]))
        
        matches = sum((ref_ngrams & cand_ngrams).values())
        total = sum(cand_ngrams.values())
        
        if total == 0:
            return 0.0
        precisions.append(matches / total)
    
    # Brevity penalty
    bp = min(1.0, len(candidate) / len(reference)) if len(reference) > 0 else 0.0
    
    # Geometric mean
    bleu = bp * math.exp(sum(math.log(p) for p in precisions) / len(precisions))
    return bleu


def compute_perplexity(log_probs):
    """Compute perplexity from log probabilities."""
    if isinstance(log_probs, torch.Tensor):
        log_probs = log_probs.tolist()
    mean_log_prob = sum(log_probs) / len(log_probs)
    perplexity = math.exp(-mean_log_prob)
    return perplexity
