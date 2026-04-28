from __future__ import annotations

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

from src.config.app_config import AppConfig
from src.utils.ui import thong_bao_khong_co_du_lieu
from src.visualization.theme import ap_dung_giao_dien_plotly


def ve_tab_sang_tao(
    du_lieu: dict[str, pd.DataFrame],
    movies_loc: pd.DataFrame,
    config: AppConfig,
) -> None:
    colors = config.colors

    st.subheader("Góc nhìn sáng tạo")
    c1, c2 = st.columns(2)

    with c1:
        directors = du_lieu["directors_exploded"]
        director_df = directors[directors["show_id"].isin(movies_loc["show_id"])]
        director_stat = (
            director_df.merge(
                movies_loc[["show_id", "vote_average", "revenue"]],
                on="show_id",
                how="left",
            )
            .groupby("dao_dien", as_index=False)
            .agg(
                doanh_thu_trung_binh=("revenue", "mean"),
                diem_danh_gia_trung_binh=("vote_average", "mean"),
                so_phim=("show_id", "nunique"),
            )
        )
        director_stat = director_stat[
            (director_stat["so_phim"] >= 2)
            & (director_stat["doanh_thu_trung_binh"] > 0)
        ]
        if director_stat.empty:
            thong_bao_khong_co_du_lieu()
        else:
            fig_director = px.scatter(
                director_stat,
                x="doanh_thu_trung_binh",
                y="diem_danh_gia_trung_binh",
                size="so_phim",
                hover_name="dao_dien",
                title="Hiệu suất doanh thu và điểm số của đạo diễn",
                labels={
                    "doanh_thu_trung_binh": "Doanh thu trung bình",
                    "diem_danh_gia_trung_binh": "Điểm đánh giá trung bình",
                    "so_phim": "Số phim",
                    "dao_dien": "Đạo diễn",
                },
            )
            fig_director.update_traces(
                marker={"color": colors.netflix_gold, "opacity": 0.58}
            )
            x_data = director_stat["doanh_thu_trung_binh"].astype(float).to_numpy()
            y_data = director_stat["diem_danh_gia_trung_binh"].astype(float).to_numpy()
            if x_data.size >= 2:
                he_so = np.polyfit(np.log10(x_data), y_data, 1)
                x0, x1 = float(x_data.min()), float(x_data.max())
                y0 = float(he_so[0] * np.log10(x0) + he_so[1])
                y1 = float(he_so[0] * np.log10(x1) + he_so[1])
                fig_director.add_shape(
                    type="line",
                    x0=x0,
                    y0=y0,
                    x1=x1,
                    y1=y1,
                    xref="x",
                    yref="y",
                    layer="above",
                    line={"color": colors.netflix_red, "width": 5},
                )
                fig_director.add_annotation(
                    x=x1,
                    y=y1,
                    text="OLS",
                    showarrow=False,
                    xanchor="right",
                    yanchor="bottom",
                    font={"color": colors.netflix_red, "size": 11},
                    bgcolor="rgba(255,255,255,0.75)",
                )
            fig_director.update_xaxes(
                type="log", exponentformat="power", showexponent="all", dtick=1
            )
            st.plotly_chart(
                ap_dung_giao_dien_plotly(fig_director, config), width="stretch"
            )

    with c2:
        casts = du_lieu["casts_exploded"]
        cast_df = casts[casts["show_id"].isin(movies_loc["show_id"])]
        cast_stat = (
            cast_df.merge(movies_loc[["show_id", "revenue"]], on="show_id", how="left")
            .groupby("dien_vien", as_index=False)["revenue"]
            .sum()
            .rename(columns={"dien_vien": "Diễn viên", "revenue": "Tổng doanh thu"})
            .sort_values("Tổng doanh thu", ascending=False)
            .head(15)
            .sort_values("Tổng doanh thu", ascending=True)
        )
        if cast_stat.empty:
            thong_bao_khong_co_du_lieu()
        else:
            fig_cast = px.bar(
                cast_stat,
                x="Tổng doanh thu",
                y="Diễn viên",
                orientation="h",
                color="Tổng doanh thu",
                color_continuous_scale=config.palettes.seq_count,
                title="Top diễn viên mang lại doanh thu cao nhất",
            )
            st.plotly_chart(ap_dung_giao_dien_plotly(fig_cast, config), width="stretch")

    genre_mix_df = (
        movies_loc[["show_id", "genres", "popularity", "vote_average"]].dropna().copy()
    )
    if genre_mix_df.empty:
        thong_bao_khong_co_du_lieu()
    else:
        genre_mix_df["so_the_loai"] = (
            genre_mix_df["genres"]
            .astype(str)
            .apply(lambda text: len([g for g in text.split(",") if g.strip()]))
        )
        genre_mix_df = genre_mix_df[genre_mix_df["so_the_loai"] > 0]
        if genre_mix_df.empty:
            thong_bao_khong_co_du_lieu()
        else:
            genre_mix_df["nhom_so_the_loai"] = genre_mix_df["so_the_loai"].apply(
                lambda v: "4+" if v >= 4 else str(int(v))
            )
            thutu_nhom = ["1", "2", "3", "4+"]
            mix_stat = genre_mix_df.groupby("nhom_so_the_loai", as_index=False).agg(
                popularity_tb=("popularity", "mean"),
                diem_tb=("vote_average", "mean"),
                so_luong=("show_id", "nunique"),
            )
            mix_stat["nhom_so_the_loai"] = pd.Categorical(
                mix_stat["nhom_so_the_loai"], categories=thutu_nhom, ordered=True
            )
            mix_stat = mix_stat.sort_values("nhom_so_the_loai")
            diem_min = float(mix_stat["diem_tb"].min())
            diem_max = float(mix_stat["diem_tb"].max())
            diem_pad = max(0.15, (diem_max - diem_min) * 0.25)
            y2_min = max(0.0, diem_min - diem_pad)
            y2_max = min(10.0, diem_max + diem_pad)
            if y2_max <= y2_min:
                y2_min, y2_max = max(0.0, diem_min - 0.2), min(10.0, diem_max + 0.2)

            fig_mix = make_subplots(specs=[[{"secondary_y": True}]])
            fig_mix.add_trace(
                go.Bar(
                    x=mix_stat["nhom_so_the_loai"],
                    y=mix_stat["popularity_tb"],
                    name="Độ phổ biến trung bình",
                    marker={"color": colors.netflix_gold, "opacity": 0.72},
                    customdata=mix_stat[["so_luong"]],
                    hovertemplate=(
                        "Số thể loại: %{x}<br>Popularity TB: %{y:.2f}<br>Số phim: %{customdata[0]}<extra></extra>"
                    ),
                ),
                secondary_y=False,
            )
            fig_mix.add_trace(
                go.Scatter(
                    x=mix_stat["nhom_so_the_loai"],
                    y=mix_stat["diem_tb"],
                    name="Điểm đánh giá trung bình",
                    mode="lines+markers",
                    line={"color": colors.netflix_red, "width": 3},
                    marker={"color": colors.netflix_red, "size": 8},
                    hovertemplate="Số thể loại: %{x}<br>Điểm TB: %{y:.2f}<extra></extra>",
                ),
                secondary_y=True,
            )
            fig_mix.update_layout(
                title="Tác động của tính đa dạng thể loại đến thành công",
                xaxis_title="Số thể loại",
                barmode="group",
                margin={"t": 60, "l": 10, "r": 10, "b": 10},
                legend={
                    "x": 0.98,
                    "y": 1.02,
                    "xanchor": "right",
                    "yanchor": "bottom",
                    "bgcolor": "rgba(255,255,255,0.95)",
                    "bordercolor": "#E5E7EB",
                    "borderwidth": 1,
                    "font": {"color": colors.text_dark},
                    "title": {"font": {"color": colors.netflix_red}},
                },
            )
            fig_mix.update_xaxes(
                title="Số thể loại", tickfont={"color": colors.text_dark}
            )
            fig_mix.update_yaxes(
                title_text="Độ phổ biến trung bình",
                secondary_y=False,
                showgrid=True,
                gridcolor="#E5E7EB",
                griddash="dot",
                tickfont={"color": colors.text_dark},
                title_font={"color": colors.text_dark},
                rangemode="tozero",
            )
            fig_mix.update_yaxes(
                title_text="Điểm đánh giá trung bình",
                secondary_y=True,
                showgrid=False,
                tickfont={"color": colors.text_dark},
                title_font={"color": colors.text_dark},
                range=[y2_min, y2_max],
            )
            st.plotly_chart(ap_dung_giao_dien_plotly(fig_mix, config), width="stretch")
