from collections import defaultdict
a=defaultdict(list)
words=["cat","apple","rat","bat","bar","atom","car"]
for word in words:
    a[len(word)].append(word)
print(list(a.values()))