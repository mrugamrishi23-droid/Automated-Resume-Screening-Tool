import csv
from pathlib import Path

FIELDS = [
    "rank", "resume", "overall_score", "skill_score", "similarity_score",
    "matched_skills", "missing_skills", "recommendation"
]

def save_report(results, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        for rank, result in enumerate(results, start=1):
            writer.writerow({"rank": rank, **result})

def print_results(results):
    print("\nRESUME SCREENING RESULTS")
    print("-" * 88)
    print(f"{'Rank':<6}{'Resume':<28}{'Score':>9}  Recommendation")
    print("-" * 88)
    for rank, item in enumerate(results, start=1):
        print(f"{rank:<6}{item['resume'][:26]:<28}{item['overall_score']:>7.2f}%  {item['recommendation']}")
    print("-" * 88)
    print("Note: Scores are an initial relevance aid, not an automated hiring decision.")
