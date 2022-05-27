import json
import time

from tasks import task6, task7, task7faker, task1, task2, task4, task5, task8, task3

if __name__ == '__main__':

    list1 = [0, 1, 1, 0]
    list2 = [1, 1, 1, 1]

    print(task1.task1(list1))
    print(task1.task1(list2))

    task2.wave("hello world")

    task3gen = task3.endless_wave("-- -- --", "+")
    for _ in range(10):
        print(next(task3gen))

    print(task4.find_word("ygyu gygy goyg polp zzzq opoo"))

    print (task5.task5("mouse"))
    print (task5.task5("male"))
    print (task5.task5("qwerty"))

    print(task6.roman_to_int("MCMXC"))
    print(task6.roman_to_int("MMVIII"))
    print(task6.roman_to_int("MDCLXVI"))

    fake_people = json.dumps(task7.generate_people(3),ensure_ascii=False,indent=4)
    print(fake_people)

    fakeppl = json.dumps(task7faker.generate_people_faker(3),ensure_ascii=False,indent=4)
    print(fakeppl)

    print(task8.time_from_pattern(time.time(),'%Y %m %d'))

