# Resume Evaluator – AI-Powered CV Information Extraction

## Overview

Resume Evaluator is a Python-based project that uses the Groq API and Large Language Models (LLMs) to extract structured information from CVs and resumes.

The project converts unstructured CV text into organized JSON data, making resume information easier to process, validate, and analyze.

It uses **Pydantic** to define data models and validate the extracted information to ensure a consistent output structure.

## Features

- AI-powered CV information extraction.
- Structured JSON output.
- Personal information extraction.
- Education and experience extraction.
- Skills and project identification.
- Certifications and languages extraction.
- Pydantic-based data validation.
- Environment variable management for API security.

## Technologies Used

- Python
- Groq API
- LLM (OpenAI GPT-OSS 120B)
- Pydantic
- python-dotenv
- JSON

## Extracted Information

The system extracts the following information:

| Category | Information |
|---|---|
| Personal Details | Name, Email, Phone, Address |
| Professional Summary | Career summary |
| Skills | Technical and professional skills |
| Education | Degree, Institution, Start Year, End Year |
| Experience | Job Title, Company, Duration, Responsibilities |
| Projects | Project names |
| Certifications | Professional certifications |
| Languages | Known languages |

## Project Structure

```text
Resume-Evaluator/
│
├── main.py
├── .env
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/rizwankhannasar/Resume-Evaluator.git
```

### 2. Navigate to the Project Directory

```bash
cd Resume-Evaluator
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install groq python-dotenv pydantic
```

### 5. Configure Environment Variables

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from the [Groq Console](https://console.groq.com/).

**Important:** Never share or upload your `.env` file or API key to GitHub.

### 6. Run the Project

```bash
python main.py
```

## How It Works

1. Loads environment variables using `python-dotenv`.
2. Initializes the Groq API client.
3. Defines structured CV models using Pydantic.
4. Sends CV text to the selected LLM.
5. Receives extracted information in JSON format.
6. Validates the JSON response using Pydantic.
7. Displays the structured and validated CV information.

## Example Output

```json
{
    "name": "Rizwan Khan",
    "email": "rizwan@example.com",
    "phone": "03001234567",
    "address": null,
    "professional_summary": "Software Engineering student interested in AI and Web Development.",
    "skills": [
        "Python",
        "JavaScript",
        "React",
        "Node.js",
        "MongoDB"
    ],
    "education": [
        {
            "degree": "BS Software Engineering",
            "institution": "MUST",
            "start_year": 2023,
            "end_year": 2027
        }
    ],
    "experience": [],
    "projects": [
        "StudentHub",
        "NEXORA AI Assistant"
    ],
    "certifications": [],
    "languages": []
}
```

## Future Improvements

- PDF and DOCX resume upload support.
- Automatic text extraction from uploaded resumes.
- Resume evaluation and scoring.
- Job description matching.
- Skills gap analysis.
- Resume improvement suggestions.
- Web-based user interface.

## Author

**Rizwan Khan Nasar**

Software Engineering Student | AI & Web Development

GitHub: [@rizwankhannasar](https://github.com/rizwankhannasar)

---

*This project is developed for learning and exploring AI-powered information extraction, structured outputs, and data validation using Python.*
