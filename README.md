# DAA-Project
1. Title
SmartNav: Visual GPS with Dijkstra’s Algorithm

2. Objective
The objective of this project is to design and develop a Python-based desktop application that simulates a basic GPS navigation system. The application allows users to find the shortest path between two predefined cities using Dijkstra's Algorithm. Through a graphical interface developed using Tkinter, users can interactively select a start and end city, and the system calculates and displays the most efficient route based on fixed distances between connected cities.
Detailed Goals:
To implement Dijkstra’s Algorithm for shortest path detection in a city road network.
To visually demonstrate the step-by-step working of the algorithm, including updates to distances and visited nodes.
To provide an intuitive and user-friendly interface using Tkinter, enabling easy interaction for all users.
To show the final path and total travel distance in kilometers, clearly presented in the output area.
To help students and learners understand how real-world GPS systems use algorithms to compute optimal routes.
To create a clean and educational simulation without requiring internet or external APIs.

3. Introduction
In today’s world, navigation systems play a vital role in transportation and logistics. These systems compute the best routes based on certain algorithms and predefined or real-time data. One of the most widely used algorithms for route finding is Dijkstra’s Algorithm. This project is a simulation of such a GPS system in a simplified city map using Python.
Users can select a source and destination city from dropdown menus. The system then calculates the shortest route using Dijkstra’s Algorithm and displays each step of the route-finding process. Each node visit and distance update is shown clearly, helping users and students understand the logic behind the shortest path calculation. The GUI is built using Tkinter, and the results are shown in a large scrollable output area. This educational tool is ideal for DAA (Design and Analysis of Algorithms) students who want to see theory in action.
4. Tools and Technologies Used
This project utilizes a combination of programming tools, libraries, and data structures to build a simplified yet powerful GPS navigation system:
Programming Language: Python 3 – A popular and easy-to-understand language ideal for beginners and educational projects.
Graphical Interface: Tkinter – Python’s built-in GUI toolkit used to create an interactive and visually appealing interface, complete with dropdowns, buttons, and a scrollable output window.
Data Structure: Dictionary – Used to represent the graph, where each city node connects to neighboring cities with associated distances.
Algorithm: Dijkstra’s Algorithm – A fundamental graph traversal algorithm that calculates the shortest path from a source node to all other nodes, especially suitable for static maps with non-negative distances.
These tools together make the application lightweight, responsive, and easy to extend. The logic is simple enough for academic use but practical enough to resemble real-world navigation logic.

5. Algorithm Used: Dijkstra’s Algorithm
What is Dijkstra’s Algorithm?
Dijkstra's Algorithm is a famous shortest path algorithm used to find the minimum distance from a starting node (source city) to all other nodes (destination cities) in a weighted graph, where weights represent distances (and are non-negative). In your project, this algorithm is used to simulate a GPS navigation system that helps users find the shortest travel path between cities.
Step-by-Step Working of the Algorithm
Let's say the user selects:
Start City: Home
Destination City: Office
Step 1: Initialization
Set the distance to all cities as ∞ (infinity), except the start city, which is set to 0.
Create a priority queue (min-heap) to keep track of cities to explore based on the shortest known distance.
Maintain a visited set to skip already explored cities.
Create a previous city mapping to reconstruct the path later.
distances = {'Home': 0, 'School': inf, 'Mall': inf, 'Hospital': inf, 'Office': inf}

Step 2: Begin from Start City
Start exploring from Home (distance = 0).
Check all its neighbors:
School is 12 km → update School = 12
Mall is 18 km → update Mall = 18
Push these updates to the priority queue.
Step 3: Move to the Closest City
The next closest city is School (12 km). Explore its neighbors:
Mall: already has 18 km, School → Mall = 23, so no update.
Hospital: School → Hospital = 12 + 15 = 27 → update Hospital = 27
Step 4: Continue the Process
Visit Mall next (18 km), explore:
Hospital = 18 + 22 = 40, but already known distance to Hospital is 27, so skip.
Office = 18 + 25 = 43 → update Office = 43
Visit Hospital (27 km), explore:
Office = 27 + 10 = 37 → better than 43, so update Office = 37
Step 5: Stop at Destination
Once Office is visited, we now have:
Shortest path = Home → School → Hospital → Office. Total Distance = 37 km




Key Concepts Used


6. Road Network Used
Home ↔ School: 12 km
Home ↔ Mall: 18 km
School ↔ Mall: 11 km
School ↔ Hospital: 15 km
Mall ↔ Hospital: 22 km
Mall ↔ Office: 25 km
Hospital ↔ Office: 10 km

7. Project Features
1.  Dropdown Menu for Selecting Start and Destination Cities
What it Does:The user interface includes two dropdown menus – one for selecting the Start City and another for the Destination City.
Purpose: This allows the user to easily choose cities from a predefined map instead of typing names manually, reducing input errors.
User Benefit: Makes the application easy to use and beginner-friendly, especially for non-technical users or students during demos.
2. Live Path Discovery with Explanation of Updates
What it Does: When the user clicks "Find Shortest Path", the algorithm starts running and updates are shown live in the output area:
Which city is being visited now.
Which cities have their distances updated.
Which cities are skipped because a shorter path already exists.
Purpose: This provides a step-by-step walkthrough of how Dijkstra’s Algorithm works internally.
User Benefit: Helps learners visualize the logic behind shortest path discovery instead of just showing the final result.
3. Display of Visited Cities and Skipped Ones
What it Does:The output clearly shows:
Which cities the algorithm visits in each step.
Which neighboring cities get their distances updated.
Which cities are skipped due to already having a better (shorter) path.
Purpose: Mimics how a real GPS system evaluates routes in real-time.
User Benefit: Enhances algorithm transparency and makes debugging and understanding much easier.
4. Final Route and Total Distance Shown in Kilometers
What it Does: After the algorithm completes, it displays the final shortest route from Start to Destination and the total distancein km. Example :  Path: Home ➜ School ➜ Hospital ➜ Office  And Total Distance : 37 km
Purpose: Provides a clear summary for the user at the end of the process.
User Benefit: Gives the exact travel route and its cost (distance), just like in real-world navigation apps.
5. Enlarged Text Output Area for Better Readability
What it Does: The program uses a ScrolledText widget in the GUI to display messages and algorithm steps in a large, scrollable box.
Purpose: Allows detailed step-by-step outputs to be easily readable and not cut off.
User Benefit: Improves user experience by preventing clutter and allows users to scroll back and review previous steps.



8. Application Code Summary
The main components of the code:
Graph: Dictionary representing roads and distances
Dijkstra Function: Calculates shortest path with explanations
Tkinter GUI: Provides user interaction via dropdowns and a button
Scrolled Text Area: Displays step-by-step simulation and result

9. Installation Instructions
a. Install Required Python Library (Tkinter is built-in) — pip install tk
b. Run the ApplicationSave the script as app.py and execute: — python app.py

10. Working of the System
Launch the application.
Choose a Start City and Destination City from the list.
Click Find Shortest Path.
The system displays the step-by-step route calculation.
Final output includes the shortest path and total distance (in km).

13. Advantages
Easy-to-understand visualization of pathfinding: The project displays each step of the pathfinding process with detailed text output, showing how distances are updated and which cities are visited. This helps users clearly see how Dijkstra’s Algorithm works behind the scenes.
User-friendly interface with dropdown selection: The use of dropdown menus for selecting the start and destination cities makes the app easy to use for everyone—no need to type or remember city names manually.
Great tool for students learning Dijkstra’s Algorithm: With its step-by-step explanation, interactive GUI, and real-world example, this project serves as an excellent educational aid for students studying shortest path algorithms in computer science.

14. Limitations
Works only on predefined city network
No real-time traffic or obstacle considerations

15. Future Enhancements
Real-Time Traffic Factor: The system can be upgraded to simulate live traffic by adjusting the road distances dynamically. This helps reflect real-world congestion, making the shortest path calculation more realistic and efficient.
Dynamic City and Input Support: Instead of a fixed city map, users can input custom cities and roads through files or APIs. This flexibility allows users to test different scenarios or real-world maps.
Graphical Map Visualization: By using libraries like Graphviz or NetworkX, a visual map of the city and calculated routes can be displayed, making it easier for users to understand the path and connections between cities.
Multiple Vehicle Routing Simulation: The system can be expanded to handle multiple vehicles with different start and end points, helping simulate traffic load, optimize overall routing, and study real-time logistics.
16. Conclusion
The Vehicle GPS Navigation System using Dijkstra’s Algorithm successfully demonstrates how shortest path algorithms are used in real-world navigation tools. This project combines algorithmic problem-solving with a user-friendly graphical interface to simulate a GPS system. By allowing users to choose a start and destination city and then visualizing each step of the route discovery process, the application acts as both a practical tool and an educational resource.
The core strength of this project lies in its implementation of Dijkstra's Algorithm, which ensures that the shortest route is always calculated efficiently using a priority queue and greedy strategy. Each city is evaluated based on the minimum cost to reach it, and the GUI displays how and why certain cities are chosen, updated, or skipped. This kind of step-by-step breakdown makes the project especially helpful for students learning Design and Analysis of Algorithms (DAA).
Through the use of Python's Tkinter library, the interface remains simple, intuitive, and interactive. Users are guided clearly through each operation — from selecting cities to reading the final results — in a scrollable output area that improves readability. Even complex data like distance tables and visited cities are shown in real-time, making the internal workings of the algorithm completely transparent.
Key Takeaways:
Demonstrates real-world utility of Dijkstra’s Algorithm in navigation.
Provides a clean, interactive GUI using Python and Tkinter.
Helps learners and users visualize graph traversal and pathfinding logic.
Acts as a foundation for more complex routing systems with traffic, maps, and live data.

17. GITHUB LINK:- https://github.com/vikasjoc/DAA-Project.git
