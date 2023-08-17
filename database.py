```python
from py2neo import Graph, Node, Relationship

class Database:
    def __init__(self, uri, user, password):
        self.graph = Graph(uri, user=user, password=password)

    def insert_ev(self, ev):
        tx = self.graph.begin()
        ev_node = Node("ElectricVehicle", name=ev.name, range=ev.range, list_price=ev.list_price, battery_size=ev.battery_size)
        tx.create(ev_node)
        tx.commit()

    def query_ev(self, name):
        return self.graph.run("MATCH (ev:ElectricVehicle {name: $name}) RETURN ev", name=name).data()
```