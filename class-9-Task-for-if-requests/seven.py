actors = [
    {"id": 1, "name": "Shah Rukh Khan", "age": 58, "nationality": "Indian"},
    {"id": 2, "name": "Leonardo DiCaprio", "age": 49, "nationality": "American"},
    {"id": 3, "name": "Priyanka Chopra", "age": 41, "nationality": "Indian"},
    {"id": 4, "name": "Tom Cruise", "age": 62, "nationality": "American"}
]


for actor in actors:
    if actor['age']<=45:
        print(actor['name'])