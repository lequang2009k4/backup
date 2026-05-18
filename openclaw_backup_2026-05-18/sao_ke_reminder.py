#!/usr/bin/env python3
"""
Cron script: Gửi nhắc sao kê hàng ngày lúc 10:00 AM (GMT+7)
- Query bảng cskh với điều kiện ngay_sao_ke = ngày hiện tại
- Gửi tin nhắn Zalo cho user HOẶC group dựa trên ID format (group: prefix)
- Nội dung: "{bank} - {digits} của anh/chị đã có thông báo sao kê , anh/chị kiểm tra giúp em nhé !"
- Qui tắc: tìm user trước, không ra thì tìm group
"""

import subprocess
from datetime import datetime

# Lấy ngày hiện tại theo GMT+7
today = datetime.now()
day_of_month = today.day

print(f"[CRON] Running sao ke reminder - ngay_sao_ke = {day_of_month}")

# Kết nối MySQL và lấy bản ghi (4 cột: Nickname, ID, bank, digits)
result = subprocess.run(
    ["sudo", "mysql", "cskh", "--batch", "--skip-column-names",
     "-e", f"SELECT Nickname, customer_name, ID, bank, digits FROM cskh WHERE ngay_sao_ke = {day_of_month};"],
    capture_output=True, text=True
)

if result.returncode != 0:
    print(f"[ERROR] MySQL query failed: {result.stderr}")
    exit(1)

lines = [line for line in result.stdout.strip().split("\n") if line.strip()]
print(f"[INFO] Found {len(lines)} records to notify")

if not lines:
    print("[INFO] No records found for today. Skip.")
    exit(0)

# Xử lý từng bản ghi
for line in lines:
    parts = line.split("\t")
    if len(parts) < 4:
        print(f"[WARN] Skipping malformed line: {line}")
        continue

    nickname = parts[0].strip()
    customer_name = parts[1].strip()
    zalo_id = parts[2].strip()
    bank = parts[3].strip()
    digits = parts[4].strip()

    # Nếu ID trống → thử tra từ danh bạ Zalo (user trước, không ra thì tìm group)
    if not zalo_id or zalo_id == "NULL" or zalo_id == "":
        print(f"[WARN] Missing Zalo ID for '{nickname}', resolving...")
        zalo_id = None

        # Thử tìm user trước
        resolve_user = subprocess.run(
            ["openclaw", "directory", "peers", "list", "--channel", "zalouser", "--query", nickname],
            capture_output=True, text=True
        )
        if resolve_user.returncode == 0:
            for l in resolve_user.stdout.split("\n"):
                if nickname in l:
                    cols = l.split("|")
                    if len(cols) >= 1:
                        found_id = cols[0].strip()
                        if found_id and found_id != "ID":
                            zalo_id = found_id
                            print(f"[INFO] Resolved as USER: {nickname} -> {zalo_id}")
                            break

        # Không tìm thấy user → thử tìm group
        if not zalo_id:
            print(f"[INFO] User not found, trying group for '{nickname}'...")
            resolve_group = subprocess.run(
                ["openclaw", "directory", "groups", "list", "--channel", "zalouser", "--query", nickname],
                capture_output=True, text=True
            )
            if resolve_group.returncode == 0:
                for l in resolve_group.stdout.split("\n"):
                    if nickname in l:
                        cols = l.split("|")
                        if len(cols) >= 1:
                            found_id = cols[0].strip()
                            if found_id and found_id != "ID":
                                zalo_id = found_id
                                print(f"[INFO] Resolved as GROUP: {nickname} -> {zalo_id}")
                                break

        # Cập nhật ID vào CSDL nếu tìm được
        if zalo_id:
            subprocess.run(
                ["sudo", "mysql", "cskh", "--batch", "--skip-column-names",
                 "-e", f"UPDATE cskh SET ID = '{zalo_id}' WHERE Nickname = '{nickname}' AND bank = '{bank}' AND digits = '{digits}';"],
                capture_output=True, text=True
            )
        else:
            print(f"[SKIP] Cannot resolve Zalo ID for '{nickname}'")

    if not zalo_id or zalo_id == "NULL" or zalo_id == "":
        print(f"[SKIP] No Zalo ID resolved for '{nickname}'")
        continue

    # Gửi tin nhắn
    card_label = f"{bank} - {digits}"
    message = f"{customer_name} {card_label} của anh/chị đã có thông báo sao kê , anh/chị kiểm tra giúp em nhé !"

    send_result = subprocess.run(
        ["openclaw", "message", "send", "--channel", "zalouser", "--target", zalo_id, "--message", message],
        capture_output=True, text=True
    )

    if send_result.returncode == 0 and "✅ Sent" in send_result.stdout:
        target_label = "GROUP" if zalo_id.startswith("group:") else "USER"
        print(f"[OK] Sent to [{target_label}] {nickname} ({zalo_id}): {card_label}")
    else:
        print(f"[FAIL] Failed to send to {nickname}: {send_result.stdout} {send_result.stderr}")

print(f"[DONE] Processed {len(lines)} records")