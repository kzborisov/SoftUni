import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='db_demos',
    user='postgres',
    password='1123QwER',
)

cursor = conn.cursor()

result = cursor.execute("""
SELECT CONCAT(e.name, ' (', e.job_title, ' )') AS "Employee",
       CONCAT(m.name, ' (', m.job_title, ' )') AS "Manager"
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.id;
""")


class Employee:
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager

    def __repr__(self):
        return f"{self.name}, {self.manager}"


employees = [Employee(*row) for row in cursor.fetchall()]
[print(e) for e in employees]

conn.close()
# ORM - Object-Relational Mapping
# Mapping Classes to Table

