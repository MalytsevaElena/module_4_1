def divide(first, second):
    if second != 0:
        res = first / second
#        print(res)
        return res

    else:
        res = 'Ошибка'
#        print(res)
        return res


if __name__ == '__main__':
   result1 = divide(69, 3)
   result2 = divide(3, 0)
   result3 = divide(49, 7)
   result4 = divide(15, 0)
