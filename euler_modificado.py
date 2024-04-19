import math
def euler_modificado(f, y0, t, h):
    k1 = f(t, y0)
    print('k1=f({},{})='.format(t,y0))
    print(k1)
    input()
    k2 = f(t+h/2, [round(y0[i],3) + round(h/2*k1[i],3) for i in range(len(k1))])
    print('k2=f({},{})='.format(t+h/2,[y0[i] + h/2*k1[i] for i in range(len(k1))]))
    print(k2)
    input()
    return [y0[i] + h*k2[i] for i in range(len(k1))]

n_var = int(input("Digite o número de variáveis: "))

if n_var == 2:
    y0 = [float(input("y0[{}]: ".format(i))) for i in range(n_var)]
    h = float(input("h: "))
    def f(t, y):
        dy1 = y[1]
        dy2 = 2*(10*math.exp(6*t) - 5*(y[0]+1)*y[1] - (y[0]+y[1])**2)
        return [dy1, dy2]
elif n_var == 3:
    y0 = [float(input("y0[{}]: ".format(i))) for i in range(n_var)]
    h = float(input("h: "))
    def f(t, y):
        dy1 = y[1]
        dy2 = y[2]
        dy3 = 2*(10*math.exp(6*t) - 5*(y[0]+1)*y[2] - (y[0]+y[1])**2)
        return [dy1, dy2, dy3]
elif n_var == 4:
    y0 = [float(input("y0[{}]: ".format(i))) for i in range(n_var)]
    h = float(input("h: "))
    def f(t, y):
        dy1 = y[1]
        dy2 = y[2]
        dy3 = y[3]
        dy4 = 2*(10*math.exp(6*t) - 5*(y[0]+1)*y[3] - (y[0]+y[1])**2)
        return [dy1, dy2, dy3, dy4]
t = 0
y1 = euler_modificado(f, y0, t, h)
print('y1=')
print(y1)
t = t+h
y2 = euler_modificado(f, y1, t, h)
print('y2=')
print(y2)
print('passo dobrado')
h2 = h/2
t = 0
y1_2 = euler_modificado(f, y0, t, h2)
print('y1/2=')
print(y1_2)
t = t+h2
y2_2 = euler_modificado(f, y1_2, t, h2)
print('y1=')
print(y2_2)
t = t+h2
y3_2 = euler_modificado(f, y2_2, t, h2)
print('y3/2=')
print(y3_2)
t = t+h2
y4_2 = euler_modificado(f, y3_2, t, h2)
print('y2=')
print(y4_2)
print('erro:')
erro = [4/3*(y2_2[i]-y1[i]) for i in range(len(y2_2))] 
print(erro)
y1_ast = [-1/3 * (y1[i] - 4*y2_2[i]) for i in range(len(y2_2))]
e_perc = [100 * erro[i]/y1_ast[i] for i in range(len(y2_2))]
input()
print('y1_ast=')
print(y1_ast)
print('e_perc=')
print(e_perc)
input()
K = max([erro[i]/h**3 for i in range(len(y2_2))])
print('K=', K)