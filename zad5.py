import random

names = ['Damian', 'Ola', 'Barbara', 'Robert', 'Zygmunt', 'Ewa']
first = [x[0] for x in names]
print(first)

list_rand = []
for x in range(5):
    sub_list = []
    for i in range(4):
        sub_list += [random.randint(1, 10)]

    list_rand.append(sub_list)

print(list_rand)
