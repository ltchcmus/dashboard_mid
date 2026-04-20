# Objective
Soan noi dung report hoc thuat bang LaTeX cho cac phan: du lieu, tien xu ly, sau tien xu ly, features, va EDA; dam bao bam sat dung quy trinh nhom da thuc hien trong codebase.

# Context
- Du an dashboard_mid cho mon Data Visualization.
- Du lieu goc: data/raw/netflix_movies_detailed_up_to_2025.csv.
- Pipeline da duoc the hien ro trong notebooks/preprocessing.ipynb, notebooks/EDA.ipynb, notebooks/eda_export_images.ipynb, src/main.py va netflix_presentation_slides.md.
- Can van phong hoc thuat, ro rang, tranh van phong may moc.

# Final Prompt
"#codebase Day la tong quan do an giua ki mon Data Visualization cua nhom toi. Bay gio, toi can lam report cho cac phan nhu du lieu, truoc tien xu li, sau tien xu li, cac features, eda... Ban hay phan tich, nghien cuu cac qua trinh nay ma nhom toi da lam, sau do giup toi trinh bay cac phan nay trong bao cao mot cach day du, chi tiet, ro rang, bam sat voi nhung thu chung toi da lam nhe. Ban hay su dung Latex, trinh bay duoi dang cac section de toi copy-paste thuan tien. Ban hay dong vai tro nhu mot sinh vien xuat sac thuc hien do an, su dung tu ngu hoc thuat, chuan xac, nhung khong duoc tao cam giac \"AI generated\"."

# Expected Output
- Van ban LaTeX co cau truc section/subsection day du.
- Trinh bay so lieu before/after preprocessing va giai thich logic xu ly.
- Mo ta feature schema, bridge tables, feature engineering va cac EDA insight chinh.
- Noi dung khop voi code va dataset hien co trong repo.