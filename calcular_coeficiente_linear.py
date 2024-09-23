import math


def calcular_coeficiente_linear(I0, I, x):
    if I0 <= 0 or I <= 0 or x <= 0:
        raise ValueError("Os valores de I0, I e x devem ser maiores que zero.")
    mu = -math.log(I / I0) / x
    return mu


I0 = float(input("Digite a intensidade inicial da radiação (I0): "))
I = float(input("Digite a intensidade da radiação após passar pelo material (I): "))
x = float(input("Digite a espessura do material (x): "))

try:
    coeficiente_linear = calcular_coeficiente_linear(I0, I, x)
    print(f"O coeficiente linear de atenuação é: {coeficiente_linear:.4f}")
except ValueError as e:
    print(e)
