# Bible NLP Analysis

A **Natural Language Processing (NLP) project** that analyzes biblical text to identify the most frequently used words across different books of the HOLY BIBLE. The project includes **data extraction, cleaning, visualization**, and a **Streamlit-based front-end** for interactive exploration.

---

## 📌 Table of Contents
- [Introduction](#introduction)
- [Data Collection](#data-collection)
- [Data Cleaning & Preprocessing](#data-cleaning--preprocessing)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Visualization & Insights](#visualization--insights)
- [Building the Streamlit App](#building-the-streamlit-app)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## 📖 Introduction
This project performs **NLP analysis** on the **Bible** to analyze word frequencies across different books. It follows a structured workflow:

✅ **Extract** text using APIs/web scraping.  
✅ **Clean** and preprocess the text.  
✅ **Analyze** word frequencies and patterns.  
✅ **Visualize** the results using word clouds and bar charts.  
✅ **Develop** an interactive Streamlit app.  

## Data Collection
For this project, the biblical text was fetched using the Bible API. We used the Bible API (bible-api.com) and structured it into JSON format. The data consists of:  
- **Book**: The name of the book (e.g., Genesis, Exodus).  
- **Chapter**: The chapter number.  
- **Reference**: The verse reference.  
- **Text**: The actual biblical text content.

## 🧹 Data Cleaning & Preprocessing
To ensure accurate analysis, the text undergoes multiple preprocessing steps:

### ✅ Steps Involved:
1. **Lowercasing** – Convert all text to lowercase for uniformity.
2. **Removing Punctuation & Special Characters** – Clean unnecessary symbols.
3. **Tokenization** – Split text into individual words.
4. **Stopwords Removal** – Remove common words like *"the"*, *"and"*, *"of"*, etc.
5. **Lemmatization** – Convert words to their base form (e.g., *running* → *run*).

## 🔍 Exploratory Data Analysis (EDA)
After cleaning the dataset, we conduct **Exploratory Data Analysis (EDA)** to gain insights into the text structure, word usage, and distribution.

### 📊 Key Analyses:
1. **Word Frequency Analysis**  
   - Identify the most frequently occurring words across different books of the Bible.
   - Generate bar plots of the top words.

2. **Word Cloud Visualization**  
   - Create a visual representation of the most common words.
   - Helps in quickly identifying dominant themes.

3. **Book-Wise Word Distribution**  
   - Compare the vocabulary usage across different books.

### **Code Implementation**
📌 **Notebook**: `notebooks/2_Cleaning_and_Analysis.ipynb`

## 🎛️ Building the Streamlit App - https://bible-nlp-analysis.streamlit.app/

After performing Exploratory Data Analysis (EDA), we develop an interactive **Streamlit web app** to visualize and analyze the Bible text dynamically.

📌 **Supporting Script**: `notebooks/3_streamlit_code.py`  

## Future Improvements
1. **Phrase-Level Analysis**– Instead of individual words, analyze meaningful phrases.
2. **Sentiment Analysis**- Determine sentiment across different books.
3. **Topic Modeling**- Identify recurring themes in the Bible.

## Author
Sehaj Malhotra

Master’s in Data Analytics Engineering – Northeastern University

LinkedIn - https://www.linkedin.com/in/sehajmalhotra/
