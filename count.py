from collections import Counter

phones = ['iphone', 'samsung', 'lg', 'iphone', 'iphone', 'lg']

count = Counter(phones)
print(count)

text = 'Ехал грека через реку видит грека в реке рак'
count = Counter(text.lower().replace(' ', ''))
print(count)