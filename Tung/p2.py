from ortools.linear_solver import pywraplp
#input
n,m,k,s,t = map(int,input().split())
edges = [list(map(int,input().split())) for i in range(m)]

f_edges = [list(map(int,input().split())) for i in range(k)]

In = [set() for i in range(n)]
Out = [set() for i in range(n)]
for u,v,c in edges:
    In[v].add((u,c))
    Out[u].add((v,c))

#solver
solver = pywraplp.Solver(name='factory-mlip',problem_type=pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
inf = solver.infinity()
x = {}
d = {}
for e in edges:
    u,v,c = e
    x[(u,v)] = solver.IntVar(lb=0,ub=1,name=f'x_{u}_{v}')
    d[(u,v)] = c
for e in f_edges:
    u1,v1,u2,v2 = e
    solver.Add(x[(u1,v1)]+x[(u2,v2)]<=1)

solver.Add(solver.Sum(x[(v[0],s)] for v in In[s])==0)
solver.Add(solver.Sum(x[(s,v[0])] for v in Out[s])==1)
solver.Add(solver.Sum(x[(v[0],t)] for v in In[t])==1)
solver.Add(solver.Sum(x[(t,v[0])] for v in Out[t])==0)

for u in range(n):
    if u!=s and u!=t:
        solver.Add(solver.Sum(x[(v[0],u)] for v in In[u])==solver.Sum(x[(u,v[0])] for v in Out[u]))

z = solver.Sum(x[key]*d[key] for key,value in x.items())
solver.Minimize(z)

status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    print(int(solver.Objective().Value()))
    # for key,value in x.items():
    #     if value.solution_value()>0:
    #         print(key[0],key[1])
else:
    print(-1)