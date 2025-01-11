import os
import argparse
import hashlib
from scripts.brute_force import brute_force_crack
from scripts.visualise_cracking_times import visualize_cracking_times

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Password Cracking Simulation")
    parser.add_argument('--attack', choices=['brute-force', 'visualize'], required=True,
                        help="Choose the type of attack to run.")
    parser.add_argument('--target', help="Path to the target password hash file (for brute-force).")
    parser.add_argument('--output', help="Path to store the output results (for brute-force).")
    parser.add_argument('--input', help="Path to the input file for visualization (for visualize).")
    
    return parser.parse_args()

def main():
    args = parse_args()

    if args.attack == 'brute-force':
        # Ensure the output directory exists
        if args.output:
            os.makedirs(os.path.dirname(args.output), exist_ok=True)
        if args.target:
            brute_force_crack(target_file=args.target, output_file=args.output)
        else:
            print("Error: Target file for brute-force attack not provided.")
    
    elif args.attack == 'visualize':
        # Ensure the output directory exists
        if args.input and args.output:
            os.makedirs(os.path.dirname(args.output), exist_ok=True)
            visualize_cracking_times(input_file=args.input, output_file=args.output)
        else:
            print("Error: Input and output paths for visualization must be provided.")

if __name__ == "__main__":
    main()
