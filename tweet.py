from TwitterAPI import TwitterAPI
import pprint
consumer_key = "J3lMNAgfjFyqcCOjrmEDZCzsw"
consumer_secret = "hNx7JzA1CI4fyOysTHJl8cdJDUtQWiOuVT0qlfkCL2IHO7aS72"
access_token_key = "2360201306-dfNbwC3J4NmJBzTCsJeYkA9PUxSRer4KZRbmIjN"
access_token_secret = "T6GL0dS0hrSOQ3PqD83ezxpASNDa2nax7oykynnuflsTi"

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)



def get_tweet(number=24, search="#drunk"):
    r = api.request('search/tweets', {'q': search, 'result_type': 'recent'})
    return [item['text'].decode('utf-8').decode('unicode-escape') for item in list(r.get_iterator())][:number]



search_terms = ['#drunk', '#drinking', '#alcohol', '#hammered' , '#beer', '#wine', '#vodka', '#tequila']
for term in search_terms:
    print term
    pprint.pprint(get_tweet(number=10, search=term))
