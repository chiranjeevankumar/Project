import os
from pathlib import Path

os.chdir(Path(__file__).resolve().parent)
app_code = Path("app.py").read_text(encoding="utf-8")
exec(compile(app_code, "app.py", "exec"))
