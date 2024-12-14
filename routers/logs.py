from fastapi import APIRouter, UploadFile, File, HTTPException,Response
from fastapi.responses import FileResponse
from utils import parse_logs, filter_logs
import os

router = APIRouter(
    prefix="/logs",
    tags=["logs"],
)

# Temporary in-memory storage for parsed logs
logs_storage = []

@router.post("/upload/")
async def upload_log(response: Response,file: UploadFile = File(...)):
    """
    Upload a log file, parse it, and store the data.
    """
    if file.content_type not in ["text/plain", "application/octet-stream"]:
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    content = await file.read()
    logs = parse_logs(content.decode("utf-8"))
    logs_storage.clear()
    logs_storage.extend(logs)
    response.headers["Access-Control-Allow-Origin"] = "*"
    
    return {"message": "Log file uploaded and parsed successfully"}

@router.get("/")
def get_logs(response:Response,severity: str = None, keyword: str = None):
    """
    Get logs with optional filters for severity and keyword.
    """
    filtered_logs = filter_logs(logs_storage, severity, keyword)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return {"logs": filtered_logs}

@router.get("/download/")
def download_filtered_logs(response:Response,severity: str = None, keyword: str = None):
    """
    Generate and return a filtered log file for download.
    """
    filtered_logs = filter_logs(logs_storage, severity, keyword)
    print(keyword)
    file_path = "filtered_logs.txt"
    with open(file_path, "w") as file:
        for log in filtered_logs:
            file.write(f"[{log['timestamp']}] [{log['severity']}] [{log['node']}]: {log['message']}\n")
    response.headers["Access-Control-Allow-Origin"] = "*"
    return FileResponse(file_path, media_type="text/plain", filename="filtered_logs.txt")
