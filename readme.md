# ResumeAudit 📄

## Problem
Students apply to dozens of jobs but rarely get feedback on why their resumes fail.  
The issue is not lack of skills — it’s poor presentation, missing keywords, and weak structure.

Recruiters don’t read resumes. They scan.

## What ResumeAudit Does
ResumeAudit analyzes a resume and gives instant, AI-based feedback by:
- Scoring the resume
- Highlighting missing or weak skills
- Comparing good vs bad resume structure
- Showing why one resume performs better than another

## How It Works
- `index.html` → Frontend UI where resumes are uploaded and analyzed  
- `model.py` → Python-based resume analysis model  
- `good_resume` → Sample well-structured resume  
- `bad_resume` → Sample poorly-structured resume  

The system compares resumes and explains **why one passes the scan and the other doesn’t**.

## Why This Is Different
- Built specifically for **students**
- Focuses on clarity, relevance, and impact — not fluff
- Shows **real examples** instead of generic advice
- Simple, fast, and demo-friendly

## Tech Stack
- HTML, CSS, JavaScript
- Python (AI/logic layer)

## How to Run
1. Open `index.html` in a browser
2. Run `model.py` to process resume analysis
3. Use the provided good and bad resumes to see the difference

## Use Case
- Students preparing for placements
- Resume reviews before job applications
- Demo tool for understanding resume quality

## Future Improvements
- PDF upload support
- Job-specific resume scoring
- Deployment as a web app
- More detailed AI feedback

## Built By
Students, for students — to solve a problem we personally faced.
