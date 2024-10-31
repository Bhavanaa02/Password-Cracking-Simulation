import itertools
import hashlib
import string
import time

# Define the target hashed password (hashed in SHA-256 for this example)
TARGET_HASH = hashlib.sha256("password123".encode()).hexdigest()

# Character set to use for brute-force attempts
CHARACTER_SET = string.ascii_lowercase + string.digits

# Specify the minimum and maximum password length to attempt
MIN_LENGTH = 1
MAX_LENGTH = 5

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def brute_force_crack():
    """Attempt to brute-force the password."""
    start_time = time.time()
    attempt_count = 0

    for length in range(MIN_LENGTH, MAX_LENGTH + 1):
        # Generate all possible combinations of the character set for the current length
        for guess in itertools.product(CHARACTER_SET, repeat=length):
            attempt_count += 1
            guess_password = ''.join(guess)
            guess_hash = hash_password(guess_password)

            # Check if the generated hash matches the target hash
            if guess_hash == TARGET_HASH:
                end_time = time.time()
                print(f"Password found: '{guess_password}'")
                print(f"Total attempts: {attempt_count}")
                print(f"Time taken: {end_time - start_time:.2f} seconds")
                return guess_password

    print("Password not found within the given constraints.")
    return None

if __name__ == "__main__":
    print("Starting brute-force password cracking...")
    brute_force_crack()

