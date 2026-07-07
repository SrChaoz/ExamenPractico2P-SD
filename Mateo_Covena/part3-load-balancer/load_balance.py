from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from random import Random
from threading import Lock
from time import perf_counter, sleep


class LoadBalancer:
    def __init__(self, servers):
        if not servers:
            raise ValueError("declra un servidor")

        self.servers = list(servers)
        self.current_index = 0
        self.active_connections = {server: 0 for server in self.servers}
        self.lock = Lock()

    def round_robin(self):
        with self.lock:
            server = self.servers[self.current_index]
            self.current_index = (self.current_index + 1) % len(self.servers)
            self.active_connections[server] += 1
            return server

    def least_connections(self):
        with self.lock:
            server = min(
                self.servers,
                key=lambda server: (self.active_connections[server], self.servers.index(server)),
            )
            self.active_connections[server] += 1
            return server

    def acquire(self, algorithm):
        if algorithm == "round_robin":
            return self.round_robin()
        if algorithm == "least_connections":
            return self.least_connections()
        raise ValueError(f"Algoritmo no soportado: {algorithm}")

    def finish_request(self, server):
        with self.lock:
            self.active_connections[server] -= 1


def simulate_requests(servers, algorithm, durations, max_workers=10):
    balancer = LoadBalancer(servers)
    distribution = Counter()
    start_time = perf_counter()

    def handle_request(duration):
        server = balancer.acquire(algorithm)
        try:
            sleep(duration)
            return server
        finally:
            balancer.finish_request(server)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(handle_request, duration) for duration in durations]
        for future in as_completed(futures):
            distribution[future.result()] += 1

    elapsed = perf_counter() - start_time
    return distribution, elapsed


def print_comparison(servers, request_count=50):
    rng = Random(42)
    durations = [rng.uniform(0.05, 0.2) for _ in range(request_count)]

    rr_distribution, rr_elapsed = simulate_requests(servers, "round_robin", durations)
    lc_distribution, lc_elapsed = simulate_requests(servers, "least_connections", durations)

    print(f"Simulacion de {request_count} peticiones\n")
    print("Round robin:")
    for server in servers:
        print(f"  {server}: {rr_distribution[server]}")
    print(f"  Tiempo total: {rr_elapsed:.3f}s")

    print("\nLeast connections:")
    for server in servers:
        print(f"  {server}: {lc_distribution[server]}")
    print(f"  Tiempo total: {lc_elapsed:.3f}s")


if __name__ == "__main__":
    servers = ["Servidor1", "Servidor2"]
    print_comparison(servers)