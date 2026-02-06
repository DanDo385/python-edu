"""Project 48: Prompt Engineering - SOLUTION"""

def create_few_shot_prompt(examples, query):
    """Create few-shot prompt with examples."""
    prompt_parts = []
    for inp, out in examples:
        prompt_parts.append(f"Input: {inp}\nOutput: {out}")
    prompt_parts.append(f"Input: {query}\nOutput:")
    return "\n\n".join(prompt_parts)


def create_chain_of_thought_prompt(query):
    """Create chain-of-thought prompt."""
    return f"Let's think step by step.\n\nQuestion: {query}\n\nStep-by-step reasoning:"
