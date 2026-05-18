# Cronjob Backup - Sao Ke Reminder
# Created: 2026-05-19 06:33 GMT+7

## Cronjob: Sao Ke Reminder

| Trường | Giá trị |
|---|---|
| **ID** | `1caa58ac-c4e6-4436-8ee2-d17190b9183a` |
| **Tên** | Run the sao ke reminder script: python3 /home/ubuntu/.openclaw/scripts/sao_ke_reminder.py |
| **Mô tả** | Sao ke reminder 10AM daily |
| **Trạng thái** | Enabled ✅ |
| **Script** | `python3 /home/ubuntu/.openclaw/scripts/sao_ke_reminder.py` |
| **Lịch chạy** | Mỗi ngày lúc 10:00 AM (Asia/Ho_Chi_Minh) |
| **Session target** | isolated |
| **Delivery** | announce → telegram:6051382519 |

## Schedule Details

```
Cron expression : 0 10 * * *
Timezone        : Asia/Ho_Chi_Minh
Run time        : 10:00 AM daily
```

## State

| Trường | Giá trị |
|---|---|
| **Next run** | 2026-05-19 10:00 GMT+7 |
| **Last run** | 2026-05-18 10:00 GMT+7 |
| **Last status** | ok ✅ |
| **Last duration** | 166,156 ms (~2.7 phút) |
| **Consecutive errors** | 0 |
| **Consecutive skipped** | 0 |

## Delivery Preview

```
announce -> telegram:6051382519 (explicit)
```

## Payload

```json
{
  "kind": "agentTurn",
  "lightContext": true,
  "message": "Run the sao ke reminder script: python3 /home/ubuntu/.openclaw/scripts/sao_ke_reminder.py"
}
```

## Notes

- Cronjob chạy mỗi sáng 10h AM, nhắc nhở sao kê
- Kết quả gửi về Telegram cho user 6051382519
- Script: `/home/ubuntu/.openclaw/scripts/sao_ke_reminder.py`