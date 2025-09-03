# Generate 100 actors list with dict type data
actors = []

for i in range(1, 101):
    actor = {
        "id": i,
        "name": f"Actor {i}",
        "age": 20 + (i % 40),   # age between 20-59
        "nationality": "Indian" if i % 2 == 0 else "American"
    }
    actors.append(actor)

# Print first 5 to check
for a in actors[:5]:
    print(a)

# Length check
print("Total actors:", len(actors))
