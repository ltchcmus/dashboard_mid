from __future__ import annotations

import streamlit as st

from src.config.app_config import AppConfig


def _build_global_css(config: AppConfig) -> str:
    colors = config.colors
    theme = config.theme
    return f"""
    <style>
    body, .stApp {{
        font-family: {config.font_family} !important;
        -webkit-font-smoothing: antialiased;
    }}
    .stApp {{
        background: {theme.app_background};
        color: {colors.text_dark};
    }}
    [data-testid='stHeader'] {{
        background: {colors.netflix_red} !important;
        height: {theme.header_height_px}px !important;
        min-height: {theme.header_height_px}px !important;
        display: flex !important;
        align-items: center !important;
    }}
    [data-testid='stHeader']::before {{
        content: "{config.title}";
        color: #FFFFFF !important;
        font-size: {theme.header_font_size_rem}rem;
        font-weight: 700;
        line-height: 1.05;
        margin-left: 1rem;
        white-space: nowrap;
    }}
    [data-testid='stHeader'] * {{
        color: #FFFFFF !important;
    }}
    [data-testid='stToolbar'] {{
        background: transparent !important;
    }}
    [data-testid='stMainBlockContainer'] {{
        padding-top: {theme.main_padding_top_rem}rem;
    }}
    h1, h2, h3 {{
        color: {colors.netflix_red};
    }}
    p, span, .stMarkdown, .stTable, .stDataFrame {{
        font-weight: 400 !important;
    }}
    p, span, label, .stCaption, .stMarkdown, .stMetric, .stMetricLabel, .stMetricValue {{
        color: {colors.text_dark} !important;
    }}
    .stMetricLabel p {{
        color: {colors.netflix_red} !important;
        font-weight: 600 !important;
    }}
    .stMetricValue {{
        color: {colors.netflix_red} !important;
        font-weight: 700 !important;
    }}
    .plotly svg text,
    .plotly .xtitle,
    .plotly .ytitle,
    .plotly .legendtitle,
    .plotly .legendtext,
    .plotly .hovertext {{
        font-weight: 600 !important;
    }}
    [data-testid='stTabs'] [data-baseweb='tab-list'] {{
        gap: 0.5rem;
        background: #F9FAFB;
        border: 1px solid #E5E7EB;
        border-bottom: 2px solid #E5E7EB;
        border-radius: 0.9rem 0.9rem 0.55rem 0.55rem;
        padding: 0.35rem 0.75rem 0.1rem;
        box-shadow: 0 8px 18px rgba(15, 23, 42, 0.08);
    }}
    [data-testid='stTabs'] [data-baseweb='tab'],
    [data-testid='stTabs'] button[role='tab'] {{
        color: {colors.text_dark};
        font-size: {theme.tab_font_size_rem}rem !important;
        font-weight: 700 !important;
        border-radius: 0.7rem 0.7rem 0 0;
        padding: 0.55rem 1.2rem 0.45rem;
        border: 1px solid #E5E7EB;
        border-bottom: 3px solid transparent;
        background: #FFFFFF;
        transition: all 0.15s ease;
        cursor: pointer;
    }}
    [data-testid='stTabs'] [data-baseweb='tab'][aria-selected='true'],
    [data-testid='stTabs'] button[role='tab'][aria-selected='true'] {{
        color: {colors.netflix_red} !important;
        font-size: {theme.tab_font_size_active_rem}rem !important;
        font-weight: 800 !important;
        background: #FFFFFF;
        border-color: {colors.netflix_red};
        border-bottom: 3px solid {colors.netflix_red};
        box-shadow: 0 10px 18px rgba(229, 9, 20, 0.18);
    }}
    [data-testid='stTabs'] [data-baseweb='tab']:hover,
    [data-testid='stTabs'] button[role='tab']:hover {{
        background: #FFF5F5;
        border-color: #F3C0C3;
    }}
    [data-testid='stSidebar'] {{
        background: {theme.sidebar_background};
        border-right: 1px solid #E6F2F2;
    }}
    [data-testid='stSidebar'] * {{
        color: {colors.text_dark} !important;
    }}
    [data-testid='stSidebar'] h2,
    [data-testid='stSidebar'] h3 {{
        color: {colors.netflix_red} !important;
        font-weight: 700;
    }}
    [data-testid='stSidebar'] label,
    [data-testid='stSidebar'] .stCaption,
    .stCaption,
    .streamlit-expanderHeader p {{
        font-weight: 600 !important;
    }}
    [data-testid='stSidebar'] [data-baseweb='select'] > div,
    [data-testid='stSidebar'] [data-baseweb='popover'] > div,
    [data-testid='stSidebar'] [data-baseweb='input'] > div {{
        border: 1px solid {colors.netflix_red} !important;
        box-shadow: none !important;
        background: #FFF6F6 !important;
    }}
    [data-testid='stSidebar'] [data-baseweb='tag'] {{
        background: {colors.netflix_red} !important;
        color: #FFFFFF !important;
    }}
    [data-testid='stSidebar'] [data-baseweb='slider'] [role='slider'] {{
        background: {colors.netflix_red} !important;
        border-color: {colors.netflix_red} !important;
    }}
    [data-testid='stSidebar'] [data-baseweb='slider'] > div > div {{
        background: {colors.netflix_red} !important;
    }}
    [data-testid='stSidebar'] .stButton > button {{
        background: {colors.netflix_red} !important;
        color: #FFFFFF !important;
        border: 1px solid {colors.netflix_red} !important;
        font-weight: 700;
    }}
    [data-testid='stSidebar'] .stButton > button * {{
        color: #FFFFFF !important;
        fill: #FFFFFF !important;
    }}
    [data-testid='stSidebar'] .stButton > button:hover {{
        background: #B20710 !important;
        border-color: #B20710 !important;
        color: #FFFFFF !important;
    }}
    [data-testid='stSidebar'] .stButton > button:hover * {{
        color: #FFFFFF !important;
        fill: #FFFFFF !important;
    }}
    @media (min-width: 0px) {{
        .plotly .main-svg text,
        .stMetricLabel p,
        .stCaption {{
            font-weight: 600 !important;
        }}
    }}
    </style>
    """


def ap_dung_giao_dien_toan_cuc(config: AppConfig) -> None:
    st.markdown(_build_global_css(config), unsafe_allow_html=True)
