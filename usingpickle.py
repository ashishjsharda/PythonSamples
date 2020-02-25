import pickle
pickled_string=pickle.dumps([1,2,3,"b","a","c"])
print(pickle.loads(pickled_string))
