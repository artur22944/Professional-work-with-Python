# Задание «Квадратное уравнение»
def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    return b**2-4*a*c


def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    if discriminant(a, b, c) < 0:
        return 'корней нет'
    elif discriminant(a, b, c) == 0:
        x1 = (-b+discriminant(a, b, c)**0.5)/(2*a)
        return x1
    else:
        x1 = (-b+discriminant(a, b, c)**0.5)/(2*a)
        x2 = (-b-discriminant(a, b, c)**0.5)/(2*a)
        return x1, x2


# 