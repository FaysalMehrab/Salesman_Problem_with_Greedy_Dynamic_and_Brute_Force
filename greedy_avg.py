import random
import timeit
import matplotlib.pyplot as plt
# Function to generate random distance matrix for n cities
def generate_random_distances(n):
    distances = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0)  # Distance from a city to itself is 0
            else:
                row.append(random.randint(1, 100))  # Random distance between 1 and 100
        distances.append(row)
    return distances
def tsp_greedy(distances):
    n = len(distances)
    start = 0
    unvisited = set(range(1, n))
    current_distance = 0
    current_city = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        current_distance += distances[current_city][next_city]
        unvisited.remove(next_city)
        current_city = next_city
    current_distance += distances[current_city][start]
    return current_distance
# Average running time for the average case
def calculate_average_running_time(algorithm, num_cities, num_runs):
    total_time = 0
    for _ in range(num_runs):
        distances = generate_random_distances(num_cities)
        total_time += timeit.timeit(lambda: algorithm(distances), number=1)
    return total_time / num_runs
num_cities_list = [5, 10, 15, 20, 25] # Number of cities
num_runs = 5  # Number of runs for each case

# list to store the average running times for the Greedy Algorithm
average_times_greedy = []
# Calculating average running times for Greedy Algorithm
for num_cities in num_cities_list:
    average_time_greedy = calculate_average_running_time(tsp_greedy, num_cities, num_runs)
    average_times_greedy.append(average_time_greedy)
# Graph to visualize the average running times for Greedy Algorithm
plt.figure(figsize=(10, 6))
plt.plot(num_cities_list, average_times_greedy, marker='o', label='Greedy')
plt.xlabel('Number of Cities')
plt.ylabel('Average Running Time (seconds)')
plt.title('Average Running Time for Greedy Algorithm')
plt.legend()
plt.grid()
plt.show()
