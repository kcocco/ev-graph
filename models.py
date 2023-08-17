from py2neo import Graph, Node, Relationship

class EV:
    def __init__(self, name, range, list_price, battery_size):
        self.name = name
        self.range = range
        self.list_price = list_price
        self.battery_size = battery_size

    def create_node(self, graph):
        ev_node = Node("ElectricVehicle", name=self.name, range=self.range, list_price=self.list_price, battery_size=self.battery_size)
        graph.create(ev_node)
        return ev_node

    def create_relationship(self, graph, node1, node2, relationship_type):
        rel = Relationship(node1, relationship_type, node2)
        graph.create(rel)