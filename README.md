📰 New York Times Headline Analyzer (Made in Replit)
This project demonstrates the use of Python to collect, clean, and analyze historical headline data from the New York Times Archive API. It compares coverage between two major health events — the 1918 Spanish Flu and the 2020 COVID-19 pandemic — by analyzing headline trends, word frequency, monetary references, and sentiment.

📁 Project Structure
data_collection.py
Fetches NYT headlines for October 1918 and October 2020 using the Archive API. Extracts and cleans the article titles, saving them to titles_1918.txt and titles_2020.txt.

analysis.py
Analyzes the text data by:
Counting the 10 most frequent words (after removing stopwords)
Calculating how often the keywords "flu", "virus", and "death" appear
Extracting and summing all dollar amounts mentioned in headlines
Performing sentiment analysis using VADER

🔧 Technologies Used
Python
Requests (for API access)
Regular Expressions
VADER Sentiment Analyzer (vaderSentiment)
NYT Archive API
dotenv (for secure API key storage)

📊 Example Insights (Your Output May Vary)
Most common words in 1918 vs. 2020 headlines
Percentage of articles mentioning “flu”, “virus”, or “death”
Total dollar amounts referenced in each period
Average sentiment score per time period

Setup
Get an API key at developer.nytimes.com
Store your key securely in a .env file
Install Dependencies (pip install requests python-dotenv vaderSentiment)
Run data_collection.py and ananlysis.py
