# Solution in Words: Recursion and Divide-and-Conquer

## How to Think About This Problem

### Understanding Recursion

Think of recursion like Russian nesting dolls: each doll contains a smaller version of itself, until you reach the smallest one.

**Mental Model:**
```
Problem → Smaller version of same problem → Even smaller → ... → Base case
```

### Step-by-Step Thinking

#### 1. Identify Base Case

**What we're doing:** Finding the simplest case that doesn't need recursion.

**How to think about it:**
- What's the smallest input?
- What's the answer for that input?
- This stops the recursion

**Example for factorial:**
- Base case: n = 0 or n = 1
- Answer: 1 (by definition)

#### 2. Identify Recursive Case

**What we're doing:** Breaking the problem into smaller versions.

**How to think about it:**
- How can we express this problem in terms of itself?
- What's a smaller version of the same problem?
- How do we combine results?

**Example for factorial:**
- n! = n × (n-1)!
- Smaller problem: (n-1)!
- Combine: multiply n by result of smaller problem

#### 3. Trust the Recursion

**What we're doing:** Assuming the recursive call works correctly.

**How to think about it:**
- Don't trace through every recursive call mentally
- Trust that if you solve the smaller problem correctly, the larger one works
- Focus on: base case + how to combine results

### Common Patterns

#### Pattern 1: Direct Recursion
Function calls itself directly.

**Thinking:**
- Base case: return simple value
- Recursive case: call self with smaller input, combine result

#### Pattern 2: Divide and Conquer
Split problem, solve recursively, combine.

**Thinking:**
- Divide: Split into smaller parts
- Conquer: Solve each part recursively
- Combine: Merge results

### Problem-Solving Strategy

1. **Find base case**: When do we stop?
2. **Find recursive relation**: How does n relate to n-1?
3. **Write function**: Base case + recursive call
4. **Test mentally**: Trace through small example

