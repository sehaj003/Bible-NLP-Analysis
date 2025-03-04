import requests
import json
import time

def get_bible_verses(book, chapter):
    url = f"https://bible-api.com/{book} {chapter}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

books = ["Genesis", "Exodus", "Psalms", "John", "Revelation"]
bible_data = []

for book in books:
    for chapter in range(1,6):
        data = get_bible_verses(book, chapter)
        if data:
            bible_data.append({
                "reference": data["reference"],
                "text": data["text"],
                "book": book,
                "chapter": chapter
                })

        time.sleep(1)


with open("bible_data.json", "w") as f:
    json.dump(bible_data, f, indent = 4)

print("Bible data saved successfully:")
