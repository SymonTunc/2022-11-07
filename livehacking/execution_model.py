def squares(numbers):
    retnums = []
    for n in numbers:
        retnums.append(n**2)
    return retnums

if __name__ == '__main__':
    sqs = squares([0,1,2,3,4,5,6])
    print(sqs)
