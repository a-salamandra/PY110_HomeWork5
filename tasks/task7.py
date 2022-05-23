import random
from string import ascii_lowercase, digits

def generate_people(n):
    return [generate_person() for _ in range(n)]

def generate_person():

    random_first_name = "".join(random.sample(ascii_lowercase, random.randint(2, 7))).title()
    random_last_name = "".join(random.sample(ascii_lowercase, random.randint(2, 11))).title()
    random_email = "".join("".join(random.sample(ascii_lowercase, random.randint(4, 10)))
                           + "@"
                           + "".join(random.sample(ascii_lowercase, random.randint(2, 5)))
                           + "".join((random.choice(['.net', '.com', '.ru']))))
    random_phone = "".join("+7"+"".join(random.sample(digits, 10)))

    return {"first_name": random_first_name,"last name": random_last_name, "email": random_email,"phone": random_phone}