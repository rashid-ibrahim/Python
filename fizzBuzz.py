
def fizzBuzz(n):
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(str(i))
        print("\n")

def main():
    num = input('Enter a number to run FizzBuzz until: ')
    fizzBuzz(num)
    return 0


'''
I wanted to make this where the program could take a user input in the main function
but I also did not want to have to enter the number each time I ran the program.
'''
if __name__ == '__main__':
    fizzBuzz(20)
