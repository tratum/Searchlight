# Searchlight
![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
<br>

Searchlight is a powerful and efficient Text Processing API for PDF's developed with Python. It processes Documents to highlight specified search words and includes various features like word search, unique words count, highlighting search word and integration with MongoDB and AWS S3 bucket.
<br>

## Features
- Word Search: Search for specific words in a PDF.
- Unique Words Count: Count the number of unique words in a PDF.
- Highlighting: Highlights the Search Word in the PDF.
- MongoDB Integration: Store data and results in MongoDB.
- AWS S3 Integration: Upload and retrieve PDFs from an AWS S3 bucket.
<br>

## Installation
1. Clone the repository
   ```bash
   git clone https://github.com/tratum/Searchlight.git
   ```
2. Navigate to the project directory
   ```bash
   cd Searchlight
   ```
3. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`   
   ```
4. Install the required dependencies
   ```bash
   pip install -r requirements.txt
   ```
   <br>

## Configuration
1. Create a .env file in the root directory
   ```bash
   cd Searchlight
   touch .env
   ```
2. Navigate to the ``.env`` file and Configure your MongoDB and AWS S3 Settings
   ```python
   ATLAS_URI= your_mongodb_uri
   DB_NAME= your_db_name
   COLLECTION_NAME= your_collection_name
   RAW_COLLECTION_NAME= your_collection_name
   USER_COLLECTION_NAME=tbl_users
   AWS_ACCESS_KEY ='your_aws_access_key'
   AWS_SECRET_KEY='your_aws_secret_access_key'
   BUCKET_NAME='your_s3_bucket_name'
   ```
<br>

## Usage
1. Start the API Server
   ```bash
   python -m uvicorn main:app --reload
   ```
2. Use the following endpoint to upload a PDF and perform Text Processing
   ```bash
   http://127.0.0.1:8000/searchlight/upload
   ```
   **Mandatory Parameters are:**
       <br>
   
     - ``keyword``: The word to search and highlight in the PDF.
     - ``pdf`` : The PDF file to process.
<br>

  ## Example
  Here is an example of how to use the API with ``cURL``:
  ```bash
    curl -X POST "http://127.0.0.1:8000/searchlight/upload" -F "keyword=example" -F "pdf=@/path/to/your/document.pdf"
  ```
<br>

## Contribution
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.
<br>

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details
<br>

## Acknowledgements

- This project is built with [FastAPI](https://fastapi.tiangolo.com/)  
