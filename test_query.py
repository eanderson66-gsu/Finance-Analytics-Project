import duckdb as db

con = db.connect("setup_example.duckdb")

result = con.sql("SELECT COUNT(*) AS total_customers FROM raw_customers").fetch()

print("Connection succesful")
print(result)

con.close()
