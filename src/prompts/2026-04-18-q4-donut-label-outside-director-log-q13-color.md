# Objective
Tinh chinh sua giao dien va ma hoa mau cho dashboard theo feedback:
- Q4 donut: label nho hien thi de doc hon va sap xep thu tu theo logic chat luong.
- Tab sang tao chart dao dien: dung log scale cho truc doanh thu trung binh, bo ma hoa mau theo diem danh gia.
- Q13: bar chart dung mau theo bien da dinh nghia, khong hardcode.

# Context
- File chinh sua: src/main.py
- Dashboard Streamlit + Plotly
- Yeu cau UX: giu kha nang doc khi nhom du lieu nho, giu quy uoc mau nhat quan

# Final Prompt
"o Q4, donut, vi nhom xuat sac kha nho, khong nhin thay chu thich. co cach nao voi cho nho thi chu thich ben ngoai donut khong? label sort toi muon theo logic tu xuat sac den kem. o tab sang tao, chart dao dien muon log scale truc doanh thu trung binh, khong can chu thich thang log. o bieu do nay, khong can encode mau gradient theo diem danh gia. o Q13, bar chart chua dung mau chuan theo bien da dinh nghia, chinh lai."

# Expected Output
- Q4 donut hien thi label/percent ro rang hon voi nhom nho, thu tu bucket: Xuat sac -> Tot -> Kha -> TB -> Kem.
- Director scatter dung x-axis log, marker mot mau tu he bien; khong con gradient theo diem.
- Q13 bar dung mau tu bien semantic token da khai bao.
- Code compile OK, khong loi trong src/main.py.
