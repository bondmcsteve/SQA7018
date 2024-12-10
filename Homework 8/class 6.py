import math
import cmath

class QuantumState:
    def __init__(self, state_vector):
        self.state_vector = state_vector

    # Operator overloading for addition
    def __add__(self, other):
        if len(self.state_vector) != len(other.state_vector):
            raise ValueError("State vectors must be of the same dimension.")
        result = [a + b for a, b in zip(self.state_vector, other.state_vector)]
        return QuantumState(result)

    # Operator overloading for scalar multiplication
    def __mul__(self, scalar):
        result = [scalar * a for a in self.state_vector]
        return QuantumState(result)

    # Operator overloading for inner product
    def __matmul__(self, other):
        if len(self.state_vector) != len(other.state_vector):
            raise ValueError("State vectors must be of the same dimension.")
        result = sum(a.conjugate() * b for a, b in zip(self.state_vector, other.state_vector))
        return result

    # Static method for normalization
    @staticmethod
    def normalize(state_vector):
        norm = math.sqrt(sum(abs(a) ** 2 for a in state_vector))
        if norm == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return [a / norm for a in state_vector]

class SpinState(QuantumState):
    def measure_spin(self, direction):
        # Simplified example: assume direction is 'up' or 'down'
        if direction == 'up':
            basis_state = [1, 0]
        elif direction == 'down':
            basis_state = [0, 1]
        else:
            raise ValueError("Direction must be 'up' or 'down'.")
        prob_amplitude = sum(a.conjugate() * b for a, b in zip(self.state_vector, basis_state))
        probability = abs(prob_amplitude) ** 2
        return probability

# Define spin-up and spin-down states
spin_up = SpinState([1, 0])
spin_down = SpinState([0, 1])

# Compute sum
superposition = spin_up + spin_down

# Compute inner product
inner_product = spin_up @ spin_down

# Normalize the superposition state
normalized_state_vector = QuantumState.normalize(superposition.state_vector)
normalized_superposition = SpinState(normalized_state_vector)

# Print results
print("Spin Up State:", spin_up.state_vector)
print("Spin Down State:", spin_down.state_vector)
print("Superposition State:", superposition.state_vector)
print("Normalized Superposition State:", normalized_superposition.state_vector)
print(f"Inner Product of spin_up and spin_down: {inner_product}")
print(f"Probability of measuring 'up' in superposition state: {normalized_superposition.measure_spin('up'):.2f}")
print(f"Probability of measuring 'down' in superposition state: {normalized_superposition.measure_spin('down'):.2f}")


