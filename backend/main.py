from fastapi import FastAPI, File, Form, UploadFile


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/files/")
async def create_file(file: UploadFile = File(...), password: str = Form(...)
):
    return {
        "password": password,
        "filename": file.filename,
        "fileb_content_type": file.content_type,
    }