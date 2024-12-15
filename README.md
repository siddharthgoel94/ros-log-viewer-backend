# Backend for Log Management Application  

This is the backend service for the Log Management Application, built with FastAPI. It provides APIs for uploading, filtering, and downloading log files.  

---

## Features  

- Upload log files and parse them.  
- Filter logs by severity and keyword.  
- Download filtered logs as a file.    

---

## Installation  

### 1. **Clone the Repository**  
```bash  
git https://github.com/siddharthgoel94/ros-log-viewer-backend 
```
### 2. **Install Requirements**  
```bash  
pip install -r requirements.txt  
```
### 3. **Run the development server**  
```bash  
uvicorn main:app --reload    
```
  
By default, the server will run at http://127.0.0.1:8000