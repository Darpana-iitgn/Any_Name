def calculate_average_score(scores: list[float]) -> float:
    if not scores:
        return 0.0
    total_score = sum(scores)
    return total_score / len(scores)

def find_highest_score(scores: list[float]) -> float:
    if not scores:
        return 0.0
    return max(scores)

def generate_student_report(student_data: dict) -> str:
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
    students = [
        {'name': 'Alice Johnson', 'scores': [85.0, 90.0, 88.5, 92.0]},
        {'name': 'Bob Williams', 'scores': [75.0, 80.5, 79.0, 77.5]},
        {'name': 'Charlie Brown', 'scores': [95.0, 98.0, 96.5, 97.0]},
        {'name': 'Diana Prince', 'scores': [60.0, 65.0, 58.0]},
        {'name': 'Eve Adams', 'scores': []}
    ]

    print("Generating reports for all students:")
    for student in students:
        report = generate_student_report(student)
        print(report)
        print("\n")