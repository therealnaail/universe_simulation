import numpy as np
import matplotlib.pyplot as plt

print("Universe Simulation made by therealnaail \n")
# Simulation parameters
num_particles = 100
G = 6.67e-11  # Gravitational constant
timestep = float(input("Time Step:"))  # Simulation timestep 
num_steps = int(input("Number of particles:"))  # Number of simulation steps

# Initial conditions
masses = np.random.uniform(1e10, 1e12, num_particles)  # Masses of particles
positions = np.random.uniform(-1e6, 1e6, (num_particles, 3))  # Positions of particles
velocities = np.random.uniform(-1e3, 1e3, (num_particles, 3))  # Velocities of particles

# Simulation loop
for i in range(num_steps):
    # Calculate acceleration for each particle
    accelerations = np.zeros((num_particles, 3))
    for j in range(num_particles):
        for k in range(num_particles):
            if j != k:
                r = positions[k] - positions[j]
                d = np.sqrt(np.sum(r ** 2))
                a = G * masses[k] / d ** 3 * r
                accelerations[j] += a

    # Update positions and velocities
    positions += velocities * timestep
    velocities += accelerations * timestep

    # Plot positions
    plt.clf()
    plt.scatter(positions[:, 0], positions[:, 1], s=masses / 1e10)
    plt.gca().set_aspect('equal')
    plt.xlim(-1e6, 1e6)
    plt.ylim(-1e6, 1e6)
    plt.title(f"Universe Simulation - Time Step {i}")
    plt.xlabel("X Position (m)")
    plt.ylabel("Y Position (m)")
    plt.pause(0.001)
    plt.savefig(f"universe_step_{i}.png")
