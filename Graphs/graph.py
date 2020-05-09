from vertex import Vertex

class Graph:
  def __init__(self):
    self.graph_dict = {}

  def add_vertex(self, node):
    self.graph_dict[node.value] = node

  def add_edge(self, from_node, to_node, weight = 0):
    self.graph_dict[from_node.value].add_edge(to_node.value, weight)
    self.graph_dict[to_node.value].add_edge(from_node.value, weight)

  def explore(self):
    print("Exploring the graph....\n")
    #FILL IN EXPLORE METHOD BELOW
    currentRoom = "entrance"
    pathTotal = 0

    print("\nStarting off at the {0}\n".format(currentRoom))

    while currentRoom != "treasure room":
      node = self.graph_dict[currentRoom]
      for connectedRoom, weight in node.edges.items():
        key = connectedRoom[0]
        print("enter {0} for {1}: {2} cost".format(key, connectedRoom, weight))
      
      validChoices = [i[0] for i in node.edges.keys()]
      print("\nYou have accumulated: {0} cost".format(pathTotal))
      choice = input("\nWhich room do you move to? ")

      if choice not in validChoices:
        print("please select from these letters: {0}".format(validChoices))
      else:
        for room in node.edges.keys():
          if room[0] is choice:
            currentRoom = room
            pathTotal += node.edges[currentRoom]
        print("\n*** You have chosen: {0} ***\n".format(currentRoom))
      
    print("Made it to the treasure room with {0} cost".format(pathTotal))

  def print_map(self):
    print("\nMAZE LAYOUT\n")
    for node_key in self.graph_dict:
      print("{0} connected to...".format(node_key))
      node = self.graph_dict[node_key]
      for adjacent_node, weight in node.edges.items():
        print("=> {0}: cost is {1}".format(adjacent_node, weight))
      print("")
    print("")

def build_graph():
  graph = Graph()
  
  # MAKE ROOMS INTO VERTICES BELOW...
  entrance = Vertex("entrance")
  anteChamber = Vertex("ante-chamber")
  kingsRoom = Vertex("king's room")
  grandGallery = Vertex("grand gallery")
  treasureRoom = Vertex("treasure room")

  # ADD ROOMS TO GRAPH BELOW...
  graph.add_vertex(entrance)  
  graph.add_vertex(anteChamber)
  graph.add_vertex(kingsRoom)
  graph.add_vertex(grandGallery)
  graph.add_vertex(treasureRoom)

  # ADD EDGES BETWEEN ROOMS BELOW...
  graph.add_edge(entrance, anteChamber, 7)
  graph.add_edge(entrance, kingsRoom, 3)
  graph.add_edge(anteChamber, kingsRoom, 1)
  graph.add_edge(grandGallery, anteChamber, 2)
  graph.add_edge(grandGallery, kingsRoom, 2)
  graph.add_edge(treasureRoom, anteChamber, 6)
  graph.add_edge(treasureRoom, grandGallery, 4)

  # DON'T CHANGE THIS CODE
  graph.print_map()
  return graph
