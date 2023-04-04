import numpy as np

def point_derivative(fun, x, eps = 0.001, mode = 3):
    if mode == 2:
        return (fun(x + eps) - fun(x))/eps    
    elif mode == 3:
        return (fun(x + eps) - fun(x - eps))/(2 * eps)
    
def segment_derivative(fun, a, b, eps = 0.001, mode = 3):
    segment = np.arange(a, b, eps)
    df = []

    for i in segment:
        df.append(point_derivative(fun, i, eps, mode))

    return segment, df

def integrate_rect(fun, a, b, n):
    segment = np.linspace(a, b, n)
    sum_up = 0
    sum_down = 0

    for i in range(1, n):
        sum_up += (segment[i] - segment[i - 1]) * fun(segment[i])    
        sum_down += (segment[i] - segment[i - 1]) * fun(segment[i-1])

    return sum_up, sum_down

def integrate_trap(fun, a, b, n):
    segment, dx = np.linspace(a, b, n, retstep = True)
    integral = 0

    for i in range(1, n):
        integral += fun(segment[i-1]) + fun(segment[i])
        
    return dx * integral/2

    

    
