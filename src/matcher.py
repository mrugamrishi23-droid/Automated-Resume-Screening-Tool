from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def score_resume(filename, resume_text, job_description, required_skills):
    """
    Transparent scoring model:
      60% required-skill coverage + 40% TF-IDF cosine similarity.
    Scores support human review; they are not hiring decisions.
    """
    matched = [skill for skill in required_skills if skill in resume_text]
    missing = [skill for skill in required_skills if skill not in resume_text]
    skill_score = (len(matched) / len(required_skills) * 100) if required_skills else 0.0

    vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
    matrix = vectorizer.fit_transform([job_description, resume_text])
    similarity_score = float(cosine_similarity(matrix[0:1], matrix[1:2])[0][0] * 100)

    overall_score = (0.60 * skill_score) + (0.40 * similarity_score)

    # Illustrative threshold only. Always have a person review the resume.
    if overall_score >= 60:
        recommendation = "SHORTLIST FOR HUMAN REVIEW"
    else:
        recommendation = "REVIEW / NOT SHORTLISTED"

    return {
        "resume": filename,
        "overall_score": round(overall_score, 2),
        "skill_score": round(skill_score, 2),
        "similarity_score": round(similarity_score, 2),
        "matched_skills": ", ".join(matched),
        "missing_skills": ", ".join(missing),
        "recommendation": recommendation,
    }
