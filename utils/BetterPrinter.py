#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

import sys
import time


def viewCount(iteration: int, message: str, multiplier: int = 20):
    n = message[:(int(iteration) % len(message) + 1)]
    print(f"{n} ", end='\r')
    sys.stdout.flush()


def multipleMessage(messages: list[str]):
    for message in messages:
        i = 0
        for _ in range(len(message)):
            i += 1
            print(message[:i], end="\r")
            time.sleep(0.1)
            sys.stdout.flush()
        time.sleep(3)
        for _ in range(i):
            i -= 1
            print(message[:i], end="\r")
            time.sleep(0.1)
            sys.stdout.flush()
