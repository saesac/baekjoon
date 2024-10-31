for i in range(3, 0, -1):
    s = input()
    if s not in ['Fizz', 'Buzz', 'FizzBuzz']:
        last = int(s) + i

if last%15==0:
    print('FizzBuzz')
elif last%3==0:
    print('Fizz')
elif last%5==0:
    print('Buzz')
else:
    print(last)