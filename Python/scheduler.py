'''
Given a set of nodes and pods, write a scheduler to schedule pods on the nodes.
Nodes will have cpu and memory capacity.
Pods will have cpu and memory requests.

'''

class Node:
    def __init__(self, name, cpu_capacity, memory_capacity):
        self.name = name
        self.cpu_capacity = cpu_capacity
        self.memory_capacity = memory_capacity
        self.available_cpu = cpu_capacity
        self.available_memory = memory_capacity
        self.pods = []

    def can_schedule(self, pod):
        print("Available CPU and Memory on a node")
        print(self.name)
        print(self.available_cpu)
        print(self.available_memory)

        print("CPU and Memory requests of a pod")
        print(pod.name)
        print(pod.cpu_request)
        print(pod.memory_request)

        return self.available_cpu >= pod.cpu_request and self.available_memory >= pod.memory_request

    def schedule_pod(self, pod):
        if self.can_schedule(pod):
            self.pods.append(pod)
            self.available_cpu -= pod.cpu_request
            self.available_memory -= pod.memory_request
            return True
        return False

class Pod:
    def __init__(self, name, cpu_request, memory_request):
        self.name = name
        self.cpu_request = cpu_request
        self.memory_request = memory_request

class Scheduler:
    def __init__(self, nodes):
        self.nodes = nodes

    def schedule(self, pods):
        for pod in pods:
            scheduled = False
            for node in self.nodes:
                if node.schedule_pod(pod):
                    print(f"Pod {pod.name} scheduled on Node {node.name}")
                    scheduled = True
                    break
            if not scheduled:
                print(f"Pod {pod.name} could not be scheduled due to insufficient resources")

def main():
    # Example usage
    nodes = [Node("Node1", 10, 32), Node("Node2", 20, 64)]
    pods = [Pod("Pod1", 5, 16), Pod("Pod2", 15, 32), Pod("Pod3", 10, 16)]

    scheduler = Scheduler(nodes)
    scheduler.schedule(pods)


if __name__ == "__main__":
    main()
