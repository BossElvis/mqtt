sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print(words)
print([len(word) for word in words])
print([len(word) for word in words if word != "the"])
words1 = ["hello", "my", "name", "is", "Sam"]
print((words1[0].upper(),len(words1[0])))

