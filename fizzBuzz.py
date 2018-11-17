# number = int(input("正の整数を入れてね: "))

def convertFizzBuzz(number):
    if number % 15 == 0:
        return "FizzBuzz"

    elif number % 3 == 0:
        return "Fizz"

    elif number % 5 == 0:
        return "Buzz"

    else:
        return str(number)


print(convertFizzBuzz(1))
print(convertFizzBuzz(2))
print(convertFizzBuzz(3))
print(convertFizzBuzz(4))
print(convertFizzBuzz(5))
print(convertFizzBuzz(6))
print(convertFizzBuzz(7))
print(convertFizzBuzz(8))
print(convertFizzBuzz(9))
print(convertFizzBuzz(10))
print(convertFizzBuzz(11))
print(convertFizzBuzz(12))
print(convertFizzBuzz(13))
print(convertFizzBuzz(14))
print(convertFizzBuzz(15))
print(convertFizzBuzz(16))
