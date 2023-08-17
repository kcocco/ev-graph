# data.py

```python
from py2neo import Graph, Node

def create_sample_data(graph):
    # Create sample EV data
    ev1 = Node("ElectricVehicle", name="Tesla Model 3", range=263, list_price=39090, battery_size=54)
    ev2 = Node("ElectricVehicle", name="Nissan Leaf", range=149, list_price=31600, battery_size=40)
    ev3 = Node("ElectricVehicle", name="Chevy Bolt", range=259, list_price=36700, battery_size=66)

    # Add the nodes to the graph
    graph.create(ev1)
    graph.create(ev2)
    graph.create(ev3)
```
