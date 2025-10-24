from dataclasses import dataclass
from typing import List, Optional, Any
from .base import ETLModel

@dataclass
class Links:
    css_class: str
    icon: str
    hidden: Optional[bool]
    path: str
    label: str

@dataclass
class DashboardCard(ETLModel):
    longName: str
    shortName: str
    originalName: str
    courseCode: str
    assetString: str
    href: str
    term: str
    subtitle: str
    enrollmentType: str
    id: str
    isFavorited: bool
    links: List[Links]
    observee: Optional[str] = None
    image: Optional[str] = None
    position: Optional[int] = None
