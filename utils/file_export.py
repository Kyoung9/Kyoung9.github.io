import csv
import os
from typing import Iterable, Dict, List

def _default_export_dir() -> str:
    # Serverless platforms (like Vercel) only allow writes under /tmp.
    if os.getenv("VERCEL") == "1" or os.getenv("NOW_REGION"):
        return "/tmp"
    if os.getenv("AWS_LAMBDA_FUNCTION_NAME") or os.getenv("LAMBDA_TASK_ROOT"):
        return "/tmp"
    return "exports"

def export_csv(
    rows: Iterable[Dict[str, str]],
    file_stem: str,
    field_names: List[str],
    export_dir: str | None = None,
) -> str:
    export_dir = export_dir or _default_export_dir()
    try:
        os.makedirs(export_dir, exist_ok=True)
        path = os.path.join(export_dir, f"{file_stem}.csv")
        with open(path, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)
        return path
    except OSError:
        if export_dir != "/tmp":
            os.makedirs("/tmp", exist_ok=True)
            path = os.path.join("/tmp", f"{file_stem}.csv")
            with open(path, "w", newline="", encoding="utf-8-sig") as f:
                writer = csv.DictWriter(f, fieldnames=field_names)
                writer.writeheader()
                for row in rows:
                    writer.writerow(row)
            return path
        raise
