import os
from snuetl import ETL
from pathlib import Path
from typing import Any
import json

if __name__ == "__main__":
    output_dir = input("Enter output directory path: ")
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    x_csrf_token = os.getenv("x_csrf_token")
    legacy_normandy_session = os.getenv("legacy_normandy_session")
    etl = ETL(x_csrf_token, legacy_normandy_session)
    cards = etl.get_dashboard_cards()
    for course in cards:
        course_id = course.id
        course_output_path = output_path / str(course_id)
        course_output_path.mkdir(parents=True, exist_ok=True)
        print(f"----- Fetching for course: {course.originalName} // ID: {course_id} -----")
        json.dump([item.to_dict() for item in etl.get_course_announcements(course_id)], open(course_output_path / f"announcements.json", "w", encoding="utf-8"), ensure_ascii=False, indent=4)
        json.dump([item.to_dict() for item in etl.get_course_users(course_id)], open(course_output_path / f"users.json", "w", encoding="utf-8"), ensure_ascii=False, indent=4)
        json.dump(etl.get_assignments(course_id), open(course_output_path / f"assignments.json", "w", encoding="utf-8"), ensure_ascii=False, indent=4)
        json.dump(etl.get_assignment_submissions(course_id), open(course_output_path / f"submissions.json", "w", encoding="utf-8"), ensure_ascii=False, indent=4)
    print("----- Fetching completed -----")