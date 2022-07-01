import sys
with open("C://Users//User//Desktop//FinalTestRecord.txt") as f:
    for line in f:
        if not line.isspace():
            sys.stdout.write(line)
            f = open("C://Users//User//Desktop//Final.txt", "a")
            f.write(line)
            f.close()