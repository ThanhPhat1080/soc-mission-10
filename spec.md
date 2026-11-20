# Đặc tả sản phẩm — Mission 10: Chuyến du hành cùng Gia Huy

**Phiên bản:** 1.0 — 18/11/2026  
**Trạng thái:** Đặc tả trước khi xây dựng game  
**Đối tượng:** Gia Huy (Sóc), 10 tuổi, cùng bạn bè và các em nhỏ hơn

## 1. Tóm tắt

Game sinh nhật HTML5 chạy cục bộ trên laptop, kết nối TV/máy chiếu qua HDMI. Quản trò điều hành bằng chuột; các bé cùng nghe câu hỏi, thảo luận, trả lời và đoán từ khóa. Trải nghiệm mang chủ đề phi hành gia, có 10 ô nhiệm vụ, hiệu ứng mở chữ và màn kết thúc chúc mừng.

Thiệp tham khảo cung cấp cảm hứng về màu sắc, bố cục vũ trụ và nhân vật phi hành gia. Nội dung ngày giờ, địa điểm trên thiệp không thuộc dữ liệu game.

## 2. Mục tiêu thiết kế

- Trẻ em nhìn rõ nội dung khi chiếu lên màn hình lớn.
- Quản trò điều khiển đơn giản, chủ động xác nhận câu trả lời.
- Tạo nhịp chơi vui vẻ bằng hiệu ứng vừa đủ rõ, không làm rối màn hình.
- Câu hỏi, hình minh họa, nhạc và ảnh có thể được gia đình bổ sung sau.
- Chạy tại chỗ trong trình duyệt, không cần tài khoản hay kết nối mạng.

## 3. Người dùng và thiết bị

- **Quản trò:** chọn ô, mở câu hỏi/hint, xác nhận đúng và mở đáp án cuối.
- **Người chơi:** nhóm trẻ khoảng 10 tuổi và các em nhỏ hơn; cùng trả lời bằng lời nói.
- **Thiết bị:** laptop chạy trình duyệt hiện đại, xuất hình và âm thanh ra TV qua HDMI.
- **Hiển thị:** ưu tiên màn hình ngang 16:9, có khả năng co giãn với kích thước khác.

## 4. Luồng trải nghiệm

1. **Chào mừng:** tiêu đề “Mission 10 — Chuyến du hành cùng Gia Huy”, nhân vật phi hành gia chibi vẫy tay và nút “Bắt đầu nhiệm vụ”.
2. **Bảng nhiệm vụ:** 10 ô lớn chưa mở. Quản trò chọn ô bất kỳ.
3. **Câu hỏi:** câu hỏi hiện trong popup chiếm gần toàn màn hình. Có thể có ảnh đi kèm. Quản trò điều khiển các gợi ý của câu hỏi nếu bộ câu sau này có cung cấp.
4. **Trả lời:** các bé trả lời trực tiếp; game không thu âm và không chấm giọng nói.
5. **Xác nhận đúng:** quản trò bấm “Đúng rồi!”. Có hiệu ứng mở thẻ, âm thanh hurray và chữ cái được lộ ra.
6. **Trở về bảng:** câu hỏi đóng; ô đã mở được đánh dấu. Chữ bí mật hiện ở vị trí xáo trộn.
7. **Đoán từ khóa:** sau khi mở đủ 10 ô, các bé nhìn các chữ và cùng đánh vần/đoán. Nút “Hint” cuối game chỉ xuất hiện ở giai đoạn này và nội dung hint chỉ hiện khi quản trò bấm.
8. **Công bố đáp án:** khi các bé đã đoán, quản trò bấm “Đáp án”. Các chữ chuyển động, sắp xếp thành “SQUIRREL10”.
9. **Chúc mừng:** tên lửa lớn bay từ cạnh dưới màn hình lên cao, có vệt lửa; dòng “Happy birthday, Gia Huy” xuất hiện với hiệu ứng. Phát tiếng vỗ tay và lời chúc Happy Birthday vui nhộn, sau đó nhạc Happy Birthday nổi lên. Có thể nối sang slideshow ảnh do gia đình cung cấp.

## 5. Màn hình và trạng thái

### 5.1 Màn hình mở đầu

- Tiêu đề sự kiện và tên Gia Huy/Sóc.
- Phi hành gia chibi dựa trên ảnh nhân vật chính; số 10 ở trước ngực, hoạt ảnh vẫy tay.
- Nút bắt đầu rõ ràng, dễ bấm.

### 5.2 Bảng nhiệm vụ

- 10 ô đánh số, bố trí dạng lưới dễ quan sát.
- Trạng thái trực quan: chưa mở / đang chọn / đã hoàn thành.
- Khu vực trung tâm cho nhân vật và bảng chữ bí mật.
- Không hiển thị chữ trước khi ô tương ứng được mở.

### 5.3 Popup câu hỏi

- Phủ gần toàn màn hình để trẻ tập trung.
- Vùng chữ câu hỏi lớn; ảnh minh họa tùy chọn.
- Nút điều khiển quản trò: “Gợi ý 1”, “Gợi ý 2” (chỉ khi câu có gợi ý), “Đúng rồi!”, “Đóng câu hỏi”.
- Đáp án có thể được quản trò nói ra; bộ câu hỏi sẽ do gia đình cung cấp sau.

### 5.4 Màn đoán từ khóa

- Chỉ chuyển sang khi đủ 10 ô đã mở.
- Hiện 10 chữ theo thứ tự xáo trộn; các bé tự đánh vần và suy luận.
- Nút “Hint” hiện ở giai đoạn này; hint chưa lộ cho tới khi quản trò bấm nút.
- Nút “Đáp án” để công bố sau khi nhóm đã đoán.

### 5.5 Màn chúc mừng

- Chữ cái tự xếp thành **SQUIRREL10** với chuyển động rõ ràng, có điểm dừng.
- Tên lửa hoạt ảnh kích thước lớn bay lên từ đáy màn hình, đuôi lửa/sao kéo theo.
- Tiêu đề “Happy birthday, Gia Huy” xuất hiện nổi bật.
- Âm thanh theo trình tự: tiếng vỗ tay + lời chúc vui nhộn, sau đó nhạc Happy Birthday.
- Màn hình kết thúc có thể chuyển sang slideshow gia đình.

## 6. Quy tắc chữ bí mật

- Từ khóa: **S – Q – U – I – R – R – E – L – 1 – 0**.
- Mỗi ô nhiệm vụ mở đúng một ký tự.
- Mười ký tự được phân bố lộn xộn trên bảng; người chơi phải quan sát và đánh vần.
- Hai chữ R là hai ô riêng; ký tự cuối là số 1 và số 0.
- Khi công bố, các ô chuyển vị trí để tạo thành “SQUIRREL10”.

## 7. Điều khiển quản trò

**Có:** chọn ô, mở/đóng câu hỏi, mở hint của câu (nếu có), xác nhận trả lời đúng, mở hint cuối game, công bố đáp án.

**Không đưa vào phạm vi:** điều khiển âm lượng/tắt tiếng trong game; bỏ qua câu; mở ô hỗ trợ; kết thúc sớm. Âm thanh phát qua TV bằng HDMI.

## 8. Nội dung và tài nguyên do gia đình cung cấp

- Bộ 10 câu hỏi cùng đáp án và hint nếu cần.
- Hình minh họa cho từng câu hỏi.
- Ảnh rõ mặt Gia Huy để làm nhân vật chibi.
- Nhạc nền thông thường, hiệu ứng hurray, tiếng vỗ tay/lời chúc, bài Happy Birthday.
- Ảnh slideshow, thứ tự ảnh và thời lượng mong muốn.
- Nội dung hint cuối game.

Đặc tả này không tự điền bộ câu hỏi. Nội dung câu hỏi và hình ảnh sẽ do gia đình cung cấp.

## 9. Định hướng giao diện

Ba hướng mẫu được đính kèm dưới dạng trang xem trước:

1. **Mission Control:** xanh navy và vàng kem, gần với thiệp tham khảo; cảm giác phi hành gia cổ điển.
2. **Cosmic Arcade:** tím/xanh điện, sáng và năng động; phù hợp không khí trò chơi.
3. **Storybook Space:** nền kem, xanh dịu, hình minh họa mềm; tạo cảm giác thân thiện với các em nhỏ.

Khuyến nghị chọn **Mission Control** làm hướng chính vì bám sát thiệp mời và dễ nhìn khi chiếu TV. Có thể mượn các điểm nhấn chuyển động vui nhộn của Cosmic Arcade.

## 10. Ngoài phạm vi giai đoạn đặc tả

- Soạn câu hỏi hoặc minh họa câu hỏi.
- Tạo nhân vật chibi từ ảnh khi ảnh chưa được cung cấp.
- Tích hợp nhạc/âm thanh/slideshow khi chưa có tệp nguồn.
- Nhận diện giọng nói, chấm điểm tự động, lưu bảng điểm.

## 11. Tiêu chí hoàn thành bản game

- Quản trò có thể mở 10 ô theo thứ tự tùy chọn và xác nhận từng câu đúng.
- Mỗi ô chỉ mở một ký tự đúng một lần; tiến độ hiển thị rõ.
- Popup câu hỏi có thể đóng để trở về bảng.
- Hint cuối không lộ cho đến khi được bấm.
- Nút “Đáp án” kích hoạt sắp xếp chữ, hoạt ảnh tên lửa, dòng chúc mừng và chuỗi âm thanh theo đúng thứ tự.
- Tên lửa, chữ và nút đủ lớn để thấy từ khoảng cách phòng tiệc.
- Âm thanh phát qua đầu ra HDMI của máy tính.

