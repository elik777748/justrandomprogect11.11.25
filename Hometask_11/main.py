import jwt
from datetime import datetime, timedelta
import time

SECRET_KEY = ""
ALGORITHM = "HS256"


payload = {
    "name": "Yelysei",
    "age": 15,
    "city": "Odesa",
    "exp": datetime.utcnow() + timedelta(seconds=500)
}


# token_1000 = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
# print("TOKEN (1000 sec):", token_1000)
# decoded = jwt.decode(token_1000, SECRET_KEY, algorithms=[ALGORITHM])
# print("DECODED:", decoded)

# token_10 = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
# print("TOKEN (10 sec):", token_10)
# time.sleep(15)
# decoded = jwt.decode(token_10, SECRET_KEY, algorithms=[ALGORITHM])
# print("DECODED:", decoded)


token_500 = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
print("TOKEN (10 sec):", token_500)
decoded = jwt.decode(token_500, "wrong_key", algorithms=[ALGORITHM])
print("DECODED:", decoded)
