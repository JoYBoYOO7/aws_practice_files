# EC2 and MySQL Setup: A Step-by-Step Guide

This guide provides a complete walkthrough for creating an AWS EC2 instance, installing a MySQL server, managing a student database with various SQL queries, and performing a database backup using `mysqldump`.

## Table of Contents

- [Part 1: Launch and Connect to EC2 🚀](#part-1-launch-and-connect-to-ec2-)
  - [Step 1: Launch an EC2 Instance](#step-1-launch-an-ec2-instance)
  - [Step 2: Connect to Your Instance via SSH](#step-2-connect-to-your-instance-via-ssh)
- [Part 2: Install and Configure MySQL Server 🗄️](#part-2-install-and-configure-mysql-server-️)
  - [Step 3: Install MySQL](#step-3-install-mysql)
  - [Step 4: Start and Secure MySQL](#step-4-start-and-secure-mysql)
- [Part 3: Create the Student Database 🎓](#part-3-create-the-student-database-)
  - [Step 5: Create the Database](#step-5-create-the-database)
  - [Step 6: Create the `students` Table](#step-6-create-the-students-table)
- [Part 4: Insert Data ✍️](#part-4-insert-data-️)
  - [Step 7: Insert Five Student Records](#step-7-insert-five-student-records)
- [Part 5: Execute SQL Queries 🔍](#part-5-execute-sql-queries-)
  - [Ten Sample Queries](#ten-sample-queries)
- [Part 6: Backup the Database 💾](#part-6-backup-the-database-)
  - [Step 8: Export the Database using `mysqldump`](#step-8-export-the-database-using-mysqldump)

---

## Part 1: Launch and Connect to EC2 🚀

### Step 1: Launch an EC2 Instance

First, you'll need a virtual server in the cloud.

1.  **Navigate to EC2:** Log in to your AWS Management Console and go to the EC2 service.
2.  **Launch Instance:** Click the **Launch instance** button.
3.  **Choose an AMI:** Select **Amazon Linux 2 AMI**, as it's free-tier eligible and stable.
4.  **Choose Instance Type:** Select the `t2.micro` instance type, which is part of the AWS Free Tier.
    - ``
5.  **Configure Key Pair:** Either choose an existing key pair or create a new one. **Download and save your `.pem` file securely!** You will need it to connect to your instance.
6.  **Network Settings (Security Group):** This is crucial for access. Create a new security group with the following inbound rules:
    - **Type:** `SSH`, **Protocol:** `TCP`, **Port Range:** `22`, **Source:** `My IP` (for security).
    - **Type:** `MySQL/Aurora`, **Protocol:** `TCP`, **Port Range:** `3306`, **Source:** `My IP`. This allows you to connect to your database from your own computer if needed.
7.  **Launch:** Review your settings and click **Launch instance**.

### Step 2: Connect to Your Instance via SSH

Once your instance is in the "running" state, you can connect to it.

1.  **Get Public IP:** Select your instance in the EC2 dashboard and copy its **Public IPv4 address**.
2.  **Open a Terminal:** Use your preferred terminal (Terminal on macOS/Linux, PowerShell on Windows).
3.  **Set Permissions:** Navigate to where you saved your `.pem` file and restrict its permissions. This is a one-time step.
    ```bash
    chmod 400 your-key-name.pem
    ```
4.  **Connect:** Use the following SSH command, replacing the placeholders with your details.
    ```bash
    ssh -i "your-key-name.pem" ec2-user@your-public-ip-address
    ```
    When prompted, type `yes` to continue. You are now connected!
    - ``

---

## Part 2: Install and Configure MySQL Server 🗄️

### Step 3: Install MySQL

Now, let's install the database server on your instance.

1.  **Update Packages:** Update your instance's packages first.
    ```bash
    sudo yum update -y
    ```
2.  **Install MySQL Server:**
    ```bash
    sudo yum install -y mysql-server
    ```

### Step 4: Start and Secure MySQL

1.  **Start the Service:**
    ```bash
    sudo systemctl start mysqld
    sudo systemctl enable mysqld
    ```
2.  **Secure Installation:** Run the security script to set a `root` password and remove insecure defaults.
    ```bash
    sudo mysql_secure_installation
    ```
    You will be prompted to set a strong password and answer `Y` (yes) to the subsequent security questions.

---

## Part 3: Create the Student Database 🎓

### Step 5: Create the Database

1.  **Log in to MySQL:**
    ```bash
    mysql -u root -p
    ```
    Enter the root password you just created.
2.  **Create the Database:** Execute the following SQL command.
    ```sql
    CREATE DATABASE student_db;
    ```
3.  **Use the Database:**
    ```sql
    USE student_db;
    ```

### Step 6: Create the `students` Table

Define the structure for your student records.

```sql
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(50),
    year INT,
    dob DATE
);
```

Part 4: Insert Data ✍️

## Step 7: Insert Five Student Records

Let's add some sample data to the students table.

```sql
INSERT INTO students (name, department, year, dob) VALUES
('Arjun Kumar', 'Computer Science', 2, '2004-08-15'),
('Priya Sharma', 'Electronics', 3, '2003-05-22'),
('Rohan Mehta', 'Mechanical', 2, '2004-11-10'),
('Sneha Patil', 'Computer Science', 4, '2002-02-28'),
('Vikram Singh', 'Civil', 3, '2003-07-19');
```

## Part 5: Execute SQL Queries 🔍

Here are ten queries to manage and retrieve data. For the JOIN query, we'll first create a courses table.

### Create a courses table:

SQL

```sql
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    department VARCHAR(50)
);

INSERT INTO courses VALUES
(101, 'Data Structures', 'Computer Science'),
(201, 'Circuit Theory', 'Electronics'),
(301, 'Thermodynamics', 'Mechanical');

```

Ten Sample Queries
Select all students.

SQL

```sql
SELECT * FROM students;
Select students from the 'Computer Science' department. (WHERE Clause)

SELECT name, year FROM students WHERE department = 'Computer Science';

UPDATE students SET department = 'Mechanical Engineering' WHERE student_id = 3;
Delete a student record. (DELETE Clause)

-- Add a temporary record to delete
INSERT INTO students (name, department, year, dob) VALUES ('Temp User', 'Civil', 1, '2005-01-01');
-- Now delete it
DELETE FROM students WHERE name = 'Temp User';
List students born after 2003. (WHERE with Date)

SELECT name, dob FROM students WHERE dob > '2003-12-31';
Count the total number of students. (Aggregate Function COUNT)

SELECT COUNT(*) AS total_students FROM students;
Find students in their 2nd or 3rd year. (IN Clause)

SELECT name, department, year FROM students WHERE year IN (2, 3);
List students whose names start with 'A'. (LIKE Clause)

SELECT * FROM students WHERE name LIKE 'A%';
List students and the courses available in their department. (JOIN Clause)

SELECT s.name, s.department, c.course_name
FROM students s
JOIN courses c ON s.department = c.department;
Count how many students are in each department. (GROUP BY Clause)


SELECT department, COUNT(student_id) AS number_of_students
FROM students
GROUP BY department;
```

## Part 6: Backup the Database 💾

Step 8: Export the Database using mysqldump
Finally, create a backup file of your entire database.

Exit MySQL: Type exit; in the MySQL prompt to return to the EC2 command line.

Run mysqldump: This command will create a student_db_backup.sql file in your current directory.

Bash

```sql
mysqldump -u root -p student_db > student_db_backup.sql
```

You will be prompted to enter your MySQL root password.

Verify the Backup: Check that the file was created successfully.

Bash

```
ls -l
You should see student_db_backup.sql listed in the output.
```
