# Overview

[src/gradebook.py](src/gradebook.py) is a small program that stores students, records their scores, and prints a grade report. It works, but it is hard to read and hard to change.

Your task is to **refactor** it using the practices from Robert C. Martin's (Uncle Bob's) *Clean Code*. Refactoring means improving the structure of the code **without changing what it does**.

# Rules

1. **Keep the behavior the same.** When you finish, running the program must print exactly the same report as it does now.
2. **Do not add features.** Ignore the `TODO` in the file. Weighted categories are not part of this activity.
3. **Work in small steps.** Make one change, run the program, and check the output before you make the next change.

# Getting Started

1. Run the original program and save its output. You will compare against this file later:

   ```bash
   python3 src/gradebook.py > expected_output.txt
   ```

   The report should look like this:

   ```
   ==================================================
   GRADE REPORT
   --------------------------------------------------
   Ada Lovelace        CS      94.5  A
   Alan Turing         CS      82.5  B
   Grace Hopper        CS      94.8  A
   Katherine Johnson   MATH    67.5  D
   Margaret Hamilton   CS      83.3  B
   --------------------------------------------------
   Class average: 84.5 (B)
   Median: 83.3
   Honor roll: Ada Lovelace, Grace Hopper
   --------------------------------------------------
   23 scores recorded
   ==================================================
   ```

2. Read the whole file before you change anything. Make a list of the problems you find.

3. After each change, check that the output has not changed:

   ```bash
   python3 src/gradebook.py | diff expected_output.txt -
   ```

   If `diff` prints nothing, the output is the same. If it prints lines, your last change broke something. Fix it before you continue.

# What to Look For

Use these *Clean Code* topics to guide your review. Each one applies to this file at least once.

| Topic | Questions to ask |
|-------|------------------|
| **Meaningful names** (Ch. 2) | Does each name say what the thing is or does? Are there one-letter names, abbreviations, type prefixes (`strName`), or joke names? Do the names follow Python conventions (`snake_case` for functions and variables, `PascalCase` for classes)? |
| **Functions** (Ch. 3) | Does each function do one thing? Are any functions too long? Do any functions take a flag argument (a `True`/`False` that changes what they do)? Do any take too many arguments? |
| **Comments** (Ch. 4) | Does a comment only repeat what the code says? Is a comment wrong? Is there commented-out code or a change log that version control should track instead? Could a better name replace the comment? |
| **Formatting** (Ch. 5) | Is related code grouped together? Are functions defined near the code that calls them? Is spacing and quoting consistent? |
| **Objects and data structures** (Ch. 6) | Do getters and setters add value, or are they Java habits? Is the class just a bag of data while other functions do its work? |
| **Error handling** (Ch. 7) | Do functions return error codes such as `-1`, `-2`, `-3`, or `None` instead of raising exceptions? |
| **Duplication (DRY)** (Ch. 17) | Is the same logic written more than once? |
| **Magic numbers and globals** (Ch. 17) | Are there unnamed numbers like `90`, `5`, or `50`? Does the code depend on module-level mutable state? |

