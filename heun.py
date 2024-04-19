import math
def heun(f, y0, t, h):
    k1 = f(t, y0)
    print('k1=f({},{})='.format(t,y0))
    print(k1)
    input()
    k2 = f(t+h, [y0[i] + h*k1[i] for i in range(len(k1))])
    print('k2= f({},{})='.format(t+h, [y0[i] + h*k1[i] for i in range(len(k1))]))
    print(k2)
    input()
    return [y0[i] + h*(k1[i] + k2[i])/2 for i in range(len(k1))]

n_var = int(input("Digite o número de variáveis: "))

if n_var == 2:
    y0 = [float(input("y0[{}]: ".format(i))) for i in range(n_var)]
    h = float(input("h: "))
    def f(t,y):
        dy1 = y[1] + math.sin(y[0]*t/2)
        dy2 = y[0]**3 + 2*y[0]
        return [dy1, dy2]
elif n_var == 3:
    y0 = [float(input("y0[{}]: ".format(i))) for i in range(n_var)]
    def f(t,y):
        dy1 = y[1] + math.sin(y[0]*t/2)
        dy2 = y[0]**3 + 2*y[0]
        dy3 = y[2] + math.sin(y[1]*t/2)
        return [dy1, dy2, dy3]
elif n_var == 4:
    y0 = [float(input("y0[{}]: ".format(i))) for i in range(n_var)]
    def f(t,y):
        dy1 = y[1] + math.sin(y[0]*t/2)
        dy2 = y[0]**3 + 2*y[0]
        dy3 = y[2] + math.sin(y[1]*t/2)
        dy4 = y[3] + math.sin(y[2]*t/2)
        return [dy1, dy2, dy3, dy4]
t = 0
y1 = heun(f, y0, t, h)
print(y1)
t = t+h
print('passo dobrado')
h2 = h/2
t = 0
y1_2 = heun(f, y0, t, h2)
print('y1/2=')
print(y1_2)
t = t+h2
y2_2 = heun(f, y1_2, t, h2)
print('y1=')
print(y2_2)
erro = [4/3*(y2_2[i]-y1[i]) for i in range(len(y2_2))] 
print('erro:', erro)
y1_ast = [-1/3 * (y1[i] - 4*y2_2[i]) for i in range(len(y2_2))]
input()
print('y1*=' , y1_ast)
e_perc = [100 * erro[i]/y1_ast[i] for i in range(len(y2_2))]
input()
print('erro percentual:')
print(e_perc)
input()
K = max([erro[i]/h**3 for i in range(len(y2_2))])
print('K=', K)