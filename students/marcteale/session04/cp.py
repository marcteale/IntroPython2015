#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3
import sys

chunk = 4096

if len(sys.argv) == 3:
    try:
        open(sys.argv[1])
    except:
        print('{}: {}: No such file or directory'.format(sys.argv[0], sys.argv[1]))
        sys.exit(1)
    source = sys.argv[1]
    destination = sys.argv[2]
    i = open(source)
    data = i.read()
    o = open(destination, 'w+')
    o.write(data)
    o.close()
else:
    print("Usage: {} <source> <destination>".format(sys.argv[0]))
