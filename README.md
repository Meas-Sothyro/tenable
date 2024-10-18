# Tenable Scan Result Processing Application

This application helps process CSV files for VA (Vulnerability Assessment) and Hardening data by formating the color based on the severity, extract information of the plugin outputs, remove duplication in the Vulnerabilities Assessment scan

## Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Meas-Sothyro/tenable.git
    cd app
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **MacOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. **Start the FastAPI server**:
    ```bash
    uvicorn main:app --reload
    ```

2. **Access the application**:
    Open your web browser and navigate to:
    ```
    http://127.0.0.1:8000/
    ```

3. **Upload CSV files**:
    - Use the web interface to upload multiple CSV files.
    - The application will process the files and generate a combined Excel report.
    - The report will be automatically downloaded once processing is complete.
