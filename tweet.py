import random
from TwitterAPI import TwitterAPI

consumer_key = "J3lMNAgfjFyqcCOjrmEDZCzsw"
consumer_secret = "hNx7JzA1CI4fyOysTHJl8cdJDUtQWiOuVT0qlfkCL2IHO7aS72"
access_token_key = "2360201306-dfNbwC3J4NmJBzTCsJeYkA9PUxSRer4KZRbmIjN"
access_token_secret = "T6GL0dS0hrSOQ3PqD83ezxpASNDa2nax7oykynnuflsTi"

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

drunk_hashtags = [
    '#drunk', '#drinking', '#alcohol', '#beer', '#wine', '#vodka', '#tequila', '#happyhour',
    '#whiskey', '#cider', '#drinks'
]
normal_hashtags = [
    '#python', '#london', '#australia', 'and', '#sport', '#startups', '#bike', '#running',
    '#windows', '#apple', '#facebook'
]


def get_tweet(search_for_drunks=True):
    if search_for_drunks:
        hashtags = drunk_hashtags
    else:
        hashtags = normal_hashtags

    tweets = []

    for hashtag in hashtags:
        r = api.request('search/tweets', {
            'result_type': 'recent',
            'count': 200,
            'q': hashtag
        })

        tweets += [item['text'].encode('utf-8') for item in list(r.get_iterator())]
    return list(set(tweets))
