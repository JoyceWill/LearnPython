# Determine the most frequently occurring items

words = [
    'will', 'joyce', 'ivy', 'fanfan', 'dongdong', 'joyce', 'will', 'ivy'
]

from collections import Counter

words_counts = Counter(words)
top_three = words_counts.most_common(3)
print top_three