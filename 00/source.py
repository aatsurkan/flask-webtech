'''
Напишите функцию для нахождения кратного факториала числа Kfactorial.

Функция factorial должна иметь 2 параметра:

    n - число для которого вычисляется факториал (обязательный)
    k - кратность факториала (необязательный, значение по-умолчанию - 1)

Пример:

5!!=(2⋅1−1)⋅(2⋅2−1)⋅(2⋅3−1)=1⋅3⋅5

5!!!=(3⋅1−1)⋅(3⋅2−1)=2⋅5


Отсюда легко сформулировать 2 правила:

    Условие остановки рекурсии - Kfactorial(n, k) = n, если n<=k
    Шаг рекурсии -  Kfactorial(n, k) = n *  Kfactorial(n-k, k), если n > k
'''

def Kfactorial (n, k = 1):
    if (n == 0 or n == 1):
        return 1    
    elif (n <= k):
        return n
    else:
        return n * Kfactorial(n-k, k)

print(Kfactorial(10, 1))
print(Kfactorial(8))
print(Kfactorial(6, 3))

