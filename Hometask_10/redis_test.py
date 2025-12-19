import redis
from dotenv import load_dotenv
import os

load_dotenv()

r = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True
)


print(r.ping())
# r.set("favorite_car", "TOYOTA")
# r.setex("favorite_pet", 7200, "Айка")
# r.rpush("shopping_list", "milk", "bread", "eggs", "cheese")
# r.expire("shopping_list", 604800)
r.hset("cake_ingredients", mapping={"flour": 250, "milk": 500})
# r.hset("cake_ingredients", "sugar", 300)
r.hset("cake_ingredients", "sugar", 500)
print(r.get("favorite_car"))
print(r.get("favorite_pet"))
print(r.lrange("shopping_list",0,2))
print(r.hgetall("cake_ingredients"))
r.delete("cake_ingredients")
print(r.hgetall("cake_ingredients"))