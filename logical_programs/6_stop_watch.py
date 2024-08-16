'''

@Author:Vijay Kumar M N
@Date: 2024-07-31
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-07-31
@Title : python program to calculate the elapsed time.
'''

import time

class Stopwatch:
   

    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        
        self.start_time = time.time()
        print("Stop watch started.")

    def stop(self):
        
        if self.start_time is None:
            print("Stop watch has not been started.")
            return
        self.end_time = time.time()
        print("Stop watch stopped.")

    def elapsed_time(self):
        """
        Description:
        Calculate and return the elapsed time between start and stop.
        
        Returns:
        float: The elapsed time in seconds.
        """
        if self.start_time is None:
            print("Stopwatch has not been started.")
            return None
        if self.end_time is None:
            print("Stopwatch has not been stopped.")
            return None
        elapsed = self.end_time - self.start_time
        return elapsed

def main():
   
    stopwatch = Stopwatch()
    
    input("Press Enter to start the stopwatch...")
    stopwatch.start()
    
    input("Press Enter to stop the stopwatch...")
    stopwatch.stop()
    
    elapsed = stopwatch.elapsed_time()
    if elapsed is not None:
        print(f"Elapsed time: {elapsed:.2f} seconds")

if __name__ == "__main__":
    main()
