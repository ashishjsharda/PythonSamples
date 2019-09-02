'''
Created on Sep 2, 2019
Word Counter Python
@author: asharda
'''
from collections import Counter
word_set = " This is a series of strings to count " \
   "many words . They sometime hurt and words sometime inspire "\
   "Also sometime fewer words convey more meaning than a bag of words "\
   "Be careful what you speak or what you write or even what you think of. "\
# Create list of all the words in the string
word_list = word_set.split()

# Get the count of each word.
word_count = Counter(word_list)

# Use most_common() method from Counter subclass
print(word_count.most_common(1))
