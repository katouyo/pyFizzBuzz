# number = int(input("正の整数を入れてね: "))

def convertFizzBuzz(number):
    if number % 15 == 0:
        return "FizzBuzz"

    if number % 3 == 0:
        return "Fizz"

    if number % 5 == 0:
        return "Buzz"

    return str(number)


for number in range(1, 101):
    result = convertFizzBuzz(number)
    print(result)
