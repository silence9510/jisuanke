#整数转罗马数字
def numToRomanNum(Num):

        NumDic = {
            '1': ('I', 'IV', 'V', 'IX'),
            '2': ('X', 'XL', 'L', 'XC'),
            '3': ('C', 'CD', 'D', 'CM'),
            '4': ('M')
        }
        items = sorted(NumDic.items())
        retstr = ''
        for item in items:  # 语句间的缩进很重要，思路清晰与否全都体现在代码上。
            str = ''
            (Num, modNum) = divmod(Num, 10)
            if modNum != 0:
                if item[0] != '4':
                    if modNum <= 3:
                        while modNum > 0:
                            str = str.join(['', item[1][0]])
                            modNum -= 1
                    elif modNum < 5:
                        str = item[1][1]
                    elif modNum == 5:
                        str = item[1][2]
                    elif modNum < 9:
                        str = item[1][2]
                        while modNum > 5:
                            str = str.join(['', item[1][0]])
                            modNum -= 1
                    else:
                        str = item[1][3]
                else:
                    while modNum > 0:
                        str = str.join(['', item[1][0]])
                        modNum -= 1
                retstr = str.join(['', retstr])
        return retstr

print(numToRomanNum(int(input())))