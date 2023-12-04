import os

def word(words):
    cuvinte =[]
    for word in words:
        cuvinte.apend(word)
    cuvinte.sort()
    print(cuvinte[0])
    print(cuvinte[-1])
    for word in cuvinte:





def main():
    FileObject = open(C:\Users\Andrada\Documents\GitHub\Python\test, mode='r'
                      , buffering=-1, encoding=None,
                      errors=None, newline=None, closefd=True, opener=None)
    try:
        f = open("file.txt")
        for line in f:
           word(line.strip())
        f.close()
    except:
        print("Unable to open file file.txt")

main()
