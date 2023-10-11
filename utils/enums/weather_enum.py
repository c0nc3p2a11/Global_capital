from faker import Faker


fake_ru = Faker("ru_RU")
valid_negative = []
invalid_negative = []

for _ in range(3):
    invalid_negative.append(fake_ru.city_name())
    print(invalid_negative)


class Cities:
    VALID_POSITIVE = ["Алматы", "Aлма-ата", "Almaty"]
    INVALID_NEGATIVE = invalid_negative
