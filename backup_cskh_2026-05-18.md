# CSKH Database Backup
# Created: 2026-05-18 10:11 GMT+7

## Bảng: cskh

| Nickname | customer_name | ID | bank | digits | ngay_sao_ke |
|---|---|---|---|---|---|
| Lê Văn Quang | Lê Văn Quang | 724787544187901138 | SHINHAN | 8338 | 16 |
| A MANH MARKUS | PHAM DUY | group:3627891552856832644 | Techcombank | 7744 | 16 |
| A CHAU CAM VINH 1.8 | CHAU CAM VINH | group:1525245647247290358 | Techcombank | 9716 | 16 |
| SẾP LONG | LE KHANH HUNG | group:5600551427749700709 | Techcombank | 9276 | 16 |
| Sếp Long | LE THI VAN | group:5600551427749700709 | VIB 2IN1 | 6148 | 17 |
| NGUYEN DANG KHA SHIN HOME | NGUYEN DANG KHA | 6269492902478661341 | HOME CREDIT | 7797 | 18 |
| A MANH MARKUS | NGUYEN VIET DUC | group:3627891552856832644 | UOB | 5637 | 19 |

## Schema

```
cskh
├── Nickname      varchar(255)
├── customer_name varchar(255)
├── ID            varchar(255)
├── bank          varchar(50)
├── digits        varchar(10)
└── ngay_sao_ke   int
```

## Ghi chú

- **LE TRONG TIN** đã bị xóa (ngày 18, NULL Zalo ID)
- 7 bản ghi còn lại (tính đến 2026-05-18)