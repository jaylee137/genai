from fastapi import FastAPI, UploadFile, File
from parse_pdf import FileParser
from llm_api import LLMApi
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Define CORS policies
origins = [
    "http://localhost",
    "http://localhost:3000",  # Add the specific origin of your frontend
    # Add more origins as needed
]

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile | None = None):
    try:
        if not file.filename.endswith(".pdf"):
            return "Please upload a PDF file"
        pdf_text = FileParser.convert_pdf_to_text(file.file)
        try:
            llmapi = LLMApi()
            json_output = llmapi.call_llm(pdf_text)
            return json_output
        except:
            return "LLM access failed"
    except:
        return  "Please upload a file"
    
    
    
