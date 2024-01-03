number_decimal = int(input('Entre com um número inteiro: '))

number_binary = ''

while number_decimal > 0:
    res = number_decimal % 2
    number_decimal //= 2
    number_binary = str(res) + number_binary

print(f'{number_binary}')
