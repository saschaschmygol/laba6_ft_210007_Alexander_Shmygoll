import numpy as np                                        # модуль для работы с матрицами
while True:
    try:
        cr_amount = int(input("Введите кол-во критериев: "))
        break
    except ValueError:
        print('Вводите число !!!')


i = 1

matr = np.eye(cr_amount)                                  #создание матрицы


for q in range(i, cr_amount+1):                           # заполнение матрицы
  for p in range(i+1, cr_amount+1):
      while True:
          try:
              matr[q - 1][p - 1] = round(float(input("Введите сравнение критерия {0}-{1}: ".format(q, p))), 3)
              matr[p - 1][q - 1] = round((matr[q - 1][p - 1]) ** (-1), 2)
              break
          except:
              print('Вводите целое число от 1 до 10')

  i += 1

sum_matr = [round(sum(j),2) for j in matr]                    # создание списка весовых коэффициентов

for k in sum_matr:
  print(round(k/sum(sum_matr), 2), end=' ')                      # вывод списка






























