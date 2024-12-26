class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp # proportional gain
        self.ki = ki # integral gain 
        self.kd = kd # derivative gain

        self.prev_error = 0 # previous error for derivative term
        self.integral_error = 0 # commulative error for integral term

    def compute(self, setpoint, current_value):
        """
            It will compute the out of the PID controller
            arguments
                setpoint: target value (avg utilization)
                current_value: current utilization of the node

            returns
                adjustment to be applied to the node's weight
        """

        error = setpoint - current_value

        self.integral_error += error 
        derivative = error - self.prev_error

        pid_output = self.kp * error + self.ki * self.integral_error + self.kd * derivative

        self.prev_error = error

        return pid_output 