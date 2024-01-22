import matplotlib.pyplot as plt
import random
random.seed(7)

matrice1 = [
    [0, 6, 6, 1, 4],
    [6, 0, 8, 3, 5],
    [6, 8, 0, 6, 4],
    [1, 3, 6, 0, 2],
    [4, 5, 4, 2, 0]
]
matrice2 = [
    [0,1,1,3,4,5,6,1,7],
    [1,0,5,4,3,6,1,9,2],
    [1,5,0,1,6,1,9,3,7],
    [3,4,1,0,5,9,7,2,1],
    [4,3,6,5,0,9,1,2,1],
    [5,6,1,9,9,0,2,1,7],
    [6,1,9,7,1,2,0,4,5],
    [1,9,3,2,2,1,4,0,7],
    [7,2,7,1,1,7,5,7,0],
]

matrice = matrice2
vector_size = len(matrice)


def calculate_cost(x): # calculer distance
  prev_ele = x[0]
  cost = 0
  for ele in x[1:]:
    cost += matrice[prev_ele-1][ele-1]
    prev_ele = ele
  return cost

def best_sol(sol1, sol2):
  if calculate_cost(sol1) < calculate_cost(sol2):
    return sol1
  return sol2

def generate_neighbor(v):
  x = v.copy()
  v1 = random.randint(2, vector_size)
  v2 = random.randint(2, vector_size)
  while v1 == v2:
    v2 = random.randint(2, vector_size)
  # print(f"city {v1} replaced with city {v2}.")
  i, j = x.index(v1), x.index(v2)
  x[i], x[j] = x[j], x[i]
  return x

L = 5
tab = []
r1 = []
maxiterations = 80
x0 = [1,3,8,9,7,5,4,2,6,1]
x_best = x0
hist = []

for _ in range(maxiterations):
  print("iteration number:", _+1)
  x1 = generate_neighbor(x0)

  while x1 in tab:
    x1 = generate_neighbor(x0)

  x0 = best_sol(x0, x1)
  if calculate_cost(x0) < calculate_cost(x_best):
    x_best = x0

  if len(tab) < L:
    tab.append(x1)
    r1.append(5)
  index_to_delete = []
  for index in range(len(index_to_delete)):
    print(index, len(r1), len(tab))
    if r1[index] == 0:
      index_to_delete.append(index)
    else:
      r1[index]-=1
  for index in index_to_delete:
    del tab[index]
    del r1[index]
  hist.append(calculate_cost(x_best))

print(f"Best solution is x_best={x_best} with cost of {calculate_cost(x_best)}")
print(hist)
plt.plot([_ for _ in range(len(hist))], hist)
plt.xlabel("Number of iterations")
plt.ylabel("la distance ")
plt.grid()
plt.show()
