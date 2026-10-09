triples = [(a, b, c)
           for a in range(1, 31)
           for b in range(a + 1, 31)
           for c in range(b + 1, 31)
           if a**2 + b**2 == c**2]

print(triples)