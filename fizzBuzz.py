inputNumber = int(input("正の整数を入れてね: "))

if inputNumber % 15 == 0:
    output = "FizzBuzz"

elif inputNumber % 3 == 0:
    output = "Fizz"

elif inputNumber % 5 == 0:
    output = "Buzz"

elif inputNumber % 7 == 0:
    output = "aaaa"

else:
    output = str(inputNumber)

print(output)
