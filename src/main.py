from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st
from wordcloud import WordCloud

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "processed"
NETFLIX_RED = "#E50914"
NETFLIX_TEAL = "#008080"
TEXT_DARK = "#1F2937"
CHART_BG = "#FFFFFF"
PALETTE = [NETFLIX_RED, NETFLIX_TEAL, "#F9A826", "#5DA5DA", "#60BD68"]


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
		title={"font": {"color": NETFLIX_RED, "size": 20}},
		clickmode="event+select",
		legend={"font": {"color": TEXT_DARK}, "title": {"font": {"color": TEXT_DARK}}},
		xaxis={"tickfont": {"color": TEXT_DARK}, "title": {"font": {"color": TEXT_DARK}}},
		yaxis={"tickfont": {"color": TEXT_DARK}, "title": {"font": {"color": TEXT_DARK}}},
	)
	fig.update_coloraxes(colorbar_tickfont_color=TEXT_DARK, colorbar_title_font_color=TEXT_DARK)
	return fig


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

	# Bo qua chu ky rerun nhieu chart cung tra ve [] (khong phai thao tac xoa co chu dich).
	if all(v == [] for v in de_xuat_khong_none.values()) and len(de_xuat_khong_none) > 1:
		return

	has_non_empty = any(v != [] for v in de_xuat_khong_none.values())

	changed = False
	for key, value in de_xuat_khong_none.items():
		# Neu chart khac vua co selection moi, khong de event rong cua chart nay xoa filter hien co.
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

	nam_min = int(movies["release_year"].min())
	nam_max = int(movies["release_year"].max())

	st.sidebar.header("Bộ lọc hệ thống")
	khoang_nam = st.sidebar.slider(
		"Năm phát hành",
		min_value=nam_min,
		max_value=nam_max,
		value=(nam_min, nam_max),
	)

	danh_sach_the_loai = sorted(genres_exploded["the_loai"].dropna().unique().tolist())
	the_loai_chon = st.sidebar.multiselect("Thể loại", options=danh_sach_the_loai)

	danh_sach_ngon_ngu = sorted(movies["language_name"].dropna().unique().tolist())
	ngon_ngu_chon = st.sidebar.selectbox("Ngôn ngữ", options=["Tất cả"] + danh_sach_ngon_ngu)

	loc_theo_nam = movies[
		movies["release_year"].between(khoang_nam[0], khoang_nam[1], inclusive="both")
	]

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
	roi["roi"] = roi["revenue"] / roi["budget"]
	roi_tb = roi["roi"].mean()

	c1, c2, c3, c4 = st.columns(4)
	c1.metric("Tổng doanh thu", dinh_dang_tien_te(tong_doanh_thu))
	c2.metric("Điểm đánh giá trung bình", f"{diem_trung_binh:.2f}" if pd.notna(diem_trung_binh) else "N/A")
	c3.metric("Thể loại phổ biến nhất", top_genre)
	c4.metric("Tỷ lệ lợi nhuận trung bình (ROI)", f"{roi_tb:.2f}x" if pd.notna(roi_tb) else "N/A")


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
			color_continuous_scale=["#FFD6D9", NETFLIX_RED],
			title="Những quốc gia nào là công xưởng nội dung chính?",
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
			use_container_width=True,
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
				color_continuous_scale=["#FFE5E8", NETFLIX_RED],
				title="Sự đa dạng ngôn ngữ trên nền tảng",
			)
			fig_tree.update_layout(margin={"t": 60, "l": 0, "r": 0, "b": 0}, height=420)
			su_kien_lang = st.plotly_chart(
				ap_dung_giao_dien_plotly(fig_tree),
				use_container_width=True,
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
				title="Thể loại nào đang thống trị về mặt số lượng?",
				color="Số lượng phim",
				custom_data=["Thể loại"],
				color_continuous_scale=["#FFE2E4", NETFLIX_RED],
			)
			fig_bar.update_layout(yaxis_title="Thể loại", xaxis_title="Số lượng phim", height=420)
			su_kien_genre = st.plotly_chart(
				ap_dung_giao_dien_plotly(fig_bar),
				use_container_width=True,
				key="chart_bar_the_loai",
				on_select="rerun",
			)
			gia_tri_genre = trich_gia_tri_tu_su_kien_plotly(su_kien_genre, ["customdata", "y"])

	dong_bo_loc_tuong_tac_tu_tab1(gia_tri_qg, gia_tri_lang, gia_tri_genre)


def ve_tab_chat_luong(movies_loc: pd.DataFrame, genres_loc: pd.DataFrame) -> None:
	st.subheader("Chất lượng và sự đón nhận")

	c1, c2 = st.columns(2)

	with c1:
		scatter_df = movies_loc[["title", "popularity", "vote_average"]].dropna().copy()
		if scatter_df.empty:
			st.info("Không có dữ liệu để vẽ biểu đồ tương quan phổ biến và điểm số.")
		else:
			q_pop = scatter_df["popularity"].quantile(0.75)
			q_vote = scatter_df["vote_average"].quantile(0.75)

			def gan_nhom(row: pd.Series) -> str:
				if row["popularity"] >= q_pop and row["vote_average"] >= q_vote:
					return "Vừa nổi tiếng vừa chất lượng"
				if row["popularity"] >= q_pop:
					return "Bom tấn đại chúng"
				if row["vote_average"] >= q_vote:
					return "Phim được đánh giá cao"
				return "Nhóm còn lại"

			scatter_df["Nhóm phim"] = scatter_df.apply(gan_nhom, axis=1)
			scatter_plot_df = scatter_df[scatter_df["popularity"] > 0].copy()

			if scatter_plot_df.empty:
				st.info("Không có dữ liệu popularity > 0 để hiển thị trên trục log.")
			else:
				so_diem_loai = len(scatter_df) - len(scatter_plot_df)
				if so_diem_loai > 0:
					st.caption(f"Đã ẩn {so_diem_loai} phim có độ phổ biến <= 0 để hiển thị trục log.")

				fig_scatter = px.scatter(
					scatter_plot_df,
				x="popularity",
				y="vote_average",
				color="Nhóm phim",
				color_discrete_sequence=PALETTE,
				hover_name="title",
				opacity=0.6,
				title="Mối quan hệ giữa độ nổi tiếng và điểm số thực tế",
				labels={"popularity": "Độ phổ biến", "vote_average": "Điểm đánh giá trung bình"},
			)
				fig_scatter.update_xaxes(type="log")
				fig_scatter.update_traces(marker={"size": 8})
				st.plotly_chart(ap_dung_giao_dien_plotly(fig_scatter), use_container_width=True)

	with c2:
		corr_cols = ["popularity", "vote_count", "vote_average", "budget", "revenue"]
		corr_df = movies_loc[corr_cols].dropna()
		if corr_df.empty:
			st.info("Không đủ dữ liệu để vẽ ma trận tương quan.")
		else:
			fig, ax = plt.subplots(figsize=(7, 5))
			fig.patch.set_facecolor(CHART_BG)
			ax.set_facecolor(CHART_BG)
			sns.heatmap(
				corr_df.corr(numeric_only=True),
				annot=True,
				fmt=".2f",
				cmap="RdBu_r",
				cbar=True,
				ax=ax,
			)
			ax.set_title("Ma trận tương quan giữa chất lượng và tài chính")
			ax.tick_params(colors=TEXT_DARK)
			st.pyplot(fig)

	box_df = genres_loc.merge(
		movies_loc[["show_id", "vote_average"]], on="show_id", how="left"
	).dropna(subset=["vote_average"])
	if box_df.empty:
		st.info("Không có dữ liệu để vẽ phân bố điểm số theo thể loại.")
	else:
		fig_box = px.box(
			box_df,
			x="the_loai",
			y="vote_average",
			points=False,
			title="Phân bố điểm số theo từng thể loại",
			labels={"the_loai": "Thể loại", "vote_average": "Điểm đánh giá trung bình"},
			color_discrete_sequence=[NETFLIX_TEAL],
		)
		fig_box.update_layout(xaxis={"categoryorder": "total descending"})
		st.plotly_chart(ap_dung_giao_dien_plotly(fig_box), use_container_width=True)


def ve_tab_tai_chinh(movies_loc: pd.DataFrame, genres_loc: pd.DataFrame) -> None:
	st.subheader("Hiệu quả đầu tư")

	c1, c2 = st.columns(2)

	with c1:
		roi_df = movies_loc[(movies_loc["budget"] > 0) & (movies_loc["revenue"] > 0)].copy()
		roi_df["roi"] = roi_df["revenue"] / roi_df["budget"]
		roi_top = roi_df.sort_values("roi", ascending=False).head(10)
		if roi_top.empty:
			st.info("Không có dữ liệu ROI hợp lệ sau khi lọc.")
		else:
			fig_roi = px.bar(
				roi_top.sort_values("roi", ascending=True),
				x="roi",
				y="title",
				orientation="h",
				color="roi",
				color_continuous_scale=["#FFD6D9", NETFLIX_RED],
				title="Top 10 phim có tỷ lệ lợi nhuận (ROI) cao nhất",
				labels={"roi": "Tỷ lệ lợi nhuận (ROI)", "title": "Tên phim"},
			)
			fig_roi.update_xaxes(
				type="log",
				exponentformat="power",
				showexponent="all",
				dtick=1,
				showgrid=True,
				gridcolor="#D9D9D9",
				griddash="dash",
			)
			st.plotly_chart(ap_dung_giao_dien_plotly(fig_roi), use_container_width=True)

	with c2:
		budget_df = genres_loc.merge(
			movies_loc[["show_id", "release_year", "budget"]], on="show_id", how="left"
		)
		budget_df = budget_df[budget_df["budget"] > 0]
		if budget_df.empty:
			st.info("Không có dữ liệu ngân sách để phân tích theo năm.")
		else:
			top_genres = (
				budget_df["the_loai"].value_counts().head(6).index.tolist()
			)
			budget_df = budget_df[budget_df["the_loai"].isin(top_genres)]
			budget_year = (
				budget_df.groupby(["release_year", "the_loai"], as_index=False)["budget"]
				.mean()
				.rename(columns={"release_year": "Năm", "the_loai": "Thể loại", "budget": "Ngân sách trung bình"})
			)
			fig_line = px.line(
				budget_year,
				x="Năm",
				y="Ngân sách trung bình",
				color="Thể loại",
				color_discrete_sequence=PALETTE,
				title="Ngân sách trung bình đầu tư cho mỗi thể loại qua các năm",
			)
			st.plotly_chart(ap_dung_giao_dien_plotly(fig_line), use_container_width=True)

	bubble_df = (
		movies_loc[movies_loc["budget"] > 0]
		.groupby("language_name", as_index=False)
		.agg(
			ngan_sach_tb=("budget", "mean"),
			doanh_thu_tb=("revenue", "mean"),
			so_luong_phim=("show_id", "nunique"),
		)
		.rename(columns={"language_name": "Nhóm ngôn ngữ"})
	)
	if bubble_df.empty:
		st.info("Không có dữ liệu để vẽ biểu đồ bong bóng ngôn ngữ.")
	else:
		fig_bubble = px.scatter(
			bubble_df,
			x="ngan_sach_tb",
			y="doanh_thu_tb",
			size="doanh_thu_tb",
			color="Nhóm ngôn ngữ",
			hover_data=["so_luong_phim"],
			color_discrete_sequence=PALETTE,
			title="Ngân sách và doanh thu theo từng nhóm ngôn ngữ",
			labels={
				"ngan_sach_tb": "Ngân sách trung bình",
				"doanh_thu_tb": "Doanh thu trung bình",
				"so_luong_phim": "Số lượng phim",
			},
		)
		st.plotly_chart(ap_dung_giao_dien_plotly(fig_bubble), use_container_width=True)


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
		director_stat = director_stat[director_stat["so_phim"] >= 2]
		if director_stat.empty:
			st.info("Không đủ dữ liệu để đánh giá đạo diễn (cần tối thiểu 2 phim/đạo diễn).")
		else:
			fig_director = px.scatter(
				director_stat,
				x="doanh_thu_trung_binh",
				y="diem_danh_gia_trung_binh",
				size="so_phim",
				hover_name="dao_dien",
				color="diem_danh_gia_trung_binh",
				color_continuous_scale=["#D8F3F3", NETFLIX_TEAL],
				title="Những đạo diễn nào mát tay nhất?",
				labels={
					"doanh_thu_trung_binh": "Doanh thu trung bình",
					"diem_danh_gia_trung_binh": "Điểm đánh giá trung bình",
					"so_phim": "Số phim",
					"dao_dien": "Đạo diễn",
				},
			)
			st.plotly_chart(ap_dung_giao_dien_plotly(fig_director), use_container_width=True)

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
			st.info("Không có dữ liệu diễn viên sau khi lọc.")
		else:
			fig_cast = px.bar(
				cast_stat,
				x="Tổng doanh thu",
				y="Diễn viên",
				orientation="h",
				color="Tổng doanh thu",
				color_continuous_scale=["#FFD6D9", NETFLIX_RED],
				title="Những diễn viên thường xuất hiện trong các phim bom tấn",
			)
			st.plotly_chart(ap_dung_giao_dien_plotly(fig_cast), use_container_width=True)

	st.markdown("### Đặc điểm chủ đề của các phim thành công (Điểm > 8.0)")
	text_df = movies_loc[movies_loc["vote_average"] > 8.0]["description"].dropna()
	van_ban = " ".join(text_df.astype(str).tolist())
	if not van_ban.strip():
		st.info("Không có đủ mô tả phim để tạo Word Cloud.")
	else:
		cloud = WordCloud(
			width=1400,
			height=450,
			background_color="white",
			colormap="Reds",
			max_words=120,
		).generate(van_ban)
		fig, ax = plt.subplots(figsize=(14, 4.5))
		fig.patch.set_facecolor(CHART_BG)
		ax.set_facecolor(CHART_BG)
		ax.imshow(cloud, interpolation="bilinear")
		ax.axis("off")
		st.pyplot(fig)


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
			background: #FFD6D9 !important;
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

	st.caption(
		"Bức tranh toàn cảnh về chất lượng nội dung, hiệu quả tài chính và ảnh hưởng toàn cầu của Netflix"
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
		st.warning("Không có dữ liệu sau khi áp dụng bộ lọc. Vui lòng nới điều kiện lọc.")
		st.stop()

	hien_thi_kpi(movies_loc, genres_loc)
	tab1, tab2, tab3, tab4 = st.tabs(
		[
			"Toàn cảnh Netflix toàn cầu",
			"Chất lượng và sự đón nhận",
			"Hiệu quả đầu tư",
			"Góc nhìn sáng tạo",
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
