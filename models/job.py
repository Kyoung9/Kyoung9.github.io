from dataclasses import dataclass, field
from typing import Optional, Dict, Any

@dataclass
class Job:
    title: str
    company: str
    link: str
    source: str
    location: Optional[str] = None
    salary: Optional[str] = None
    extra: Dict[str, Any] = field(default_factory=dict)

    