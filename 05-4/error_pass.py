try:
    f = open('없는파일', 'r')
except FileNotFoundError:
    pass