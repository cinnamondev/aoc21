def main():
    arr = openFile('./Day1/input.txt')
    print(part1(arr))
    print(part2(arr))

def openFile(dir):
    with open(dir,'r') as data:
        return [int(x) for x in data.readlines()]

def part1(array):
    count = 0
    for i in range(len(array)-1):
        if array[i+1] > array[i]:
            count += 1
    return count

def part2(array):
    count = 0
    for i in range(len(array)-3):
        j = i+1
        a = array[i] +  array[i+1] +  array[i+2]
        b = array[j] +  array[j+1] +  array[j+2]
        if b>a:
            count +=1
    return count


if __name__ == "__main__":
    main()