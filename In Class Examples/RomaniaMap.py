from search import *

def main():
    # Print any available node in the graph
    print("Display any available node in the graph: ")
    print(romania_map.nodes())
    print()

    # Print any available direct node with the distance in the graph
    print("Display any available direct node with the distance in the graph: ")
    print(romania_map.get('Arad'))
    print()

    # Print the distance if Bucharest is the direct node in the graph or None
    print("Display the distance if Bucharest is the direct node in the graph or None: ")
    print(romania_map.get('Arad', 'Bucharest'))
    print()

    # Print the distance if Bucharest is the direct node in the graph or None
    print("Display the distance if Bucharest is the direct node in the graph or None: ")
    print(romania_map.get('Fagaras', 'Bucharest'))
    print()

    # Print the actual coordinate of each city in the graph
    print("Display the actual coordinate of each city in the graph: ")
    print(romania_map.locations)

if __name__ == "__main__":
    main()