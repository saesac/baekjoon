while True:
    try:
        s = input()
        if s == '#':
            break
        print(sum([1 for i in s if i.lower() in 'aeiou']))
    except EOFError:
        break