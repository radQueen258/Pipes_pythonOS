#!/usr/bin/env python3
import sys
import random
import time

def main():
    
    if len(sys.argv) != 2:
        sys.exit(1)
    
    try:
        
        N = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    if not (120 <= N <= 180):
        sys.exit(1)

    
    operators = ['+', '-', '*', '/']
    for _ in range(N):
        X = random.randint(1, 9)
        O = random.choice(operators)
        Y = random.randint(1, 9)
        print(f"{X} {O} {Y}", flush=True)
        time.sleep(1)  # Sleep for 1 second

    sys.exit(0)

if __name__ == "__main__":
    main()
