words = input().split(" ")

print(words)

filtered_words = list(filter(lambda x: len(x) % 2 == 0,words))
print(filtered_words)

print("\n".join(filtered_words))