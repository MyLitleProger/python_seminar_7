# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь.
# Напишите функцию find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета.
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет,
# зато искусственные спутники были запущены на круговые орбиты.
# Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты.
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса.
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса.
# При решении задачи используйте списочные выражения.
# Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса,
# а затем найти и сам эллипс, имеющий такую площадь.
# Гарантируется, что самая далекая планета ровно одна
import math
from random import randint

planets = [(randint(1, 10), randint(1, 10)) for _ in range(10)]
print(f'общий список планет с осями {planets}')


def find_farthest_orbit(planets: list):
    planets = list(filter(lambda x: x[0] != x[1], planets))
    print(f'Исключили планеты с равными осями: {planets}')
    weight_planets = list(enumerate(map(lambda x: round(math.pi * x[0] * x[1], 2), planets), 1))
    print(f'Вес планет: {weight_planets}')
    result = list(zip(planets, weight_planets))
    return result


all_planets = find_farthest_orbit(planets)

max_planet = all_planets[0]
for max_p in all_planets:
    if max_p[1][1] > max_planet[1][1]:
        max_planet = max_p

print(f'Самая большая планеты с индексом {max_planet[1][0]}, '
      f'массой {max_planet[1][1]} и осями: {max_planet[0]}')
