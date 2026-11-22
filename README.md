# Automated Resume Screening Tool

An educational Python project that extracts text from PDF, DOCX, and TXT resumes, compares each resume with a job description, calculates transparent relevance scores, ranks candidates, and exports a CSV report.

> **Responsible-use note:** This is a learning prototype, not a production ATS or hiring decision-maker. Scores can be incomplete or misleading. Use job-related criteria only, validate the system, and require human review. Do not use protected characteristics or proxies to rank candidates.

## Problem statement
Manually reviewing many resumes can be time-consuming. This prototype demonstrates how text extraction, skill matching, and TF-IDF cosine similarity can help organize resumes for an initial human review.

## Features
- PDF, DOCX, and TXT text extraction
- Text normalization
- Required-skill coverage
- TF-IDF and cosine similarity
- Weighted score and ranking
- Illustrative shortlist recommendation
- CSV report
- Optional Streamlit upload interface
- Synthetic sample resumes and job description

## Scoring method
- Skill coverage: 60%
- TF-IDF cosine similarity: 40%
- Overall = 0.60 × skill coverage + 0.40 × similarity

The example threshold is 60/100 and is configurable in `src/matcher.py`. It is only a demonstration setting, not a validated hiring cutoff. The score does not measure candidate quality, potential, or job performance.

## Tech stack
Python, Pandas, NumPy, PyPDF2, python-docx, Regex, scikit-learn, TF-IDF, cosine similarity, Streamlit.

## Folder structure
```text
Automated-Resume-Screening-Tool/
├── resumes/                 # Synthetic or consented sample resumes
├── data/                    # Job description and required skills
├── src/                     # Parsing, cleaning, matching, reporting modules
├── outputs/                 # Generated CSV reports (ignored by Git)
├── images/                  # Project screenshots
├── docs/                    # Design notes and test evidence
├── main.py                  # Command-line entry point
├── app.py                   # Optional Streamlit interface
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup
Python 3.10+ is recommended.

### Windows PowerShell
```powershell
py -3.11 -m venv venv
.env\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation, run this for the current terminal:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.env\Scripts\Activate.ps1
```

### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run the command-line version
1. Put resumes in `resumes/`.
2. Edit `data/job_description.txt`.
3. Edit `data/required_skills.txt` (one skill per line).
4. Run:
```bash
python main.py
```
The report is created at `outputs/screening_report.csv`.

## Run the Streamlit interface
```bash
streamlit run app.py
```
Open the local URL shown in the terminal, upload resumes, review the table, and download the CSV.

## Sample output
Exact scores depend on the installed scikit-learn version and text content. The included synthetic resumes should demonstrate ranking differences. The CSV includes rank, filename, overall score, skill score, similarity score, matched skills, missing skills, and recommendation.

## Screenshots
Save screenshots in `images/`, for example:
- `project-folder.png`
- `sample-resumes.png`
- `terminal-run.png`
- `ranking-table.png`
- `csv-report.png`
- `streamlit-dashboard.png`
- `github-repository.png`

Embed them here after capturing:
```markdown
![Terminal run](images/terminal-run.png)
```

## Learning outcomes
- Reading files and handling multiple document formats
- Text preprocessing and regular expressions
- Basic NLP feature extraction
- TF-IDF and cosine similarity
- Designing modular Python applications
- CSV reporting and simple dashboards
- Git, GitHub, testing, and responsible AI considerations

## Limitations and future improvements
- Scanned/image-only PDFs need OCR; this version extracts selectable PDF text.
- Skill matching is literal phrase matching and may miss synonyms or context.
- TF-IDF is a baseline and does not understand meaning like modern language models.
- Resume formatting can affect extraction.
- Add unit tests, synonym dictionaries, configurable weights, audit logs, accessibility checks, and bias evaluation before any real-world pilot.

## Repository safety
Use synthetic data or resumes shared with explicit permission. Remove names, phone numbers, email addresses, addresses, and other personal details before publishing sample files. Do not commit confidential resumes or generated reports containing personal data.

## License
Add a license if you want others to reuse the project (for example, MIT).
