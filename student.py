"""Module for student score analysis."""

from typing import List

def calculate_average_score(scores: List[float]) -> float:
    """Calculates the average of scores."""
    if not scores:
        return 0.0
    total_score = sum(scores)
    return total_score / len(scores)

def find_highest_score(scores: List[float]) -> float:
    """Finds the highest score."""
    if not scores:
        return 0.0
    return max(scores)

def generate_student_report(student_data: dict) -> str:
    """Generates a formatted student report."""
    name = student_data.get('name', 'N/A')
    scores = student_data.get('scores', [])
    average = calculate_average_score(scores)
    highest = find_highest_score(scores)

    report_lines = [
        f"--- Student Report: {name} ---",
        f"Scores: {', '.join(map(str, scores))}",
        f"Average Score: {average:.2f}",
        f"Highest Score: {highest:.2f}",
        "-----------------------------"
    ]
    return "\n".join(report_lines)

if __name__ == "__main__":
    students_list = [
        {'name': 'Alice Johnson', 'scores': [85.0, 90.0, 88.5, 92.0]},
        {'name': 'Bob Williams', 'scores': [75.0, 80.5, 79.0, 77.5]},
        {'name': 'Charlie Brown', 'scores': [95.0, 98.0, 96.5, 97.0]},
        {'name': 'Diana Prince', 'scores': [60.0, 65.0, 58.0]},
        {'name': 'Eve Adams', 'scores': []}
    ]

    print("Generating reports for all students:")
    for student_entry in students_list:
        REPORT = generate_student_report(student_entry)
        print(REPORT)
        print("\n")
