from ortools.linear_solver import pywraplp

n,m = map(int,input().split())
A = [float(i)for i in input().split()]
B = [float(i) for i in input().split()]
C = [[float(i) for i in input().split()] for i in range(n)]

#solver
solver = pywraplp.Solver.CreateSolver("GLOP")

#variables
inf = solver.infinity()
x = [[solver.NumVar(0,A[i],f'x_{i}_{j}') for j in range(m)] for i in range(n)]

#constraint
for i in range(n):
    solver.Add(solver.Sum(x[i][j] for j in range(m))<=A[i])
for j in range(m):
    solver.Add(solver.Sum(x[i][j] for i in range(n))>=B[j])

#objective
z = solver.Sum(solver.Sum(x[i][j]*C[i][j] for j in range(m)) for i in range(n))
solver.Minimize(z)

status = solver.Solve()

# print(status)
l=[]
if status == pywraplp.Solver.OPTIMAL:
    # print(solver.Objective().Value())
    print(n*m)
    for i in range(n):
        for j in range(m):
             print(i+1,j+1,float(x[i][j].solution_value()))
    #         if tmp>0:
    #             l.append((i+1,j+1,tmp))
    # print(len(l))
    # for i in l:
    #     print(*i)

# 3*9+1*20 = 27+20=47
# 2*12+3*8=24+24=48
# sum = 95

# 2->2 (17)=34
# 1->1 9 = 18
# 1->3 20 = 20
# 2->1 3 = 3
# 37+38