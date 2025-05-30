print("----------------------------------------")
digi1 = float(input("Give your first number : "))
digi2 = float(input("Give your second number : "))
operator = input("Give your operator : '+','-','*','/' :: ")

if operator == "+":
    print(round(digi1 + digi2,3))
elif operator == "-":
    print(round(digi1 - digi2,3))
elif operator == "*":
    print(round(digi1 * digi2,3))
elif operator == "/":
    print(round(digi1 / digi2,3))
else:
    print("Your given operator does not exists!!!!")


