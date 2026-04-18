# Objective
Cap nhat dashboard theo feedback UX moi:
1) Donut Q4 can hien thi callout co duong noi ro rang cho slice nho.
2) Them dropdown Quoc gia o sidebar, dat ben tren dropdown The loai.
3) Bo toan bo phan insight button va cac dong caption storytelling duoc chi dinh.

# Context
- Du an: Streamlit dashboard Netflix
- File chinh sua: src/main.py
- Yeu cau UI tap trung vao do de doc va don gian hoa bo cuc noi dung

# Final Prompt
"1. O donut chart, slice xuat sac da duoc callout o ngoai, tuy nhien khong thay co duong noi gi vao slice de bieu thi no thuoc slice nao.
2. toi muon them 1 drop down filter nam o tren drop down the loai de chon Quoc gia.
3. toi muon bo toan bo cac button insight. bo di cac dong sau trong dashboard:
Buc tranh toan canh ve chat luong noi dung, hieu qua tai chinh va anh huong toan cau cua Netflix
Tab nay tra loi: ..."

# Expected Output
- Donut Q4 dung outside label de hien thi callout ro rang voi connector line.
- Sidebar co dropdown "Quoc gia" dat truoc "The loai", bo loc van hoat dong dung theo show_id.
- Xoa toan bo st.expander("💡 Insight chính") va 5 dong caption bi yeu cau.
- src/main.py compile OK, khong loi syntax.
