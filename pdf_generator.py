#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PDF 報價單產生器（雲端版）"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── 字型設定 ──────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_NAME = "ChineseFont"

FONT_CANDIDATES = [
    os.path.join(BASE_DIR, "NotoSansCJK.otf"),   # 雲端部署附帶
    "/System/Library/Fonts/STHeiti Medium.ttc",   # macOS
    "/System/Library/Fonts/PingFang.ttc",
]

for fp in FONT_CANDIDATES:
    if os.path.exists(fp):
        try:
            pdfmetrics.registerFont(TTFont(FONT_NAME, fp))
            break
        except Exception:
            continue

# ── 公司固定資訊 ──────────────────────────────────────
COMPANY = {
    "name":    "好年企業有限公司",
    "tel":     "TEL：06-2324880",
    "fax":     "FAX：06-2318948",
    "email":   "Email：phoneann@gmail.com",
    "address": "地址：台南市永康區中山路101巷2號",
    "handler": "謝豐安",
}

def make_doc_number(date_str: str, seq: int) -> str:
    date_str = date_str.replace("-", "/")
    y, m, d = date_str.split("/")
    roc = int(y) - 1911
    return f"{roc:03d}{int(m):02d}{int(d):02d}{seq:02d}"

def calc_subtotal(qty_str, price_str):
    """能算就算，數量為文字（如「1批」）則回傳空字串"""
    try:
        q = float(str(qty_str).replace(",","").strip())
        p = float(str(price_str).replace(",","").strip())
        return int(q * p)
    except Exception:
        return ""

def build_pdf(data: dict, output_path: str):
    customer   = data["customer"]
    image_path = data.get("image_path", "")
    items      = data["items"]
    remarks    = data.get("remarks", "").strip()

    seq = int(customer["seq"]) if str(customer["seq"]).isdigit() else 1
    doc_num = make_doc_number(customer["date"], seq)

    doc = SimpleDocTemplate(
        output_path, pagesize=A4,
        topMargin=12*mm, bottomMargin=12*mm,
        leftMargin=15*mm, rightMargin=15*mm,
    )
    W = A4[0] - 30*mm

    def S(size=9, bold=False, align="LEFT"):
        return ParagraphStyle(
            name="s", fontName=FONT_NAME, fontSize=size,
            leading=size*1.4,
            alignment={"LEFT":0,"CENTER":1,"RIGHT":2}[align],
        )
    def P(text, **kw): return Paragraph(str(text), S(**kw))

    elements = []
    elements.append(P(f"{COMPANY['name']}　客戶報價單", size=16, align="CENTER"))
    elements.append(Spacer(1, 3*mm))

    info_data = [
        [P(f"客戶名稱：{customer['name']}"),  P(f"電話：{customer['phone']}")],
        [P(f"客戶編號：{customer['number']}"), P(f"統一編號：{customer['tax_id']}")],
        [P(f"有效日期：{customer['valid']}"),  P(f"報價日期：{customer['date']}")],
        [P(f"單據編號：{doc_num}"),             P(f"製單人員：{COMPANY['handler']}")],
    ]
    info_t = Table(info_data, colWidths=[W*0.5, W*0.5])
    info_t.setStyle(TableStyle([
        ("FONTNAME",(0,0),(-1,-1),FONT_NAME),("FONTSIZE",(0,0),(-1,-1),9),
        ("TOPPADDING",(0,0),(-1,-1),1),("BOTTOMPADDING",(0,0),(-1,-1),1),
        ("BOX",(0,0),(-1,-1),0.5,colors.black),
        ("INNERGRID",(0,0),(-1,-1),0.5,colors.lightgrey),
    ]))
    elements.append(info_t)
    elements.append(Spacer(1, 2*mm))

    # 品項合併
    groups = []
    for item in items:
        if groups and groups[-1]["name"] == item["name"]:
            groups[-1]["rows"].append(item)
        else:
            groups.append({"name": item["name"], "img": item.get("_img",""), "rows": [item]})

    col_w = [W*0.07, W*0.33, W*0.13, W*0.13, W*0.13, W*0.21]
    header = [P("項次",align="CENTER"),P("品名",align="CENTER"),P("數量",align="CENTER"),
              P("單價/元",align="CENTER"),P("小計",align="CENTER"),P("備註",align="CENTER")]
    table_data   = [header]
    table_styles = [
        ("FONTNAME",(0,0),(-1,-1),FONT_NAME),("FONTSIZE",(0,0),(-1,-1),9),
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#DDDDDD")),
        ("BOX",(0,0),(-1,-1),0.5,colors.black),
        ("INNERGRID",(0,0),(-1,-1),0.5,colors.lightgrey),
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),("ALIGN",(2,0),(-1,-1),"CENTER"),
    ]

    row_idx  = 1
    item_seq = 1
    for g in groups:
        name = g["name"]
        rows = g["rows"]
        n    = len(rows)
        img_path_g = g.get("img","") or image_path or ""

        img_cell = ""
        if img_path_g and os.path.exists(img_path_g):
            try:
                img = Image(img_path_g)
                ih  = 35*mm
                iw  = ih * (img.imageWidth / img.imageHeight)
                if iw > col_w[1]-4*mm:
                    iw = col_w[1]-4*mm
                    ih = iw * (img.imageHeight / img.imageWidth)
                img._restrictSize(iw, ih)
                img_cell = img
            except Exception:
                img_cell = P(f"[圖片載入失敗]", size=7)

        for i, row in enumerate(rows):
            sub = calc_subtotal(row["qty"], row["price"])
            sub_str = f"{sub:,}" if isinstance(sub, int) else sub
            if i == 0:
                table_data.append([
                    P(str(item_seq),align="CENTER"),
                    img_cell if img_cell != "" else P(name,align="CENTER"),
                    P(row["qty"],align="CENTER"),P(row["price"],align="CENTER"),
                    P(sub_str,align="CENTER"),P(row["note"]),
                ])
            else:
                table_data.append([
                    P(""),P(name if i==n-1 else "",align="CENTER"),
                    P(row["qty"],align="CENTER"),P(row["price"],align="CENTER"),
                    P(sub_str,align="CENTER"),P(row["note"]),
                ])
        if n > 1:
            table_styles.append(("SPAN",(0,row_idx),(0,row_idx+n-1)))
            table_data[row_idx+n-1][1] = P(name,align="CENTER")
        row_idx  += n
        item_seq += 1

    while len(table_data) < 4:
        table_data.append(["","","","","",""])

    dt = Table(table_data, colWidths=col_w, repeatRows=1)
    dt.setStyle(TableStyle(table_styles))
    elements.append(dt)
    elements.append(Spacer(1,4*mm))

    for line in [COMPANY["tel"],COMPANY["fax"],COMPANY["email"],COMPANY["address"]]:
        elements.append(P(line, size=9))

    # 交易條件備註
    if remarks:
        elements.append(Spacer(1,3*mm))
        remarks_data = [[P("交易條件", align="CENTER"), P(remarks)]]
        remarks_table = Table(remarks_data, colWidths=[W*0.2, W*0.8])
        remarks_table.setStyle(TableStyle([
            ("FONTNAME",  (0,0), (-1,-1), FONT_NAME),
            ("FONTSIZE",  (0,0), (-1,-1), 9),
            ("BOX",       (0,0), (-1,-1), 0.5, colors.black),
            ("INNERGRID", (0,0), (-1,-1), 0.5, colors.lightgrey),
            ("BACKGROUND",(0,0), (0,-1),  colors.HexColor("#DDDDDD")),
            ("VALIGN",    (0,0), (-1,-1), "MIDDLE"),
            ("TOPPADDING",(0,0), (-1,-1), 4),
            ("BOTTOMPADDING",(0,0),(-1,-1), 4),
        ]))
        elements.append(remarks_table)

    elements.append(Spacer(1,6*mm))

    sign_t = Table([[P(f"承辦人：{COMPANY['handler']}",align="CENTER"), P("廠商回覆：")]],
                   colWidths=[W*0.4, W*0.6])
    sign_t.setStyle(TableStyle([
        ("FONTNAME",(0,0),(-1,-1),FONT_NAME),("FONTSIZE",(0,0),(-1,-1),9),
        ("BOX",(0,0),(-1,-1),0.5,colors.black),("INNERGRID",(0,0),(-1,-1),0.5,colors.lightgrey),
        ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6),
    ]))
    elements.append(sign_t)
    doc.build(elements)
