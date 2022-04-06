import random
from src.Block import Block

class TestBlock:
    
    def test_is_even_number(self):
        block = Block()
        number = 10
        assert block.is_even_number(number) == True

    def test_is_not_even_number(self):
        block = Block()
        number = 3
        assert block.is_even_number(number) == False

    def test_is_the_greatest_number(self):
        block = Block()
        rand_number = random.randint(1, pow(2 , 32))
        assert block.is_the_greatest_number(rand_number) == True

    def test_is_the_greatest_number_not_initialized(self):
        block = Block()
        block.max_number = 5
        number = 10
        assert block.is_the_greatest_number(number) == True

    def test_is_not_the_greatest_number(self):
        block = Block()
        block.max_number = 10
        number = 5
        assert block.is_the_greatest_number(number) == False

    def test_is_the_lesser_number(self):
        block = Block()
        rand_number = random.randint(1, pow(2 , 32))
        assert block.is_the_lesser_number(rand_number) == True

    def test_is_the_lesser_number_not_initialized(self):
        block = Block()
        block.min_number = 5
        number = 3
        assert block.is_the_lesser_number(number) == True

    def test_is_not_the_lesser_number(self):
        block = Block()
        block.min_number = 5
        number = 10
        assert block.is_the_lesser_number(number) == False

    def test_is_the_first_number(self):
        block = Block()
        assert block.is_the_first_number() == True

    def test_is_not_the_first_number(self):
        block = Block()
        block.first_number = random.randint(1, pow(2 , 32))
        assert block.is_the_first_number() == False

    def test_process_number(self):
        block = Block()
        block.process_number(10)
        assert block.max_number == 10
        assert block.min_number == 10
        assert block.first_number == 10
        assert block.last_number == 10
        assert block.number_of_prime_numbers == 0
        assert block.number_of_even_numbers == 1
        assert block.number_of_odd_numbers == 0

        block.process_number(50)
        assert block.max_number == 50
        assert block.min_number == 10
        assert block.first_number == 10
        assert block.last_number == 50
        assert block.number_of_prime_numbers == 0
        assert block.number_of_even_numbers == 2
        assert block.number_of_odd_numbers == 0

        block.process_number(7)
        block.process_number(5)
        block.process_number(23)
        assert block.max_number == 50
        assert block.min_number == 5
        assert block.first_number == 10
        assert block.last_number == 23
        assert block.number_of_prime_numbers == 3
        assert block.number_of_even_numbers == 2
        assert block.number_of_odd_numbers == 3

        block.process_number(100)
        assert block.max_number == 100
        assert block.min_number == 5
        assert block.first_number == 10
        assert block.last_number == 100
        assert block.number_of_prime_numbers == 3
        assert block.number_of_even_numbers == 3
        assert block.number_of_odd_numbers == 3

    def test_reset(self):
        block = Block()
        rand_number = random.randint(1, pow(2 , 32))
        block.process_number(rand_number)
        assert isinstance(block.max_number, int)
        assert isinstance(block.min_number, int)
        assert isinstance(block.first_number, int)
        assert isinstance(block.last_number, int)
        assert isinstance(block.number_of_prime_numbers, int)
        assert isinstance(block.number_of_even_numbers, int)
        assert isinstance(block.number_of_odd_numbers, int)

        block.reset()
        assert block.max_number == None
        assert block.min_number == None
        assert block.first_number == None
        assert block.last_number == None
        assert block.number_of_prime_numbers == 0
        assert block.number_of_even_numbers == 0
        assert block.number_of_odd_numbers == 0