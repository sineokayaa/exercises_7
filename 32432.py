n = int(input())
m = int(input())
gr = []
cities = {}
n = 0
for i in range(m):
    x = input().split()
    gr.append(list(y for y in x))
    if x[0] not in cities.keys():
        cities[x[0]] = n
        n += 1
    if x[1] not in cities.keys():
        cities[x[1]] = n
        n += 1

print('gr-', gr)
print(cities)

for i in range(len(gr)):
    gr[i][0] = cities[gr[i][0]]
    gr[i][1] = cities[gr[i][1]]

print(gr)


def lst_to_matrix(g, n):
    # n = max(max(v1, v2) for v1, v2, c in g) + 1  # к-во вершин(+1 т.к. нумируем с 0)
    matr = []
    for i in range(n):  # для каждый вершины
        matr.append([float('inf')] * n)
    for city_1, city_2, dist in g:
        matr[city_1][city_2] = dist
        matr[city_2][city_1] = dist
    return matr


matrix = lst_to_matrix(gr, n)  # каждая вершина какие имеет пути до други вершин
for i in range(len(matrix)):
    for k in range(len(matrix[i])):
        if matrix[i][k] != float('inf'):
            matrix[i][k] = int(matrix[i][k])
print(matrix)


def floyd(m, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if m[i][k] + m[k][j] < m[i][j]:
                    m[i][j] = min((m[i][j]), m[i][k] + m[k][j])
    return m
floyd(matrix, n)
task = input().split()
symb_1 = task[0]
symb_2 = task[1]
num_1 = cities[symb_1]
num_2 = cities[symb_2]
print(matrix[num_1][num_2])