class FizzBuzz:
    def __init__(self, number):
        self.number = number

    def check_if_FizzBuzz(self):
        if self.number % 3 == 0 and self.number % 5 == 0:
            return 'FizzBuzz'
        elif self.number % 3 == 0:
            return 'Fizz'
        elif self.number % 5 == 0:
            return 'Buzz'
        else:
            return str(self.number)


def main():
    number = 101
    for i in range(1, number):
        fb = FizzBuzz(i)
        print(fb.check_if_FizzBuzz())


if __name__ == '__main__':
    main()