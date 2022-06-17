import os
global prev_line
prev_line = ""
while True:

    with open("C://Users//User//Desktop//TestRecord.txt", "rb") as file:
        try:
            file.seek(-2, os.SEEK_END)
            while file.read(1) != b'\n':
                file.seek(-2, os.SEEK_CUR)
        except OSError:
            file.seek(0)
        last_line = file.readline().decode()
        if prev_line != last_line:
            print(last_line)
        prev_line = last_line
