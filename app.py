```python
from database import GraphDatabaseConnection
from models import EVModel
from data import example_data
from py2neo import Graph

def run_query(query):
    graph_db = GraphDatabaseConnection().graph_db
    return graph_db.run(query)

def print_result(result):
    for record in result:
        print(record)

def main():
    # Initialize the graph database connection
    graph_db = GraphDatabaseConnection().graph_db

    # Create the EV model in the graph database
    EVModel(graph_db).create_model()

    # Populate the graph database with example data
    for data in example_data:
        graph_db.create(data)

    # Run a query
    query = "MATCH (ev:ElectricVehicle) RETURN ev"
    result = run_query(query)

    # Print the result
    print_result(result)

if __name__ == "__main__":
    main()
```