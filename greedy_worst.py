import random
import timeit
import matplotlib.pyplot as plt
# Function to generate a worst-case distance matrix for n cities
def generate_worst_case_distances(n):
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distances[i][j] = random.randint(1, 100)  # Random distances between 1 and 100
    return distances
# Greedy Algorithm
def tsp_greedy(distances):
    n = len(distances)
    start = 0
    unvisited = set(range(1, n))
    current_distance = 0
    current_city = start
    tour = [current_city]
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        current_distance += distances[current_city][next_city]
        unvisited.remove(next_city)
        current_city = next_city
        tour.append(current_city)
    # Return to the starting city to complete the tour
    current_distance += distances[current_city][start]
    tour.append(start)
    return current_distance, tour
# Calculate the worst-case running time for the worst case
def calculate_worst_case_running_time(algorithm, num_cities):
    distances = generate_worst_case_distances(num_cities)
    return timeit.timeit(lambda: algorithm(distances), number=1)
# Number of cities for the worst case
num_cities_list = [1, 2, 3, 4, 5]  # You can adjust this as needed
# Initialize a list to store the worst-case running times for the Greedy Algorithm
worst_case_times_greedy = []
# Calculate worst-case running times for Greedy Algorithm
for num_cities in num_cities_list:
    worst_case_time_greedy = calculate_worst_case_running_time(tsp_greedy, num_cities)
    worst_case_times_greedy.append(worst_case_time_greedy)
# Create a graph to visualize the worst-case running times for Greedy Algorithm
plt.figure(figsize=(10, 6))
plt.plot(num_cities_list, worst_case_times_greedy, marker='o', label='Greedy')
plt.xlabel('Number of Cities')
plt.ylabel('Worst-Case Running Time (seconds)')
plt.title('Worst-Case Running Time for Greedy Algorithm')
plt.legend()
plt.grid()
plt.show()
