import timeit
import matplotlib.pyplot as plt
from itertools import permutations
# Function to generate a best-case distance matrix for n cities
def generate_best_case_distances(n):
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            distances[i][j] = j - i  # Nearest unvisited city is always the next city
            distances[j][i] = distances[i][j]
    return distances
# Brute Force Algorithm
def tsp_brute_force(distances):
    n = len(distances)
    min_distance = float('inf')
    min_path = []
    for path in permutations(range(n)):
        total_distance = 0
        for i in range(n - 1):
            total_distance += distances[path[i]][path[i + 1]]
        total_distance += distances[path[-1]][path[0]]  # Return to the starting city
        if total_distance < min_distance:
            min_distance = total_distance
            min_path = list(path)
    return min_distance, min_path
# Function to measure execution time for a given algorithm, number of cities, and number of runs
def measure_execution_time(algorithm, num_cities, num_runs):
    total_time = 0
    for _ in range(num_runs):
        distances = generate_best_case_distances(num_cities)
        start_time = timeit.default_timer()
        algorithm(distances)
        end_time = timeit.default_timer()
        total_time += end_time - start_time
    return total_time / num_runs
# Number of cities for the best case
num_cities_list = [3, 4, 5, 6, 7, 8]  # You can adjust this as needed
num_runs = 5  # Number of runs for each case
# Initialize a list to store the execution times for the best case
execution_times_best_case = []
# Calculate execution times for the best case
for num_cities in num_cities_list:
    execution_time_best_case = measure_execution_time(tsp_brute_force, num_cities, num_runs)
    execution_times_best_case.append(execution_time_best_case)
# Create a graph for the best case
plt.figure(figsize=(10, 6))
plt.plot(num_cities_list, execution_times_best_case, marker='o', label='Best Case')
plt.xlabel('Number of Cities')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time for Brute Force Algorithm (Best Case)')
plt.legend()
plt.grid()
plt.show()
