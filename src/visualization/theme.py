from __future__ import annotations

from src.config.app_config import AppConfig


def ap_dung_giao_dien_plotly(fig, config: AppConfig):
    colors = config.colors
    fig.update_layout(
        template="plotly_white",
        paper_bgcolor=colors.chart_bg,
        plot_bgcolor=colors.chart_bg,
        font={"family": config.font_family, "size": 13, "color": colors.text_dark},
        title={
            "font": {"color": colors.netflix_red, "size": 20},
            "x": 0.5,
            "xanchor": "center",
        },
        clickmode="event+select",
        legend={
            "font": {"color": colors.text_dark, "size": 13},
            "title": {"font": {"color": colors.text_dark, "size": 13}},
        },
        xaxis={
            "tickfont": {"color": colors.text_dark, "size": 12},
            "title": {"font": {"color": colors.text_dark, "size": 13}},
        },
        yaxis={
            "tickfont": {"color": colors.text_dark, "size": 12},
            "title": {"font": {"color": colors.text_dark, "size": 13}},
        },
        hoverlabel={"font_size": 12, "font_family": config.font_family},
    )
    fig.update_coloraxes(
        colorbar_tickfont_color=colors.text_dark,
        colorbar_title_font_color=colors.text_dark,
    )
    return fig
