#!/usr/bin/env python3

from queue import Queue
from communication import Communication

def main():
    #Create queue
    queue = Queue()
    #Start the others threads and give it the queue

    #Start the Communication program
    Communication(queue)

if __name__ == "__main__":
    main()
