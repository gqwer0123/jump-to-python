f1 = open('연습문제/chapter4/test05.txt', 'w')
f1.write('Life is too short')
f1.close()

f2 = open('연습문제/chapter4/test05.txt', 'r')
print(f2.read())
f2.close()