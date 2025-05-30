🚀 How to Use
1. Start the MySQL Container
bash
Copy
Edit
docker-compose up -d
This will start the MySQL server in a Docker container with the necessary configuration.

2. Log in to the MySQL Container
As studentuser:
bash
Copy
Edit
docker exec -it student-mysql mysql -u studentuser -p
Enter password: studentpass

As root:
bash
Copy
Edit
docker exec -it student-mysql mysql -u root -p
Enter password: rootpassword

3. Create a Database and Table (Optional)
If you want to manually create a new table inside studentdb:

sql
Copy
Edit
USE studentdb;

CREATE TABLE students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  age INT
);
4. Import SQL Dump (e.g., setup.sql)
If you have a SQL file named setup.sql in the same directory:

bash
Copy
Edit
docker cp setup.sql student-mysql:/setup.sql

docker exec -it student-mysql mysql -u studentuser -p studentdb < /setup.sql
You'll be prompted for studentpass.

✅ This will import the database structure and data into studentdb.

🧼 Cleanup
To stop and remove the container:

bash
Copy
Edit
docker-compose down
To also remove the associated volumes (i.e., stored data):

bash
Copy
Edit
docker-compose down -v
📂 Notes
Make sure port 3306 is not already in use.

setup.sql should contain valid SQL commands like CREATE TABLE or INSERT INTO.

