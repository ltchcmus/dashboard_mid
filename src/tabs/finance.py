from __future__ import annotations

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

from src.config.app_config import AppConfig
from src.utils.ui import thong_bao_khong_co_du_lieu
from src.visualization.theme import ap_dung_giao_dien_plotly


def ve_tab_tai_chinh(
    movies_loc: pd.DataFrame, genres_loc: pd.DataFrame, config: AppConfig
) -> None:
    colors = config.colors
    palettes = config.palettes
    thresholds = config.thresholds

    st.subheader("Hiệu quả đầu tư")

    c1, c2 = st.columns(2)

    with c1:
        roi_df = movies_loc[
            (movies_loc["budget"] > thresholds.min_budget)
            & (movies_loc["revenue"] > thresholds.min_revenue)
        ].copy()
        roi_df["roi"] = np.where(
            (roi_df["budget"] > thresholds.min_budget)
            & (roi_df["revenue"] > thresholds.min_revenue),
            (roi_df["revenue"] - roi_df["budget"]) / roi_df["budget"],
            np.nan,
        )
        roi_top = roi_df.sort_values("roi", ascending=False).head(10)
        if roi_top.empty:
            thong_bao_khong_co_du_lieu()
        else:
            max_roi = float(roi_top["roi"].max())
            roi_top_hien_thi = roi_top.sort_values("roi", ascending=True).copy()
            fig_roi = px.bar(
                roi_top_hien_thi,
                x="roi",
                y="title",
                orientation="h",
                color="roi",
                custom_data=["budget", "revenue"],
                color_continuous_scale=palettes.diverge_quality,
                title="Top dự án có tỷ suất lợi nhuận (ROI) cao nhất",
                labels={"roi": "Tỷ lệ lợi nhuận (ROI)", "title": "Tên phim"},
            )
            fig_roi.update_traces(
                hovertemplate=(
                    "Tên phim=%{y}<br>"
                    "Tỷ lệ lợi nhuận (ROI)=%{x:.4f}<br>"
                    "Ngân sách=$%{customdata[0]:,.0f}<br>"
                    "Doanh thu=$%{customdata[1]:,.0f}"
                    "<extra></extra>"
                )
            )
            fig_roi.update_xaxes(
                type="linear",
                showgrid=True,
                gridcolor="#D1D5DB",
                griddash="dash",
                showline=True,
                linecolor=colors.text_dark,
                linewidth=1.2,
                zeroline=True,
                zerolinecolor="#D1D5DB",
                range=[0, max_roi * 1.15] if max_roi > 0 else None,
            )
            fig_roi.add_vline(
                x=max_roi, line_dash="dash", line_color=colors.netflix_red, line_width=2
            )
            fig_roi.add_annotation(
                x=max_roi,
                y=1,
                xref="x",
                yref="paper",
                text=f"ROI max: {max_roi:.2f}",
                showarrow=False,
                xanchor="left",
                yanchor="bottom",
                bgcolor="rgba(255,255,255,0.75)",
                font={"color": colors.netflix_red, "size": 11},
            )
            st.plotly_chart(ap_dung_giao_dien_plotly(fig_roi, config), width="stretch")

    with c2:
        budget_df = genres_loc.merge(
            movies_loc[["show_id", "release_year", "budget"]], on="show_id", how="left"
        )
        budget_df = budget_df[budget_df["budget"] > 0]
        if budget_df.empty:
            thong_bao_khong_co_du_lieu()
        else:
            top_genres = budget_df["the_loai"].value_counts().head(7).index.tolist()
            budget_df["nhom_the_loai"] = budget_df["the_loai"].apply(
                lambda val: val if val in top_genres else "Khác"
            )
            budget_year = (
                budget_df.groupby(["release_year", "nhom_the_loai"], as_index=False)[
                    "budget"
                ]
                .mean()
                .rename(
                    columns={
                        "release_year": "Năm",
                        "nhom_the_loai": "Thể loại",
                        "budget": "Ngân sách trung bình",
                    }
                )
            )

            thutu_the_loai_q8 = top_genres + ["Khác"]
            budget_year["Thể loại"] = pd.Categorical(
                budget_year["Thể loại"], categories=thutu_the_loai_q8, ordered=True
            )
            budget_year = budget_year.sort_values(["Thể loại", "Năm"])
            vivid_palette = palettes.vivid_genre[: len(thutu_the_loai_q8)]
            q8_color_map = {
                theloai: vivid_palette[idx % len(vivid_palette)]
                for idx, theloai in enumerate(thutu_the_loai_q8)
            }
            fig_line = px.line(
                budget_year,
                x="Năm",
                y="Ngân sách trung bình",
                color="Thể loại",
                color_discrete_map=q8_color_map,
                title="Xu hướng đầu tư ngân sách theo thời gian",
            )
            st.plotly_chart(ap_dung_giao_dien_plotly(fig_line, config), width="stretch")

    bubble_src = genres_loc.merge(
        movies_loc[["show_id", "budget", "revenue"]], on="show_id", how="left"
    )
    bubble_src = bubble_src[
        (bubble_src["budget"] > thresholds.min_budget)
        & (bubble_src["revenue"] > thresholds.min_revenue)
    ]
    if bubble_src.empty:
        thong_bao_khong_co_du_lieu()
    else:
        top_genres_q9 = (
            bubble_src.groupby("the_loai")["show_id"]
            .nunique()
            .sort_values(ascending=False)
            .head(8)
            .index.tolist()
        )
        bubble_src["nhom_the_loai"] = bubble_src["the_loai"].apply(
            lambda val: val if val in top_genres_q9 else "Khác"
        )
        bubble_df = (
            bubble_src.groupby("nhom_the_loai", as_index=False)
            .agg(
                ngan_sach_tb=("budget", "mean"),
                doanh_thu_tb=("revenue", "mean"),
                so_luong_phim=("show_id", "nunique"),
            )
            .rename(columns={"nhom_the_loai": "Nhóm thể loại"})
        )

        thutu_the_loai_q9 = top_genres_q9 + ["Khác"]
        bubble_df["Nhóm thể loại"] = pd.Categorical(
            bubble_df["Nhóm thể loại"], categories=thutu_the_loai_q9, ordered=True
        )
        bubble_df = bubble_df.sort_values("Nhóm thể loại")
        color_map = {
            theloai: palettes.vivid_genre[idx % len(palettes.vivid_genre)]
            for idx, theloai in enumerate(thutu_the_loai_q9)
        }

        fig_bubble = px.scatter(
            bubble_df,
            x="ngan_sach_tb",
            y="doanh_thu_tb",
            size="so_luong_phim",
            color="Nhóm thể loại",
            hover_data={
                "so_luong_phim": ":,.0f",
                "ngan_sach_tb": ":,.0f",
                "doanh_thu_tb": ":,.0f",
            },
            color_discrete_map=color_map,
            size_max=52,
            title="Tương quan giữa Ngân sách và Doanh thu theo thể loại",
            labels={
                "ngan_sach_tb": "Ngân sách trung bình",
                "doanh_thu_tb": "Doanh thu trung bình",
                "so_luong_phim": "Kích thước bong bóng (Số lượng phim)",
            },
        )
        x_min = float(bubble_df["ngan_sach_tb"].min())
        x_max = float(bubble_df["ngan_sach_tb"].max())
        y_min = float(bubble_df["doanh_thu_tb"].min())
        y_max = float(bubble_df["doanh_thu_tb"].max())
        x_pad = max((x_max - x_min) * 0.12, 1.0)
        y_pad = max((y_max - y_min) * 0.12, 1.0)
        x_range = [max(0.0, x_min - x_pad), x_max + x_pad]
        y_range = [max(0.0, y_min - y_pad), y_max + y_pad]
        visible_min = max(x_range[0], y_range[0])
        visible_max = min(x_range[1], y_range[1])

        fig_bubble.update_xaxes(
            title="Ngân sách trung bình",
            type="linear",
            range=x_range,
            showgrid=True,
            gridcolor="#E5E7EB",
            griddash="dot",
            showline=True,
            linecolor=colors.text_dark,
            linewidth=1.2,
            zeroline=False,
        )
        fig_bubble.update_yaxes(
            title="Doanh thu trung bình",
            type="linear",
            range=y_range,
            showgrid=True,
            gridcolor="#E5E7EB",
            griddash="dot",
            showline=True,
            linecolor=colors.text_dark,
            linewidth=1.2,
            zeroline=False,
        )
        fig_bubble.add_shape(
            type="line",
            x0=visible_min,
            y0=visible_min,
            x1=visible_max,
            y1=visible_max,
            line={"color": colors.netflix_red, "dash": "dash", "width": 2},
        )
        fig_bubble.add_annotation(
            x=visible_max,
            y=visible_max,
            text="Đường hòa vốn: Doanh thu = Ngân sách",
            showarrow=False,
            xanchor="right",
            yanchor="bottom",
            bgcolor="rgba(255,255,255,0.75)",
            font={"color": colors.text_dark, "size": 10},
        )
        fig_bubble.update_layout(height=680)
        st.plotly_chart(ap_dung_giao_dien_plotly(fig_bubble, config), width="stretch")
        st.caption(
            "Kích thước bong bóng biểu diễn số lượng phim trong từng nhóm thể loại."
        )
