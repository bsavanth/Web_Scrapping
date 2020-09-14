
import ply.lex as lex
import os
import StringIO
import shutil
import sys
import time
#import matplotlib.pyplot as plt

tokens = [
    "tag",
    "other",
    "regularstream",
    "time",
    "digit"
]

def t_tag(t):
    r"\<[!\/]?([A-Za-z]|-)+[^>]*\>"
    pass

def t_time(t):
    r"[0-9]{2}:[0-9]{2}:[0-9]{2}"
    pass


def t_digit(t):
    r"[0-9]+"
    string =t.value
    stream.write(string)
    stream.write("\n")


def t_regularstream(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    string =t.value
    stream.write(string.lower())
    stream.write("\n")

def t_other(t):
    r"\n|."
    pass

def t_error(t):
    pass


inputDir = sys.argv[1]
outputDir = sys.argv[2]

try:
    os.makedirs(outputDir)
except IOError:
    print("Cannot create input directory, remove output directory and try again")


hold=[]
start=time.time()
for filename in os.listdir(inputDir):

    try:
        f=open(inputDir+"/"+filename)
        stream = StringIO.StringIO()
        lex.lex()
        lex.input(f.read())
        while 1:
            t = lex.token()
            if not t: break
        with open(outputDir+'/'+filename+'.txt', 'w') as writer:
                stream.seek (0)
                shutil.copyfileobj (stream, writer)
    except IOError:
         print("Cannot read input file " + filename)

    finally:
        stream.close()
        t=time.time()-start
        hold.append(t)

print
print("Parsing successful")
print
t=50
print 'No.of files' , '\t\tTime in seconds'
print
while t < len(hold):
    print '  ',t,'\t\t\t',hold[t]
    t+=50

print
print
#plt.plot(hold)
#plt.xlabel('No.of Documents')
#plt.ylabel('Time in seconds')
#plt.show()



