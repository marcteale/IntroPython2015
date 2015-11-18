

def foo(fore='black', back='blue', link='red', visited='purple'):
    return "\nfore = {}\nback = {}\nlink = {}\nvisited = {}".format(fore, back, link, visited)


def foo2(fore='black', back='blue', link='red', visited='purple', **kwargs):
    return "\nfoo2\nfore = {}\nback = {}\nlink = {}\nvisited = {}".format(fore, back, link, visited)

print(foo())

kwargs = {"back": "pink", "link": "puce", "visited": "mauve"}
print(foo(**kwargs))
print(foo2(**kwargs))

args = ('orange', 'smuh', 'grue')
print(foo(*args))

print(foo('white', *args))
