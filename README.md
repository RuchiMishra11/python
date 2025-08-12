# python
learning python
DAY1 NOTES


# **Python Lecture 1 – Beginner-Friendly Notes**

## **What is Python?**

Python is a **programming language** — a way to tell the computer what to do.

Why Python is popular:

* **Simple & Easy** – Syntax (the way you write code) looks like plain English.
* **Free & Open Source** – Anyone can download and use it without paying.
* **High-Level Language** – You don’t need to worry about hardware details like memory addresses; Python handles that for you.
* **Created by Guido van Rossum** in 1991.
* **Portable** – Code you write on one system works on other systems without changes.

💡 **Analogy:**
Think of Python as you speaking English to a translator (the Python interpreter). The translator converts it into the computer’s own language (machine code).

---

### **Cheat Sheet for What is Python**

* **High-level:** Human-friendly, not hardware-focused.
* **Open source:** Free to use & modify.
* **Portable:** Runs anywhere with Python installed.
* **Example:**

```python
print("Hello, World!")
```

---

## **Our First Program**

In Python, the `print()` function is used to display text on the screen.

Example:

```python
print("Hello World")
```

**Explanation:**

* `print` is a built-in function.
* `"Hello World"` is a **string** (text inside quotes).
* When run, it shows:

```
Hello World
```

---

### **Cheat Sheet for Our First Program**

* **Syntax:** `print("text")`
* Text inside quotes → string
* Example:

```python
print("My name is John")
print(2 + 3)
```

---

## **Python Character Set**

The set of characters Python understands:

1. **Letters** – A to Z (uppercase) and a to z (lowercase)
2. **Digits** – 0 to 9
3. **Special Symbols** – `+`, `-`, `*`, `/`, `%`, etc.
4. **Whitespace** – space, tab, newline
5. **Other Characters** – All ASCII & Unicode (e.g., emojis: 😀)

💡 **Example:**

```python
print("Hello 😀")
```

---

### **Cheat Sheet for Python Character Set**

* **Letters:** A-Z, a-z
* **Digits:** 0-9
* **Symbols:** `+ - * / % ** = < >`
* **Whitespace:** ` ` (space), `\t` (tab), `\n` (newline)
* **Unicode:** Supports emojis & symbols

---

## **Variables**

A **variable** is a name that stores data in memory.

Example:

```python
name = "Shradha"
age = 23
price = 25.99
```

* Here, `name`, `age`, and `price` are variables.
* Think of a variable as a **label on a box** where you store values.

---

### **Cheat Sheet for Variables**

* **Syntax:** `variable_name = value`
* **Rules:**

  * Must start with a letter or `_`
  * Cannot start with a number
  * No spaces or special symbols
* Example:

```python
city = "Delhi"
marks = 95
```

---

## **Memory**

When you assign a variable:

```python
name = "Shradha"
```

Python stores `"Shradha"` in memory, and `name` points to it (like a tag).

---

## **Rules for Identifiers**

Identifiers = Names given to variables, functions, etc.

Rules:

1. Start with a letter or `_`
2. Can contain letters, digits, `_`
3. Case-sensitive (`Name` ≠ `name`)
4. No keywords (e.g., you can’t name a variable `for`)

---

### **Cheat Sheet for Identifiers**

✅ Valid: `myName`, `age1`, `_price`
❌ Invalid: `1age`, `my name`, `for`

---

## **Data Types**

In Python:

* **int** → whole numbers (`5`, `-2`)
* **float** → decimal numbers (`3.14`, `-0.5`)
* **str** → text (`"Hello"`)
* **bool** → True or False
* **None** → represents "nothing"

---

### **Cheat Sheet for Data Types**

```python
x = 5          # int
y = 3.14       # float
name = "Ali"   # string
is_happy = True  # boolean
nothing = None   # NoneType
```

---

## **Keywords**

Keywords = Special reserved words in Python with fixed meaning.
Example: `False`, `True`, `None`, `and`, `or`, `if`, `else`, `for`, `while`.

💡 You **cannot** use them as variable names.

---

## **Comments in Python**

Used to explain code; ignored by the computer.

* **Single-line:**

```python
# This is a comment
```

* **Multi-line:**

```python
"""
This is
a multi-line
comment
"""
```

---

## **Types of Operators**

* **Arithmetic:** `+`, `-`, `*`, `/`, `%`, `**`
* **Relational:** `==`, `!=`, `>`, `<`, `>=`, `<=`
* **Assignment:** `=`, `+=`, `-=`, `*=`, `/=`
* **Logical:** `not`, `and`, `or`

---

## **Type Conversion vs Type Casting**

* **Type Conversion:** Python automatically converts data type.

```python
a, b = 1, 2.0
sum = a + b  # int + float → float
```

* **Type Casting:** You manually convert data type.

```python
a, b = 1, "2"
c = int(b)   # "2" → 2
sum = a + c
```

---

## **Input in Python**

`input()` lets you take input from the user.

Example:

```python
name = input("Enter your name: ")   # Always returns string
age = int(input("Enter age: "))     # Convert to int
price = float(input("Enter price: "))  # Convert to float
```

---

## **Practice Problems**

1. Input 2 numbers & print their sum.
2. Input side of square & print area.
3. Input 2 floating numbers & print average.
4. Input 2 integers `a` and `b`, print `True` if `a >= b`, else `False`.

---

