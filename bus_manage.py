
import mysql.connector
from faker import Faker
import random

# Create a Faker instance
fake = Faker()

# Establish a database connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="myproject")
    # Create a cursor object to interact with the database
cursor = db_connection.cursor()


# Function to insert random data into bus_detail table
def insert_bus_data():
    for _ in range(10):
        driver_id = fake.random_int(min=1, max=5)
        conductor_id = fake.random_int(min=1, max=5)
        bus_number = fake.unique.random_int(min=1000, max=9999, step=1)
        bus_model = fake.word()
        seating_capacity = random.randint(20, 60)
        route = fake.city() + " to " + fake.city()
        departure_time = fake.time(pattern="%H:%M:%S")
        arrival_time = fake.time(pattern="%H:%M:%S")

        sql = "INSERT INTO bus_detail (driver_id,conductor_id,bus_number, bus_model, seating_capacity, route, departure_time, arrival_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (driver_id,conductor_id,bus_number, bus_model, seating_capacity, route, departure_time, arrival_time)

        cursor.execute(sql, values)
        db_connection.commit()



# Call functions to insert data
insert_bus_data()
# insert_conductor_data()
# insert_driver_data()
# insert_platform_data()
# insert_ticket_data()

# Close the cursor and the database connection

cursor.close()
db_connection.close()
