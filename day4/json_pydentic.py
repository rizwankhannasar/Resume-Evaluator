
import os
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel, Field
from typing import List, Optional

# Load environment variables
load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

# Initialize Groq client
client = Groq(api_key=my_api_key)

# Model
model = "openai/gpt-oss-120b"


# Define Pydantic models
class Education(BaseModel):
    degree: Optional[str] = None
    institution: Optional[str] = None
    start_year: Optional[int] = None
    end_year: Optional[int] = None


class Experience(BaseModel):
    job_title: Optional[str] = None
    company: Optional[str] = None
    duration: Optional[str] = None
    responsibilities: List[str] = Field(default_factory=list)


class CV(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    professional_summary: Optional[str] = None
    skills: List[str] = Field(default_factory=list)
    education: List[Education] = Field(default_factory=list)
    experience: List[Experience] = Field(default_factory=list)
    projects: List[str] = Field(default_factory=list)
    certifications: List[str] = Field(default_factory=list)
    languages: List[str] = Field(default_factory=list)


# Response format
response_format = {
    "type": "json_object"
}

# System prompt
system_prompt = {
    "role": "system",
    "content": """
    You are a professional CV information extraction assistant.

    Extract all available information from the user's CV.

    Return the extracted information in valid JSON format.

    Rules:
    - Extract only information present in the CV.
    - Do not invent or assume missing information.
    - Use null for missing single-value fields.
    - Use empty lists for missing list fields.
    - Keep the extracted information accurate.
    """
}

# CV text
text = """
Name: Rizwan Khan
Email: rizwan@example.com
Phone: 03001234567

Professional Summary:
Software Engineering student interested in AI and Web Development.

Skills:
Python, JavaScript, React, Node.js, MongoDB

Education:
BS Software Engineering, MUST, 2023-2027

Projects:
StudentHub
NEXORA AI Assistant
"""

# User prompt
prompt = f"""
Extract information from the following CV:

{text}
"""

messages = [
    system_prompt,
    {
        "role": "user",
        "content": prompt
    }
]

# Generate response
response = client.chat.completions.create(
    model=model,
    messages=messages,
    response_format=response_format,
    temperature=0.2
)

# Get AI response
result = response.choices[0].message.content

print("######## AI GENERATED JSON ########")
print(result)

# Validate response using Pydantic
cv_data = CV.model_validate_json(result)

print("\n######## VALIDATED CV ########")
print(cv_data.model_dump_json(indent=4))
