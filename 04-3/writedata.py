f = open('04-3/새파일.tex', 'w', encoding="UTF-8")
for i in range(1, 11):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()