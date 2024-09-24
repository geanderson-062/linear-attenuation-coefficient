# Cálculo do Coeficiente Linear de Atenuação da Radiação

Este projeto contém um algoritmo em Python para calcular o **coeficiente linear de atenuação da radiação** ao atravessar um material. Esse coeficiente (\( \mu \)) é uma medida que quantifica a redução da intensidade da radiação ao passar por um material, sendo fundamental em áreas como física médica e engenharia de materiais.

## Fórmula

A fórmula usada para calcular o coeficiente linear de atenuação é baseada na **equação de atenuação exponencial**:

```
I = I0 * e^(-μ * x)
```

Onde:

- `I`: intensidade da radiação após atravessar o material;
- `I0`: intensidade inicial da radiação;
- `μ`: coeficiente linear de atenuação;
- `x`: espessura do material.

Para calcular \( \mu \), a equação pode ser rearranjada como:

```
μ = -ln(I / I0) / x
```

## Requisitos

- Python 3.x

## Como Usar

1. Clone este repositório para seu ambiente local:
   ```bash
   git clone <URL-do-repositório>
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd <nome-do-diretório>
   ```
3. Execute o script `calcular_coeficiente_linear.py`:
   ```bash
   python calcular_coeficiente_linear.py
   ```

### Exemplo de Uso

O script solicita ao usuário os valores de **intensidade inicial** (`I0`), **intensidade final** (`I`) e a **espessura do material** (`x`), calculando e exibindo o coeficiente de atenuação.

```python
import math

def calcular_coeficiente_linear(I0, I, x):
    if I0 <= 0 or I <= 0 or x <= 0:
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

1. **Entrada de Dados**: O usuário deve fornecer os valores da intensidade inicial (`I0`), intensidade final (`I`) e espessura do material (`x`).
2. **Cálculo**: O algoritmo calcula o coeficiente linear de atenuação usando a fórmula apresentada.
3. **Saída**: O valor do coeficiente \( \mu \) é exibido na tela.

## Tratamento de Erros

O programa verifica se os valores fornecidos para `I0`, `I` e `x` são maiores que zero. Se não forem, uma mensagem de erro é exibida.

## Contribuições

Contribuições são bem-vindas! Caso você tenha sugestões de melhoria ou encontre problemas, sinta-se à vontade para abrir uma issue ou enviar um pull request.
