import psycopg2

conn = psycopg2.connect(host="localhost", dbname="FlaskCars", user="postgres", password="admin123", port="5432")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS cars(
    id INT PRIMARY KEY,
    model VARCHAR(255),
    price INT
);    
""")

cur.execute("""INSERT INTO cars (id, model, price) VALUES
(1, 'Audi-123',100),
(2, 'GM-44x',200)
ON CONFLICT DO NOTHING 
""")

cur.execute("""SELECT * FROM cars WHERE model= %s;""", ('GM-44x',))
print(cur.fetchone())
conn.commit()
cur.close()
conn.close()