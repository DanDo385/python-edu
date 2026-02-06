"""Project 49: LLM Evaluation Metrics"""

def compute_bleu(reference, candidate, n=4):
    """
    Compute BLEU score.
    
    Args:
        reference: Reference text (list of tokens)
        candidate: Generated text (list of tokens)
        n: Maximum n-gram order
    
    Returns:
        BLEU score
    """
    # TODO: Implement BLEU score
    return 0.0


def compute_perplexity(log_probs):
    """
    Compute perplexity from log probabilities.
    
    Args:
        log_probs: Log probabilities for each token
    
    Returns:
        Perplexity score
    """
    # TODO: Implement perplexity
    # Perplexity = exp(-mean(log_probs))
    return 0.0
