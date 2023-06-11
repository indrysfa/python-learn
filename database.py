import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost", user="root", password="root", database="python"
)
# Create a cursor object
cursor = conn.cursor()


# Create new table
cursor.execute("create table users(id INT, name VARCHAR(30), email VARCHAR(40))")


# Create operation (insert data)
sql = "INSERT INTO users (id, name, email) VALUES (%s, %s, %s)"
values = (2, "gustaf", "gustaf@gmail.com")  # Replace with your actual values
cursor.execute(sql, values)
conn.commit()


# Read operation (retrieve data)
# Define the SELECT statement
sql = "SELECT * FROM users WHERE id = %s"

# Execute the SELECT statement
id = 1  # Replace with the desired ID value
cursor.execute(sql, (id,))

# Fetch the retrieved data
result = cursor.fetchone()
print(result)


# Update operation (modify data)
# Define the UPDATE statement
sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"

# Execute the UPDATE statement
name = "harbor"  # Replace with the new value for column1
email = "harbor@gmail.com"  # Replace with the new value for column2
id = 1  # Replace with the ID value of the row you want to update
cursor.execute(sql, (name, email, id))
conn.commit()


# # Delete operation (remove data)
# Define the DELETE statement
sql = "DELETE FROM users WHERE id = %s"

# Execute the DELETE statement
id = 1  # Replace with the ID value of the row you want to delete
cursor.execute(sql, (id,))
conn.commit()


# Close the cursor and the database connection
cursor.close()
conn.close()
