text = "the quick brown fox jumps over the lazy dog"
unique = {len(i) for i in text.split()}
print(*unique)