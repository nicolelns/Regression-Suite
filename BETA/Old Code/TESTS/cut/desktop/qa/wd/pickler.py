import pickle

dict = {'nicole.smith@nymag.com':['qatest1', 'foo', ''], 'abcde@nymag.com':['qatest1', 'foo', ''], 'nicolelns':['qatest1', 'foo', ''],  'abcde':['qatest1', 'foo', ''], '':['qatest1', 'foo', '']}

tuple = (('asdf', '$$$$$$$$$', 'asdfasdfas65654564563456', ''), ('test.test', 'nicole.smith@nymag.com', 'anywhere@foo.com', ''), ('@@@@11', 'abcdef', 'qatest1', ''), ('9999', 'ab$de', '10001', ''))

pickle.dump(dict, open('../data/pickle/login.p', 'wb'))
pickle.dump(tuple, open('../data/pickle/register.p', 'wb'))