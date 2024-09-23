# Cálculo do Coeficiente Linear de Atenuação da Radiação

Este projeto contém um algoritmo em Python para calcular o coeficiente linear de atenuação da radiação ao passar por um material. O coeficiente linear de atenuação é uma medida de quanto a radiação é reduzida ao atravessar um material específico.

## Fórmula

A fórmula utilizada para calcular o coeficiente linear de atenuação (\( \mu \)) é derivada da equação de atenuação exponencial:

\[ I = I_0 \cdot e^{-\mu x} \]

Onde:

- \( I \) é a intensidade da radiação após passar pelo material.
- \( I_0 \) é a intensidade inicial da radiação.
- \( \mu \) é o coeficiente linear de atenuação.
- \( x \) é a espessura do material.

Rearranjando a fórmula para resolver \( \mu \):

\[ \mu = -\frac{\ln(I/I_0)}{x} \]

## Requisitos

- Python 3.x

## Como Usar

1. Clone este repositório para o seu ambiente local.
2. Execute o script `calcular_coeficiente_linear.py`.

### Exemplo de Uso

O script solicita ao usuário os valores de \( I_0 \), \( I \) e \( x \), e então calcula e imprime o coeficiente linear de atenuação.

```python
import math

def calcular_coeficiente_linear(I0, I, x):
    if I0 <= 0 ou I <= 0 ou x <= 0:
        raise ValueError("Os valores de I0, I e x devem ser maiores que zero.")
    mu = -math.log(I / I0) / x
    return mu

# Exemplo de uso
I0 = float(input("Digite a intensidade inicial da radiação (I0): "))
I = float(input("Digite a intensidade da radiação após passar pelo material (I): "))
x = float(input("Digite a espessura do material (x): "))

try:
    coeficiente_linear = calcular_coeficiente_linear(I0, I, x)
    print(f"O coeficiente linear de atenuação é: {coeficiente_linear:.4f}")
except ValueError as e:
    print(e)
```

### Passo a Passo

1. **Entrada de Dados**: O usuário deve fornecer os valores de intensidade inicial da radiação (\( I_0 \)), intensidade da radiação após passar pelo material (\( I \)) e a espessura do material (\( x \)).
2. **Cálculo**: O algoritmo calcula o coeficiente linear de atenuação usando a fórmula mencionada.
3. **Saída**: O coeficiente linear de atenuação é exibido na tela.

## Tratamento de Erros

O algoritmo inclui uma verificação para garantir que os valores de \( I_0 \), \( I \) e \( x \) sejam maiores que zero. Caso contrário, uma mensagem de erro é exibida.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
