import json
import random
import time
from src.App import App
from src.Block import Block
from src.helpers.constants import BLOCKS_QTY

class TestApp():

    def test_initialize_blocks_in_constuctor(self):
        app = App('')
        assert isinstance(app.blocks, list)
        assert len(app.blocks) == BLOCKS_QTY

    def test_create_blocks_list(self):
        app = App('')
        blocks = app.create_blocks_list()
        assert isinstance(blocks, list)
        assert len(blocks) == BLOCKS_QTY

    def test_reset_blocks(self):
        app = App('')

        for index in range(1, (BLOCKS_QTY + 1)):
            block = app.get_block_by_index(index)

            for _ in range(10):
                rand_number = random.randint(1, pow(2 , 32))
                block.process_number(rand_number)

        for block in app.blocks:
            block.reset()
            assert block.max_number == None
            assert block.min_number == None
            assert block.first_number == None
            assert block.last_number == None
            assert block.number_of_prime_numbers == 0
            assert block.number_of_even_numbers == 0
            assert block.number_of_odd_numbers == 0

    def test_get_block_by_index(self):
        app = App('')
        index = random.randint(1, 100)
        block = app.get_block_by_index(index)
        assert isinstance(block, Block)

        index = random.randint(1, 100)
        block = app.get_block_by_index(index)
        assert isinstance(block, Block)

        index = random.randint(1, 100)
        block = app.get_block_by_index(index)
        assert isinstance(block, Block)

    def test_get_non_existent_block_by_index(self):
        app = App('')
        index = random.randint(101, 1000)
        block = app.get_block_by_index(index)
        assert block == None

    def test_handle_socket_response(self):
        app = App('')
        index = random.randint(1, 100)
        json_data = {}
        json_data['a'] = index
        json_data['b'] = 7
        app.handle_socket_response(json.dumps(json_data))
        json_data = {}
        json_data['a'] = index
        json_data['b'] = 100
        app.handle_socket_response(json.dumps(json_data))

        block = app.get_block_by_index(index)
        assert block.max_number == 100
        assert block.min_number == 7
        assert block.first_number == 7
        assert block.last_number == 100
        assert block.number_of_prime_numbers == 1
        assert block.number_of_even_numbers == 1
        assert block.number_of_odd_numbers == 1

    def test_get_elapsed_seconds(self):
        app = App('')
        app.control_time = time.time()
        time.sleep(10)
        elapsed_time = app.get_elapsed_seconds()
        assert round(elapsed_time, 0) == 10