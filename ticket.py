import mysql.connector
from faker import Faker
import random

# Create a Faker instance
fake = Faker()

# Database connection parameters
db_config = {
    "host": "localhost",  # Change this to your MySQL host
    "user": "root",  # Change this to your MySQL username
    "password": "password",  # Change this to your MySQL password
    "database": "AICTSL_BUS",  # Change this to your database name
}

# Establish a database connection
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Insert random data into 'ticket' table
    for _ in range(10):  # Insert data for 10 tickets
        # Generate valid foreign key values (bus_id, conductor_id, driver_id, platform_id)
        bus_id = random.randint(1, 10)  # Assuming you have 10 buses in the 'bus_detail' table
        conductor_id = random.randint(1, 5)  # Assuming you have 5 conductors
        driver_id = random.randint(1, 5)  # Assuming you have 5 drivers
        platform_id = random.randint(1, 5)  # Assuming you have 5 platforms
        ticket_number = fake.unique.random_element(elements=("TICKET001", "TICKET002", "TICKET003"))
        passenger_name = fake.name()
        departure_time = fake.time_object(end_datetime=None)
        departure_date = fake.date_of_birth(minimum_age=18, maximum_age=60)
        fare = round(random.uniform(10.0, 50.0), 2)

        insert_query = "INSERT INTO ticket (bus_id, conductor_id, driver_id, platform_id, ticket_number, passenger_name, departure_time, departure_date, fare) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (bus_id, conductor_id, driver_id, platform_id, ticket_number, passenger_name, departure_time, departure_date, fare)
        cursor.execute(insert_query, data)

    # Commit the changes
    conn.commit()
    print("Data inserted successfully!")

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    # Close the database connection
    if conn.is_connected():
        cursor.close()
        conn.close()
