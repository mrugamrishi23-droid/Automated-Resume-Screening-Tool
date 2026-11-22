from pathlib import Path
import pandas as pd
import streamlit as st
from src.resume_parser import extract_text
from src.text_utils import clean_text, load_required_skills
from src.matcher import score_resume

ROOT = Path(__file__).resolve().parent
st.set_page_config(page_title="Resume Screening Tool", layout="wide")
st.title("Automated Resume Screening Tool")
st.caption("Educational prototype — use scores only to support human review.")

jd_default = (ROOT / "data" / "job_description.txt").read_text(encoding="utf-8")
skills_default = (ROOT / "data" / "required_skills.txt").read_text(encoding="utf-8")
jd = st.text_area("Job description", jd_default, height=220)
skills_text = st.text_area("Required skills (one per line)", skills_default, height=150)
uploads = st.file_uploader("Upload resumes (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"], accept_multiple_files=True)

if st.button("Screen resumes", type="primary"):
    skills = [s.strip().lower() for s in skills_text.splitlines() if s.strip()]
    results = []
    if not uploads:
        st.warning("Upload at least one resume.")
    elif not jd.strip() or not skills:
        st.warning("Enter a job description and at least one required skill.")
    else:
        for upload in uploads:
            temp_path = ROOT / f"_temp_{upload.name}"
            temp_path.write_bytes(upload.getvalue())
            try:
                text = clean_text(extract_text(temp_path))
                if text:
                    results.append(score_resume(upload.name, text, clean_text(jd), skills))
            finally:
                temp_path.unlink(missing_ok=True)
        results.sort(key=lambda x: x["overall_score"], reverse=True)
        if results:
            df = pd.DataFrame(results)
            df.insert(0, "rank", range(1, len(df) + 1))
            st.dataframe(df, use_container_width=True)
            st.download_button("Download CSV report", df.to_csv(index=False).encode("utf-8-sig"),
                               "screening_report.csv", "text/csv")
