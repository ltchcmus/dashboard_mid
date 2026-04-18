# Objective
Cai tien chia nhom ngan sach Q5 (tab 2) bang cach them rank truoc qcut de giam hien tuong bi roi bot bin khi gia tri budget trung lap nhieu.

# Context
User yeu cau "them rank khi chia bins de bo bot su drop". Truoc do dung qcut truc tiep tren budget voi duplicates='drop', co the lam giam so nhom.

# Final Prompt
- Tinh `budget_rank = hist_df['budget'].rank(method='first')`.
- Dung `pd.qcut(budget_rank, q=4, labels=False)` thay cho qcut truc tiep tren budget.
- Giu nguyen labels Q1..Q4 va nhom diem so.

# Expected Output
- Q5 on dinh hon ve so luong nhom ngan sach (it bi drop bin do duplicate values).
- Van giu dung nghia chia theo tu phan vi.