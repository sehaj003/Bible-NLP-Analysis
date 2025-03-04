import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter

# Load the cleaned Bible data
with open("bible_cleaned.json", "r") as f:
    bible_data = json.load(f)

# Prepare book-wise word frequencies
book_word_freq = {}
for book in set(entry["book"] for entry in bible_data):
    book_words = []
    for entry in bible_data:
        if entry["book"] == book:
            book_words.extend(entry["cleaned_text"].split())

    book_word_freq[book] = Counter(book_words).most_common(10)

# Streamlit UI
st.title("Bible Keyword Frequency Explorer 📖✨")

# Book selection
book_list = sorted(book_word_freq.keys())
selected_book = st.selectbox("Select a Book:", book_list)

# Get top words for the selected book
top_words = book_word_freq[selected_book]
df = pd.DataFrame(top_words, columns=["Word", "Count"])

# Display results
st.subheader(f"Most Common Words in {selected_book}")
st.dataframe(df)

# Bar Chart
st.subheader("Word Frequency Bar Chart")
plt.figure(figsize=(8, 4))
sns.barplot(x=df["Word"], y=df["Count"], palette="viridis")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title(f"Top 10 Words in {selected_book}")
st.pyplot(plt)

# Word Cloud
st.subheader("Word Cloud Visualization")
wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(dict(top_words))
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
st.pyplot(plt)
