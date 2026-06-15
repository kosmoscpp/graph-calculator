import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("Python Graphing Calculator")
    print("-----------------------------")
    expr_str = input("Enter expression in x (e.g. sin(x) + x**2 - log(x)): ")
    x_min, x_max = map(float, input("Enter x range (min max): ").split())

    # Define variable and parse expression
    x = sp.symbols('x')
    try:
        expr = sp.sympify(expr_str)
    except Exception as e:
        print("X Invalid expression:", e)
        return

    # sympy expression ko numpy function me convert kro
    f = sp.lambdify(x, expr, modules=["numpy"])

    # values nikalo
    xs = np.linspace(x_min, x_max, 500)
    ys = f(xs)

    # Plotting
    plt.figure(figsize=(8, 5))
    plt.axhline(0, color="black", linewidth=0.7)  # x-axis
    plt.axvline(0, color="black", linewidth=0.7)  # y-axis
    plt.plot(xs, ys, label=str(expr))
    plt.legend()
    plt.title("Graph of " + str(expr))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
