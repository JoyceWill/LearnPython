words = [
    'will', 'joyce', 'ivy', 'fanfan', 'dongdong', 'joyce', 'will', 'ivy'
]

from collections import Counter

words_count = Counter(words)
print words_count
top_three = words_count.most_common(3)
print top_three