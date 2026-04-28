from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.config.app_config import load_config
from src.services.data_loader import tai_du_lieu
from src.services.filter_state import khoi_tao_loc_tuong_tac
from src.services.filters import ap_dung_loc_tuong_tac, bo_loc_toan_cuc
from src.services.kpi import hien_thi_kpi
from src.tabs import (
    ve_tab_chat_luong,
    ve_tab_sang_tao,
    ve_tab_tai_chinh,
    ve_tab_toan_canh,
)
from src.utils.style import ap_dung_giao_dien_toan_cuc


def main() -> None:
    config = load_config()
    st.set_page_config(
        page_title=config.title,
        page_icon=None,
        layout="wide",
        initial_sidebar_state="expanded",
    )

    ap_dung_giao_dien_toan_cuc(config)
    khoi_tao_loc_tuong_tac()

    try:
        du_lieu = tai_du_lieu(config)
    except Exception as exc:
        st.error(f"Không thể tải dữ liệu: {exc}")
        st.stop()

    movies_base, genres_base = bo_loc_toan_cuc(du_lieu)
    movies_loc, genres_loc = ap_dung_loc_tuong_tac(du_lieu, movies_base, genres_base)

    if movies_loc.empty:
        st.warning(
            "Không có dữ liệu phù hợp với bộ lọc hiện tại. Vui lòng điều chỉnh lựa chọn."
        )
        st.stop()

    hien_thi_kpi(movies_loc, genres_loc, config)
    st.markdown("### Chọn góc nhìn phân tích")
    st.caption("Nhấn vào từng tab để chuyển nhóm phân tích.")
    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Toàn cảnh",
            "Chất lượng",
            "Tài chính",
            "Sáng tạo",
        ]
    )

    with tab1:
        ve_tab_toan_canh(du_lieu, movies_loc, genres_loc, config)
    with tab2:
        ve_tab_chat_luong(movies_loc, genres_loc, config)
    with tab3:
        ve_tab_tai_chinh(movies_loc, genres_loc, config)
    with tab4:
        ve_tab_sang_tao(du_lieu, movies_loc, config)


if __name__ == "__main__":
    main()
