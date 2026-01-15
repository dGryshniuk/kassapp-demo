price = float(input("Введіть ціну товару: "))
vat = 0.2  # 20% ПДВ
final_price = price * (1 + vat)
print(f"Ціна з ПДВ: {final_price}")
