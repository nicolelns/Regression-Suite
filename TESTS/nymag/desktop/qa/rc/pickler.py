import pickle

dictionary = {'http://dev.nymag.biz/':'New York Magazine -- NYC Guide to Restaurants, Fashion, Nightlife, Shopping, Politics, Movies'}

pickle.dump(dictionary, open('../data/pickle/newnavUrls.p', 'wb'))