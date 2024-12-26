# Mini Robinhood - PID Controller : Load Balancer

A Python project that demonstrates how a [PID controller](https://en.wikipedia.org/wiki/Proportional%E2%80%93integral%E2%80%93derivative_controller) can be used to dynamically adjust weights for nodes in a load balancer. This approach ensures traffic is evenly distributed across nodes by keeping their utilization close to the average utilization. 

> The blog explaining it in more detail is publish here - 

## Features

- Dynamic Weight Adjustment: Adjusts weights of nodes based on their utilization using PID principles.
- Traffic Simulation: Distributes traffic to nodes proportionally to their weights.
- Scalability: Works for any number of nodes.
- PID Explained: Each node has its own PID controller, balancing short-term and long-term deviations.

## Customization

- Tune PID Parameters: Adjust Kp, Ki, and Kd in the PIDController class for different system behaviors.
- Number of Nodes: Add or remove nodes in the nodes list.
- Traffic Behavior: Modify the distribute_traffic function to simulate different traffic patterns.