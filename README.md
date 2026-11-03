# Email and Phone Number Finder

A Python utility that scans text files to automatically extract and list valid email addresses and phone numbers using Regular Expressions (`re`).

---

## Project Overview

The **Email and Phone Number Finder** script streamlines data extraction tasks by reading raw text from a source file (`sample 1.txt`)[cite: 2] and applying precise regex patterns to isolate contact information[cite: 2].

---

## Features

* **File Input Handling**: Opens and reads unstructured text data directly from a designated file path (`sample 1.txt`)[cite: 2].
* **Email Extraction**: Employs a comprehensive regex pattern (`r'(\b[a-zA-Z0-9._+%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b)'`) combined with `re.findall()` to pull all valid email addresses[cite: 2].
* **Phone Number Extraction**: Utilizes a flexible pattern (`r'(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})'`) to match standard phone formats featuring optional parentheses, periods, hyphens, or spaces[cite: 2].
* **Itemized Output Presentation**: Organizes and displays the discovered emails and phone numbers in a clean, bulleted terminal view[cite: 2].

---

## Code Structure

* `file(filepath)`: Reads the target text file and returns its content as a string[cite: 2].
* `e_pattern(text)`: Extracts all email occurrences matching the defined regex rules[cite: 2].
* `p_pattern(text)`: Extracts all phone number occurrences matching the defined regex rules[cite: 2].
* `main()`: Manages the execution pipeline by loading the file, running both regex extractors, and printing formatted results[cite: 2].

---

## Requirements

* Python 3.x (Relies exclusively on Python's built-in `re` module; no third-party libraries required)[cite: 2].

---

## Usage Instructions

1. Ensure your source text file is named `sample 1.txt` and saved in the same directory as the script[cite: 2].
2. Open your terminal or command prompt in the project folder.
3. Run the script using the command:
   ```bash
   python "Email and number finder.py"
