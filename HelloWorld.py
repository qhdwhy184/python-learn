import sys

def huihui():
        if len(sys.argv) >=2:
                name = sys.argv[1]
        else:
                name = 'World'
        print 'Hello', name, sys.argv[0]

huihui()