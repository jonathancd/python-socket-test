import asyncio
import json
import sys
import threading
import time
import websockets
from src.Block import Block
from src.helpers.constants import BLOCKS_QTY, SECONDS_TO_RESET

class App():
    def __init__(self, uri_socket):
        self.blocks = self.create_blocks_list()
        self._control_time = None
        self._is_running = True
        self._uri_socket = uri_socket
        self._websocket_conn = None

    @property
    def control_time(self):
        return self._control_time

    @property
    def is_running(self):
        return self._is_running

    @property
    def uri_socket(self):
        return self._uri_socket

    @property
    def websocket_conn(self):
        return self._websocket_conn

    @control_time.setter
    def control_time(self, control_time):
        self._control_time = control_time

    @is_running.setter
    def is_running(self, is_running):
        self._is_running = is_running

    @websocket_conn.setter
    def websocket_conn(self, websocket_conn):
        self._websocket_conn = websocket_conn

    def check_time_elapsed(self):
        while True:
            if self.has_minute_passed():
                self.print_resumes()
                self.reset_blocks()
                self.control_time = time.time()
            
            if self.is_running == False:
                break

    async def connect_socket(self):
        try:
            async with websockets.connect(self.uri_socket, ping_interval = None) as websocket:
                self.websocket_conn = websocket
                self.control_time = time.time()
                thread_control = threading.Thread(target=self.check_time_elapsed)
                thread_control.daemon = True
                thread_control.start()
                    
                while True:
                    response = await self.websocket_conn.recv()
                    thread_process = threading.Thread(target=self.handle_socket_response, args=(response,))
                    thread_process.daemon = True
                    thread_process.start()

                    if self.is_running == False:
                        break
        except (KeyboardInterrupt, SystemExit):
            self.is_running = False
            cleanup_stop_thread()
            sys.exit()
        finally:
            await self.websocket_conn.close()
            pass
    
    def create_blocks_list(self):
        blocks = []
        for _ in range(BLOCKS_QTY):
            blocks.append(Block())
        return blocks

    def get_block_by_index(self, index):
        try:
            return self.blocks[index - 1]
        except IndexError:
            return None

    def get_elapsed_seconds(self):
        current_time = time.time()
        seconds = current_time - self.control_time
        return seconds
    
    def handle_socket_response(self, response):
        data = json.loads(response)
        index = data.get('a')
        number = data.get('b')
        block = self.get_block_by_index(index)

        if block is not None:
            block.process_number(number)

    def has_minute_passed(self):
        elapsed_seconds = self.get_elapsed_seconds()
        return round(elapsed_seconds, 0) == SECONDS_TO_RESET

    def print_resumes(self):
        for index, block in enumerate(self.blocks):
            print('Block: {}'.format((index + 1)))
            block.print_resume()

    def reset_blocks(self):
        for block in self.blocks:
            block.reset()

    def run(self):
        try:
            asyncio.run(self.connect_socket())
        except asyncio.CancelledError:
            self.is_running = False