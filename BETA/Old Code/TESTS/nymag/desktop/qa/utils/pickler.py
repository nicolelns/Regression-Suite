import pickle
import urllib
import urlparse

prod_nav_dictionary = {'http://www.nymag.com':'New York Magazine -- NYC Guide to Restaurants, Fashion, Nightlife, Shopping, Politics, Movies', 'http://nymag.com/news/':'News, Intelligencer, Politics, Business -- New York Magazine', 'http://nymag.com/daily/intel/':'Daily Intel -- New York News -- New York Magazine', 'http://nymag.com/daily/sports/':'The Sports Section -- Sports News on NYMag.com by Will Leitch and Joe DeLessio', 'http://nymag.com/restaurants/':'New York Restaurants and Recipes - NYC Dining and Chefs - New York Magazine', 'http://nymag.com/nightlife/':'New York Bars and NYC Nightlife -- New York Magazine', 'http://nymag.com/arts/':'Arts and Events in NYC - New York Magazine', 'http://nymag.com/agenda/':'Agenda - New York Magazine Events Calendar - Concerts, Theater, Movies, Art, and More', 'http://nymag.com/fashion/':'Fashion & Style on New York Magazine - Designers, Runway Shows, Trends, News', 'http://nymag.com/fashion/fashionshows/':'Fashion Shows - Fashion Week in New York, Milan, Paris, London -- Runway Photos and Videos -- New York Magazine', 'http://nymag.com/daily/fashion/':'The Cut -- Fashion Week, Models, Street Style, Red Carpet Dresses and Fashion News', 'http://nymag.com/shopping/':'Shopping in New York City - New York Stores and Sales - New York Magazine', 'http://nymag.com/travel/':'U.S. and International Travel Destinations - Vacation Ideas - New York Magazine', 'http://nymag.com/realestate/':'Real Estate - New York Magazine', 'http://nymag.com/visitorsguide/':'Visitors Guide -- New York Magazine', 'http://nymag.com/beauty/':' Beauty Guide - New York Spas, Salons, and Fitness - New York Magazine', 'http://nymag.com/homedesign/':'Home Design Guide - New York Magazine - Apartment Tours', 'http://nymag.com/weddings/':'New York Wedding Guide - Weddings Index', 'http://nymag.com/bestdoctors/':"New York's Best Doctors and Health Features -- New York Magazine", 'http://nymag.com/marketplace/':'New York Magazine -- Marketplace', 'http://nymag.com/bestofny/':'Best of New York - New York Magazine'}

pickle.dump(prod_nav_dictionary, open('/Users/nsmith/Desktop/TESTS/nymag/desktop/prod/data/pickle/newnavUrls.p', 'wb'))

qa_nav_dictionary = {}
urls = prod_nav_dictionary.keys()
titles = prod_nav_dictionary.values()
new_param = "://stg.nymetro.com"
n = 0

for each in prod_nav_dictionary:

    url = urls[n]
    title = titles[n]
    split = urlparse.urlsplit(url)

    if split[1] == "nymag.com":
        new_url = split[0] + new_param + split[2] 

        qa_nav_dictionary[new_url] = title
    
    else:
        qa_nav_dictionary[url] = title

    n += 1

pickle.dump(qa_nav_dictionary, open('../data/pickle/qa.newnavUrls.p', 'wb'))

print qa_nav_dictionary 