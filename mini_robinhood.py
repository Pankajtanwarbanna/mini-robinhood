import random 
from pid_controller import PIDController

# nodes - with their respective sample weights and utilization
nodes = [
    { "node_id": 1, "weight": 0.5, "utilization": 1 },
    { "node_id": 2, "weight": 0.7, "utilization": 1 },
    { "node_id": 3, "weight": 0.4, "utilization": 1 },
]

# distributing traffic among nodes 
def distribute_traffic():
    total_weight = sum(node["weight"] for node in nodes)

    for node in nodes:
        node["utilization"] += random.uniform(0.05, 0.15) * ( node["weight"] / total_weight ) # just throwing traffic as per their weights

def avg_utilization():
    return sum(node["utilization"] for node in nodes) / len(nodes)

# --------- Mini Robinhood Demo ---- #
class MiniRobinhoodDemo:
    @staticmethod
    def run():
        # setting up a pid_controller for each node
        pid_controllers = [
            PIDController(1, 0.1, 0.5) for _ in nodes
        ]

        # simulating for 10 iterations 
        for itr in range(10):
            print('Iteration: ', itr)

            avg_util = avg_utilization()
            print(f"Average Utilization: {avg_util}")


            # now, adjusting weights using PID controllers
            for index, node in enumerate(nodes):
                adjustment = pid_controllers[index].compute(avg_util, node["utilization"])
                node["weight"] += adjustment

                print(f"  Node {node['node_id']} - Utilization: {node['utilization']:.2f}, New Weight: {node['weight']:.2f}")

            distribute_traffic()

            print('----------------------------------')


        print('Done')

if __name__ == "__main__":
    MiniRobinhoodDemo.run()