## Conversor de Temperatura

# Celsius para Fahrenheint

valor_celsius = input('Informe a temperatura em Celsius: ' )

valor_celsius = float(valor_celsius)

fahrenheint_convertido = (9/5) * valor_celsius + 32

print('Temperatura em graus Fahrenheint:', fahrenheint_convertido)

# Fahrenheint para Celsius

valor_fahrenheit = input('Informe a temperatura em Celsius: ' )

valor_fahrenheit = float(valor_fahrenheit)

celsius_convertido = (valor_fahrenheit - 32) * 5 / 9
print('Temperatura em graus Celsisus:', celsius_convertido)