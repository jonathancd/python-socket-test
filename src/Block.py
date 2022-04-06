import sympy

class Block():
    def __init__(self):
        self._max_number = None
        self._min_number = None
        self._first_number = None
        self._last_number = None
        self._number_of_prime_numbers = 0
        self._number_of_even_numbers = 0
        self._number_of_odd_numbers = 0

    @property
    def max_number(self):
        return self._max_number

    @property
    def min_number(self):
        return self._min_number

    @property
    def first_number(self):
        return self._first_number

    @property
    def last_number(self):
        return self._last_number

    @property
    def number_of_prime_numbers(self):
        return self._number_of_prime_numbers

    @property
    def number_of_even_numbers(self):
        return self._number_of_even_numbers

    @property
    def number_of_odd_numbers(self):
        return self._number_of_odd_numbers

    @max_number.setter
    def max_number(self , max_number):
        self._max_number = max_number
    
    @min_number.setter
    def min_number(self , min_number):
        self._min_number = min_number

    @first_number.setter
    def first_number(self , first_number):
        self._first_number = first_number

    @last_number.setter
    def last_number(self , last_number):
        self._last_number = last_number

    @number_of_prime_numbers.setter
    def number_of_prime_numbers(self, number_of_prime_numbers):
        self._number_of_prime_numbers = number_of_prime_numbers

    @number_of_even_numbers.setter
    def number_of_even_numbers(self, number_of_even_numbers):
        self._number_of_even_numbers = number_of_even_numbers

    @number_of_odd_numbers.setter
    def number_of_odd_numbers(self, number_of_odd_numbers):
        self._number_of_odd_numbers = number_of_odd_numbers

    def is_even_number(self, number):
        return (number % 2) == 0

    def is_the_first_number(self):
        return self.first_number is None

    def is_the_greatest_number(self, number):
        return self.max_number is None or number > self.max_number

    def is_the_lesser_number(self, number):
        return self.min_number is None or number < self.min_number

    def print_resume(self):
        print('Max number: {}'.format(self.max_number))
        print('Min number: {}'.format(self.min_number))
        print('First number: {}'.format(self.first_number))
        print('Last number: {}'.format(self.last_number))
        print('Qty prime numbers: {}'.format(self.number_of_prime_numbers))
        print('Qty even numbers: {}'.format(self.number_of_even_numbers))
        print('Qty odd number: {}\n'.format(self.number_of_odd_numbers))

    def process_number(self, number):
        self.last_number = number

        if self.is_the_first_number():
            self.first_number = number

        if self.is_the_greatest_number(number):
            self.max_number = number

        if self.is_the_lesser_number(number):
            self.min_number = number

        if sympy.isprime(number):
            self.number_of_prime_numbers += 1

        if self.is_even_number(number):
            self.number_of_even_numbers += 1
        else:
            self.number_of_odd_numbers += 1

    def reset(self):
        self.first_number = None
        self.last_number = None
        self.max_number = None
        self.min_number = None
        self.number_of_prime_numbers = 0
        self.number_of_even_numbers = 0
        self.number_of_odd_numbers = 0