# Roll Damping Coefficient Estimation Script

This repository contains a Python script (roll_damp.py) that estimates the roll damping coefficient using the Ikeda method.

## Overview

Roll damping is an important factor in naval architecture and marine engineering, influencing the stability of a ship in the water. This script leverages the IKEA method to compute the roll damping coefficient, a key parameter in assessing the rolling motion of a vessel.

## Features

Estimates the roll damping coefficient based on the IKEA method.
Can be used for marine engineering and ship stability calculations.
Written in Python for easy customization and integration with other engineering tools.

## Requirements

Ensure that you have the following installed:

Python 3.x
Required Python libraries (install using the command below)
```
bash
pip install -r requirements.txt
```

## Usage

To use the script, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/your-username/roll-damping.git
```
2. Navigate to the project directory:
```bash
cd roll-damping
```

3. Run the script:
```bash
python roll_damp.py
```

## Input

The script expects certain parameters related to the ship's geometry and motion, which are either passed as command-line arguments or prompted within the script itself.

## Output

The script will output the estimated roll damping coefficient based on the inputs provided.

## Contributions

Contributions are welcome! If you want to contribute, please follow the standard GitHub fork and pull request process.

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/pciuh/roll-damping/blob/main/LICENSE) file for details.
