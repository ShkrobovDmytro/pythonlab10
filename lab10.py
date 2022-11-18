import sympy as sp
from math import factorial


def taylor(x):
    y = 0
    d1 = sp.diff(f, x)  # перша похідна
    d2 = sp.diff(d1, x)  # друга похідна
    d3 = sp.diff(d2, x)  # третя похідна
    d4 = sp.diff(d3, x)  # 4та похідна
    print('d1=', d1)
    print('d2=', d2)
    print('d3=', d3)
    print('d4=', d4)
    print("f(0)=", f.subs({x: 0}))
    print("d1(0)=", d1.subs({x: 0}))
    print("d3(0)=", d2.subs({x: 0}))
    print("d3(0)=", d3.subs({x: 0}))
    y += f.subs({x: 0}) + d1.subs({x: 0}) * x + d2.subs({x: 0}) * (x - 0) ** 2 / factorial(2) + d3.subs({x: 0}) * (
            x - 0) ** 3 / factorial(3)
    # sp.plot(d4, (x, -1, 1), label='d4', title="Графік четвертої похідної")  # графік 4ї похідної при x є [-1, 1]
    print('y = ', y)
    return y


x = sp.symbols('x')
f = sp.exp(sp.sin(x)) + 2 * x
taylor_x = taylor(x)
sp.plot(taylor_x, f, (x, -1, 1), title='Графік функції f та її наближення', legend=True)
