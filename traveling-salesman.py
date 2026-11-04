from itertools import permutations

def shortest_route(distances):
    n = len(distances)
    best_route = None
    best_distance = float("inf")

    for route in permutations(range(1, n)):
        path = (0,) + route + (0,)

        distance = sum(
            distances[path[i]][path[i + 1]]
            for i in range(n)
        )

        if distance < best_distance:
            best_distance = distance
            best_route = path

    return best_route, best_distance


distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

route, distance = shortest_route(distances)

print("Оптимальный маршрут:", route)
print("Минимальное расстояние:", distance)
