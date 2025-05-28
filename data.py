#Chih-Hsueh Hsieh 
import re
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#imported from link
data_stopwords = requests.get(
  "https://gist.githubusercontent.com/larsyencken/1440509/raw//stopwords.txt"
).text

def remove_stopwords(input_string):
  dict_stopwords = {}
  for val in data_stopwords.split("\n"):
    dict_stopwords[val.strip()] = 1
  output_string = ""
  for word in input_string.lower().split():
    if (word in dict_stopwords):
      continue
    output_string += word + " "
  output_string = output_string.strip()
  return output_string
#functiont to count frequent words
def frequent_words(file_name):
    with open(file_name, 'r') as file:
        titles = file.readlines()
    #removes the stopped words from frequent words
    words = [remove_stopwords(title) for title in titles]
    all_words = ' '.join(words).split()
  #counts the word and adds to count
    tmp_list = {}
    for word in all_words:
      tmp_list[word] = tmp_list.get(word, 0) + 1
    #prints the word and the count
    print(f"\n************************\nMost frequent words in {file_name}\n************************\n")
    sorted_list= sorted(tmp_list.items(), key=lambda x: x[1], reverse=True)
    #prints only the top 10 words
    for word, count in sorted_list[:10][::-1]:
        print(f"{word}, {count}")
#function to calcuate the appearances the words in variable
def calculate_fraction_appearance(file_name):
    words = 'flu', 'virus', 'death'
    with open(file_name, 'r') as file:
        titles = file.readlines()
    #puts titles in one string
    all_titles = ' '.join(titles).lower()
    #counts the occurances that are similar
    tmp_list = {}
    for word in all_titles.split():
      tmp_list[word] = tmp_list.get(word, 0) + 1
    #fraction the appearance
    fractions = {}
    for word in words:
        fractions[word] = tmp_list.get(word, 0) / len(tmp_list)
    print(f"\n************************\nFraction of articles in {file_name}\n************************\n")
    for word, fraction in fractions.items():
        print(f"{word} {fraction:.3f}")
def extract_dollar_amounts(title):
    #regular expression to caculate dollar
    matches = re.findall(r'\$([1-9]\d*|0)(\.\d+)?', title)
    return [float(match[0].replace(',', '')) for match in matches]
def calculate_dollar_amounts(file_name):
    with open(file_name, 'r') as file:
        titles = file.readlines()
    #calculat total
    total_dollars = sum([sum(extract_dollar_amounts(title)) for title in titles])
    print(f"\n************************\nDollar amounts {file_name}\n************************\n")
    print(f"{file_name} ${total_dollars:,.0f}")

def calculate_sentiment(file_name):
  #opens file
    with open(file_name, 'r') as file:
        titles = file.readlines()
    analyzer = SentimentIntensityAnalyzer()
    #semtiment score test
    scores = [analyzer.polarity_scores(title)['compound'] for title in titles]
    #calcuates average
    sentiment = sum(scores) / len(scores)
    print(f"\n************************\nSentiment {file_name}\n************************\n")
    print(f"The average sentiment of the articles is {sentiment:.3f}")

#prints using functions in the alternating order
frequent_words('titles_1918.txt')
frequent_words('titles_2020.txt')
calculate_fraction_appearance('titles_1918.txt')
calculate_fraction_appearance('titles_2020.txt')   
calculate_dollar_amounts('titles_1918.txt')
calculate_dollar_amounts('titles_2020.txt')  
calculate_sentiment('titles_1918.txt')
calculate_sentiment('titles_2020.txt')




