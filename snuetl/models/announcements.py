from dataclasses import dataclass
from typing import List, Optional, Any

@dataclass
class Permissions:
    attach: bool
    update: bool
    reply: bool
    delete: bool

@dataclass
class Author:
    id: str
    display_name: str
    avatar_image_url: Optional[str]
    html_url: str
    pronouns: Optional[str]

@dataclass
class Attachment:
    id: str
    display_name: str
    url: str
    filename: str
    content_type: str
    size: int

@dataclass
class LockInfo:
    can_view: bool
    asset_string: str

@dataclass
class Announcement:
    id: str
    title: str
    last_reply_at: str
    created_at: str
    posted_at: str
    position: int
    podcast_has_student_posts: bool
    discussion_type: str
    allow_rating: bool
    only_graders_can_rate: bool
    sort_by_rating: bool
    is_section_specific: bool
    user_name: str
    discussion_subentry_count: int
    permissions: Permissions
    user_can_see_posts: bool
    read_state: str
    unread_count: int
    subscribed: bool
    attachments: List[Attachment]
    published: bool
    can_unpublish: bool
    locked: bool
    can_lock: bool
    comments_disabled: bool
    author: Author
    html_url: str
    url: str
    pinned: bool
    can_group: bool
    topic_children: List[Any]
    group_topic_children: List[Any]
    locked_for_user: bool
    message: str
    subscription_hold: bool
    user_count: int
    delayed_post_at: Optional[str] = None
    assignment_id: Optional[str] = None
    root_topic_id: Optional[str] = None
    lock_at: Optional[str] = None
    require_initial_post: Optional[bool] = None
    podcast_url: Optional[str] = None
    group_category_id: Optional[str] = None
    lock_info: Optional[LockInfo] = None
    lock_explanation: Optional[str] = None
    todo_date: Optional[str] = None
    
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Announcement":
        return cls(**data)
    
    @classmethod
    def list_from_dicts(cls, data_list: List[dict[str, Any]]) -> List["Announcement"]:
        return [cls.from_dict(data) for data in data_list]
    
    def to_dict(self) -> dict[str, Any]:
        return self.__dict__