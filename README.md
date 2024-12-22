# Checkout AGRICHAIN Solution

## Description
This project implements a supermarket checkout system in Python. It calculates the total price of scanned items, applying discounts where applicable.

### Features
- Object-Oriented Design
- Discount and Individual Pricing Support
- Unit Tests for Validation

---

## Directory Structure
checkout-kata/ 
    ├── src/ │ 
    ├── checkout.py # Main Python script for the checkout system │ 
    ├── init.py # To make src a package (can be empty) 
    ├── tests/ │ 
    ├── test_checkout.py # Unit test script │ 
    ├── init.py # To make tests a package (can be empty) 
    ├── Dockerfile # Docker configuration 
    ├── requirements.txt # Python dependencies 
    ├── README.md # Documentation


## Prerequisites
- Python 3 or higher

## Setup and Usage

### Running Locally
1. Download the ZIP file containing the code from the provided link.
   
2. Extract the ZIP file into a desired directory.

3. Open a terminal and navigate to the extracted folder:
    ```bash
    cd "AGRITECH-SOL"
    ```

4. Check Python Installation:
    Ensure that Python 3.9 or higher is installed on your system:
    ```bash
    python --version
    ```
    If the version is below Python 3.9, install the latest Python version from [python.org](https://www.python.org/downloads/).

5. Run the program:
    ```bash
    python src/checkout.py
    ```

---

## Example Input and Output
- **Input:** `AAABBD`  
- **Output:** `Total price: 190`

---

## Running Tests
To validate the functionality with unit tests:
```bash
python -m unittest discover tests
```
