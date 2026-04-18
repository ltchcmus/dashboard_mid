# Objective
Fix hien tuong map click bi nhay select/unselect lien tuc do rerun lap lai cung mot su kien selection.

# Context
Dashboard su dung on_select='rerun' va toggle add/remove cho bo loc. Plotly co the giu nguyen selection payload qua nhieu run lien tiep, dan den toggle bi goi lap va trang thai bi dao qua lai.

# Final Prompt
- Them co che de-duplicate event selection theo tung filter key.
- Neu event signature trung voi lan truoc -> bo qua, khong toggle lai.
- Neu selection rong -> reset signature key do de cho phep click lai trong lan sau.

# Expected Output
- Click quoc gia tren map khong con nhay qua lai select/unselect.
- Toggle van dung khi user bo chon va chon lai.
- Khong gay crash session state.