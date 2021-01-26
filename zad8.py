with open('textzad8.txt', 'w+') as f:
    f.write('Some text in here')
    f.seek(0)
    print(f.read())
