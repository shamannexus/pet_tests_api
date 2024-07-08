# Pet test API

This repository contains automated tests for https://petstore.swagger.io/v2 using pytest.

## Installation

1. **Clone the repository:**
  ```
git clone git@github.com:shamannexus/pet_tests_api.git
  ```
2. **Set up a virtual environment:**

- Install virtualenv if not already installed:

  ```
  pip install virtualenv
  ```

- Create a new virtual environment:

  ```
    python -m venv venv
  ```

- Activate the virtual environment:

  - On Windows:

    ```
    venv\Scripts\activate
    ```

  - On macOS/Linux:

    ```
    source venv/bin/activate
    ```

3. **Install Python dependencies:**
    ```
    pip install -r requirements.txt
    ```

This will install all necessary Python packages including pytest and Appium-Python-Client.
  
## Running Tests

- **Run the test file:**
  ```
  cd tests/ 
  pytest test_api.py
  ```
