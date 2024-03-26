#!/usr/bin/env python3

"""
Simple script for generating mock data
"""

import sys, time
from random import randint, choices

if not len(sys.argv) == 2:
    sys.exit(f"Usage: python3 {sys.argv[0]} <amount>")

amount = int(sys.argv[1])

loremipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua.""".replace("\n", "\\\\n")

def randomstr() -> str:
    return "".join(
        choices("qwertyuiopasdfghjklzxcvbnm0123456789", k=5)
    )

def main() -> None:

    pre = "USE `infinitescroller`; INSERT INTO `feed` VALUES\n"

    for _ in range(amount-1):
        ts = time.time() + (randint(-1024, 1024))
        pre += f"('{randomstr()}', '404.jpg', {int(ts)}, '{loremipsum}'),\n"

    # trailing comma fix (pluhh)
    pre += f"('{randomstr()}', '404.jpg', {int(time.time())}, '{loremipsum}')"

    with open("mock.sql", "w+") as fd:
        fd.write(pre)

if __name__ == "__main__":
    main()