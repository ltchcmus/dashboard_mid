# Objective
Sua treemap ngon ngu de khong con cam giac zoom full 1 ngon ngu sau click, va doi mau cua treemap sang scale log thay vi gia tri goc.

# Context
User bao treemap ngon ngu van bi zoom full tile khi click; dong thoi muon mau scale theo log.

# Final Prompt
- Treemap ngon ngu khong duoc phu thuoc vao filter ngon ngu dang chon (de van nhin thay day du ngon ngu khac va click tiep).
- Color cua treemap dung cot log10(count) thay vi count truc tiep.
- Colorbar hien theo don vi goc (10^x) de doc de hon.

# Expected Output
- Click English khong lam treemap chi con 1 o full do du lieu dau vao van day du ngon ngu.
- Mau treemap duoc tinh theo log scale.
- Van giu co che click-to-filter ngon ngu.