# Solution Explanation: LLM Inference

## Overview

KV caching stores computed keys/values to avoid recomputation during generation, significantly speeding up inference.

## Key Points

- Cache keys and values per layer
- Reuse cached values for previous tokens
- Reduces computation during generation
- Essential for efficient LLM inference
