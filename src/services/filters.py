from __future__ import annotations

import pandas as pd
import streamlit as st

from src.services.filter_state import ap_dung_pending_filter_updates


def ap_dung_loc_tuong_tac(
    du_lieu: dict[str, pd.DataFrame],
    movies_base: pd.DataFrame,
    genres_base: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    movies_loc = movies_base.copy()

    countries_chon = st.session_state.get("quoc_gia_chon", [])
    if countries_chon:
        show_ids_qg = du_lieu["countries"][
            du_lieu["countries"]["country_name"].isin(countries_chon)
        ]["show_id"].unique()
        movies_loc = movies_loc[movies_loc["show_id"].isin(show_ids_qg)]

    languages_chon = st.session_state.get("ngon_ngu_chon", [])
    if languages_chon:
        movies_loc = movies_loc[movies_loc["language_name"].isin(languages_chon)]

    genres_chon = st.session_state.get("the_loai_chon", [])
    if genres_chon:
        show_ids_genre = du_lieu["genres_exploded"][
            du_lieu["genres_exploded"]["the_loai"].isin(genres_chon)
        ]["show_id"].unique()
        movies_loc = movies_loc[movies_loc["show_id"].isin(show_ids_genre)]

    genres_loc = genres_base[genres_base["show_id"].isin(movies_loc["show_id"])]
    return movies_loc, genres_loc


def bo_loc_toan_cuc(
    du_lieu: dict[str, pd.DataFrame],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    movies = du_lieu["movies"].copy()
    genres_exploded = du_lieu["genres_exploded"]
    countries = du_lieu["countries"]
    ap_dung_pending_filter_updates()

    nam_min = int(movies["release_year"].min())
    nam_max = int(movies["release_year"].max())

    st.sidebar.header("Bộ lọc hệ thống")
    if "khoang_nam_chon" not in st.session_state:
        st.session_state["khoang_nam_chon"] = (nam_min, nam_max)

    khoang_nam = st.sidebar.slider(
        "Năm phát hành",
        min_value=nam_min,
        max_value=nam_max,
        key="khoang_nam_chon",
    )

    danh_sach_quoc_gia = sorted(countries["country_name"].dropna().unique().tolist())
    st.sidebar.multiselect(
        "Quốc gia",
        options=danh_sach_quoc_gia,
        key="quoc_gia_chon",
        placeholder="Chọn quốc gia",
    )

    danh_sach_the_loai = sorted(genres_exploded["the_loai"].dropna().unique().tolist())
    st.sidebar.multiselect(
        "Thể loại",
        options=danh_sach_the_loai,
        key="the_loai_chon",
        placeholder="Chọn thể loại",
    )

    danh_sach_ngon_ngu = sorted(movies["language_name"].dropna().unique().tolist())
    st.sidebar.multiselect(
        "Ngôn ngữ",
        options=danh_sach_ngon_ngu,
        key="ngon_ngu_chon",
        placeholder="Chọn ngôn ngữ",
    )

    if st.sidebar.button("Xóa tất cả bộ lọc", use_container_width=True):
        st.session_state["pending_filter_updates"] = {
            "quoc_gia_chon": [],
            "the_loai_chon": [],
            "ngon_ngu_chon": [],
            "khoang_nam_chon": (nam_min, nam_max),
        }
        st.session_state["chart_event_signature"] = {
            "quoc_gia_chon": None,
            "ngon_ngu_chon": None,
            "the_loai_chon": None,
        }
        st.session_state["chart_event_skip_once"] = {
            "quoc_gia_chon": False,
            "ngon_ngu_chon": False,
            "the_loai_chon": False,
        }
        st.rerun()

    quoc_gia_chon = st.session_state.get("quoc_gia_chon", [])
    the_loai_chon = st.session_state.get("the_loai_chon", [])
    ngon_ngu_chon = st.session_state.get("ngon_ngu_chon", [])

    loc_theo_nam = movies[
        movies["release_year"].between(khoang_nam[0], khoang_nam[1], inclusive="both")
    ]

    if quoc_gia_chon:
        show_ids_quoc_gia = countries[countries["country_name"].isin(quoc_gia_chon)][
            "show_id"
        ].unique()
        loc_theo_nam = loc_theo_nam[loc_theo_nam["show_id"].isin(show_ids_quoc_gia)]

    if ngon_ngu_chon:
        loc_theo_nam = loc_theo_nam[loc_theo_nam["language_name"].isin(ngon_ngu_chon)]

    if the_loai_chon:
        show_ids_the_loai = genres_exploded[
            genres_exploded["the_loai"].isin(the_loai_chon)
        ]["show_id"].unique()
        loc_theo_nam = loc_theo_nam[loc_theo_nam["show_id"].isin(show_ids_the_loai)]

    genres_loc = genres_exploded[
        genres_exploded["show_id"].isin(loc_theo_nam["show_id"])
    ]
    return loc_theo_nam, genres_loc
