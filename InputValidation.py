def collatz(number):
    if number % 2 == 0:
        res = number // 2
        print(res)
        return res
        
    else :
        res = 3 * number + 1
        print(res)
        return res
while True:
    try :
        x = int(input())
        if collatz(x) == 1:
            break
    except ValueError:
        print('Input must be an integer')
   
