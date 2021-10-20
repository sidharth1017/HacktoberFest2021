def stars(quabtity):
    for i in range(0, int(quabtity)+1):
        print("*" * i)

if __name__ == '__main__':
    try:
        stars((input("Enter a number of stars ")))
    except:
        printf("Invalid input")
