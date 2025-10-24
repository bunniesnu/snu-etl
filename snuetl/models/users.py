from dataclasses import dataclass
from typing import List, Optional, Any
from .base import ETLModel

@dataclass
class Grades:
    html_url: str

@dataclass
class Enrollments:
    id: str
    user_id: str
    course_id: str
    type: str
    created_at: str
    updated_at: str
    associated_user_id: Optional[str]
    start_at: Optional[str]
    end_at: Optional[str]
    course_section_id: str
    root_account_id: str
    limit_privileges_to_course_section: bool
    enrollment_state: str
    role: str
    role_id: str
    last_activity_at: str
    last_attended_at: Optional[str]
    total_activity_time: int
    grades: Grades
    html_url: str
    can_be_removed: bool

@dataclass
class User(ETLModel):
    id: str
    name: str
    created_at: str
    sortable_name: str
    short_name: str
    avatar_url: str
    enrollments: List[Enrollments]
    custom_links: Optional[List[Any]] = None