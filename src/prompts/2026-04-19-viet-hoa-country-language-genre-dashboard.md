# Objective
- Convert country, language, and genre values to Vietnamese in the dashboard and update dashboard header/title to Vietnamese.

# Context
- User requested pure Vietnamese display for language, genre, and country fields used in filters/charts.
- Existing dataset values are mostly English.
- Map chart must remain functional while labels are shown in Vietnamese.

# Final Prompt
với cái cột ngôn ngữ, với thể loại, quốc gia á, đang được sử dụng tiếng anh, nhưng đề yêu cầu dùng thuần tiếng việt không biết nó có dịch được hết sang tiếng việt không nhỉ, nếu được bạn có thể giúp tôi convert lại data cột đó sang tiếng việt rồi render lên dashboar cũng tiếng việc không, cái header dashboard cũng sửa lại thành tiếng việt không

# Expected Output
- Runtime Vietnamese translation layer for language, genre, country fields in dashboard.
- Choropleth map still working (use English internal location while showing Vietnamese labels).
- Dashboard page title/header changed to Vietnamese.
- Requirements updated for localization support libraries.
