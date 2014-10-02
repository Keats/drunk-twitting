import random
from TwitterAPI import TwitterAPI

consumer_key = "J3lMNAgfjFyqcCOjrmEDZCzsw"
consumer_secret = "hNx7JzA1CI4fyOysTHJl8cdJDUtQWiOuVT0qlfkCL2IHO7aS72"
access_token_key = "2360201306-dfNbwC3J4NmJBzTCsJeYkA9PUxSRer4KZRbmIjN"
access_token_secret = "T6GL0dS0hrSOQ3PqD83ezxpASNDa2nax7oykynnuflsTi"

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

drunk_hashtags = ['#drunk', '#drinking', '#alcohol', '#beer', '#wine', '#vodka', '#tequila']
normal_hashtags = ['#python', '#london', '#australia', '#europe', '#sport', '#startups']


def get_tweet(number=24, search_for_drunks=True):
    api_options = {
        'result_type': 'recent',
        'count': 200,
        'q': random.choice(drunk_hashtags) if search_for_drunks else random.choice(normal_hashtags)
    }

    if search_for_drunks:
        r = api.request('search/tweets', api_options)
    else:
        r = api.request('search/tweets', api_options)
    return [item['text'].encode('utf-8') for item in list(r.get_iterator())][:number]
