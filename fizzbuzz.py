<? python

fizzbuzz = 1

while fizzbuzz <= 100:
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print('FizzBuzz')
        fizzbuzz += 1
    elif fizzbuzz % 3 == 0:
        print('Fizz')
        fizzbuzz += 1
    elif fizzbuzz % 5 == 0:
        print('Buzz')
        fizzbuzz += 1
    else:
        print(fizzbuzz)
        fizzbuzz += 1
