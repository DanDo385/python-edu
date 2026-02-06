# Solution in Words: Control Flow and Loops

## How to Think About This Problem

### Understanding Conditionals

Think of conditionals as decision points in your program—like choosing which path to take at a fork in the road.

**Mental Model:**
```
If condition is True:
    Take path A
Else:
    Take path B
```

### Step-by-Step Thinking Process

#### 1. Making Decisions with If/Elif/Else

**What we're doing:** Checking conditions and executing different code based on the result.

**How to think about it:**
- Start with the most specific condition first
- Work your way to more general cases
- Use `elif` for multiple related conditions
- Use `else` as a catch-all for everything else

**Example thought process for FizzBuzz:**
- "First, check if divisible by BOTH 3 and 5" → Most specific case
- "If not, check if divisible by 3" → One condition
- "If not, check if divisible by 5" → Other condition
- "Otherwise, just use the number" → Default case

**Order matters!** If you check "divisible by 3" before "divisible by both", you'll never catch the "both" case.

#### 2. Using For Loops

**What we're doing:** Repeating an action for each item in a sequence.

**How to think about it:**
- Identify what you're iterating over (numbers, items in a list, characters in a string)
- Decide what to do with each item
- Consider if you need the index or just the value

**Example thought process for summing 1 to N:**
- "I need to go through numbers 1, 2, 3, ..., N" → Use range(1, N+1)
- "For each number, add it to a running total" → Initialize sum = 0, then sum += number
- "After all numbers, return the total" → Return sum

#### 3. Using While Loops

**What we're doing:** Repeating an action as long as a condition is true.

**How to think about it:**
- Identify the condition that must be true to continue
- Make sure something changes inside the loop (or it runs forever!)
- Consider what happens when the condition becomes false

**Example thought process:**
- "Keep going while count < 10" → Condition: count < 10
- "Inside loop, do something and increment count" → count += 1
- "When count reaches 10, condition becomes False, loop stops" → Exit condition

**Danger:** Infinite loops happen when the condition never becomes False!

#### 4. Break and Continue

**What we're doing:** Controlling loop execution flow.

**Break:** "Stop the loop right now, don't check anything else"
- Use when you've found what you're looking for
- Exits the entire loop immediately

**Continue:** "Skip the rest of this iteration, go to the next one"
- Use when you want to skip certain items
- Stays in the loop, just moves to next iteration

**Example thought process:**
- "I'm searching for a number. When I find it, I can stop" → Use break
- "I want to process numbers, but skip negative ones" → Use continue

### Common Patterns

#### Pattern 1: Accumulator Pattern
Start with an initial value, then accumulate results in a loop.

**Thinking:**
1. Initialize accumulator (sum = 0, product = 1, result = [])
2. Loop through items
3. Update accumulator with each item
4. Return accumulator

**Example:** Summing numbers
```
sum = 0              # Start with nothing
for num in numbers:  # Go through each number
    sum = sum + num  # Add it to the total
return sum           # Give back the total
```

#### Pattern 2: Conditional Accumulation
Only add items that meet certain criteria.

**Thinking:**
1. Initialize accumulator
2. Loop through items
3. Check condition
4. If condition true, update accumulator
5. Return accumulator

**Example:** Sum only even numbers
```
sum = 0
for num in numbers:
    if num % 2 == 0:  # Is it even?
        sum += num    # Only add if even
return sum
```

#### Pattern 3: Early Exit
Stop as soon as you find what you're looking for.

**Thinking:**
1. Loop through items
2. Check if current item matches what you want
3. If yes, return it or break
4. If no, continue to next item

**Example:** Find first even number
```
for num in numbers:
    if num % 2 == 0:  # Found it!
        return num    # Stop and return
# If we get here, no even number found
```

### FizzBuzz Thinking Process

**Problem:** For numbers 1 to N, print "Fizz" if divisible by 3, "Buzz" if divisible by 5, "FizzBuzz" if divisible by both, otherwise print the number.

**Step-by-step thinking:**

1. **Loop through numbers 1 to N**
   - Use `for i in range(1, N+1)`

2. **Check conditions in the right order:**
   - First: Is it divisible by BOTH 3 and 5? (Most specific)
     - Check: `i % 3 == 0 and i % 5 == 0`
     - If yes: "FizzBuzz"
   - Second: Is it divisible by 3? (One condition)
     - Check: `i % 3 == 0`
     - If yes: "Fizz"
   - Third: Is it divisible by 5? (Other condition)
     - Check: `i % 5 == 0`
     - If yes: "Buzz"
   - Otherwise: Just the number itself
     - Else: `i`

3. **Why this order?**
   - If we check "divisible by 3" first, we'd catch 15 and say "Fizz" before checking "also divisible by 5"
   - By checking "both" first, we catch the special case before the individual cases

### Edge Cases to Consider

1. **Empty sequences:** What if the list/range is empty? Loop won't execute—is that okay?
2. **Zero:** Is 0 included? `range(0, N)` starts at 0, `range(1, N+1)` starts at 1
3. **Negative numbers:** How do comparisons work with negatives?
4. **Infinite loops:** While loops that never terminate—always ensure condition changes
5. **Off-by-one errors:** `range(1, N)` gives 1 to N-1, use `range(1, N+1)` for 1 to N

### Problem-Solving Strategy

1. **Understand the problem:** What are you trying to accomplish?
2. **Identify the pattern:** Is this a counting problem? A search? A transformation?
3. **Choose the right loop:** For known iterations → `for`, For conditional → `while`
4. **Plan the conditions:** What decisions need to be made? In what order?
5. **Handle edge cases:** What about empty inputs? Zero? Negative numbers?
6. **Test mentally:** Walk through with small examples (N=5, N=15)

### Example: Complete Thought Process

**Problem:** "Find the sum of all even numbers from 1 to N"

**Thinking:**
1. I need to look at numbers from 1 to N → `for i in range(1, N+1)`
2. I only want even numbers → Check `i % 2 == 0`
3. I need to add them up → Use accumulator pattern
4. Start with sum = 0
5. For each number, if it's even, add it to sum
6. Return the sum

**Code structure:**
```
sum = 0                    # Start with nothing
for i in range(1, N+1):    # Look at each number
    if i % 2 == 0:         # Is it even?
        sum = sum + i      # Add it to total
return sum                 # Give back the total
```

This systematic approach helps you break down any control flow problem into manageable steps.

