
import copy

import numpy as np

set_x = np.array([1.0,2.0,3.0,4.0])
set_y = np.array([220.0,400.0,750.0,920.0])

def compute_cost(x,y,w,b):

    m = x.shape[0]

    cost = 0

    for i in range(m):
        j = w*x[i]+b
        j = (j-y[i])**2
        cost+=j
    cost_total = 1 / (2 * m) * cost

    return cost_total

def compute_gradiant(x, y, w, b):

    m = x.shape[0]

    w_cost = 0
    b_cost = 0

    for i in range(m):
        func_wb = w*x[i] + b
        w_cost_calc = (func_wb - y[i])*x[i]
        b_cost_calc = func_wb - y[i]
        w_cost += w_cost_calc
        b_cost += b_cost_calc
    w_final = w_cost/m
    b_final = b_cost/m

    return w_final, b_final

def calculate_gradient_descent(x, y, start_w, start_b, alpha, iterations):

    w = copy.deepcopy(start_w)
    
    b = start_b

    j_totals = []
    wb = []

    for i in range(iterations):

        grad_w, grad_b = compute_gradiant(x,y,w,b)

        b = b - alpha * grad_b
        w = w - alpha * grad_w

        if i < 100000:
            j_totals.append(compute_cost(x,y,w,b))
            wb.append([w,b])

    return w, b, j_totals, wb




start_w = 43
start_b = 10
alpha = 0.2365 #1.0e-2
iterations = 100000


w, b, j, wb = calculate_gradient_descent(set_x, set_y, start_w, start_b, alpha, iterations)

print(w,b)


