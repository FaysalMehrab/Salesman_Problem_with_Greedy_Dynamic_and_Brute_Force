import random
import timeit
import matplotlib.pyplot as plt
from itertools import permutations

# Function to generate random distance matrix for n cities
def generate_average_case_distances(n):
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
        distances = generate_average_case_distances(num_cities)
        start_time = timeit.default_timer()
        algorithm(distances)
        end_time = timeit.default_timer()
        total_time += end_time - start_time
    return total_time / num_runs

# Number of cities for the average case
num_cities_list = [3, 4, 5, 6, 7, 8]  # You can adjust this as needed
num_runs = 5  # Number of runs for each case

# Initialize a list to store the execution times for the average case
execution_times_average_case = []

# Calculate execution times for the average case
for num_cities in num_cities_list:
    execution_time_average_case = measure_execution_time(tsp_brute_force, num_cities, num_runs)
    execution_times_average_case.append(execution_time_average_case)

# Create a graph for the best case
plt.figure(figsize=(10, 6))
plt.plot(num_cities_list, execution_times_average_case, marker='o', label='Average Case')
plt.xlabel('Number of Cities')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time for Brute Force Algorithm (Average Case)')
plt.legend()
plt.grid()
plt.show()
