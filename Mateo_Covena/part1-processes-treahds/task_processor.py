import multiprocessing 
import threading 
import time 
import random 
 
class TaskProcessor: 
    def __init__(self): 
        self.tasks_completed = multiprocessing.Value('i', 0) 
     
    def process_task(self, task_id, difficulty): 
        """Simula procesamiento de 4 tareas con diferente dificultad"""
        start = time.time()

        total = 0
        work_units = difficulty * 2_000_000
        for i in range(work_units):
            total += (i % 97) * (i % 13)

        elapsed = time.time() - start
        with self.tasks_completed.get_lock():
            self.tasks_completed.value += 1

        print(
            f"Tarea {task_id} dificultad {difficulty} completada en {elapsed:.3f}s "
            f"  checksum={total % 1000}"
        )
     
    def run_with_threads(self, tasks): 
        """Ejecutar tareas usando hilos"""
        with self.tasks_completed.get_lock():
            self.tasks_completed.value = 0

        threads = []
        start = time.time()

        for task_id, difficulty in tasks:
            thread = threading.Thread(
                target=self.process_task,
                args=(task_id, difficulty)
            )
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        elapsed = time.time() - start
        completed = self.tasks_completed.value
        return elapsed, completed
     
    def run_with_processes(self, tasks): 
        """Ejecutar tareas usando procesos"""
        with self.tasks_completed.get_lock():
            self.tasks_completed.value = 0

        processes = []
        start = time.time()

        for task_id, difficulty in tasks:
            process = multiprocessing.Process(
                target=self.process_task,
                args=(task_id, difficulty)
            )
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        elapsed = time.time() - start
        completed = self.tasks_completed.value
        return elapsed, completed



if __name__ == "__main__":
    random.seed()

    # 4 tareas con dificultad aleatoria entre 1 y 5.
    tasks = [(task_id, random.randint(1, 5)) for task_id in range(1, 5)]
    print("Tareas generadas:")
    for task_id, difficulty in tasks:
        print(f"Tarea {task_id}: dificultad {difficulty}")

    processor = TaskProcessor()

    print("\nEjecutando con hilos")
    thread_time, thread_completed = processor.run_with_threads(tasks)
    print(f"Tareas completadas hilos: {thread_completed}")

    print("\nEjecutando con procesos")
    process_time, process_completed = processor.run_with_processes(tasks)
    print(f"Tareas completadas procesos: {process_completed}")

#    analyze_results(thread_time, process_time)