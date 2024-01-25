def average(numbers: []) -> float:
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)

def greatest(numbers: []) -> int:
    big = 0
    for number in numbers:
        if number > big:
            big = number
    return big


if __name__ == '__main__':
    print('valeria')
    numbers = [1, 2, 3, 4, 5]
    print(average(numbers))
    print(greatest(numbers))

    numbers2 = [4, 4, 4, 4]
    print(average(number2))
