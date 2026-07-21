#ITS100 Lecture7 While Loops Lab7.2
l = []
while True:
    n = input("Input: Enter a word:")
    if n =='exit':
        break
    else:
        l.append(n.capitalize())
print(f"output: {l}")