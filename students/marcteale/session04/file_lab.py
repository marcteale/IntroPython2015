#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

import io

langs = dict()
for line in open('../../../Examples/students.txt'):
    if line == 'name: languages\n':
        continue
    else:
        line=line.rstrip()
        student,languages=line.split(':',2)
        languages = languages.lower();
        languages = languages.replace(',','')
        languages = languages.replace('and','')
        print("student: {}\nlangs: {}\n\n".format(student,languages))
        for language in languages.split():
            if language in langs:
                langs[language] += 1
            else:
                langs[language] = 1
print(langs)
