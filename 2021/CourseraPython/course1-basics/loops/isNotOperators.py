smallest = None
print('Before')
for value in [3, 41, 12, 9, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value

# 'is' is stronger than == , which is mathematical

print(smallest, value)
print('After', smallest)
