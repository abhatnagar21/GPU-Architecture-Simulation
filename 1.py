import random
import time
from multiprocessing import Pool, cpu_count

# Simulated GPU Task
def gpu_task(task_id):
    # Simulate task execution time (in milliseconds)
    execution_time = random.randint(10, 100)  # Simulating execution time
    time.sleep(execution_time / 1000)  # Convert ms to seconds
    print(f"Task {task_id} completed in {execution_time} ms")
    return execution_time

# GPU Simulation Class
class GPUSimulator:
    def __init__(self, num_cores):
        self.num_cores = num_cores  # Number of GPU cores
        self.task_queue = []  # Task queue
        self.task_results = []  # To store the execution times

    def add_task(self, num_tasks):
        """Add tasks to the task queue."""
        for i in range(num_tasks):
            self.task_queue.append(i)
        print(f"{num_tasks} tasks added to the queue.")

    def execute_tasks(self):
        """Execute tasks using GPU cores in parallel."""
        with Pool(self.num_cores) as pool:
            start_time = time.time()
            self.task_results = pool.map(gpu_task, self.task_queue)
            end_time = time.time()

        total_time = (end_time - start_time) * 1000  # Convert seconds to milliseconds
        avg_time = sum(self.task_results) / len(self.task_results)
        
        print(f"\n--- Simulation Complete ---")
        print(f"Total execution time: {total_time:.2f} ms")
        print(f"Average task execution time: {avg_time:.2f} ms")

# Main Execution
if __name__ == "__main__":
    num_cores = min(cpu_count(), 8)  # Limit to 8 cores max for this simulation
    print(f"Simulating GPU with {num_cores} cores...\n")

    # Initialize the GPU simulator with num_cores
    gpu_sim = GPUSimulator(num_cores)

    # Add 20 tasks to the task queue
    gpu_sim.add_task(20)

    # Execute tasks on the simulated GPU
    gpu_sim.execute_tasks()
