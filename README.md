# Number Pattern Generator

A simple Python program that generates a number pattern from 1 up to a given positive integer.

This project was built as part of a Python coding lab to practice:
- Functions
- For loops
- Input validation
- String manipulation

---

## 📌 Features

- Generates a sequence of numbers from `1` to `n`
- Returns numbers as a space-separated string
- Validates input type and value
- Handles edge cases gracefully

---

## 🧠 Function Overview

### `number_pattern(n)`

**Parameters:**
- `n` (int): A positive integer

**Returns:**
- A string of numbers from `1` to `n` separated by spaces
- An error message if input is invalid

---

## ✅ Examples

```python
number_pattern(4)
# Output: "1 2 3 4"

number_pattern("4")
# Output: "Argument must be an integer value."

number_pattern(0)
# Output: "Argument must be an integer greater than 0."
