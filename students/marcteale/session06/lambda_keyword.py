

def function_builder(num):
    l = list()
    for i in range(num):
        l.append(lambda x, e=i: x+e)
    return l


the_list = function_builder(4)

print(the_list[0](2))
