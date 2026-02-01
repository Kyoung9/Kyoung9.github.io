import csv
import os
from typing import Iterable, Dict, List

def export_csv(rows: Iterable[Dict[str, str]], file_stem: str, field_names: List[str], export_dir: str = "exports") -> str:
    os.makedirs(export_dir, exist_ok=True)
    path = os.path.join(export_dir, f"{file_stem}.csv")

    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return path