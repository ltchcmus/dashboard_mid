from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st

from src.config.app_config import AppConfig
from src.utils.dataframe import tach_cot_danh_sach
from src.utils.i18n import TranslationService


@st.cache_data(show_spinner=False)
def tai_du_lieu(config: AppConfig) -> dict[str, pd.DataFrame]:
    data_dir = Path(config.data_dir)
    tep_can_doc = {
        "movies": "movies.csv",
        "countries": "movie_countries.csv",
    }
    du_lieu: dict[str, pd.DataFrame] = {}
    for key, file_name in tep_can_doc.items():
        path = data_dir / file_name
        if not path.exists():
            raise FileNotFoundError(f"Không tìm thấy tệp dữ liệu: {path}")
        du_lieu[key] = pd.read_csv(path)

    du_lieu["movies"]["release_year"] = pd.to_numeric(
        du_lieu["movies"]["release_year"], errors="coerce"
    )
    du_lieu["movies"]["vote_average"] = pd.to_numeric(
        du_lieu["movies"]["vote_average"], errors="coerce"
    )
    du_lieu["movies"]["popularity"] = pd.to_numeric(
        du_lieu["movies"]["popularity"], errors="coerce"
    )
    du_lieu["movies"]["vote_count"] = pd.to_numeric(
        du_lieu["movies"]["vote_count"], errors="coerce"
    )
    du_lieu["movies"]["budget"] = pd.to_numeric(
        du_lieu["movies"]["budget"], errors="coerce"
    )
    du_lieu["movies"]["revenue"] = pd.to_numeric(
        du_lieu["movies"]["revenue"], errors="coerce"
    )

    translator = TranslationService.from_config(config)

    movies = du_lieu["movies"]
    movies["language_name_en"] = movies["language_name"]
    movies["language_name"] = [
        translator.viet_hoa_ngon_ngu(ma, ten)
        for ma, ten in zip(movies["language_code"], movies["language_name_en"])
    ]
    du_lieu["movies"] = movies

    countries = du_lieu["countries"].copy()
    countries["country_name_en"] = countries["country_name"].astype(str).str.strip()
    countries["country_name"] = countries["country_name_en"].apply(
        translator.viet_hoa_quoc_gia
    )
    du_lieu["countries"] = countries

    du_lieu["genres_exploded"] = tach_cot_danh_sach(
        du_lieu["movies"], "genres", "the_loai"
    )
    du_lieu["genres_exploded"]["the_loai"] = du_lieu["genres_exploded"][
        "the_loai"
    ].apply(translator.viet_hoa_the_loai)
    du_lieu["casts_exploded"] = tach_cot_danh_sach(
        du_lieu["movies"], "cast", "dien_vien"
    )
    du_lieu["directors_exploded"] = tach_cot_danh_sach(
        du_lieu["movies"], "director", "dao_dien"
    )
    return du_lieu
