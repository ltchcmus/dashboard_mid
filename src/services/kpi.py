from __future__ import annotations

import numpy as np
import pandas as pd
import streamlit as st

from src.config.app_config import AppConfig
from src.utils.formatting import dinh_dang_tien_te


def hien_thi_kpi(
    movies_loc: pd.DataFrame, genres_loc: pd.DataFrame, config: AppConfig
) -> None:
    thresholds = config.thresholds
    tong_doanh_thu = movies_loc["revenue"].fillna(0).sum()
    diem_trung_binh = movies_loc["vote_average"].mean()

    if not genres_loc.empty:
        top_genre = genres_loc["the_loai"].value_counts().index[0]
    else:
        top_genre = "N/A"

    roi = movies_loc[
        (movies_loc["budget"] > thresholds.min_budget)
        & (movies_loc["revenue"] > thresholds.min_revenue)
    ].copy()
    roi["roi"] = np.where(
        (roi["budget"] > thresholds.min_budget)
        & (roi["revenue"] > thresholds.min_revenue),
        (roi["revenue"] - roi["budget"]) / roi["budget"],
        np.nan,
    )
    roi_tb = roi["roi"].mean()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Tổng doanh thu", dinh_dang_tien_te(tong_doanh_thu))
    c2.metric(
        "Điểm đánh giá trung bình",
        f"{diem_trung_binh:.2f}" if pd.notna(diem_trung_binh) else "N/A",
    )
    c3.metric("Thể loại phổ biến nhất", top_genre)
    c4.metric(
        "Tỷ suất lợi nhuận trung bình (ROI)",
        f"{roi_tb:.1%}" if pd.notna(roi_tb) else "N/A",
    )
