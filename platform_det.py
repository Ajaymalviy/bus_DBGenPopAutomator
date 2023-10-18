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

    # Insert random data into 'platform' table
    for i in range(1, 6):  # Insert data for 5 platforms
        platform_number = i
        description = fake.sentence()

        insert_query = "INSERT INTO platform (platform_number, description) VALUES (%s, %s)"
        data = (platform_number, description)
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
