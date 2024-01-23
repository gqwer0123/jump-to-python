f = open('연습문제/chapter4/test06.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('연습문제/chapter4/test06.txt', 'w')
f.write(body)
f.close()