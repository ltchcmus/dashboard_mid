from __future__ import annotations

import pandas as pd


def dinh_dang_tien_te(gia_tri: float) -> str:
    if pd.isna(gia_tri):
        return "N/A"
    if gia_tri >= 1_000_000_000:
        return f"${gia_tri / 1_000_000_000:.2f} tỷ"
    if gia_tri >= 1_000_000:
        return f"${gia_tri / 1_000_000:.2f} triệu"
    return f"${gia_tri:,.0f}"
