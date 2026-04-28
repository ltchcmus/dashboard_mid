from __future__ import annotations

from dataclasses import dataclass, field

import pandas as pd

from src.config.app_config import AppConfig

try:
    import pycountry
except Exception:
    pycountry = None

try:
    from babel import Locale

    VI_LOCALE = Locale.parse("vi")
except Exception:
    VI_LOCALE = None


@dataclass
class TranslationService:
    genre_map: dict[str, str]
    language_fallback: dict[str, str]
    language_alias: dict[str, str]
    country_alias: dict[str, str]
    country_fallback: dict[str, str]
    _country_cache: dict[str, str] = field(default_factory=dict)

    @classmethod
    def from_config(cls, config: AppConfig) -> "TranslationService":
        mappings = config.mappings
        return cls(
            genre_map=mappings.genre_vi,
            language_fallback=mappings.language_fallback,
            language_alias=mappings.language_alias,
            country_alias=mappings.country_alias,
            country_fallback=mappings.country_fallback,
        )

    @staticmethod
    def chuan_hoa_chuoi(gia_tri: str) -> str:
        return str(gia_tri).strip().lower()

    def viet_hoa_the_loai(self, ten_the_loai: str) -> str:
        if pd.isna(ten_the_loai):
            return "Không xác định"
        ten = str(ten_the_loai).strip()
        if not ten:
            return "Không xác định"
        return self.genre_map.get(ten, ten)

    def viet_hoa_ngon_ngu(self, ma_ngon_ngu: str, ten_ngon_ngu: str) -> str:
        ma = "" if pd.isna(ma_ngon_ngu) else str(ma_ngon_ngu).strip().lower()
        ma = self.language_alias.get(ma, ma)
        ma_goc = ma.split("-")[0] if ma else ""

        if VI_LOCALE is not None:
            ten_vi = VI_LOCALE.languages.get(ma) or VI_LOCALE.languages.get(ma_goc)
            if ten_vi:
                return ten_vi[:1].upper() + ten_vi[1:]

        if ma in self.language_fallback:
            return self.language_fallback[ma]
        if ma_goc in self.language_fallback:
            return self.language_fallback[ma_goc]

        if pd.notna(ten_ngon_ngu):
            ten_goc = str(ten_ngon_ngu).strip()
            if ten_goc:
                return ten_goc

        return "Không xác định"

    def viet_hoa_quoc_gia(self, ten_quoc_gia: str) -> str:
        if pd.isna(ten_quoc_gia):
            return "Không xác định"
        ten_en = str(ten_quoc_gia).strip()
        if not ten_en:
            return "Không xác định"

        if ten_en in self._country_cache:
            return self._country_cache[ten_en]

        lookup_value = self.country_alias.get(self.chuan_hoa_chuoi(ten_en), ten_en)
        ten_vi = None

        if pycountry is not None and VI_LOCALE is not None:
            try:
                country_obj = pycountry.countries.lookup(lookup_value)
                ten_vi = VI_LOCALE.territories.get(country_obj.alpha_2)
            except LookupError:
                ten_vi = None

        if not ten_vi:
            ten_vi = self.country_fallback.get(ten_en)
        if not ten_vi:
            ten_vi = self.country_fallback.get(lookup_value)
        if not ten_vi:
            ten_vi = ten_en

        self._country_cache[ten_en] = ten_vi
        return ten_vi
