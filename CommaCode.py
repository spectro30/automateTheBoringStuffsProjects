def go():
    fruits = []
    n = int(input("lenth of list "))
    for i in range(n):
        x = input()
        fruits.append(x)
    if n == 1:
        print (fruits[i])
        return
    for i in range(n):
        if i == n-1 :
            print('and',end = " ")
        print(fruits[i],end = " ")
        if i != n-1 :
            print(',',end = " ")

go()
