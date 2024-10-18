# FastAPI File Processing Application

This is a FastAPI application that processes CSV files for VA (Vulnerability Assessment) and Hardening data. It applies data transformations, deduplicates records, and generates an Excel file with conditional formatting based on the severity of the findings.

## Features

- Upload multiple CSV files for processing
- Deduplicate data based on predefined rules
- Extract and format key information
- Generate an Excel file with custom conditional formatting
- Automatically removes processed files after download

## Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
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
    uvicorn app.main:app --reload
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

4. **API Documentation**:
    You can also access the auto-generated API documentation:
    - **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## File Structure

