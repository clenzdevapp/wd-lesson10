import random
def lottery_generator(num):
    lottery_numbers = random.sample(xrange(100),num)
    return lottery_numbers

def main():
    print("> Program: Welcome to the Lottery numbers generator.")
    print("> Program: Please enter how many random numbers would you like to have: ")
    print("User: ")
    number = raw_input()
    print("> Program: " + str(lottery_generator(int(number))))
    print("> Program: END")

if __name__ == '__main__':
    main()