from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "processed"
NETFLIX_RED = "#E50914"
NETFLIX_GOLD = "#FFB100"
TEXT_DARK = "#1F2937"
CHART_BG = "#FFFFFF"

# Semantic color system for all charts
SEQ_COUNT = ["#FFEBEE", "#E50914", "#80060B"]
DIVERGE_QUALITY = [NETFLIX_RED, "#F8F9FA", NETFLIX_GOLD]
CAT_GENRE = [
	NETFLIX_RED,
	"#221F1F",
	NETFLIX_GOLD,
	"#F5F5F1",
	"#564D4D",
	"#B20710",
	"#831010",
	"#E1E1E1",
]
NEUTRAL_GREY = "#BFBFBF"

QUALITY_BUCKET_COLORS = {
	"Kém (0-5)": "#B22222",
	"TB (5-6)": "#D96B6B",
	"Khá (6-7)": "#E5E7EB",
	"Tốt (7-8)": NETFLIX_GOLD,
	"Xuất sắc (8-10)": "#00A651",
}


def dinh_dang_tien_te(gia_tri: float) -> str:
	if pd.isna(gia_tri):
		return "N/A"
	if gia_tri >= 1_000_000_000:
		return f"${gia_tri / 1_000_000_000:.2f} tỷ"
	if gia_tri >= 1_000_000:
		return f"${gia_tri / 1_000_000:.2f} triệu"
	return f"${gia_tri:,.0f}"


def tach_cot_danh_sach(df: pd.DataFrame, cot: str, ten_moi: str) -> pd.DataFrame:
	temp = df[["show_id", cot]].copy()
	temp[cot] = (
		temp[cot]
		.fillna("")
		.astype(str)
		.str.replace(r"[\[\]']", "", regex=True)
		.str.replace('"', "", regex=False)
		.str.split(",")
	)
	temp = temp.explode(cot)
	temp[cot] = temp[cot].astype(str).str.strip()
	temp = temp.rename(columns={cot: ten_moi})
	temp = temp[temp[ten_moi].notna() & (temp[ten_moi] != "")]
	return temp.drop_duplicates()


def ap_dung_giao_dien_plotly(fig):
	fig.update_layout(
		template="plotly_white",
		paper_bgcolor=CHART_BG,
		plot_bgcolor=CHART_BG,
		font={"color": TEXT_DARK},
		title={"font": {"color": NETFLIX_RED, "size": 18}, "x": 0.5, "xanchor": "center"},
		clickmode="event+select",
		legend={"font": {"color": TEXT_DARK}, "title": {"font": {"color": TEXT_DARK}}},
		xaxis={"tickfont": {"color": TEXT_DARK}, "title": {"font": {"color": TEXT_DARK}}},
		yaxis={"tickfont": {"color": TEXT_DARK}, "title": {"font": {"color": TEXT_DARK}}},
	)
	fig.update_coloraxes(colorbar_tickfont_color=TEXT_DARK, colorbar_title_font_color=TEXT_DARK)
	return fig


def thong_bao_khong_co_du_lieu() -> None:
	st.info("Không có dữ liệu phù hợp với bộ lọc hiện tại. Vui lòng điều chỉnh lựa chọn.")


def khoi_tao_loc_tuong_tac() -> None:
	for key in ["selected_countries", "selected_languages", "selected_genres"]:
		if key not in st.session_state:
			st.session_state[key] = []


def trich_gia_tri_tu_su_kien_plotly(su_kien, truong_du_lieu: list[str]) -> list[str] | None:
	if not isinstance(su_kien, dict):
		return None
	selection = su_kien.get("selection")
	if selection is None:
		return None
	points = selection.get("points", [])
	if not points:
		return []

	ket_qua: list[str] = []
	for p in points:
		for truong in truong_du_lieu:
			gia_tri = p.get(truong)
			if isinstance(gia_tri, (list, tuple)):
				gia_tri = gia_tri[0] if gia_tri else None
			if gia_tri is None:
				continue
			chuoi = str(gia_tri).strip()
			if chuoi:
				ket_qua.append(chuoi)
				break
	return sorted(set(ket_qua))


def cap_nhat_loc_tuong_tac_tu_chart(su_kien, key_state: str, truong_du_lieu: list[str]) -> bool:
	gia_tri = trich_gia_tri_tu_su_kien_plotly(su_kien, truong_du_lieu)
	if gia_tri is not None:
		if st.session_state.get(key_state, []) != gia_tri:
			st.session_state[key_state] = gia_tri
			return True
	return False


def dong_bo_loc_tuong_tac_tu_tab1(
	gia_tri_qg: list[str] | None,
	gia_tri_lang: list[str] | None,
	gia_tri_genre: list[str] | None,
) -> None:
	de_xuat = {
		"selected_countries": gia_tri_qg,
		"selected_languages": gia_tri_lang,
		"selected_genres": gia_tri_genre,
	}
	de_xuat_khong_none = {k: v for k, v in de_xuat.items() if v is not None}
	if not de_xuat_khong_none:
		return

	if all(v == [] for v in de_xuat_khong_none.values()) and len(de_xuat_khong_none) > 1:
		return

	has_non_empty = any(v != [] for v in de_xuat_khong_none.values())

	changed = False
	for key, value in de_xuat_khong_none.items():
		if value == [] and has_non_empty and st.session_state.get(key):
			continue
		if st.session_state.get(key, []) != value:
			st.session_state[key] = value
			changed = True

	if changed:
		st.rerun()


def ap_dung_loc_tuong_tac(
	du_lieu: dict[str, pd.DataFrame],
	movies_base: pd.DataFrame,
	genres_base: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
	movies_loc = movies_base.copy()

	countries_chon = st.session_state.get("selected_countries", [])
	if countries_chon:
		show_ids_qg = du_lieu["countries"][
			du_lieu["countries"]["country_name"].isin(countries_chon)
		]["show_id"].unique()
		movies_loc = movies_loc[movies_loc["show_id"].isin(show_ids_qg)]

	languages_chon = st.session_state.get("selected_languages", [])
	if languages_chon:
		movies_loc = movies_loc[movies_loc["language_name"].isin(languages_chon)]

	genres_chon = st.session_state.get("selected_genres", [])
	if genres_chon:
		show_ids_genre = du_lieu["genres_exploded"][
			du_lieu["genres_exploded"]["the_loai"].isin(genres_chon)
		]["show_id"].unique()
		movies_loc = movies_loc[movies_loc["show_id"].isin(show_ids_genre)]

	genres_loc = genres_base[genres_base["show_id"].isin(movies_loc["show_id"])]
	return movies_loc, genres_loc


def hien_thi_trang_thai_loc_tuong_tac() -> None:
	with st.sidebar:
		st.markdown("### Bộ lọc tương tác từ biểu đồ")
		if st.button("Xóa lọc tương tác", use_container_width=True):
			st.session_state["selected_countries"] = []
			st.session_state["selected_languages"] = []
			st.session_state["selected_genres"] = []
			st.rerun()

		qg = st.session_state.get("selected_countries", [])
		lang = st.session_state.get("selected_languages", [])
		genre = st.session_state.get("selected_genres", [])

		st.caption("Quốc gia: " + (", ".join(qg) if qg else "(không chọn)"))
		st.caption("Ngôn ngữ: " + (", ".join(lang) if lang else "(không chọn)"))
		st.caption("Thể loại: " + (", ".join(genre) if genre else "(không chọn)"))


@st.cache_data(show_spinner=False)
def tai_du_lieu() -> dict[str, pd.DataFrame]:
	tep_can_doc = {
		"movies": "movies.csv",
		"countries": "movie_countries.csv",
	}
	du_lieu: dict[str, pd.DataFrame] = {}
	for key, file_name in tep_can_doc.items():
		path = DATA_DIR / file_name
		if not path.exists():
			raise FileNotFoundError(f"Không tìm thấy tệp dữ liệu: {path}")
		du_lieu[key] = pd.read_csv(path)

	du_lieu["movies"]["release_year"] = pd.to_numeric(
		du_lieu["movies"]["release_year"], errors="coerce"
	)
	du_lieu["movies"]["vote_average"] = pd.to_numeric(
		du_lieu["movies"]["vote_average"], errors="coerce"
	)
	du_lieu["movies"]["popularity"] = pd.to_numeric(
		du_lieu["movies"]["popularity"], errors="coerce"
	)
	du_lieu["movies"]["vote_count"] = pd.to_numeric(
		du_lieu["movies"]["vote_count"], errors="coerce"
	)
	du_lieu["movies"]["budget"] = pd.to_numeric(
		du_lieu["movies"]["budget"], errors="coerce"
	)
	du_lieu["movies"]["revenue"] = pd.to_numeric(
		du_lieu["movies"]["revenue"], errors="coerce"
	)

	du_lieu["genres_exploded"] = tach_cot_danh_sach(du_lieu["movies"], "genres", "the_loai")
	du_lieu["casts_exploded"] = tach_cot_danh_sach(du_lieu["movies"], "cast", "dien_vien")
	du_lieu["directors_exploded"] = tach_cot_danh_sach(
		du_lieu["movies"], "director", "dao_dien"
	)
	return du_lieu


def bo_loc_toan_cuc(du_lieu: dict[str, pd.DataFrame]) -> tuple[pd.DataFrame, pd.DataFrame]:
	movies = du_lieu["movies"].copy()
	genres_exploded = du_lieu["genres_exploded"]
	countries = du_lieu["countries"]

	nam_min = int(movies["release_year"].min())
	nam_max = int(movies["release_year"].max())

	st.sidebar.header("Bộ lọc hệ thống")
	khoang_nam = st.sidebar.slider(
		"Năm phát hành",
		min_value=nam_min,
		max_value=nam_max,
		value=(nam_min, nam_max),
	)

	danh_sach_quoc_gia = sorted(countries["country_name"].dropna().unique().tolist())
	quoc_gia_chon = st.sidebar.selectbox("Quốc gia", options=["Tất cả"] + danh_sach_quoc_gia)

	danh_sach_the_loai = sorted(genres_exploded["the_loai"].dropna().unique().tolist())
	the_loai_chon = st.sidebar.multiselect("Thể loại", options=danh_sach_the_loai)

	danh_sach_ngon_ngu = sorted(movies["language_name"].dropna().unique().tolist())
	ngon_ngu_chon = st.sidebar.selectbox("Ngôn ngữ", options=["Tất cả"] + danh_sach_ngon_ngu)

	loc_theo_nam = movies[
		movies["release_year"].between(khoang_nam[0], khoang_nam[1], inclusive="both")
	]

	if quoc_gia_chon != "Tất cả":
		show_ids_quoc_gia = countries[countries["country_name"] == quoc_gia_chon]["show_id"].unique()
		loc_theo_nam = loc_theo_nam[loc_theo_nam["show_id"].isin(show_ids_quoc_gia)]

	if ngon_ngu_chon != "Tất cả":
		loc_theo_nam = loc_theo_nam[loc_theo_nam["language_name"] == ngon_ngu_chon]

	if the_loai_chon:
		show_ids_the_loai = genres_exploded[
			genres_exploded["the_loai"].isin(the_loai_chon)
		]["show_id"].unique()
		loc_theo_nam = loc_theo_nam[loc_theo_nam["show_id"].isin(show_ids_the_loai)]

	genres_loc = genres_exploded[genres_exploded["show_id"].isin(loc_theo_nam["show_id"])]
	return loc_theo_nam, genres_loc


def hien_thi_kpi(movies_loc: pd.DataFrame, genres_loc: pd.DataFrame) -> None:
	tong_doanh_thu = movies_loc["revenue"].fillna(0).sum()
	diem_trung_binh = movies_loc["vote_average"].mean()

	if not genres_loc.empty:
		top_genre = genres_loc["the_loai"].value_counts().index[0]
	else:
		top_genre = "N/A"

	roi = movies_loc[movies_loc["budget"] > 0].copy()
	roi["roi"] = np.where(
		roi["budget"] > 0,
		(roi["revenue"] - roi["budget"]) / roi["budget"],
		np.nan,
	)
	roi_tb = roi["roi"].mean()

	c1, c2, c3, c4 = st.columns(4)
	c1.metric("Tổng doanh thu", dinh_dang_tien_te(tong_doanh_thu))
	c2.metric("Điểm đánh giá trung bình", f"{diem_trung_binh:.2f}" if pd.notna(diem_trung_binh) else "N/A")
	c3.metric("Thể loại phổ biến nhất", top_genre)
	c4.metric("Tỷ suất lợi nhuận trung bình (ROI)", f"{roi_tb:.1%}" if pd.notna(roi_tb) else "N/A")


def ve_tab_toan_canh(du_lieu: dict[str, pd.DataFrame], movies_loc: pd.DataFrame, genres_loc: pd.DataFrame) -> None:
	st.subheader("Toàn cảnh Netflix toàn cầu")

	countries = du_lieu["countries"]
	countries_loc = countries[countries["show_id"].isin(movies_loc["show_id"])]
	qg_dem = (
		countries_loc.groupby("country_name", as_index=False)["show_id"]
		.nunique()
		.rename(columns={"country_name": "Quốc gia", "show_id": "Số lượng phim"})
	)
	gia_tri_qg = None

	if qg_dem.empty:
		st.info("Không có dữ liệu quốc gia sau khi lọc.")
	else:
		qg_dem["Số lượng phim (log10)"] = qg_dem["Số lượng phim"].apply(lambda v: math.log10(v))
		log_min = int(qg_dem["Số lượng phim (log10)"].min())
		log_max = int(math.ceil(qg_dem["Số lượng phim (log10)"].max()))
		tick_vals = list(range(log_min, log_max + 1))
		tick_text = [f"{10 ** p:,}" for p in tick_vals]

		fig_map = px.choropleth(
			qg_dem,
			locations="Quốc gia",
			locationmode="country names",
			color="Số lượng phim (log10)",
			custom_data=["Quốc gia"],
			color_continuous_scale=SEQ_COUNT,
			title="Phân bố phim theo quốc gia",
			hover_data={"Số lượng phim": True, "Số lượng phim (log10)": False},
		)
		fig_map.update_coloraxes(
			colorbar_title="Số lượng phim",
			colorbar_tickvals=tick_vals,
			colorbar_ticktext=tick_text,
		)
		fig_map.update_geos(bgcolor=CHART_BG)
		fig_map.update_layout(margin={"t": 60, "l": 0, "r": 0, "b": 0}, height=560)
		su_kien_map = st.plotly_chart(
			ap_dung_giao_dien_plotly(fig_map),
			width="stretch",
			key="chart_map_quoc_gia",
			on_select="rerun",
		)
		gia_tri_qg = trich_gia_tri_tu_su_kien_plotly(su_kien_map, ["customdata", "location"])

	c1, c2 = st.columns(2)

	with c1:
		gia_tri_lang = None
		ngon_ngu = (
			movies_loc.groupby("language_name", as_index=False)["show_id"]
			.nunique()
			.rename(columns={"language_name": "Ngôn ngữ", "show_id": "Số lượng phim"})
		)
		if ngon_ngu.empty:
			st.info("Không có dữ liệu ngôn ngữ sau khi lọc.")
		else:
			fig_tree = px.treemap(
				ngon_ngu,
				path=["Ngôn ngữ"],
				values="Số lượng phim",
				color="Số lượng phim",
				custom_data=["Ngôn ngữ"],
				color_continuous_scale=SEQ_COUNT,
				title="Tỉ trọng phim theo ngôn ngữ hiển thị",
			)
			fig_tree.update_layout(margin={"t": 60, "l": 0, "r": 0, "b": 0}, height=420)
			su_kien_lang = st.plotly_chart(
				ap_dung_giao_dien_plotly(fig_tree),
				width="stretch",
				key="chart_tree_ngon_ngu",
				on_select="rerun",
			)
			gia_tri_lang = trich_gia_tri_tu_su_kien_plotly(su_kien_lang, ["customdata", "label", "id"])

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
				color_continuous_scale=SEQ_COUNT,
			)
			fig_bar.update_layout(yaxis_title="Thể loại", xaxis_title="Số lượng phim", height=420)
			su_kien_genre = st.plotly_chart(
				ap_dung_giao_dien_plotly(fig_bar),
				width="stretch",
				key="chart_bar_the_loai",
				on_select="rerun",
			)
			gia_tri_genre = trich_gia_tri_tu_su_kien_plotly(su_kien_genre, ["customdata", "y"])

	dong_bo_loc_tuong_tac_tu_tab1(gia_tri_qg, gia_tri_lang, gia_tri_genre)


def ve_tab_chat_luong(movies_loc: pd.DataFrame, genres_loc: pd.DataFrame) -> None:
	st.subheader("Chất lượng và chiến lược nội dung")

	# Hang 1: Q4 Donut : Q4 Bar = 4 : 6
	q4_donut_col, q4_bar_col = st.columns([4, 6])
	q4_df = movies_loc[["show_id", "vote_average", "popularity", "budget", "revenue"]].copy()
	q4_df = q4_df.dropna(subset=["show_id", "vote_average"])
	if q4_df.empty:
		with q4_donut_col:
			thong_bao_khong_co_du_lieu()
		with q4_bar_col:
			thong_bao_khong_co_du_lieu()
	else:
		bins = [0, 5, 6, 7, 8, 10]
		labels = ["Kém (0-5)", "TB (5-6)", "Khá (6-7)", "Tốt (7-8)", "Xuất sắc (8-10)"]
		donut_order = ["Xuất sắc (8-10)", "Tốt (7-8)", "Khá (6-7)", "TB (5-6)", "Kém (0-5)"]
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
		donut_data["Số lượng phim"] = pd.to_numeric(donut_data["Số lượng phim"], errors="coerce").fillna(0)
		donut_data = donut_data[donut_data["Số lượng phim"] > 0]

		high_quality_ids = q4_df[q4_df["vote_average"] >= 7.5]["show_id"].unique()
		hq_genres = genres_loc[genres_loc["show_id"].isin(high_quality_ids)].copy()
		hq_detail = hq_genres.merge(
			q4_df[["show_id", "popularity", "budget", "revenue"]], on="show_id", how="left"
		)
		hq_detail["roi"] = np.where(
			hq_detail["budget"] > 0,
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
					color_discrete_map=QUALITY_BUCKET_COLORS,
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
				st.plotly_chart(ap_dung_giao_dien_plotly(fig_donut), width="stretch")

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
					color_continuous_scale=DIVERGE_QUALITY,
					title="Top thể loại được duy trì chất lượng (Điểm >= 7.5)",
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
				st.plotly_chart(ap_dung_giao_dien_plotly(fig_hq_bar), width="stretch")

	# Hang 2: Q6 : Q5 = 6 : 4
	q6_col, q5_col = st.columns([6, 4])

	with q5_col:
		hist_df = movies_loc[["show_id", "budget", "vote_average", "revenue"]].dropna().copy()
		hist_df = hist_df[hist_df["budget"] > 0]
		if hist_df.empty:
			thong_bao_khong_co_du_lieu()
		else:
			hist_df["Nhóm ngân sách"] = pd.cut(
				hist_df["budget"],
				bins=[-np.inf, 20_000_000, 80_000_000, np.inf],
				labels=["Thấp", "Trung bình", "Cao"],
			)
			hist_df["Nhóm điểm số"] = pd.cut(
				hist_df["vote_average"],
				bins=[-np.inf, 6, 7.5, np.inf],
				labels=["<6", "6-7.5", ">7.5"],
			)
			hist_df["roi"] = np.where(
				hist_df["budget"] > 0,
				(hist_df["revenue"] - hist_df["budget"]) / hist_df["budget"],
				np.nan,
			)
			agg = (
				hist_df.groupby(["Nhóm ngân sách", "Nhóm điểm số"], observed=True, as_index=False)
				.agg(So_luong=("show_id", "nunique"), ROI_trung_binh=("roi", "mean"))
			)
			fig_hist = px.density_heatmap(
				agg,
				x="Nhóm ngân sách",
				y="Nhóm điểm số",
				z="So_luong",
				text_auto=True,
				color_continuous_scale=SEQ_COUNT,
				title="Tương quan lợi nhuận (ROI) theo điểm số và ngân sách",
				hover_data={"ROI_trung_binh": ":.2f", "So_luong": True},
			)
			st.plotly_chart(ap_dung_giao_dien_plotly(fig_hist), width="stretch")

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
			fig_err = go.Figure(
				go.Bar(
					x=genre_stat["diem_trung_binh"],
					y=genre_stat["the_loai"],
					orientation="h",
					error_x={"type": "data", "array": genre_stat["do_lech_chuan"], "visible": True},
					marker={
						"color": genre_stat["diem_trung_binh"],
						"colorscale": DIVERGE_QUALITY,
						"showscale": True,
						"colorbar": {"title": "Điểm TB"},
					},
					hovertemplate=(
						"Thể loại: %{y}<br>Điểm TB: %{x:.2f}<br>Độ lệch chuẩn: %{error_x.array:.2f}"  # noqa: E501
						"<br>Số phim: %{customdata}<extra></extra>"
					),
					customdata=genre_stat[["so_luong"]],
				)
			)
			fig_err.update_layout(
				title="Top thể loại có điểm đánh giá ổn định nhất",
				xaxis_title="Điểm đánh giá trung bình",
				yaxis_title="Thể loại",
			)
			st.plotly_chart(ap_dung_giao_dien_plotly(fig_err), width="stretch")


def ve_tab_tai_chinh(movies_loc: pd.DataFrame, genres_loc: pd.DataFrame) -> None:
	st.subheader("Hiệu quả đầu tư")

	c1, c2 = st.columns(2)

	with c1:
		roi_df = movies_loc[(movies_loc["budget"] > 0) & (movies_loc["revenue"] > 0)].copy()
		roi_df["roi"] = np.where(
			roi_df["budget"] > 0,
			(roi_df["revenue"] - roi_df["budget"]) / roi_df["budget"],
			np.nan,
		)
		roi_top = roi_df.sort_values("roi", ascending=False).head(10)
		if roi_top.empty:
			thong_bao_khong_co_du_lieu()
		else:
			fig_roi = px.bar(
				roi_top.sort_values("roi", ascending=True),
				x="roi",
				y="title",
				orientation="h",
				color="roi",
				color_continuous_scale=DIVERGE_QUALITY,
				title="Top dự án có tỷ suất lợi nhuận (ROI) cao nhất",
				labels={"roi": "Tỷ lệ lợi nhuận (ROI)", "title": "Tên phim"},
			)
			fig_roi.update_xaxes(
				type="log",
				exponentformat="power",
				showexponent="all",
				dtick=1,
				showgrid=True,
				gridcolor="#D1D5DB",
				griddash="dash",
			)
			st.plotly_chart(ap_dung_giao_dien_plotly(fig_roi), width="stretch")

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
				budget_df.groupby(["release_year", "nhom_the_loai"], as_index=False)["budget"]
				.mean()
				.rename(
					columns={
						"release_year": "Năm",
						"nhom_the_loai": "Thể loại",
						"budget": "Ngân sách trung bình",
					}
				)
			)

			vivid_palette = [
				"#E50914",
				"#FF7A00",
				"#FFB100",
				"#00A676",
				"#00A8E8",
				"#6A4CFF",
				"#FF3CAC",
				"#17BEBB",
			]
			thutu_the_loai_q8 = top_genres + ["Khác"]
			budget_year["Thể loại"] = pd.Categorical(
				budget_year["Thể loại"], categories=thutu_the_loai_q8, ordered=True
			)
			budget_year = budget_year.sort_values(["Thể loại", "Năm"])
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
			st.plotly_chart(ap_dung_giao_dien_plotly(fig_line), width="stretch")

	bubble_src = genres_loc.merge(
		movies_loc[["show_id", "budget", "revenue"]], on="show_id", how="left"
	)
	bubble_src = bubble_src[(bubble_src["budget"] > 0) & (bubble_src["revenue"] > 0)]
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

		vivid_palette = [
			"#E50914",
			"#FF7A00",
			"#FFB100",
			"#00A676",
			"#00A8E8",
			"#6A4CFF",
			"#FF3CAC",
			"#17BEBB",
			"#1D4ED8",
		]
		thutu_the_loai_q9 = top_genres_q9 + ["Khác"]
		bubble_df["Nhóm thể loại"] = pd.Categorical(
			bubble_df["Nhóm thể loại"], categories=thutu_the_loai_q9, ordered=True
		)
		bubble_df = bubble_df.sort_values("Nhóm thể loại")
		color_map = {
			theloai: vivid_palette[idx % len(vivid_palette)]
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
		min_val = float(min(bubble_df["ngan_sach_tb"].min(), bubble_df["doanh_thu_tb"].min()))
		max_val = float(max(bubble_df["ngan_sach_tb"].max(), bubble_df["doanh_thu_tb"].max()))
		fig_bubble.add_shape(
			type="line",
			x0=min_val,
			y0=min_val,
			x1=max_val,
			y1=max_val,
			line={"color": NETFLIX_RED, "dash": "dash", "width": 2},
		)
		fig_bubble.add_annotation(
			x=max_val,
			y=max_val,
			text="Đường hòa vốn: Doanh thu = Ngân sách",
			showarrow=False,
			xanchor="right",
			yanchor="bottom",
			bgcolor="rgba(255,255,255,0.75)",
			font={"color": TEXT_DARK, "size": 10},
		)
		fig_bubble.update_xaxes(type="log", exponentformat="power", showexponent="all", dtick=1)
		fig_bubble.update_yaxes(type="log", exponentformat="power", showexponent="all", dtick=1)
		st.plotly_chart(ap_dung_giao_dien_plotly(fig_bubble), width="stretch")
		st.caption("Kích thước bong bóng biểu diễn số lượng phim trong từng nhóm thể loại.")



def ve_tab_sang_tao(du_lieu: dict[str, pd.DataFrame], movies_loc: pd.DataFrame) -> None:
	st.subheader("Góc nhìn sáng tạo")
	c1, c2 = st.columns(2)

	with c1:
		directors = du_lieu["directors_exploded"]
		director_df = directors[directors["show_id"].isin(movies_loc["show_id"])]
		director_stat = (
			director_df.merge(
				movies_loc[["show_id", "vote_average", "revenue"]], on="show_id", how="left"
			)
			.groupby("dao_dien", as_index=False)
			.agg(
				doanh_thu_trung_binh=("revenue", "mean"),
				diem_danh_gia_trung_binh=("vote_average", "mean"),
				so_phim=("show_id", "nunique"),
			)
		)
		director_stat = director_stat[(director_stat["so_phim"] >= 2) & (director_stat["doanh_thu_trung_binh"] > 0)]
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
			fig_director.update_traces(marker={"color": NETFLIX_GOLD, "opacity": 0.8})
			fig_director.update_xaxes(type="log", exponentformat="power", showexponent="all", dtick=1)
			st.plotly_chart(ap_dung_giao_dien_plotly(fig_director), width="stretch")

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
				color_continuous_scale=SEQ_COUNT,
				title="Top diễn viên mang lại doanh thu cao nhất",
			)
			st.plotly_chart(ap_dung_giao_dien_plotly(fig_cast), width="stretch")

	genre_mix_df = movies_loc[["show_id", "genres", "popularity", "vote_average"]].dropna().copy()
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
			mix_stat = (
				genre_mix_df.groupby("nhom_so_the_loai", as_index=False)
				.agg(
					popularity_tb=("popularity", "mean"),
					diem_tb=("vote_average", "mean"),
					so_luong=("show_id", "nunique"),
				)
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
					marker={"color": NETFLIX_GOLD, "opacity": 0.72},
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
					line={"color": NETFLIX_RED, "width": 3},
					marker={"color": NETFLIX_RED, "size": 8},
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
					"font": {"color": TEXT_DARK},
					"title": {"font": {"color": NETFLIX_RED}},
				},
			)
			fig_mix.update_xaxes(title="Số thể loại", tickfont={"color": TEXT_DARK}, title_font={"color": TEXT_DARK})
			fig_mix.update_yaxes(
				title_text="Độ phổ biến trung bình",
				secondary_y=False,
				showgrid=True,
				gridcolor="#E5E7EB",
				griddash="dot",
				tickfont={"color": TEXT_DARK},
				title_font={"color": TEXT_DARK},
				rangemode="tozero",
			)
			fig_mix.update_yaxes(
				title_text="Điểm đánh giá trung bình",
				secondary_y=True,
				showgrid=False,
				tickfont={"color": TEXT_DARK},
				title_font={"color": TEXT_DARK},
				range=[y2_min, y2_max],
			)
			st.plotly_chart(ap_dung_giao_dien_plotly(fig_mix), width="stretch")


def main() -> None:
	st.set_page_config(
		page_title="Netflix Data Storytelling Dashboard",
		page_icon="🎬",
		layout="wide",
		initial_sidebar_state="expanded",
	)

	st.markdown(
		f"""
		<style>
		.stApp {{
			background: linear-gradient(180deg, #FFFFFF 0%, #FFF8F8 42%, #F4FFFF 100%);
			color: {TEXT_DARK};
		}}
		[data-testid='stHeader'] {{
			background: {NETFLIX_RED} !important;
			height: 72px !important;
			min-height: 72px !important;
			display: flex !important;
			align-items: center !important;
		}}
		[data-testid='stHeader']::before {{
			content: "Netflix Data Storytelling Dashboard";
			color: #FFFFFF !important;
			font-size: 2.2rem;
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
			padding-top: 4.8rem;
		}}
		h1, h2, h3 {{
			color: {NETFLIX_RED};
		}}
		p, span, label, .stCaption, .stMarkdown, .stMetric, .stMetricLabel, .stMetricValue {{
			color: {TEXT_DARK} !important;
		}}
		.stMetricLabel p {{
			color: {NETFLIX_RED} !important;
			font-weight: 700 !important;
		}}
		.stMetricValue {{
			color: {NETFLIX_RED} !important;
			font-weight: 800 !important;
		}}
		[data-baseweb='tab'] {{
			color: {TEXT_DARK};
		}}
		[data-baseweb='tab'][aria-selected='true'] {{
			color: {NETFLIX_RED} !important;
			font-weight: 700;
		}}
		[data-testid='stSidebar'] {{
			background: linear-gradient(180deg, #FFFFFF 0%, #F5FBFB 100%);
			border-right: 1px solid #E6F2F2;
		}}
		[data-testid='stSidebar'] * {{
			color: {TEXT_DARK} !important;
		}}
		[data-testid='stSidebar'] h2,
		[data-testid='stSidebar'] h3,
		[data-testid='stSidebar'] .stMarkdown p {{
			color: {NETFLIX_RED} !important;
			font-weight: 700;
		}}
		[data-testid='stSidebar'] [data-baseweb='select'] > div,
		[data-testid='stSidebar'] [data-baseweb='popover'] > div,
		[data-testid='stSidebar'] [data-baseweb='input'] > div {{
			border: 1px solid {NETFLIX_RED} !important;
			box-shadow: none !important;
			background: #FFF6F6 !important;
		}}
		[data-testid='stSidebar'] [data-baseweb='tag'] {{
			background: {NETFLIX_RED} !important;
			color: #FFFFFF !important;
		}}
		[data-testid='stSidebar'] [data-baseweb='slider'] [role='slider'] {{
			background: {NETFLIX_RED} !important;
			border-color: {NETFLIX_RED} !important;
		}}
		[data-testid='stSidebar'] [data-baseweb='slider'] > div > div {{
			background: {NETFLIX_RED} !important;
		}}
		[data-testid='stSidebar'] .stButton > button {{
			background: {NETFLIX_RED} !important;
			color: #FFFFFF !important;
			border: 1px solid {NETFLIX_RED} !important;
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
		</style>
		""",
		unsafe_allow_html=True,
	)

	khoi_tao_loc_tuong_tac()

	try:
		du_lieu = tai_du_lieu()
	except Exception as exc:
		st.error(f"Không thể tải dữ liệu: {exc}")
		st.stop()

	movies_base, genres_base = bo_loc_toan_cuc(du_lieu)
	hien_thi_trang_thai_loc_tuong_tac()
	movies_loc, genres_loc = ap_dung_loc_tuong_tac(du_lieu, movies_base, genres_base)

	if movies_loc.empty:
		st.warning("Không có dữ liệu phù hợp với bộ lọc hiện tại. Vui lòng điều chỉnh lựa chọn.")
		st.stop()

	hien_thi_kpi(movies_loc, genres_loc)
	tab1, tab2, tab3, tab4 = st.tabs(
		[
			"🌍 Toàn cảnh",
			"🎯 Chất lượng",
			"💰 Tài chính",
			"🎬 Sáng tạo",
		]
	)

	with tab1:
		ve_tab_toan_canh(du_lieu, movies_loc, genres_loc)
	with tab2:
		ve_tab_chat_luong(movies_loc, genres_loc)
	with tab3:
		ve_tab_tai_chinh(movies_loc, genres_loc)
	with tab4:
		ve_tab_sang_tao(du_lieu, movies_loc)


if __name__ == "__main__":
	main()
