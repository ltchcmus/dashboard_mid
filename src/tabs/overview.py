from __future__ import annotations

import math

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from src.config.app_config import AppConfig
from src.services.filter_state import (
    dong_bo_loc_tuong_tac_tu_tab1,
    trich_gia_tri_tu_su_kien_plotly,
)
from src.visualization.theme import ap_dung_giao_dien_plotly


def ve_tab_toan_canh(
    du_lieu: dict[str, pd.DataFrame],
    movies_loc: pd.DataFrame,
    genres_loc: pd.DataFrame,
    config: AppConfig,
) -> None:
    colors = config.colors
    palettes = config.palettes

    st.subheader("Toàn cảnh Netflix toàn cầu")

    movies_map = du_lieu["movies"].copy()
    genres_all = du_lieu["genres_exploded"]
    countries = du_lieu["countries"]
    khoang_nam = st.session_state.get(
        "khoang_nam_chon",
        (int(movies_map["release_year"].min()), int(movies_map["release_year"].max())),
    )
    movies_map = movies_map[
        movies_map["release_year"].between(
            khoang_nam[0], khoang_nam[1], inclusive="both"
        )
    ]

    ngon_ngu_chon = st.session_state.get("ngon_ngu_chon", [])
    if ngon_ngu_chon:
        movies_map = movies_map[movies_map["language_name"].isin(ngon_ngu_chon)]

    the_loai_chon = st.session_state.get("the_loai_chon", [])
    if the_loai_chon:
        show_ids_the_loai = genres_all[genres_all["the_loai"].isin(the_loai_chon)][
            "show_id"
        ].unique()
        movies_map = movies_map[movies_map["show_id"].isin(show_ids_the_loai)]

    countries_loc = countries[countries["show_id"].isin(movies_map["show_id"])]
    qg_dem = (
        countries_loc.groupby(["country_name_en", "country_name"], as_index=False)[
            "show_id"
        ]
        .nunique()
        .rename(
            columns={
                "country_name_en": "Quốc gia (EN)",
                "country_name": "Quốc gia",
                "show_id": "Số lượng phim",
            }
        )
    )
    countries_chon = st.session_state.get("quoc_gia_chon", [])
    gia_tri_qg = None

    if qg_dem.empty:
        st.info("Không có dữ liệu quốc gia sau khi lọc.")
    else:
        qg_dem["Số lượng phim (log10)"] = qg_dem["Số lượng phim"].apply(
            lambda v: math.log10(v)
        )
        if countries_chon:
            qg_dem["gia_tri_mau"] = -1.0
            selected_mask = qg_dem["Quốc gia"].isin(countries_chon)
            qg_dem.loc[selected_mask, "gia_tri_mau"] = qg_dem.loc[
                selected_mask, "Số lượng phim (log10)"
            ]
            selected_vals = qg_dem.loc[selected_mask, "gia_tri_mau"]
            color_min = -1.0
            color_max = float(selected_vals.max()) if not selected_vals.empty else 1.0
            if color_max <= color_min:
                color_max = color_min + 1.0

            fig_map = px.choropleth(
                qg_dem,
                locations="Quốc gia (EN)",
                locationmode="country names",
                hover_name="Quốc gia",
                color="gia_tri_mau",
                custom_data=["Quốc gia"],
                color_continuous_scale=[
                    [0.00, "#E5E7EB"],
                    [0.22, "#FEE2E2"],
                    [0.60, "#EF4444"],
                    [1.00, "#80060B"],
                ],
                range_color=[color_min, color_max],
                title="Phân bố phim theo quốc gia",
                hover_data={
                    "Quốc gia (EN)": False,
                    "Số lượng phim": True,
                    "gia_tri_mau": False,
                },
            )
            fig_map.update_coloraxes(showscale=False)
        else:
            log_min = int(qg_dem["Số lượng phim (log10)"].min())
            log_max = int(math.ceil(qg_dem["Số lượng phim (log10)"].max()))
            tick_vals = list(range(log_min, log_max + 1))
            tick_text = [f"{10 ** p:,}" for p in tick_vals]

            fig_map = px.choropleth(
                qg_dem,
                locations="Quốc gia (EN)",
                locationmode="country names",
                hover_name="Quốc gia",
                color="Số lượng phim (log10)",
                custom_data=["Quốc gia"],
                color_continuous_scale=palettes.seq_count,
                title="Phân bố phim theo quốc gia",
                hover_data={
                    "Quốc gia (EN)": False,
                    "Số lượng phim": True,
                    "Số lượng phim (log10)": False,
                },
            )
            fig_map.update_coloraxes(
                colorbar_title="Số lượng phim",
                colorbar_tickvals=tick_vals,
                colorbar_ticktext=tick_text,
            )
        fig_map.update_geos(
            bgcolor=colors.chart_bg,
            showcoastlines=False,
            showframe=False,
            projection_scale=1.12,
        )
        fig_map.update_layout(margin={"t": 48, "l": 0, "r": 0, "b": 0}, height=760)
        map_key_suffix = abs(
            hash(tuple(sorted(st.session_state.get("quoc_gia_chon", []))))
        )
        su_kien_map = st.plotly_chart(
            ap_dung_giao_dien_plotly(fig_map, config),
            width="stretch",
            key=f"chart_map_quoc_gia_{map_key_suffix}",
            on_select="rerun",
        )
        gia_tri_qg = trich_gia_tri_tu_su_kien_plotly(su_kien_map, ["customdata"])

    c1, c2 = st.columns(2)

    with c1:
        gia_tri_lang = None
        movies_lang = du_lieu["movies"].copy()
        movies_lang = movies_lang[
            movies_lang["release_year"].between(
                khoang_nam[0], khoang_nam[1], inclusive="both"
            )
        ]
        quoc_gia_chon = st.session_state.get("quoc_gia_chon", [])
        if quoc_gia_chon:
            show_ids_qg = countries[countries["country_name"].isin(quoc_gia_chon)][
                "show_id"
            ].unique()
            movies_lang = movies_lang[movies_lang["show_id"].isin(show_ids_qg)]

        if the_loai_chon:
            show_ids_the_loai = genres_all[genres_all["the_loai"].isin(the_loai_chon)][
                "show_id"
            ].unique()
            movies_lang = movies_lang[movies_lang["show_id"].isin(show_ids_the_loai)]

        ngon_ngu = (
            movies_lang.groupby("language_name", as_index=False)["show_id"]
            .nunique()
            .rename(columns={"language_name": "Ngôn ngữ", "show_id": "Số lượng phim"})
        )
        if ngon_ngu.empty:
            st.info("Không có dữ liệu ngôn ngữ sau khi lọc.")
        else:
            ngon_ngu["Số lượng phim (log10)"] = ngon_ngu["Số lượng phim"].apply(
                lambda v: math.log10(v)
            )
            log_min_lang = int(ngon_ngu["Số lượng phim (log10)"].min())
            log_max_lang = int(math.ceil(ngon_ngu["Số lượng phim (log10)"].max()))
            tick_vals_lang = list(range(log_min_lang, log_max_lang + 1))
            tick_text_lang = [f"{10 ** p:,}" for p in tick_vals_lang]

            fig_tree = px.treemap(
                ngon_ngu,
                path=["Ngôn ngữ"],
                values="Số lượng phim",
                color="Số lượng phim (log10)",
                custom_data=["Ngôn ngữ"],
                color_continuous_scale=palettes.seq_count,
                title="Tỉ trọng phim theo ngôn ngữ hiển thị",
                hover_data={"Số lượng phim": True, "Số lượng phim (log10)": False},
            )
            fig_tree.update_traces(
                maxdepth=1, pathbar={"visible": False}, root_color=colors.chart_bg
            )
            fig_tree.update_coloraxes(
                colorbar_title="Số lượng phim",
                colorbar_tickvals=tick_vals_lang,
                colorbar_ticktext=tick_text_lang,
            )
            fig_tree.update_layout(margin={"t": 60, "l": 0, "r": 0, "b": 0}, height=420)
            lang_key_suffix = abs(
                hash(tuple(sorted(st.session_state.get("ngon_ngu_chon", []))))
            )
            su_kien_lang = st.plotly_chart(
                ap_dung_giao_dien_plotly(fig_tree, config),
                width="stretch",
                key=f"chart_tree_ngon_ngu_{lang_key_suffix}",
                on_select="rerun",
            )
            gia_tri_lang = trich_gia_tri_tu_su_kien_plotly(
                su_kien_lang, ["customdata", "label", "id"]
            )

    with c2:
        gia_tri_genre = None
        the_loai_dem = (
            genres_loc.groupby("the_loai", as_index=False)["show_id"]
            .nunique()
            .rename(columns={"the_loai": "Thể loại", "show_id": "Số lượng phim"})
            .sort_values("Số lượng phim", ascending=True)
            .tail(15)
        )
        if the_loai_dem.empty:
            st.info("Không có dữ liệu thể loại sau khi lọc.")
        else:
            fig_bar = px.bar(
                the_loai_dem,
                x="Số lượng phim",
                y="Thể loại",
                orientation="h",
                title="Số lượng phim theo thể loại",
                color="Số lượng phim",
                custom_data=["Thể loại"],
                color_continuous_scale=palettes.seq_count,
            )
            fig_bar.update_layout(
                yaxis_title="Thể loại", xaxis_title="Số lượng phim", height=420
            )
            su_kien_genre = st.plotly_chart(
                ap_dung_giao_dien_plotly(fig_bar, config),
                width="stretch",
                key="chart_bar_the_loai",
                on_select="rerun",
            )
            gia_tri_genre = trich_gia_tri_tu_su_kien_plotly(
                su_kien_genre, ["customdata", "y"]
            )

    st.markdown("### Xu hướng số lượng phim theo thể loại")
    trend_src = genres_loc.merge(
        movies_loc[["show_id", "release_year"]], on="show_id", how="left"
    ).dropna(subset=["release_year"])
    if trend_src.empty:
        st.info("Không có dữ liệu xu hướng theo năm sau khi lọc.")
    else:
        trend_base = trend_src.copy()
        genre_counts = trend_base["the_loai"].value_counts()
        unique_genres = int(genre_counts.shape[0])
        if unique_genres == 0:
            st.info("Không có dữ liệu thể loại sau khi lọc.")
        else:
            max_n = min(10, unique_genres)
            if max_n >= 3:
                options = list(range(3, max_n + 1))
            else:
                options = list(range(1, max_n + 1))
            default_n = 6 if 6 in options else options[-1]
            control_1, control_2, control_3 = st.columns([1.6, 1, 1])
            with control_1:
                top_n = st.selectbox(
                    "Số thể loại hiển thị",
                    options=options,
                    index=options.index(default_n),
                )
            with control_2:
                gom_khac = st.checkbox(
                    "Gộp phần còn lại",
                    value=unique_genres > top_n,
                )
            with control_3:
                hien_tong = st.checkbox("Hiển thị tổng số phim", value=True)

            top_genres = genre_counts.head(top_n).index.tolist()
            if gom_khac and unique_genres > top_n:
                trend_src = trend_src.assign(
                    nhom_the_loai=trend_src["the_loai"].apply(
                        lambda val: val if val in top_genres else "Khác"
                    )
                )
                group_col = "nhom_the_loai"
                nhom_hien_thi = top_genres + ["Khác"]
            else:
                trend_src = trend_src[trend_src["the_loai"].isin(top_genres)]
                group_col = "the_loai"
                nhom_hien_thi = top_genres

            trend = (
                trend_src.groupby(["release_year", group_col], as_index=False)[
                    "show_id"
                ]
                .nunique()
                .rename(
                    columns={
                        "release_year": "Năm",
                        group_col: "Thể loại",
                        "show_id": "Số lượng phim",
                    }
                )
            )
            trend["Năm"] = trend["Năm"].astype(int)
            trend["Thể loại"] = pd.Categorical(
                trend["Thể loại"], categories=nhom_hien_thi, ordered=True
            )
            trend = trend.sort_values(["Thể loại", "Năm"])
            color_map = {}
            for idx, theloai in enumerate(nhom_hien_thi):
                if theloai == "Khác":
                    color_map[theloai] = colors.neutral_grey
                else:
                    color_map[theloai] = palettes.vivid_genre[
                        idx % len(palettes.vivid_genre)
                    ]

            fig_trend = px.line(
                trend,
                x="Năm",
                y="Số lượng phim",
                color="Thể loại",
                markers=True,
                color_discrete_map=color_map,
                title="Số lượng phim theo thể loại qua các năm",
            )
            if hien_tong:
                total = (
                    trend_base.groupby("release_year", as_index=False)["show_id"]
                    .nunique()
                    .rename(
                        columns={
                            "release_year": "Năm",
                            "show_id": "Tổng số phim",
                        }
                    )
                )
                fig_trend.add_trace(
                    go.Scatter(
                        x=total["Năm"],
                        y=total["Tổng số phim"],
                        mode="lines+markers",
                        name="Tổng số phim",
                        line={"color": colors.text_dark, "dash": "dash", "width": 2},
                        marker={"color": colors.text_dark, "size": 6},
                    )
                )
            fig_trend.update_layout(height=480, legend_title_text="Thể loại")
            st.plotly_chart(
                ap_dung_giao_dien_plotly(fig_trend, config), width="stretch"
            )
            caption_suffix = (
                " (gộp phần còn lại)" if gom_khac and unique_genres > top_n else ""
            )
            st.caption(
                f"Top {top_n} thể loại theo số lượng phim trong bộ lọc hiện tại{caption_suffix}."
            )

    dong_bo_loc_tuong_tac_tu_tab1(gia_tri_qg, gia_tri_lang, gia_tri_genre)
