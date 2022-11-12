class SentimentIntensityAnalyzer(object):
    pass

    def polarity_scores(self, text):
        pass

    def scores(self, text):
        pass

class Scores(object):
    pass


sentence = 'This is a good movie'

scores = SentimentIntensityAnalyzer().polarity_scores(sentence)



# create a new sentiment analyzer
analyzer = SentimentIntensityAnalyzer()
# get the sentiment scores for each sentence
scores = analyzer.polarity_scores(sentence)
# print the scores
print(scores)

# create a new sentiment analyzer

