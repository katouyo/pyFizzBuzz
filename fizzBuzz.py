inputNumber = int(input("正の整数を入れてね: "))

if inputNumber % 3 == 0:
    output = "Fizz"

elif inputNumber % 5 == 0:
    output = "Buzz"

else:
    output = str(inputNumber)

print(output)
