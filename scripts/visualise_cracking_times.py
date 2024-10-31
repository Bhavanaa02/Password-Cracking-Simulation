import itertools
import hashlib
import string
import time
import matplotlib.pyplot as plt

# Define the character sets to simulate different complexity levels
CHARACTER_SETS = {
    "Lowercase Letters": string.ascii_lowercase,
    "Lowercase + Digits": string.ascii_lowercase + string.digits,
    "Lowercase + Uppercase + Digits": string.ascii_letters + string.digits,
    "All Printable": string.printable.strip()
}

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def simulate_cracking_time(character_set, password_length):
    """Simulate brute-force cracking time for a given character set and password length."""
    start_time = time.time()
    attempts = 0

    # Generate all possible combinations for the given character set and length
    for _ in itertools.product(character_set, repeat=password_length):
        attempts += 1

    end_time = time.time()
    return end_time - start_time, attempts

def visualize_cracking_times():
    """Visualize the time taken to crack passwords of various lengths and complexities."""
    lengths = range(1, 6)  # Test password lengths from 1 to 5
    results = {complexity: [] for complexity in CHARACTER_SETS.keys()}

    for complexity, character_set in CHARACTER_SETS.items():
        for length in lengths:
            cracking_time, attempts = simulate_cracking_time(character_set, length)
            results[complexity].append(cracking_time)
            print(f"Complexity: {complexity}, Length: {length}, Time: {cracking_time:.4f} s, Attempts: {attempts}")

    # Plotting the results
    plt.figure(figsize=(10, 6))
    for complexity, times in results.items():
        plt.plot(lengths, times, label=f"{complexity}")

    plt.xlabel("Password Length")
    plt.ylabel("Cracking Time (seconds)")
    plt.title("Brute-Force Cracking Time vs Password Length and Complexity")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    visualize_cracking_times()

