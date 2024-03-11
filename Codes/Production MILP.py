from pyomo.environ import *

model = ConcreteModel()

model.A = Var(domain=NonNegativeReals)
model.B = Var(domain=NonNegativeReals)
model.C = Var(domain=NonNegativeReals)

# Binary variables
model.proc1 = Var(domain=Binary)
model.proc2 = Var(domain=Binary)
model.buyB = Var(domain=Binary)

model.con1 = Constraint(expr=model.B == 0.9 * model.A)
model.con2 = Constraint(expr=model.C <= 10 * model.proc1 + 15 * model.proc2)
model.con3 = Constraint(expr=model.C == 0.82 * model.B * model.proc1 + 0.95 * model.B * model.proc2)
model.con4 = Constraint(expr=model.B <= 950 * model.buyB + 550 * (1 - model.buyB))
model.con5 = Constraint(expr=model.A <= 16)
model.con6 = Constraint(expr=model.proc1 + model.proc2 == 1)

model.obj = Objective(
    expr=18 * model.C - 2.5 * model.A - 4 * model.B - 5 * model.C - 10 * model.proc1 - 15 * model.proc2 - 9.5 * model.buyB,
    sense=maximize
)

solver = SolverFactory('gurobi')
results = solver.solve(model)
solver.solve(model, tee=True)
print(f"Maximum profit: {model.obj():.2f}")
print(f"Process II: {model.proc1():.0f}")
print(f"Process III: {model.proc2():.0f}")
print(f"Buy B: {model.buyB():.0f}")
print(f"A: {model.A():.2f}")
print(f"B: {model.B():.2f}")
print(f"C: {model.C():.2f}")


