import psycopg

with psycopg.connect(
    dbname="neondb",
    user="neondb_owner",
    password="npg_0cApHkVtwx5W",
    host="ep-super-king-agiarlrl-pooler.c-2.eu-central-1.aws.neon.tech",
    port=5432
) as connection:
    with connection.cursor() as cursor:
        query = """
            CREATE TABLE IF NOT EXISTS brand (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50)        NOT NULL    UNIQUE
            )
        """
        cursor.execute(query)
        query_insert = "INSERT INTO brand (name) VALUES (%s)"
        cursor.execute(query_insert, ("Nissan", ))
        print("OK")