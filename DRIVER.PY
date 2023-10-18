# # # # from faker import Faker
# # # # import mysql.connector
# # # # import random

# # # # # Initialize Faker
# # # # fake = Faker()

# # # # # Connect to the MySQL database
# # # # conn = mysql.connector.connect(
# # # #     host="localhost",
# # # #     user="root",
# # # #     password="password",
# # # #     database="myproject"
# # # # )

# # # # # Create a cursor
# # # # cursor = conn.cursor()

# # # # # Update the 'route' attribute for all rows using Faker-generated descriptions
# # # # update_query = "UPDATE bus_detail SET route = %s WHERE bus_id = %s"

# # # # # Iterate through bus_id values from 1 to 140
# # # # for bus_id in range(1, 141):
# # # #     # Generate a list of descriptions with three or four places
# # # #     num_routes = random.randint(5, 8)  # Generate between 5 and 10 routes
# # # #     route_descriptions = []

# # # #     for _ in range(num_routes):
# # # #         places = fake.words(nb=random.randint(2, 4))
# # # #         route_description = ", ".join(places)
# # # #         route_descriptions.append(route_description)

# # # #     final_route_description = ", ".join(route_descriptions)
    
# # # #     cursor.execute(update_query, (final_route_description, bus_id))

# # # # # Commit the changes and close the connection
# # # # conn.commit()
# # # # conn.close()


# # # import mysql.connector

# # # # Connect to the MySQL database
# # # conn = mysql.connector.connect(
# # #      host="localhost",
# # #      user="root",
# # #      password="password",
# # #      database="myproject"
# # #  )

# # # # Create a cursor
# # # cursor = conn.cursor()

# # # # Select all rows from the ticket table where source and destination are NULL
# # # select_query = "SELECT ticket_id FROM ticket WHERE source IS NULL AND destination IS NULL"

# # # # Update the source and destination columns with the same data as route
# # # update_query = "UPDATE ticket SET source = %s, destination = %s WHERE ticket_id = %s"

# # # # Execute the select query
# # # cursor.execute(select_query)

# # # # Fetch all rows with NULL source and destination
# # # rows = cursor.fetchall()

# # # for row in rows:
# # #     ticket_id, route = row
# # #     route_parts = route.split(", ")  # Split the route by comma and space
# # #     source = route_parts[0]
# # #     destination = route_parts[-1]  # Last part of the route

# # #     cursor.execute(update_query, (source, destination, ticket_id))

# # # # Commit the changes and close the connection
# # # conn.commit()
# # # conn.close()




# # import mysql.connector

# # # Connect to the MySQL database
# # conn = mysql.connector.connect(
# #     host="localhost",
# #     user="root",
# #     password="password",
# #     database="myproject"
# #   )

# # # Create a cursor
# # cursor = conn.cursor()

# # # Select data from the bus_detail table
# # select_query = "SELECT bus_id, route FROM bus_detail"

# # # Execute the select query
# # cursor.execute(select_query)

# # # Fetch all rows from the bus_detail table
# # bus_details = cursor.fetchall()

# # # Update the 'source' and 'destination' columns in the ticket table based on bus_detail data
# # update_query = "UPDATE ticket SET source = %s, destination = %s WHERE bus_id = %s"

# # for bus_id, route in bus_details:
# #     # Split the route by comma and space to get source and destination
# #     route_parts = route.split(", ")
    
# #     if len(route_parts) >= 2:
# #         source = route_parts[0]
# #         destination = route_parts[-1]
        
# #         cursor.execute(update_query, (source, destination, bus_id))

# # # Commit the changes and close the connection
# # conn.commit()
# # conn.close()


# # import mysql.connector
# # from faker import Faker

# # # Initialize Faker
# # fake = Faker()

# # # Database connection parameters
# # db_config = {
# #     'host': 'localhost',
# #     'user': 'root',
# #     'password': 'password',
# #     'database': 'myproject',
# # }

# # # Establish a connection to the database
# # connection = mysql.connector.connect(**db_config)
# # cursor = connection.cursor()

# # # Number of rows to insert
# # num_rows = 5

# # # Create a list to store unique, non-grammatical route names
# # unique_routes = []

# # # Function to generate a unique non-grammatical route name
# # def generate_unique_route():
# #     while True:
# #         route = fake.unique.city()
# #         # Check if the generated route name is not a grammatical word
# #         if not any(word in route.lower() for word in ['and', 'the', 'of']):
# #             return route

# # # Insert fake data into the "bus_detail" table
# # for _ in range(num_rows):
# #     route = generate_unique_route()
# #     unique_routes.append(route)
# #     query = f"INSERT INTO bus_detail (route) VALUES ('{route}')"
# #     cursor.execute(query)

# # # Commit the changes and close the connection
# # connection.commit()
# # cursor.close()
# # connection.close()

# # # Print the generated route names
# # print("Generated Route Names:")
# # for route in unique_routes:
# #     print(route)

# # import mysql.connector
# # from faker import Faker

# # # Initialize Faker
# # fake = Faker()

# # # Database connection parameters


# # # Establish a connection to the database
# # connection = mysql.connector.connect(**db_config)
# # cursor = connection.cursor()

# # # Number of routes and places to generate for each bus_id
# # num_routes_per_bus_id = 5

# # # Function to generate a unique route name with a non-grammatical word
# # def generate_unique_route():
# #     while True:
# #         route = fake.city()
# #         # Check if the generated route name contains cardinal directions
# #         if any(direction in route.lower() for direction in ['east', 'west', 'south', 'north']):
# #             return route

# # # Generate routes and places for each bus_id
# # for bus_id in range(1, 151):  # Assuming bus_ids from 1 to 150
# #     for _ in range(num_routes_per_bus_id):
# #         route = generate_unique_route()
# #         query = f"INSERT INTO bus_detail (bus_id, route) VALUES ({bus_id}, '{route}')"
# #         cursor.execute(query)

# # # Commit the changes and close the connection
# # connection.commit()
# # cursor.close()import mysql.connector


# import mysql.connector
# from faker import Faker

# # Initialize Faker
# fake = Faker()

# # Database connection parameters
# db_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'password',
#     'database': 'myproject',
#  }


# # Establish a connection to the database
# connection = mysql.connector.connect(**db_config)
# cursor = connection.cursor()

# # Number of routes and places to generate for each bus_id
# num_routes_per_bus_id = 5

# # Function to generate a unique route name with a non-grammatical word
# def generate_unique_route():
#     while True:
#         route = fake.unique.city()
#         # Check if the generated route name contains cardinal directions
#         if any(direction in route.lower() for direction in ['east', 'west', 'south', 'north']):
#             continue
#         return route

# # Generate routes and places for each bus_id
# for bus_id in range(1, num_routes_per_bus_id + 1):
#     # Check if the bus_id exists in the database
#     cursor.execute(f"SELECT bus_id FROM bus_detail WHERE bus_id = {bus_id}")
#     result = cursor.fetchone()
#     if result:
#         for _ in range(5):
#             route = generate_unique_route()
#             query = f"UPDATE bus_detail SET route = '{route}' WHERE bus_id = {bus_id}"
#             cursor.execute(query)

# # Commit the changes and close the connection
# connection.commit()
# # cursor.close()
# # connection.close()
# from faker import Faker
# import mysql.connector
# import random

# # Initialize the Faker generator
# fake = Faker()

# # Connect to your MySQL database

# cursor = conn.cursor()

# # Number of fake records you want to generate for the 'route' attribute
# num_records = 139  # You can adjust this number as needed

# # Generate and insert fake route data into the 'bus_detail' table
# for bus_id in range(1, num_records + 1):
#     route = fake.text(max_nb_chars=40)  # Generate text with a maximum of 40 characters
#     route = route.replace('\n', ' ')  # Remove newline characters

#     update_query = "UPDATE bus_detail SET route = %s WHERE bus_id = %s"
#     values = (route, bus_id)

#     cursor.execute(update_query, values)
#     conn.commit()

# # Close the database connection
# conn.close()



import mysql.connector
import random

# Connect to your MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="myproject"
)
cursor = conn.cursor()

# List of predefined long route names (adjust as needed)
long_routes = [
    "Los Angeles to San Francisco via Central Valley and Pacific Coast Highway",
    "New York City to Miami through the Appalachian Mountains and Florida Keys",
    "Chicago to Denver via the Great Plains and Rocky Mountains",
    "Seattle to San Diego along the Pacific Coast and California Coast Ranges",
    # Add more long route names as needed
]

# Number of fake records you want to generate for the 'route' attribute
num_records = 139  # You can adjust this number as needed

# Generate and insert long route data into the 'bus_detail' table
for bus_id in range(1, num_records + 1):
    route = random.choice(long_routes)

    update_query = "UPDATE bus_detail SET route = %s WHERE bus_id = %s"
    values = (route, bus_id)

    cursor.execute(update_query, values)
    conn.commit()

# Close the database connection
conn.close()
