import mysql.connector
from faker import Faker

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

    # Insert random data into 'conductor' table
    for _ in range(5):  # Insert data for 5 conductors
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()

        insert_query = "INSERT INTO conductor (first_name, last_name, email) VALUES (%s, %s, %s)"
        data = (first_name, last_name, email)
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
