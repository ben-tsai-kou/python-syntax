weight=input("please type your weight: ")
unit=input("(L)bs or (K)g: ")

if unit.lower() == "l":
    converted = float(weight) * 0.453
    print(f'You are {converted} kg.')
else:
    converted = float(weight) / 0.453
    print(f'You are {converted} lbs.')