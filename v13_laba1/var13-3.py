# Заданы значения масс

M = 80

m1 = 400 

m2_start = 100

m2_end = 300

m2_step = 20

g = 9.8

print('Масса (m2);', 'Ускорение;')

# Цикл для перебора значений m2

for m2 in range(m2_start, m2_end+1, m2_step):

    # Вычисление значения ускорения по формуле

    a = (m2 - m1) / (m1 + m2 + M/2) * g

    # Вывод результата

    print(m2,'       ', a)