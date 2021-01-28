def person_print(name, last_name, *others, age):
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}'.format(name, last_name, age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)


person_print("Seweryn", "Żygas", "Kraków", age=21 )


def f(*args, **kwargs):
    for index, val in kwargs.items():
        print("%s == %s" % (index, val))

    print("args: ", args)
    print("kwargs: ", kwargs)


f("something", 250, 'third',  first=1,  second="two", color="red")
