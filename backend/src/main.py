from os import remove
from re import sub
from mimetypes import add_type
from shutil import copyfileobj, move
from pathlib import Path

from fastapi import FastAPI, File, Form, UploadFile
from fastapi import responses
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from utils.encryptor import Encrypt


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8002",
]

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/encrypt/")
async def create_file(file: UploadFile = File(...), password: str = Form(...)
):
    directory_path = str(Path.cwd().joinpath("docs"))
    file_name = f"{file.filename}"

    step_1, step_2, step_3, step_4, step_5, step_6, step_7, step_8  = [False for _ in range(8)]
    file_to_encrypt = ""
    encrypted_file_name = ""
    response = None

    with open(file_name, "wb") as file_object:
        try:
            copyfileobj(file.file, file_object)
        except:
            step_1 = False
        else:
            step_1 = True
    
    if not step_1:
        return JSONResponse(status_code=500, content={"message": "Server Error Occured:Could not copy file to disk"})
    else:
        try:
            move(file_name, directory_path)
        except:
            step_2 = False
        else:
            step_2 = True
    
    if not step_2:
        return JSONResponse(status_code=500, content={"message": "Server Error Occured: Could not move file to new file location"})
    else:
        try:
            file_to_encrypt = str(sorted(Path(directory_path).glob(file_name))[0])
        except:
            step_3 = False
        else:
            step_3 = True
    
    if not step_3:
        return JSONResponse(status_code=500, content={"message": "Server Error Occured: Could not find file matching the file name on temporary memory"})
    else:
        e = Encrypt(file_to_encrypt, password)
        try:
            e.encrypt()
        except:
            step_4 = False
        else:
            step_4 = True
    
    if not step_4:
        return JSONResponse(status_code=500, content={"message": "File encryption failed"})
    else:
        remove(file_to_encrypt)

        try:
            file_name_pattern = sub(".pdf", "", file_name)
            encrypted_file_name = str(sorted(Path(directory_path).glob(f"{file_name_pattern}.enc"))[0])
        except:
            step_5 = False
        else:
            step_5 = True

    if not step_5:
        return JSONResponse(status_code=500, content={"message": "File name f{file_name} matching .'enc' pattern extension could not be found in disk"})
    else:
        try:
            add_type("application/pdf", ".enc", strict=True)
        except:
            step_6 = False
        else:
            step_6 = True
        
    if not step_6:
        return JSONResponse(status_code=500, content={"message": "Server Error Occured: Mime type addition failed to known mimetypes"})
    else:
        try:
            response = FileResponse(encrypted_file_name, status_code=200, media_type="application/pdf.enc")
        except:
            step_7 = False
        else:
            step_7 = True
    
    if not step_7:
        return JSONResponse(status_code=500, content={"message": "Server Error Occured: Could not initiate file response with that media type 'application/pdf.enc'"})
    else:
        try:
            header_file_name = str(Path(encrypted_file_name).name)
            content_disposition = 'attachment; ' + f"{header_file_name}"
            response.headers['Content-Disposition'] = content_disposition
        except:
            step_8 = False
        else:
            step_8 = True
    
    if not step_8:
        return JSONResponse(status_code=500, content={"message": "Could not add contect disposition of attachment"})
    else:
        return response