# Request Summary

User requested adding a feature-summary view before describing data preprocessing and asked for one visual image about features.

# Files Changed

- notebooks/eda_export_images.ipynb
- netflix_presentation_slides.md
- src/prompts/2026-04-19-feature-summary-image-before-preprocessing.md
- docs/ai/2026-04-19-feature-summary-image-before-preprocessing.md

# Key Decisions

- Added a new notebook chart cell that visualizes raw features by completeness and feature group.
- Exported new image file: data/outputs/slides/eda_images/00_feature_overview_raw.png.
- Inserted new subsection "Slide 4A - Summary feature trước tiền xử lý" before preprocessing slide, including the embedded image and speaking points.

# Next Steps

1. If needed, simplify the legend labels for cleaner visual style in final deck.
2. Optionally add one table-style schema image (feature + meaning) for appendix.
3. Keep this feature-summary image immediately before missing-values slide for strongest narrative flow.
