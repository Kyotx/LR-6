A = int(input('Введите число A: '))

B = int(input('Введите число B: '))

def NOD(a, b):

    if b == 0:
        return a

    else:
        return NOD(b, a % b)

result = NOD(A, B)

print('Наибольший общий делитель чисел', A, 'и', B, 'равен', result)