
def main():
    arr = openFile("./Day2/input.txt")
    print(part1(arr))
    print(part2(arr))

def part1(array):
    x = 0
    y = 0
    z = 0
    for i in range(len(array)):
        match array[i][0]:
            case "forward":
                # do stuff in forward
                x += int(array[i][1])
            case "down":
                # do stuff in down
                z += int(array[i][1])
            case "up":
                #do stuff in up
                z -= int(array[i][1])
            case _:
                pass
    return x*z

def part2(array):
    x=0
    z=0
    aim = 0
    for i in range(len(array)):
        match array[i][0]:
            case "forward":
                # do stuff in forward
                x += int(array[i][1])
                z += aim * int(array[i][1])
            case "down":
                # do stuff in down
                aim += int(array[i][1])
            case "up":
                #do stuff in up
                aim -= int(array[i][1])
            case _:
                pass
    return x*z


def openFile(dir):
    with open(dir,'r') as data:
        return [x.strip().split(" ") for x in data.readlines()]

if __name__ == "__main__":
    main()
