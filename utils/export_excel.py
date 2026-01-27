from pathlib import Path
from openpyxl import Workbook
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_DIR = BASE_DIR / "media"

async def export_users_to_excel(users: list[dict], file_name: str | None = None):
    MEDIA_DIR.mkdir(exist_ok=True)

    if not file_name:
        date = datetime.now().strftime("%Y-%m-%d_%H-%M")
        file_name = MEDIA_DIR / f"users_{date}.xlsx"

    wb = Workbook()
    ws = wb.active
    ws.title = "Users"

    ws.append(["Full name", "Phone", "Username", "Passport", "Telegram ID", "Language"])

    for user in users:
        ws.append([
            user.get("fullname"),
            user.get("phone"),
            user.get("username"),
            user.get("passport"),
            user.get("tg_id"),
            user.get("language"),
        ])

    wb.save(file_name)
    return str(file_name)
