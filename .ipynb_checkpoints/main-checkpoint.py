import requests
from bs4 import BeautifulSoup
import json

url = "https://archiveofourown.org/users/rounakag/bookmarks"
response = requests.get(url = url)
data = response.content
# Function to extract bookmark data
def extract_bookmark_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Initialize an empty list to store the bookmarks
    bookmarks = []

    # Select all bookmark elements (adjust the selector based on actual HTML structure)
    for bookmark in soup.select('li.bookmark.blurb.group'):
        # Extract the author's name
        author = bookmark.select_one('div.header.module h4 a[rel="author"]').text if bookmark.select_one(
            'div.header.module h4 a[rel="author"]') else 'Unknown'

        # Extract the tags (excluding user-set tags)
        tags = [tag.text for tag in bookmark.select('.tags.commas li a.tag')]

        # Extract user-set tags as well if needed
        user_set_tags = [tag.text for tag in bookmark.select('.meta.tags.commas li a.tag')]

        # Extract the genres (fandom data)
        genres = [genre.text for genre in bookmark.select('h5.fandoms.heading a.tag')]

        # Append the extracted data to the bookmarks list
        bookmarks.append({
            "author's name": author,
            'tags': tags,  # Only user-set tags if needed
            'genres': genres
        })

    return bookmarks


print(extract_bookmark_data(data))

for i in range(5):
    print(extract_bookmark_data(data)[i]["author's name"])



