inputNumber = int(input("正の整数を入れてね: "))

if inputNumber % 3 == 0:
    output = "Fizz"
else:
    output = str(inputNumber)

print(output)
