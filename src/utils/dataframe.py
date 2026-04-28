from __future__ import annotations

import pandas as pd


def tach_cot_danh_sach(df: pd.DataFrame, cot: str, ten_moi: str) -> pd.DataFrame:
    temp = df[["show_id", cot]].copy()
    temp[cot] = (
        temp[cot]
        .fillna("")
        .astype(str)
        .str.replace(r"[\[\]']", "", regex=True)
        .str.replace('"', "", regex=False)
        .str.split(",")
    )
    temp = temp.explode(cot)
    temp[cot] = temp[cot].astype(str).str.strip()
    temp = temp.rename(columns={cot: ten_moi})
    temp = temp[temp[ten_moi].notna() & (temp[ten_moi] != "")]
    return temp.drop_duplicates()
