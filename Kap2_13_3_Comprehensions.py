"""
Normierung einer String-Liste auf Klein-
buchstaben. Drei Wege die zum Ziel führen
werden demonstriert.
"""
# Input
answers = ['Yes', 'yes', 'No', 'no', 'maYbE']

# Weg 1: Die klassische for-Schleife
normalized = []
for x in answers:
    normalized.append(x.lower())

# Weg 2: Lambda und map()
normalized2 = list(map(lambda y: y.lower(),
                       answers))

# Weg 3: Eine list comprehension
normalized3 = [z.lower() for z in answers]

print(normalized)
print(normalized2)
print(normalized3)

# x bleibt als einzige Variable erhalten.
print(x)

# Analog set und dict comprehensions
print({x.lower() for x in answers})
print({x: x.lower() for x in answers})
