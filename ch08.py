number_set = set(range(1, 30))
print(number_set)
processed_set = [ 'FizzBuzz' if n % 15 == 0 else 'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n for n in number_set ]
print(processed_set)
