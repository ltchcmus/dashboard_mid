# Objective
Điều chỉnh Q13 để trục điểm đánh giá trung bình dễ nhìn biến thiên hơn và loại bỏ hoàn toàn Q10 khỏi Tab 3.

# Context
- Q13 hiện đặt trục Y phải cố định [0,10] khiến đường điểm nhìn phẳng, khó quan sát thay đổi nhỏ.
- Người dùng yêu cầu xóa Q10 ở tab tài chính.

# Final Prompt
Ở Q13 muốn trục điểm đánh giá scale rộng ra để dễ nhìn thay đổi; đồng thời bỏ đi Q10 ở tab 3.

# Expected Output
- Q13 dùng dynamic range cho trục Y phải dựa trên min/max điểm trung bình, có padding an toàn.
- Q10 (box plot ROI theo thể loại) bị xóa khỏi Tab 3.
- Mã compile thành công.