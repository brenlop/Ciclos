'''
Realizar un programa para determinar cuánto ahorrará una persona en un año, 
si al final de cada mes deposita cantidades variables de dinero; 
además, se quiere saber cuánto lleva ahorrado cada mes.
'''
print("Medidor de ahorros")
total = 0
for i in range(1,13):
    ah = float(input(f"Coloca la cantidad del mes {i}: "))
    total = ah + total
    print(f"llevas {total} ahorrados")