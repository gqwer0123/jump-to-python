f = open('04-3/새파일.tex', 'r', encoding="UTF-8")
lines = f.readlines()
for line in lines:
    print(line)
f.close()