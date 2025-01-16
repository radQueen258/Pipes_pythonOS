#!/usr/bin/env python3
import os
import signal
import sys
import random


processed_count = 0

def sigusr1_handler(signum, frame):
    """Handle SIGUSR1 and print the number of processed expressions."""
    print(f"Processed {processed_count} lines", file=sys.stderr)

def main():
    global processed_count
    signal.signal(signal.SIGUSR1, sigusr1_handler)

    
    pipe_a_r, pipe_a_w = os.pipe()  
    pipe_b_r, pipe_b_w = os.pipe()  
    pipe_c_r, pipe_c_w = os.pipe()  

    
    pid1 = os.fork()
    if pid1 == 0:
        
        os.dup2(pipe_a_w, sys.stdout.fileno())  
        os.close(pipe_a_r) 
        os.close(pipe_b_r)
        os.close(pipe_b_w)
        os.close(pipe_c_r)
        os.close(pipe_c_w)
        
        random_n = random.randint(120, 180)
        os.execvp('./generator', ['./generator', str(random_n)])
    
    
    pid2 = os.fork()
    if pid2 == 0:
        
        os.dup2(pipe_b_r, sys.stdin.fileno())  
        os.dup2(pipe_c_w, sys.stdout.fileno())  
        os.close(pipe_a_r)
        os.close(pipe_a_w)
        os.close(pipe_b_w)
        os.close(pipe_c_r)
        
        os.execvp('/usr/bin/bc', ['/usr/bin/bc'])

    
    os.close(pipe_a_w)  
    os.close(pipe_b_r)
    os.close(pipe_c_w)

    try:
        while True:
            
            expression = os.read(pipe_a_r, 1024).decode().strip()
            if not expression:  
                break
            
            os.write(pipe_b_w, (expression + '\n').encode())
            
            result = os.read(pipe_c_r, 1024).decode().strip()
            
            print(f"{expression} = {result}", flush=True)
            processed_count += 1
    except KeyboardInterrupt:
        pass
    finally:
       
        os.close(pipe_a_r)
        os.close(pipe_b_w)
        os.close(pipe_c_r)
        os.waitpid(pid1, 0)  
        os.waitpid(pid2, 0)  

if __name__ == "__main__":
    main()
