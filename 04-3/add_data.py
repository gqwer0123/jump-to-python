f = open('04-3/새파일.tex', 'a', encoding="UTF-8")
for i in range(11, 20):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()