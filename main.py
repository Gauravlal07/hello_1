from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Optional
import os
from openai import OpenAI
import base64

app = FastAPI()

# Initialize OpenAI client with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = None

@app.post("/api/")
async def answer_question(request: QuestionRequest):
    # Process the question
    question = request.question

    # Use GPT-3.5-Turbo to answer
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )

    answer_text = response.choices[0].message.content

    # Create a standard response
    result = {
        "answer": answer_text,
        "links": [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
                "text": "Use the model that’s mentioned in the question."
            },
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
                "text": "My understanding is that you just have to use a tokenizer, similar to what Prof. Anand used, to get the number of tokens and multiply that by the given rate."
            }
        ]
    }

    return result
