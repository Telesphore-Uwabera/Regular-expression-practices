import re

# Sample string response
string_response = "Sample string response containing the data you are looking for"

# Regular expression patterns
movie_title_pattern = r"(.+) \((\d{4})\)"
song_lyrics_pattern = r"\[Verse (\d+)\] (.+)"
twitter_handle_pattern = r"@(\w+)"
isbn_pattern = r"ISBN (\d{3}-\d-\d{3}-\d{5}-\d)"
joke_pattern = r"Why did the (.+) \? Because (.+)"
episode_title_pattern = r"(.+) S(\d{2})E(\d{2}): (.+)"
date_pattern = r"(\d{2})-(\w{3})-(\d{4})"
hex_color_code_pattern = r"#([A-Fa-f0-9]{6})"
ip_address_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

# Extracting movie titles
movie_titles = re.findall(movie_title_pattern, string_response)

# Extracting song lyrics
song_lyrics = re.findall(song_lyrics_pattern, string_response)

# Extracting twitter handles
twitter_handles = re.findall(twitter_handle_pattern, string_response)

# Extracting ISBN numbers
isbn_numbers = re.findall(isbn_pattern, string_response)

# Extracting jokes
jokes = re.findall(joke_pattern, string_response)

# Extracting episode titles
episode_titles = re.findall(episode_title_pattern, string_response)

# Extracting dates
dates = re.findall(date_pattern, string_response)

# Extracting hex color codes
hex_color_codes = re.findall(hex_color_code_pattern, string_response)

# Extracting IP addresses
ip_addresses = re.findall(ip_address_pattern, string_response)

# Printing the extracted data
print("Movie Titles:", movie_titles)
print("Song Lyrics:", song_lyrics)
print("Twitter Handles:", twitter_handles)
print("ISBN Numbers:", isbn_numbers)
print("Jokes:", jokes)
print("Episode Titles:", episode_titles)
print("Dates:", dates)
print("Hex Color Codes:", hex_color_codes)
print("IP Addresses:", ip_addresses)