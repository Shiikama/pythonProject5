import numpy as np
                         #1 задание
# (код находит коэффициенты а, б методом крамера).

# X = [1, 2, 3, 4, 5]
# Y = [3, 5, 7, 9, 11]
# n = len(X)
#
# summx, summxy, summy, summx2 = 0, 0, 0, 0
# for i in range(0, n):
#     summxy += (X[i] * Y[i])
#     summx += X[i]
#     summy += Y[i]
#     summx2 += X[i]*X[i]
#
# a = (n*summxy - summx*summy)/(n*summx2-(summx)*(summx))
# b = 1/n * summy - a * (summx/n)
# print(a, b)


#                         2 задание (линейная регрессия)

#Сделаем функцию, которая будет находить обратную матрицу методом гауссовой прогонки
# mini_mas - матрциа на входе, от которой хотим найти обратную.
def reverse_matrix(mini_mas):

    maxi_mas = np.zeros((len(mini_mas), 2*len(mini_mas)),dtype=float)
    for i in range(len(mini_mas)):
        for j in range(2*len(mini_mas)):
            if j>=len(mini_mas):
                if i == j-len(mini_mas):
                    maxi_mas[i][j]=1
            else:
                maxi_mas[i][j]=mini_mas[i][j]
    mas = maxi_mas


    for i in range (0, len(mas)):
        a = mas[i][i]
        for j in range (2*len(mas)):
            mas[i][j] = mas[i][j]/a
        print(mas)
        for k in range (i+1, len(mas)):
            b = mas[k][i]
            for j in range(2*len(mas)):
                mas[k][j]+=mas[i][j]*(-1)*b
        print(mas)


    for i in range (len(mas)-1,0,-1):
        for k in range (i-1, -1, -1):
            b = mas[k][i]
            for j in range(2*len(mas)):
                mas[k][j]-=mas[i][j]*b
    # print(mas) #len(mas) = 3

    rev_mas = np.zeros((len(mini_mas), len(mini_mas)),dtype=float)
    for i in range (0,len(mas)):
        for j in range (0, len(mas)*2):
            if j>=len(mas):
                rev_mas[i][j-len(mas)] = mas[i][j]
    # print('X^(-1) = ', rev_mas)
    return(rev_mas)

#________ Функция, находящая трансп матрицу
def transp_matrix(mini_mas):
    tr_mas = np.zeros((len(mini_mas), len(mini_mas)))
    for i in range(0, len(mini_mas)):
        for j in range(0, len(mini_mas)):
            tr_mas[i][j]=mini_mas[j][i]
    return(tr_mas)


# Алгоритм для линейной регрессии
Y = np.array([[42000], [144000], [151000]])
print("Y = ", Y)
X = np.array([[2310, 2, 20], [2333, 2, 12], [2356, 3, 33]], dtype=float)
print("X = ", X)
rm = reverse_matrix(X)
print('X^(-1) = ', rm)
tm = transp_matrix(X)
print("X_tr = ", tm)
# Разные промежуточные вычисления
G = np.dot(X, rm) #векторное произведение
temp = np.dot(tm, X)
temp_rev = reverse_matrix(temp)
meow = np.dot(temp_rev, tm)
B = np.dot(meow, Y)
print(f"Конечный результат \n B = ", B)

# Проверка: даст ли перемножение матрицы Х на обратную ноль?
# print(np.dot(X,rm)) Ура, все нормально
