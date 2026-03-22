if __name__=="__main__":
    integer = [0, 1, 2, 3, 4]
    binary = ["0", "1", "10", "11", "100"]
    z=zip(integer, binary)
    for zi in z:
        print(zi)
    binary_dict = {int:bin for int,bin in zip(integer, binary)}
    print(binary_dict)

    integer = [1, -1, 2, 3, 5, 0, -7]
    add_i = [0-i for i in integer ]
    print(add_i)
