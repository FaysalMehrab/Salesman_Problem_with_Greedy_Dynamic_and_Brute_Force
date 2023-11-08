import random
import timeit
import matplotlib.pyplot as plt

# Function to generate a worst-case distance matrix for n cities
def generate_worst_case_distances(n):
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distances[i][j] = 100  # Set a high distance between all pairs of cities
    return distances

# Dynamic Programming Algorithm with Memoization
def tsp_dynamic_programming(distances):
    n = len(distances)
    memo = {}
    def dp(mask, v):
        if mask == (1 << n) - 1:  # All cities have been visited
            return distances[v][0]  # Return to the starting city
        if (mask, v) in memo:
            return memo[(mask, v)]
        ans = float('inf')
        for u in range(n):
            if not (mask >> u) & 1:  # Check if city u is unvisited
                ans = min(ans, distances[v][u] + dp(mask | (1 << u), u))
        memo[(mask, v)] = ans
        return ans
    return dp(1, 0)

# Calculate the worst-case distance and execution time for the worst case
def calculate_worst_distance_dynamic_programming(num_cities):
    distances = generate_worst_case_distances(num_cities)
    print("Generated Worst-Case Distances:", distances)  # Print the generated distances
    start_time = timeit.default_timer()
    result = tsp_dynamic_programming(distances)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    return result, execution_time

# Number of cities for the worst case
num_cities_list = [3, 4, 5, 6]  # You can adjust this as needed

# Initialize a list to store the worst-case distances and execution times for Dynamic Programming Algorithm
worst_distances_dynamic_programming = []
execution_times_dynamic_programming = []

# Calculate worst-case distances and execution times for Dynamic Programming Algorithm
for num_cities in num_cities_list:
    worst_distance_dynamic_programming, execution_time = calculate_worst_distance_dynamic_programming(num_cities)
    worst_distances_dynamic_programming.append(worst_distance_dynamic_programming)
    execution_times_dynamic_programming.append(execution_time)

# Create a graph to visualize the execution times for Dynamic Programming Algorithm
plt.figure(figsize=(10, 6))
plt.plot(num_cities_list, execution_times_dynamic_programming, marker='o', label='Dynamic Programming')
plt.xlabel('Number of Cities')
plt.ylabel('Execution Time (Seconds)')
plt.title('Execution Time for Dynamic Algorithm (Worst_Case)')
plt.legend()
plt.grid()
plt.show()
