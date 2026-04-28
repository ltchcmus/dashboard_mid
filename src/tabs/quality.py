from __future__ import annotations

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from src.config.app_config import AppConfig
from src.utils.ui import thong_bao_khong_co_du_lieu
from src.visualization.theme import ap_dung_giao_dien_plotly


def ve_tab_chat_luong(
    movies_loc: pd.DataFrame, genres_loc: pd.DataFrame, config: AppConfig
) -> None:
    colors = config.colors
    palettes = config.palettes
    thresholds = config.thresholds
    nguong_chat_luong = thresholds.high_quality_vote

    st.subheader("Chất lượng và chiến lược nội dung")

    q4_donut_col, q4_bar_col = st.columns([4, 6])
    q4_df = movies_loc[
        ["show_id", "vote_average", "popularity", "budget", "revenue"]
    ].copy()
    q4_df = q4_df.dropna(subset=["show_id", "vote_average"])
    if q4_df.empty:
        with q4_donut_col:
            thong_bao_khong_co_du_lieu()
        with q4_bar_col:
            thong_bao_khong_co_du_lieu()
    else:
        bins = [0, 5, 6, 7, 8, 10]
        labels = ["Kém (0-5)", "TB (5-6)", "Khá (6-7)", "Tốt (7-8)", "Xuất sắc (8-10)"]
        donut_order = [
            "Xuất sắc (8-10)",
            "Tốt (7-8)",
            "Khá (6-7)",
            "TB (5-6)",
            "Kém (0-5)",
        ]
        q4_df["rating_bucket"] = pd.cut(
            q4_df["vote_average"],
            bins=bins,
            labels=labels,
            include_lowest=True,
        )

        donut_data = (
            q4_df["rating_bucket"]
            .value_counts(dropna=False)
            .reindex(donut_order, fill_value=0)
            .rename_axis("Nhóm chất lượng")
            .reset_index(name="Số lượng phim")
        )
        donut_data["Số lượng phim"] = pd.to_numeric(
            donut_data["Số lượng phim"], errors="coerce"
        ).fillna(0)
        donut_data = donut_data[donut_data["Số lượng phim"] > 0]

        high_quality_ids = q4_df[q4_df["vote_average"] >= nguong_chat_luong][
            "show_id"
        ].unique()
        hq_genres = genres_loc[genres_loc["show_id"].isin(high_quality_ids)].copy()
        hq_detail = hq_genres.merge(
            q4_df[["show_id", "popularity", "budget", "revenue"]],
            on="show_id",
            how="left",
        )
        hq_detail["roi"] = np.where(
            (hq_detail["budget"] > thresholds.min_budget)
            & (hq_detail["revenue"] > thresholds.min_revenue),
            (hq_detail["revenue"] - hq_detail["budget"]) / hq_detail["budget"],
            np.nan,
        )
        bar_data = (
            hq_detail.groupby("the_loai", as_index=False)
            .agg(
                so_luong_phim=("show_id", "nunique"),
                avg_popularity=("popularity", "mean"),
                avg_roi=("roi", "mean"),
            )
            .sort_values("so_luong_phim", ascending=False)
            .head(10)
            .sort_values("so_luong_phim", ascending=True)
        )

        with q4_donut_col:
            if donut_data.empty:
                thong_bao_khong_co_du_lieu()
            else:
                fig_donut = px.pie(
                    donut_data,
                    values="Số lượng phim",
                    names="Nhóm chất lượng",
                    hole=0.62,
                    color="Nhóm chất lượng",
                    color_discrete_map=config.quality_bucket_colors,
                    category_orders={"Nhóm chất lượng": donut_order},
                    title="Phân bố điểm xếp hạng của phim",
                )
                fig_donut.update_traces(
                    textposition="outside",
                    textinfo="percent+label",
                    sort=False,
                    automargin=True,
                )
                fig_donut.update_layout(uniformtext_minsize=11, uniformtext_mode="hide")
                st.plotly_chart(
                    ap_dung_giao_dien_plotly(fig_donut, config), width="stretch"
                )

        with q4_bar_col:
            if bar_data.empty:
                thong_bao_khong_co_du_lieu()
            else:
                fig_hq_bar = px.bar(
                    bar_data,
                    x="so_luong_phim",
                    y="the_loai",
                    orientation="h",
                    color="avg_popularity",
                    color_continuous_scale=palettes.diverge_quality,
                    title=f"Top thể loại được duy trì chất lượng (Điểm >= {nguong_chat_luong:g})",
                    labels={
                        "so_luong_phim": "Số lượng phim chất lượng cao",
                        "the_loai": "Thể loại",
                        "avg_popularity": "Độ phổ biến TB",
                    },
                    custom_data=["avg_popularity", "avg_roi"],
                )
                fig_hq_bar.update_traces(
                    hovertemplate=(
                        "Thể loại: %{y}<br>Số phim chất lượng cao: %{x}<br>"
                        "Độ phổ biến TB: %{customdata[0]:.2f}<br>ROI TB: %{customdata[1]:.2f}<extra></extra>"
                    )
                )
                st.plotly_chart(
                    ap_dung_giao_dien_plotly(fig_hq_bar, config), width="stretch"
                )

    q6_col, q5_col = st.columns([6, 4])

    with q5_col:
        hist_df = (
            movies_loc[["show_id", "budget", "vote_average", "revenue"]].dropna().copy()
        )
        hist_df = hist_df[
            (hist_df["budget"] > thresholds.min_budget)
            & (hist_df["revenue"] > thresholds.min_revenue)
        ]
        if hist_df.empty:
            thong_bao_khong_co_du_lieu()
        else:
            budget_rank = hist_df["budget"].rank(method="first")
            so_nhom_muc_tieu = min(4, int(budget_rank.nunique()))
            if so_nhom_muc_tieu < 2:
                hist_df["Nhóm ngân sách (tứ phân vị)"] = "Q1 (Thấp)"
            else:
                ma_phan_vi = pd.qcut(
                    budget_rank,
                    q=so_nhom_muc_tieu,
                    labels=False,
                    duplicates="drop",
                )
                if ma_phan_vi.isna().all():
                    hist_df["Nhóm ngân sách (tứ phân vị)"] = "Q1 (Thấp)"
                else:
                    so_nhom_ngan_sach = int(ma_phan_vi.max()) + 1
                    nhan_phan_vi = ["Q1 (Thấp)", "Q2", "Q3", "Q4 (Cao)"]
                    hist_df["Nhóm ngân sách (tứ phân vị)"] = ma_phan_vi.map(
                        {i: nhan_phan_vi[i] for i in range(so_nhom_ngan_sach)}
                    )
            hist_df["Nhóm điểm số"] = pd.cut(
                hist_df["vote_average"],
                bins=[-np.inf, 6, thresholds.high_quality_vote, np.inf],
                labels=[
                    "<6",
                    f"6-{thresholds.high_quality_vote:g}",
                    f">{thresholds.high_quality_vote:g}",
                ],
            )
            agg = hist_df.groupby(
                ["Nhóm ngân sách (tứ phân vị)", "Nhóm điểm số"],
                observed=True,
                as_index=False,
            ).agg(So_luong=("show_id", "nunique"))
            fig_hist = px.density_heatmap(
                agg,
                x="Nhóm ngân sách (tứ phân vị)",
                y="Nhóm điểm số",
                z="So_luong",
                histfunc="sum",
                text_auto=True,
                color_continuous_scale=palettes.seq_count,
                title="Phân bố số lượng phim theo điểm số và ngân sách",
                labels={
                    "Nhóm ngân sách (tứ phân vị)": "Nhóm ngân sách (tứ phân vị)",
                    "Nhóm điểm số": "Nhóm điểm số",
                    "So_luong": "Tổng số phim",
                },
                hover_data={"So_luong": True},
            )
            fig_hist.update_coloraxes(colorbar_title_text="Tổng số phim")
            st.plotly_chart(ap_dung_giao_dien_plotly(fig_hist, config), width="stretch")

    with q6_col:
        err_df = genres_loc.merge(
            movies_loc[["show_id", "vote_average"]], on="show_id", how="left"
        ).dropna(subset=["vote_average"])
        if err_df.empty:
            thong_bao_khong_co_du_lieu()
        else:
            genre_stat = (
                err_df.groupby("the_loai", as_index=False)["vote_average"]
                .agg(diem_trung_binh="mean", do_lech_chuan="std", so_luong="count")
                .fillna({"do_lech_chuan": 0})
                .sort_values("diem_trung_binh", ascending=False)
                .head(15)
                .sort_values("diem_trung_binh", ascending=True)
            )
            genre_stat["phuong_sai"] = genre_stat["do_lech_chuan"] ** 2
            fig_err = go.Figure(
                go.Bar(
                    x=genre_stat["diem_trung_binh"],
                    y=genre_stat["the_loai"],
                    orientation="h",
                    error_x={
                        "type": "data",
                        "array": genre_stat["do_lech_chuan"],
                        "visible": True,
                    },
                    marker={
                        "color": genre_stat["phuong_sai"],
                        "colorscale": palettes.diverge_quality,
                        "showscale": True,
                        "colorbar": {"title": "Phương sai"},
                    },
                    hovertemplate=(
                        "Thể loại: %{y}<br>Điểm TB: %{x:.2f}<br>Độ lệch chuẩn: %{error_x.array:.2f}"
                        "<br>Phương sai: %{customdata[0]:.3f}<br>Số phim: %{customdata[1]}<extra></extra>"
                    ),
                    customdata=genre_stat[["phuong_sai", "so_luong"]],
                )
            )
            fig_err.update_layout(
                title="Top thể loại có điểm đánh giá ổn định nhất",
                xaxis_title="Điểm đánh giá trung bình",
                yaxis_title="Thể loại",
            )
            st.plotly_chart(ap_dung_giao_dien_plotly(fig_err, config), width="stretch")
