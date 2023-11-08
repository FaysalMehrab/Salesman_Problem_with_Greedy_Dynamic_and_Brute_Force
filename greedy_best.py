import random
import timeit
import matplotlib.pyplot as plt
# Function to generate a best-case distance matrix for n cities
def generate_best_case_distances(n):
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            distances[i][j] = j - i  # Nearest unvisited city is always the next city
            distances[j][i] = distances[i][j]
    return distances
# Greedy Algorithm
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
# running time for the best-case scenario
def calculate_best_case_running_time(algorithm, distances, num_runs):
    total_time = 0
    for _ in range(num_runs):
        total_time += timeit.timeit(lambda: algorithm(distances), number=1)
    return total_time / num_runs
# List of different numbers of cities
num_cities_list = [5, 10, 15, 20, 25]  # You can adjust this list as needed
# Number of runs for each number of cities
num_runs = 5
# Lists to store the best-case running times for the Greedy Algorithm
best_case_times_greedy = []
# Iterate over different numbers of cities and calculate best-case running times
for num_cities in num_cities_list:
    best_case_distances = generate_best_case_distances(num_cities)
    best_case_time_greedy = calculate_best_case_running_time(tsp_greedy, best_case_distances, num_runs)
    best_case_times_greedy.append(best_case_time_greedy)
# Graph to visualize the best-case running times for the Greedy Algorithm
plt.figure(figsize=(10, 6))
plt.plot(num_cities_list, best_case_times_greedy, marker='o', label='Greedy')
plt.xlabel('Number of Cities')
plt.ylabel('Running Time (seconds)')
plt.title('Best-Case Running Time for Greedy Algorithm')
plt.legend()
plt.grid()
plt.show()
