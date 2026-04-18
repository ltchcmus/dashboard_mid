# Objective
Can chinh bubble chart tab Tai chinh de focus pham vi 10^7 den 10^9 tren ca hai truc; dong thoi chuan hoa dieu kien tinh ROI de loai bo cac phim co budget/revenue bang 0 va bo loc nguong budget.

# Context
User muon:
- Bubble chart tap trung vao vung 1 ti (theo moc 10^x), khong hien thi qua nhieu vung ngoai quan trong.
- ROI chi tinh voi phim co revenue > 0 va budget > 5,000 USD.

# Final Prompt
1) O bubble chart tab 3, set scale focus cho ca truc x/y trong khoang 10^7 -> 10^9.
2) Khi tinh ROI, chi tinh cac phim co budget > 5,000 va revenue > 0.

# Expected Output
- Bubble chart co truc log x/y cung range [10^7, 10^9], duong y=x can doi va de quan sat.
- Tat ca diem tinh ROI trong dashboard de duoc loc dieu kien budget > 5,000 va revenue > 0.