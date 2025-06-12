from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import base64
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load scraped data
with open("tds_posts.json", "r") as f:
    discourse_data = json.load(f)

class QuestionRequest(BaseModel):
    question: str
    image: str = None
@app.get("/")
def read_root():
    return {"message": "Virtual TA is live!"}
@app.post("/api/")
async def answer_question(data: QuestionRequest):
    # TODO: Use LLM or keyword match for real answer generation
    # Dummy response
    return {
        "answer": "You must use `gpt-3.5-turbo-0125`...",
        "links": [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
                "text": "Use the model that’s mentioned in the question."
            },
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
                "text": "Use tokenizer to count tokens and multiply by rate."
            }
        ]
    }
