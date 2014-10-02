from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from tweet import get_tweet
from string import punctuation


def remove_punctuation(string):
    for p in punctuation:
        string = string.replace(p, ' ')

    # Remove excess whitespace
    string = string.replace('  ', ' ')
    return string


class DrunkTweetMatcher(object):

    def __init__(self):
        drunk_tweet_corpus = get_tweet(search_for_drunks=True)
        sober_tweet_corpus = get_tweet(search_for_drunks=False)

        y_drunk = [1 for tweet in drunk_tweet_corpus]
        y_sober = [0 for tweet in sober_tweet_corpus]

        tweet_data = drunk_tweet_corpus + sober_tweet_corpus
        tweet_data = [remove_punctuation(tweet) for tweet in tweet_data]

        drunk_flags = y_drunk + y_sober

        vectorizer = CountVectorizer(min_df=1, ngram_range=(1, 1))

        tokenized_tweets = vectorizer.fit_transform(tweet_data)

        logistic_regression = LogisticRegression()

        logistic_regression.fit(tokenized_tweets, drunk_flags)

        self.logistic_regression = logistic_regression
        self.vectorizer = vectorizer

    def match(self, tweet):

        tweet_tokenized = self.vectorizer.transform([tweet])

        tweet_classified = self.logistic_regression.predict(tweet_tokenized)

        return tweet_classified[0]


def main():
    tweet_matcher = DrunkTweetMatcher()

    while True:
        tweet = raw_input('Give us a tweet: ')

        is_drunk = tweet_matcher.match(tweet)

        if is_drunk == 1:
            print 'You are drunk!'
        else:
            print 'You are sober!'

main()