price = float(input("Введіть ціну товару: "))
discount = float(input("Введіть знижку у %: ")) / 100
final_price = price * (1 - discount)
print(f"Ціна зі знижкою: {final_price}")
