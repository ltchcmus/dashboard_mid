# Request Summary

Tách toàn bộ src/main.py thành các module chuyên trách và chuyển phần cấu hình/ thông số sang config.yaml, đọc bằng YAML.

# Files Changed

- config.yaml
- README.md
- src/main.py
- src/config/**init**.py
- src/config/app_config.py
- src/services/**init**.py
- src/services/data_loader.py
- src/services/filter_state.py
- src/services/filters.py
- src/services/kpi.py
- src/tabs/**init**.py
- src/tabs/overview.py
- src/tabs/quality.py
- src/tabs/finance.py
- src/tabs/creative.py
- src/utils/dataframe.py
- src/utils/formatting.py
- src/utils/i18n.py
- src/utils/style.py
- src/utils/ui.py
- src/visualization/theme.py
- src/prompts/2026-04-28-refactor-config-yaml.md

# Key Decisions

- Dùng config.yaml ở root để gom màu sắc, palettes, mappings, thresholds, và theme.
- Tách logic theo nhóm: utils (format/i18n/style), services (data/filter/kpi), tabs (4 tab UI), visualization (plotly theme).
- Entry point src/main.py chỉ điều phối config, load data, filters và render tabs.

# Next Steps

- Chạy thử Streamlit để xác thực import và cache hoạt động.
- Nếu cần, đưa thêm thông số chart vào config.yaml để tinh chỉnh sâu hơn.
