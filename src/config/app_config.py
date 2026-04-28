from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class AppTheme:
    app_background: str
    sidebar_background: str
    header_height_px: int
    header_font_size_rem: float
    main_padding_top_rem: float
    tab_font_size_rem: float
    tab_font_size_active_rem: float


@dataclass(frozen=True)
class AppColors:
    netflix_red: str
    netflix_gold: str
    text_dark: str
    chart_bg: str
    neutral_grey: str


@dataclass(frozen=True)
class AppPalettes:
    seq_count: list[str]
    diverge_quality: list[str]
    cat_genre: list[str]
    vivid_genre: list[str]


@dataclass(frozen=True)
class AppMappings:
    genre_vi: dict[str, str]
    language_fallback: dict[str, str]
    language_alias: dict[str, str]
    country_alias: dict[str, str]
    country_fallback: dict[str, str]


@dataclass(frozen=True)
class AppThresholds:
    min_budget: float
    min_revenue: float
    high_quality_vote: float


@dataclass(frozen=True)
class AppConfig:
    root_dir: Path
    data_dir: Path
    title: str
    font_family: str
    theme: AppTheme
    colors: AppColors
    palettes: AppPalettes
    quality_bucket_colors: dict[str, str]
    mappings: AppMappings
    thresholds: AppThresholds


def _require_section(raw: dict[str, Any], key: str) -> dict[str, Any]:
    section = raw.get(key)
    if not isinstance(section, dict):
        raise ValueError(f"Missing or invalid '{key}' section in config.yaml")
    return section


def _require_value(section: dict[str, Any], key: str, section_name: str) -> Any:
    if key not in section:
        raise ValueError(f"Missing '{key}' in {section_name} section of config.yaml")
    return section[key]


def load_config(config_path: Path | None = None) -> AppConfig:
    root_dir = Path(__file__).resolve().parents[2]
    path = config_path or root_dir / "config.yaml"
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    with path.open("r", encoding="utf-8") as handle:
        raw = yaml.safe_load(handle) or {}

    app = _require_section(raw, "app")
    theme_raw = _require_section(app, "theme")
    colors_raw = _require_section(raw, "colors")
    palettes_raw = _require_section(raw, "palettes")
    mappings_raw = _require_section(raw, "mappings")
    thresholds_raw = _require_section(raw, "thresholds")
    quality_bucket_colors = _require_section(raw, "quality_bucket_colors")

    theme = AppTheme(
        app_background=str(_require_value(theme_raw, "app_background", "app.theme")),
        sidebar_background=str(
            _require_value(theme_raw, "sidebar_background", "app.theme")
        ),
        header_height_px=int(
            _require_value(theme_raw, "header_height_px", "app.theme")
        ),
        header_font_size_rem=float(
            _require_value(theme_raw, "header_font_size_rem", "app.theme")
        ),
        main_padding_top_rem=float(
            _require_value(theme_raw, "main_padding_top_rem", "app.theme")
        ),
        tab_font_size_rem=float(
            _require_value(theme_raw, "tab_font_size_rem", "app.theme")
        ),
        tab_font_size_active_rem=float(
            _require_value(theme_raw, "tab_font_size_active_rem", "app.theme")
        ),
    )

    colors = AppColors(
        netflix_red=str(_require_value(colors_raw, "netflix_red", "colors")),
        netflix_gold=str(_require_value(colors_raw, "netflix_gold", "colors")),
        text_dark=str(_require_value(colors_raw, "text_dark", "colors")),
        chart_bg=str(_require_value(colors_raw, "chart_bg", "colors")),
        neutral_grey=str(_require_value(colors_raw, "neutral_grey", "colors")),
    )

    palettes = AppPalettes(
        seq_count=list(_require_value(palettes_raw, "seq_count", "palettes")),
        diverge_quality=list(
            _require_value(palettes_raw, "diverge_quality", "palettes")
        ),
        cat_genre=list(_require_value(palettes_raw, "cat_genre", "palettes")),
        vivid_genre=list(_require_value(palettes_raw, "vivid_genre", "palettes")),
    )

    mappings = AppMappings(
        genre_vi=dict(_require_value(mappings_raw, "genre_vi", "mappings")),
        language_fallback=dict(
            _require_value(mappings_raw, "language_fallback", "mappings")
        ),
        language_alias=dict(_require_value(mappings_raw, "language_alias", "mappings")),
        country_alias=dict(_require_value(mappings_raw, "country_alias", "mappings")),
        country_fallback=dict(
            _require_value(mappings_raw, "country_fallback", "mappings")
        ),
    )

    thresholds = AppThresholds(
        min_budget=float(_require_value(thresholds_raw, "min_budget", "thresholds")),
        min_revenue=float(_require_value(thresholds_raw, "min_revenue", "thresholds")),
        high_quality_vote=float(
            _require_value(thresholds_raw, "high_quality_vote", "thresholds")
        ),
    )

    data_dir = root_dir / str(_require_value(app, "data_dir", "app"))

    return AppConfig(
        root_dir=root_dir,
        data_dir=data_dir,
        title=str(_require_value(app, "title", "app")),
        font_family=str(_require_value(app, "font_family", "app")),
        theme=theme,
        colors=colors,
        palettes=palettes,
        quality_bucket_colors=dict(quality_bucket_colors),
        mappings=mappings,
        thresholds=thresholds,
    )
