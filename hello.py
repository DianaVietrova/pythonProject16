import time
import unittest

def measure_time(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

def example_function():

    time.sleep(2)

class TestMeasureTime(unittest.TestCase):
    def test_measure_time(self):
        elapsed_time = measure_time(example_function)
        self.assertGreaterEqual(elapsed_time, 2)

if __name__ == "__main__":
    unittest.main()