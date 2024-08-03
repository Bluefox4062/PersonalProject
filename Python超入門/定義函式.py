#def washingmachine(mode):
#    print("注水")

#    if mode == 'soft':
#        print('輕柔清洗')
#    elif mode == 'hard':
#        print('強力清洗')
#    else:
#        print('一般清洗')
        
#    print("清掉洗衣劑")
#    print("脫水")
#    print("烘乾")

#if __name__ == "__main__":
#    washingmachine('hard')

def area(radius):
    result = radius * radius * 3.14
    return result

if __name__ == "__main__":
    small = 5
    big = 10

    print(area(small))
    print(area(big))