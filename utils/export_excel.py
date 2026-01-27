from openpyxl import Workbook
from datetime import datetime

async def export_users_to_excel(users: list[dict], file_name: str | None = None):
    wb = Workbook()
    ws = wb.active
    ws.title = "Users"

    # Header
    headers = ["Full name", "Phone", "Username", "Passport", "Telegram ID", "Language"]
    ws.append(headers)

    # Rows
    for user in users:
        ws.append([
            user.get("fullname"),
            user.get("phone"),
            user.get("username"),
            user.get("passport"),
            user.get("tg_id"),
            user.get("language"),
        ])

    # File name
    if not file_name:
        date = datetime.now().strftime("%Y-%m-%d_%H-%M")
        file_name = f"users_{date}.xlsx"

    wb.save(file_name)
    return file_name
