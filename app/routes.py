from fastapi import APIRouter, File, UploadFile, BackgroundTasks
from fastapi.responses import FileResponse
import tempfile
import os
from services.file_processing import process_files
from utils.helper import remove_file_later
router = APIRouter()

@router.post("/upload/")
async def upload_files(background_tasks: BackgroundTasks, files: list[UploadFile] = File(...)):
    temp_dir = tempfile.mkdtemp()
    output_filename = os.path.join(temp_dir, "combined_processed_files.xlsx")

    # Call the service to process uploaded files
    await process_files(files, output_filename)

    # Set up the file for download and removal
    response = FileResponse(output_filename, filename="combined_processed_files.xlsx", media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response.background = lambda: remove_file_later(output_filename, background_tasks)
    return response
