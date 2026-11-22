from pathlib import Path
from src.resume_parser import extract_text
from src.text_utils import clean_text, load_required_skills
from src.matcher import score_resume
from src.report import save_report, print_results

ROOT = Path(__file__).resolve().parent

def main():
    resumes_dir = ROOT / "resumes"
    jd_path = ROOT / "data" / "job_description.txt"
    skills_path = ROOT / "data" / "required_skills.txt"
    output_dir = ROOT / "outputs"
    output_dir.mkdir(exist_ok=True)

    if not jd_path.exists():
        raise FileNotFoundError(f"Missing job description: {jd_path}")
    job_description = clean_text(jd_path.read_text(encoding="utf-8"))
    required_skills = load_required_skills(skills_path)

    results = []
    supported = {".pdf", ".docx", ".txt"}
    resume_files = sorted(p for p in resumes_dir.iterdir()
                          if p.is_file() and p.suffix.lower() in supported)

    if not resume_files:
        print("No resumes found. Add PDF, DOCX, or TXT files to the resumes/ folder.")
        return

    for resume_path in resume_files:
        try:
            raw_text = extract_text(resume_path)
            cleaned = clean_text(raw_text)
            if not cleaned.strip():
                print(f"WARNING: No readable text found in {resume_path.name}")
                continue
            results.append(score_resume(
                filename=resume_path.name,
                resume_text=cleaned,
                job_description=job_description,
                required_skills=required_skills,
            ))
        except Exception as exc:
            print(f"Could not process {resume_path.name}: {exc}")

    if not results:
        print("No readable resumes were processed.")
        return

    results.sort(key=lambda item: item["overall_score"], reverse=True)
    save_report(results, output_dir / "screening_report.csv")
    print_results(results)
    print(f"\nCSV report saved to: {output_dir / 'screening_report.csv'}")

if __name__ == "__main__":
    main()
