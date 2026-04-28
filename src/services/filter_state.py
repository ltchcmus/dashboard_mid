from __future__ import annotations

import numpy as np
import streamlit as st


def khoi_tao_loc_tuong_tac() -> None:
    for key in ["quoc_gia_chon", "ngon_ngu_chon", "the_loai_chon"]:
        if key not in st.session_state:
            st.session_state[key] = []
    if "pending_filter_updates" not in st.session_state:
        st.session_state["pending_filter_updates"] = {}
    if "chart_event_signature" not in st.session_state:
        st.session_state["chart_event_signature"] = {
            "quoc_gia_chon": None,
            "ngon_ngu_chon": None,
            "the_loai_chon": None,
        }
    if "chart_event_skip_once" not in st.session_state:
        st.session_state["chart_event_skip_once"] = {
            "quoc_gia_chon": False,
            "ngon_ngu_chon": False,
            "the_loai_chon": False,
        }


def ap_dung_pending_filter_updates() -> None:
    pending = st.session_state.get("pending_filter_updates", {})
    if not pending:
        return
    for key, values in pending.items():
        st.session_state[key] = values
    st.session_state["pending_filter_updates"] = {}


def trich_gia_tri_tu_su_kien_plotly(
    su_kien, truong_du_lieu: list[str]
) -> list[str] | None:
    if su_kien is None:
        return None

    selection = None
    if isinstance(su_kien, dict):
        selection = su_kien.get("selection")
    elif hasattr(su_kien, "selection"):
        selection = getattr(su_kien, "selection")
    elif hasattr(su_kien, "get"):
        selection = su_kien.get("selection")

    if selection is None:
        return None

    points = []
    if isinstance(selection, dict):
        points = selection.get("points", [])
    elif hasattr(selection, "get"):
        points = selection.get("points", [])
    elif hasattr(selection, "points"):
        points = getattr(selection, "points") or []

    if not points:
        return []

    ket_qua: list[str] = []
    for p in points:
        if not isinstance(p, dict) and hasattr(p, "get"):
            p = dict(p)
        for truong in truong_du_lieu:
            gia_tri = p.get(truong) if isinstance(p, dict) else None
            while isinstance(gia_tri, (list, tuple, np.ndarray)):
                if isinstance(gia_tri, np.ndarray):
                    if gia_tri.size == 0:
                        gia_tri = None
                        break
                    gia_tri = gia_tri.flat[0]
                else:
                    if not gia_tri:
                        gia_tri = None
                        break
                    gia_tri = gia_tri[0]
            if gia_tri is None:
                continue
            chuoi = str(gia_tri).strip()
            if chuoi:
                ket_qua.append(chuoi)
                break
    return sorted(set(ket_qua))


def cap_nhat_loc_toggle(key_state: str, new_items: list[str]) -> bool:
    if not new_items:
        return False
    hien_tai = list(st.session_state.get(key_state, []))
    pending = st.session_state.get("pending_filter_updates", {})
    if key_state in pending:
        hien_tai = list(pending[key_state])
    changed = False
    for item in new_items:
        if item in hien_tai:
            hien_tai.remove(item)
            changed = True
        else:
            hien_tai.append(item)
            changed = True
    if changed:
        pending = dict(st.session_state.get("pending_filter_updates", {}))
        pending[key_state] = hien_tai
        st.session_state["pending_filter_updates"] = pending
    return changed


def dong_bo_loc_tuong_tac_tu_tab1(
    gia_tri_qg: list[str] | None,
    gia_tri_lang: list[str] | None,
    gia_tri_genre: list[str] | None,
) -> None:
    de_xuat = {
        "quoc_gia_chon": gia_tri_qg,
        "ngon_ngu_chon": gia_tri_lang,
        "the_loai_chon": gia_tri_genre,
    }
    changed = False
    chart_sig = dict(st.session_state.get("chart_event_signature", {}))
    chart_skip_once = dict(st.session_state.get("chart_event_skip_once", {}))
    for key, values in de_xuat.items():
        if values is None:
            continue
        if len(values) == 0:
            chart_sig[key] = None
            chart_skip_once[key] = False
            continue

        sig = "|".join(sorted(values))
        if chart_sig.get(key) == sig and chart_skip_once.get(key, False):
            chart_skip_once[key] = False
            continue
        if cap_nhat_loc_toggle(key, values):
            chart_sig[key] = sig
            chart_skip_once[key] = True
            changed = True

    st.session_state["chart_event_signature"] = chart_sig
    st.session_state["chart_event_skip_once"] = chart_skip_once

    if changed:
        st.rerun()
