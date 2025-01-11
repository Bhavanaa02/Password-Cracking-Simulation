# Password Cracking Simulation

## Objective
The **Password Cracking Simulation** project demonstrates the process of cracking passwords using dictionary and brute-force attacks. This tool educates on the importance of strong password policies by showing the effectiveness of various cracking techniques and visualizing the time taken based on password complexity.

## Features
- Simulate a dictionary attack using **John the Ripper**.
- Implement a brute-force attack in Python to showcase password vulnerabilities.
- Visualize cracking times for different password strengths using Python scripts.
- Generate reports to analyze password strength and the efficiency of different cracking techniques.

## Prerequisites
- **Python 3.x**: Required for running brute-force attack scripts and visualization.
- **John the Ripper**: A fast password cracker for dictionary attacks. Install it from [here](https://www.openwall.com/john/).
- **Hashcat** (Optional): If you're planning to use it alongside John the Ripper (remove if not applicable).
- **Required Python Libraries**: You can install the necessary Python libraries via `requirements.txt`. This file includes the dependencies for visualizing cracking times and running the brute-force attack.

## Directory Structure
- `/scripts`: Contains Python scripts for brute-force password cracking and visualization.
- `/config`: Holds configuration files for John the Ripper.
- `/reports`: Stores generated reports on password strength and cracking analysis.

## Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Bhavanaa02/Password-Cracking-Simulation.git
   cd Password-Cracking-Simulation
   ```

2. **Install Dependencies**
   Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install External Tools**
   The following tools are used for password cracking and must be installed separately:

   - **[John the Ripper](https://www.openwall.com/john/)**: A popular password cracking tool for dictionary attacks.
     - **Installation**: Follow the instructions on the John the Ripper website for your operating system (Windows, Linux, macOS).
     - After installation, you can verify the installation by running:
       ```bash
       john --version
       ```

   - **[Hashcat](https://hashcat.net/hashcat/)** (Optional): A powerful password cracking tool for high-speed cracking.
     - **Installation**: Follow the instructions on the Hashcat website for your operating system.
     - After installation, you can verify the installation by running:
       ```bash
       hashcat --version
       ```

4. **John the Ripper Configuration**
   The `john.conf` file is used to configure **John the Ripper** for different password cracking strategies:
   - **Incremental Mode**: A brute-force mode with customizable length and character set.
   - **Wordlist Mode**: Cracking passwords using a list of known words.
   - **External Mode**: Allows for custom rules and filters.
   Modify this file according to your cracking needs.

## Example Run
To run the brute-force attack, execute the following command:
```bash
python scripts/brute_force.py --target password_hash.txt --output cracked_passwords.txt
```

To visualize the cracking times, run:
```bash
python scripts/visualise_cracking_times.py --input reports/attack_times.txt --output reports/visualization.png
```

## Ethical Disclaimer
This project is intended for educational purposes only. It demonstrates common password cracking techniques to raise awareness about password security. Please do not use this tool to crack passwords without proper authorization.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- **John the Ripper**: A fast and flexible password cracking tool used in the dictionary attack simulation.
- **Python**: Used for implementing the brute-force attack and visualizing cracking times.
- **Other Libraries**: If any third-party libraries were used for the visualizations or other parts of the project, mention them here.
- **Hashcat**: Optional, used for advanced cracking scenarios.

---
