# Regular Expression Extractor

This repository contains two Python scripts that demonstrate the use of regular expressions to extract specific patterns from text data. 

## Script 1: `regex_extractor.py`

### Description

`regex_extractor.py` is a Python script that showcases how to use regular expressions to extract various types of information from a given text response. It defines a set of regular expression patterns and then applies them to a sample string response to extract data such as movie titles, song lyrics, Twitter handles, ISBN numbers, jokes, episode titles, dates, hex color codes, and IP addresses.

### Usage

To use the script, follow these steps:

1. Import the `re` module.
2. Define your sample string response containing the data you want to extract.
3. Define regular expression patterns for the types of data you want to extract.
4. Use the `re.findall()` method to extract data using the defined patterns.
5. Print the extracted data for analysis or further processing.

### Example

```python
# Sample string response
string_response = "Sample string response containing the data you are looking for"

# Define regular expression patterns (as shown in the script)
# ...

# Extract data using re.findall()
# ...

# Print the extracted data
# ...
```

### Output

The script will print the extracted data for each defined pattern, making it easy to see the results of the extraction.

## Script 2: `name_matcher.py`

### Description

`name_matcher.py` is a simple Python script that matches and prints names from a list that follow a specific format. It uses a regular expression to identify names that consist of two words, where each word contains only letters and is separated by a space.

### Usage

To use the script, follow these steps:

1. Import the `re` module.
2. Define a list of names you want to match.
3. Define a regular expression pattern for the desired name format.
4. Iterate through the list of names and use `re.search()` to find matches.
5. Print the matched names.

### Example

```python
names = ["Telesphore", "Rib skee", "Drink water free", "Do it though"]

# Define the regular expression pattern (as shown in the script)
regex = "^\w+\s\w+$"

# Iterate through the list of names and print matches
# ...
```

### Output

The script will print the names that match the specified format.

---

These scripts provide practical examples of how regular expressions can be used for text pattern extraction in Python. You can adapt and extend them for your specific data extraction needs.
