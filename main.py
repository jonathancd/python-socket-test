#!/usr/bin/env python

import time
from src.App import App
from src.helpers.constants import URI_SOCKET

def main():
    app = App(URI_SOCKET)
    app.run()
    
if __name__ == "__main__":
    main()