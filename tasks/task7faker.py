from faker import Faker
fake_data = Faker("ru_RU")


def generate_people_faker(n):
    return [generate_person_faker() for _ in range(n)]

def generate_person_faker():

    random_name = fake_data.name()
    random_email = fake_data.ascii_email()
    random_phone = fake_data.phone_number()

    return {"name": random_name,"email": random_email,"phone": random_phone}