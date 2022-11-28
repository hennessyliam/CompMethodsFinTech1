# import libraries
import csv
from striprtf.striprtf import rtf_to_text
import matplotlib.pylab as plt
import numpy as np
import pandas as pd


#companies = ['3M Co', 'American Express Co', 'Amgen Inc', 'Apple Inc', 'Boeing Co', 'Caterpillar Inc', 'Chevron Corp', 'Cisco Systems Inc', 'Coca-Cola Co', 'Dow Inc', 'Goldman Sachs Group Inc', 'Home Depot Inc', 'Honeywell International Inc', 'Intel Corp', 'International Business Machines Corp', 'Johnson & Johnson', 'JPMorgan Chase & Co', "McDonald's Corp", 'Merck & Co Inc', 'Microsoft Corp', 'Nike Inc', 'Procter & Gamble Co', 'Salesforce Inc', 'Travelers Companies Inc', 'UnitedHealth Group Inc', 'Verizon Communications Inc', 'Visa Inc', 'Walgreens Boots Alliance Inc', 'Walmart Inc', 'Walt Disney Co']
companies = {'3M Co': [], 'American Express Co': [], 'Amgen Inc': [], 'Apple Inc': [], 'Boeing Co': [], 'Caterpillar Inc': [], 'Chevron Corp': [], 'Cisco Systems Inc': [], 'Coca-Cola Co': [], 'Dow Inc': [], 'Goldman Sachs Group Inc': [], 'Home Depot Inc': [], 'Honeywell International Inc': [], 'Intel Corp': [], 'International Business Machines Corp': [], 'Johnson & Johnson': [], 'JPMorgan Chase & Co': [], "McDonald's Corp": [], 'Merck & Co Inc': [], 'Microsoft Corp': [], 'Nike Inc': [], 'Procter & Gamble Co': [], 'Salesforce Inc': [], 'Travelers Companies Inc': [], 'UnitedHealth Group Inc': [], 'Verizon Communications Inc': [], 'Visa Inc': [], 'Walgreens Boots Alliance Inc': [], 'Walmart Inc': [], 'Walt Disney Co': []}

# count num of positive words in each article
positive_count = 0
negative_count = 0

# find positive word file list
positive_word_file = csv.reader(open('/Users/hennessyliam/CompMethodsFinTech1/6778 Docs/Loughran_Word_Lists/LoughranMcDonald_Positive.csv', 'r'))

# find negative word file list
negative_word_file = csv.reader(open('/Users/hennessyliam/CompMethodsFinTech1/6778 Docs/Loughran_Word_Lists/LoughranMcDonald_Negative.csv', 'r'))

# add positive words to python list
positive_words = []
for row in positive_word_file:
    for word in row:
        positive_words.append(word)

# add negative words to python list
negative_words = []
for row in negative_word_file:
    for word in row:
        negative_words.append(word)


listx = []
listpos = []
listneg = []
listscore = []


def get_sentiment_score(positive_count: int, negative_count: int):
    count = 0
   
# open company article
    with open('/Users/hennessyliam/CompMethodsFinTech1/6778 Docs/Sentiment_Analyzer-main/DJIA_Compiled_Articles/' + company_name + '.RTF', 'r') as f:
        content = f.read()
        text = rtf_to_text(content, encoding='latin-1', errors='ignore').split()


        for word in text:
            count +=1
            if word.upper() in positive_words:
                positive_count += 1
            if word.upper() in negative_words:
                negative_count -= 1
        
        sentiment_score = (positive_count + negative_count)
        score_per_total_words = (positive_count - negative_count) / count

        companies[company_name].append(sentiment_score)
        listx.append(company_name)
        listpos.append(positive_count)
        listneg.append(negative_count)
        listscore.append(sentiment_score)


    print(str(company_name) + " positive sentiment score " + str(positive_count))
    print(str(company_name) + " negative sentiment score " + str(negative_count))
    print(str(company_name) + " total word count " + str(count))
   #print(str(company_name) + " average sentiment score per total number of words " + str(score_per_total_words))
    print("Net sentiment score for " + str(company_name) + " is " + str(positive_count + negative_count))

for company in companies:
    company_name = company
    get_sentiment_score(positive_count, negative_count)
    print("----------------------------------------")


# define x axis as company names and y axis as positive and negative sentiment scores


fig, ax = plt.subplots()

ax.bar(listx, listpos, label='Positive', color='green')
ax.bar(listx, listneg, color='red', label='Negative')
ax.scatter(listx, listscore, color='black', label='Net Sentiment Score')

ax.set_ylabel('Sentiment Score')
ax.set_title('DOW 30 Companies Sentiment Score')
ax.set_xticklabels(labels=listx,rotation=90)

print(companies)

plt.show()






