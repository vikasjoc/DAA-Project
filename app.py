import tkinter as tk
from tkinter import messagebox, scrolledtext, Canvas
import heapq

# ----------- City Map with Distances in Double Digits -----------
graph = {
    'Home': {'School': 12, 'Mall': 18, 'Park': 20},
    'School': {'Home': 12, 'Mall': 11, 'Hospital': 15},
    'Mall': {'Home': 18, 'School': 11, 'Hospital': 22, 'Restaurant': 13},
    'Hospital': {'School': 15, 'Mall': 22, 'Office': 10, 'Airport': 30},
    'Office': { 'Hospital': 10, 'Airport': 28},
    'Park': {'Home': 20, 'Restaurant': 16},
    'Restaurant': {'Park': 16, 'Mall': 13, 'Airport': 35},
    'Airport': {'Hospital': 30, 'Office': 28, 'Restaurant': 35}
}

# Define city coordinates for visual representation (you might need to adjust these)
city_coords = {
    'Home': (50, 100),
    'School': (150, 50),
    'Mall': (150, 150),
    'Hospital': (250, 100),
    'Office': (350, 150),
    'Park': (50, 200),
    'Restaurant': (200, 200),
    'Airport': (350, 250)
}

# Colors for the map
NODE_COLOR = "lightblue"
EDGE_COLOR = "gray"
PATH_COLOR = "red"
NODE_RADIUS = 15

# ----------- Dijkstra’s Algorithm (Modified for Path Return) -----------
def dijkstra(graph, start, end, output_area):
    distance = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}
    distance[start] = 0
    visited = set()
    queue = [(0, start)]

    output_area.insert(tk.END, f"Finding shortest path from {start} to {end}\n\n")

    while queue:
        current_dist, current_node = heapq.heappop(queue)
        if current_node in visited:
            continue
        visited.add(current_node)

        output_area.insert(tk.END, f"Visiting {current_node} - current distance: {current_dist:02} km\n")

        if current_node == end:
            break

        for neighbor, weight in graph[current_node].items():
            new_dist = current_dist + weight
            if new_dist < distance[neighbor]:
                output_area.insert(tk.END, f"  Updating {neighbor}: {distance[neighbor]} km → {new_dist:02} km\n")
                distance[neighbor] = new_dist
                previous[neighbor] = current_node
                heapq.heappush(queue, (new_dist, neighbor))
            else:
                output_area.insert(tk.END, f"  Skipping {neighbor}, best is {distance[neighbor]} km\n")

        output_area.insert(tk.END, f"Distance Table: {distance}\n\n")

    # Build shortest path
    path = []
    current = end
    while current:
        path.insert(0, current)
        current = previous[current]

    if distance[end] == float('inf'):
        output_area.insert(tk.END, "No path found.\n")
        return None, None  # Return None for both path and distance
    else:
        output_area.insert(tk.END, f"Path: {' ➜ '.join(path)}\n")
        output_area.insert(tk.END, f"Total Distance: {distance[end]:02} km\n")
        return path, distance[end]

# ----------- GUI Functions -----------
def start():
    start_city = from_city.get()
    end_city = to_city.get()

    if not start_city or not end_city:
        messagebox.showerror("Error", "Please select both start and destination cities.")
        return
    if start_city == end_city:
        messagebox.showerror("Error", "Start and destination cannot be the same.")
        return

    output_area.delete('1.0', tk.END)
    shortest_path, total_distance = dijkstra(graph, start_city, end_city, output_area)
    draw_map(shortest_path)

# ----------- GUI Drawing Function -----------
def draw_map(path=None):
    canvas.delete("all")  # Clear previous drawing

    # Draw edges (roads)
    for city, neighbors in graph.items():
        x1, y1 = city_coords[city]
        for neighbor, weight in neighbors.items():
            x2, y2 = city_coords[neighbor]
            canvas.create_line(x1, y1, x2, y2, fill=EDGE_COLOR, width=2)
            # Display distance on the edge (midpoint)
            canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2 - 10, text=str(weight), fill="black")

    # Draw nodes (cities)
    for city, coords in city_coords.items():
        x, y = coords
        canvas.create_oval(x - NODE_RADIUS, y - NODE_RADIUS, x + NODE_RADIUS, y + NODE_RADIUS, fill=NODE_COLOR)
        canvas.create_text(x, y + NODE_RADIUS + 10, text=city, fill="black")

    # Highlight the shortest path
    if path:
        for i in range(len(path) - 1):
            city1 = path[i]
            city2 = path[i+1]
            x1, y1 = city_coords[city1]
            x2, y2 = city_coords[city2]
            canvas.create_line(x1, y1, x2, y2, fill=PATH_COLOR, width=4)

# ----------- GUI Layout -----------
window = tk.Tk()
window.title("Vehicle GPS Navigation (Dijkstra's Algorithm)")
window.geometry("950x700")  # Increased window size to accommodate the map
window.config(bg="")

tk.Label(window, text="Select Start and Destination", font=("Helvetica", 14, "bold"), bg="#f0f0f0").pack(pady=10)

city_list = list(graph.keys())

frame = tk.Frame(window, bg="#f0f0f0")
frame.pack(pady=5)

tk.Label(frame, text="Start City:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=0, column=0, padx=10)
from_city = tk.StringVar()
tk.OptionMenu(frame, from_city, *city_list).grid(row=0, column=1)

tk.Label(frame, text="Destination City:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=0, column=2, padx=10)
to_city = tk.StringVar()
tk.OptionMenu(frame, to_city, *city_list).grid(row=0, column=3)

tk.Button(window, text="Find Shortest Path", command=start,
          font=("Helvetica", 12), bg="#007acc", fg="white", padx=12, pady=5).pack(pady=15)

# Canvas for the map
canvas = Canvas(window, width=500, height=280, bg="white", relief=tk.RIDGE, bd=2)
canvas.pack(padx=15, pady=10)
draw_map() # Initial drawing of the map

# Enlarged Output Area
output_area = scrolledtext.ScrolledText(window, width=150, height=50, font=("Courier", 10)) # Reduced height
output_area.pack(padx=15, pady=10)

window.mainloop()