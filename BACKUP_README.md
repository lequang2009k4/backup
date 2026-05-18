# OPENCLAW BACKUP - 2026-05-18
# Hướng dẫn restore: copy toàn bộ thư mục này sang server mới, chạy setup lại channel credentials nếu cần

## CẤU TRÚC THƯ MỤC

openclaw_backup_2026-05-18/
├── workspace/
│   ├── AGENTS.md
│   ├── SOUL.md
│   ├── IDENTITY.md
│   ├── USER.md
│   ├── TOOLS.md
│   ├── HEARTBEAT.md
│   ├── backup_cskh_2026-05-18.md
│   └── memory/
├── scripts/
│   └── sao_ke_reminder.py
├── openclaw.json          # Cấu hình chính (backup credentials đã có sẵn)
├── agents/                # Agent configs
├── cron/                  # Cron job definitions
├── credentials/           # Channel credentials (telegram, zalouser, etc.)
├── plugins/              # Plugin configs
└── memory/                # Memory files

## CÁCH RESTORE TRÊN SERVER MỚI

1. Cài OpenClaw trên server mới
2. Copy toàn bộ thư mục backup vào ~/.openclaw/
3. Copy credentials/ và openclaw.json
4. Setup lại các channel (Telegram, Zalo) nếu cần
5. Import database cskh: mysql cskh < backup_cskh_2026-05-18.sql

## DATABASE CSKH

Database: cskh
Bảng: cskh (6 columns: Nickname, customer_name, ID, bank, digits, ngay_sao_ke)
7 bản ghi (LE TRONG TIN đã xóa)

SQL dump: backup_cskh_2026-05-18.sql

## CRON JOBS

- Sao ke reminder: chạy 10:00 AM mỗi ngày (Asia/Ho_Chi_Minh)
  Script: /home/ubuntu/.openclaw/scripts/sao_ke_reminder.py
  Target: tất cả bản ghi có ngay_sao_ke = ngày hiện tại
  Channel: Zalo (zalouser)

## SCRIPTS

- sao_ke_reminder.py: Gửi nhắc sao kê hàng ngày lúc 10:00 AM
  Nội dung: "{customer_name} {bank} - {digits} của anh/chị đã có thông báo sao kê, anh/chị kiểm tra giúp em nhé !"

## CREDENTIALS CẦN SETUP LẠI

- Telegram: cần bot token mới hoặc chuyển từ server cũ
- Zalo: cần OAuth token từ Zalo OA
- MySQL: host, user, password cho database cskh