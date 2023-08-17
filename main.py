```python
from database import GraphDatabaseConnection
from models import EVModel
from data import example_data
from app import query_function, print_function

def main():
    # Initialize the graph database connection
    db = GraphDatabaseConnection()

    # Create the EV model in the database
    EVModel.create_in_db(db)

    # Populate the database with example data
    for data in example_data:
        EVModel.create_from_dict(db, data)

    # Run a query on the database
    result = query_function(db)

    # Print the result
    print_function(result)

if __name__ == "__main__":
    main()
```