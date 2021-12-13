from collections import deque

def main():
    arr0 = openFileRotated("./Day3/input.txt")
    #print(part1(arr0))

    arr1 = openFile("./Day3/input.txt")
    #arr1 = openFile("./Day3/input.txt")
    print(part2(arr1))

def part1(array):
    mostcommon = '' ## starts
    leastcommon = ''
    for bits in array: # for each bit... (11)
        print("Loop")
        zero = 0
        for bit in bits:
            if bit == 0:
                zero += 1
        if zero > len(bits)/2:
            print("more zeros")
            mostcommon += "0"
            leastcommon += "1"
        else:
            print("more 1s")
            mostcommon += "1"
            leastcommon += "0"
        print(mostcommon,leastcommon)
    print(mostcommon,leastcommon)
    return int(mostcommon,2)*int(leastcommon,2)

def part2(array):
    zero = 0
    # Start out here.
    arrOxy = array
    arrCO2 = array
    bit = 0
    print("oxy")
    while len(arrOxy) != 1 and bit < 12:
        zero = 0
        bitColumn = [i[bit] for i in arrOxy]
        for i in bitColumn:
            if i == 0: zero += 1
        if zero > len(bitColumn)/2: ## zero most common, remove non zero
            for i in range(len(arrOxy)):
                arrOxy = [value for value in arrOxy if value[bit] != 1]
        else: # one most common, remove non one
            for i in range(len(arrOxy)):
                arrOxy = [value for value in arrOxy if value[bit] != 0]
        bit += 1
    print(arrOxy)

    bit = 0
    print("co2")
    while len(arrCO2) != 1 and bit < 11:
        zero = 0
        bitColumn = [i[bit] for i in arrCO2]
        for i in bitColumn:
            if i == 0: zero += 1
        if zero > len(bitColumn)/2: ## zero most common, remove non zero
            for i in range(len(arrCO2)):
                arrCO2 = [value for value in arrCO2 if value[bit] != 0]
        else: # one most common, remove non one
            for i in range(len(arrCO2)):
                arrCO2 = [value for value in arrCO2 if value[bit] != 1]
        bit += 1
    print(arrCO2)
    o,c= int("".join([str(i) for i in arrOxy[0]]),2), int("".join([str(i) for i in arrCO2[0]]),2)
    print(o,c)
    return o*c
        





def openFileRotated(dir):
    with open(dir,'r') as data:
        lines = [x.strip() for x in data.readlines()] # get lines
        l2= list([list(map(int,x)) for x in list(zip(*lines[::-1]))]) ## rotate the array.. what the hell have i made.
        #print(l2)
        return l2


def openFile(dir):
    with open(dir,'r') as data:
        l= [list(map(int,list(x.strip()))) for x in data.readlines()] # get lines
        return l



if __name__ == "__main__":
    main()