from google.cloud import storage
from flask import escape

# Initialize a Cloud Storage client
storage_client = storage.Client()
bucket_name = 'your-bucket-name'  # Replace with your bucket name

def upload_file(request):
    """
    HTTP Cloud Function to upload a file to Google Cloud Storage.
    """

    # Allow only POST requests
    if request.method != 'POST':
        return 'Method Not Allowed', 405

    try:
        # Get the file from the request
        request_json = request.get_json(silent=True)
        if not request_json or 'file' not in request_json:
            return 'No file provided', 400

        file_content = request_json['file']

        # Decode the base64-encoded file content
        file_data = base64.b64decode(file_content)

        # Create a new blob (file) in the specified bucket
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob('uploaded-file-name')  # You can give a dynamic name here

        # Upload the file data
        blob.upload_from_string(file_data)

        return 'File uploaded.', 200
    except Exception as e:
        return f'Server error: {str(e)}', 500
