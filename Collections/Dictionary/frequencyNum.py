from myLib.easyInput import eval_list

def frequency_of_num():
    numbers = eval_list("Enter values for list : ")
    d = {}
    for number in numbers:
        if number in d:
            d[number] += 1
        else:
            d[number] = 1
    return d

if __name__ == '__main__':
    print(frequency_of_num())