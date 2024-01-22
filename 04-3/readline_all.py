f = open('04-3/새파일.tex', 'r', encoding="UTF-8")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()