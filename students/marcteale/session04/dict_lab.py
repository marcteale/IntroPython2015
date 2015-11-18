#!/usr/bin/python

# http://uwpce-pythoncert.github.io/IntroToPython/exercises/dict_lab.html#exercise-dict-lab
thing = { 'name': 'Chris',
        'city': 'Seattle',
        'cake': 'Chocolate' }

print(thing)

print(thing.get('cake'))
thing.pop('cake')
print(thing)
thing['fruit'] = 'Mango'
print(thing)
for key in thing: print(key)
for item in thing.values():
    print(item)

print(thing)
new_thing = dict()
for key,value in thing.iteritems():
    new_thing[key] = value.count('t')
print(new_thing)

s2 = set()
s3 = set()
s4 = set()
for i in range(1,20):
    if i % 2 == 0 :
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)

print(s2, s3, s4)

if not s3.issubset(s2):
    print('s3 is not a subset of s2.')
if s4.issubset(s2):
    print('s4 is a subset of s2.')

python_set=set('Python')
print(python_set)
marathon_set=frozenset('marathon')
print marathon_set

print python_set.union(marathon_set)
print python_set.intersection(marathon_set)
