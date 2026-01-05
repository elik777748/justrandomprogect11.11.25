PGHOST='ep-super-king-agiarlrl-pooler.c-2.eu-central-1.aws.neon.tech'
PGDATABASE='neondb'
PGUSER='neondb_owner'
PGPASSWORD='npg_0cApHkVtwx5W'

import config
import psycopg

with psycopg.connect(
    dbname=config.PGDATABASE,
    user=config.PGUSER,
    password=config.PGPASSWORD,
    host=config.PGHOST,
    port=5432
) as connection:
    pass
