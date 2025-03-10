#pip install beautifulsoup4

from bs4 import BeautifulSoup

# Open the HTML file
with open('00_data.html', 'r', encoding='utf-8') as file:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(file, 'html.parser')

# Print the parsed HTML (the entire document as a tree structure)
print(soup.prettify())

# Example of accessing specific HTML elements
title = soup.title.string
print("Title:", title)

h1 = soup.h1.string
print("Heading:", h1)

# Extract and print the list items
items = soup.find_all('li')
for item in items:
    print("List Item:", item.string)
