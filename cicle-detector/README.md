# Tags
- Vision

# Nhóm 1: Các Mô Hình Phát Hiện Đối Tượng (Object Detection Models)

- Họ R-CNN (R-CNN, Fast R-CNN, Faster R-CNN, Cascade R-CNN): Các mô hình này thường tạo ra các vùng đề xuất (region proposals) và sau đó phân loại từng vùng, có thể được mở rộng để dự đoán góc nghiêng.
- Mask R-CNN: Mở rộng của Faster R-CNN, thêm khả năng segment đối tượng theo pixel. Thông tin về mask có thể giúp suy luận về độ nghiêng.
- Ultralytics YOLOv8 (Bạn liệt kê là YOLO11, có lẽ là một lỗi đánh máy): Các phiên bản YOLO gần đây (bao gồm cả v8) đã được cải thiện khả năng phát hiện các đối tượng ở nhiều góc độ khác nhau.
- SSD (Single Shot MultiBox Detector): Phát hiện đối tượng trực tiếp trên các feature map với các anchor box đa dạng, có thể phát hiện đối tượng nghiêng ở một mức độ nhất định.
- RetinaNet: Tập trung vào việc giải quyết vấn đề mất cân bằng giữa foreground và background trong quá trình huấn luyện, giúp phát hiện đối tượng chính xác hơn, bao gồm cả các trường hợp nghiêng.
- EfficientDet: Một họ các mô hình phát hiện đối tượng với sự cân bằng giữa độ chính xác và hiệu suất, có khả năng phát hiện đối tượng nghiêng.
- CenterNet: Phát hiện đối tượng bằng cách xác định trung tâm của đối tượng và các thuộc tính khác như kích thước và có thể mở rộng để dự đoán hướng.
- Vision Transformer (ViT): Mặc dù ban đầu được thiết kế cho phân loại ảnh, ViT và các biến thể của nó đã được áp dụng thành công cho phát hiện đối tượng và có tiềm năng phát hiện đối tượng nghiêng dựa trên cách chúng học các đặc trưng không gian.
- DETR (DEtection TRansformer)

# Nhóm 2: Các Thuật Toán Dựa Trên Đặc Trưng (Feature-Based Algorithms)

- SIFT (Scale-Invariant Feature Transform): Rất mạnh mẽ trong việc phát hiện các đặc trưng bất biến với tỷ lệ, xoay và một số thay đổi về góc nhìn. Các đặc trưng SIFT có thể được sử dụng để khớp các đối tượng bị nghiêng với các mẫu chuẩn.
- SURF (Speeded-Up Robust Features): Tương tự như SIFT nhưng nhanh hơn. Cũng có khả năng xử lý các thay đổi về tỷ lệ và xoay, phù hợp cho việc phát hiện đối tượng nghiêng.
- ORB (Oriented FAST and Rotated BRIEF): Một thuật toán nhanh và hiệu quả, kết hợp phát hiện điểm đặc trưng FAST (Features from Accelerated Segment Test) và mô tả đặc trưng BRIEF (Binary Robust Independent Elementary Features) với khả năng xử lý xoay.
- BRIEF (Binary Robust Independent Elementary Features): Một thuật toán mô tả đặc trưng nhị phân nhanh chóng, thường được sử dụng kết hợp với các thuật toán phát hiện điểm đặc trưng khác (ví dụ: FAST).
- FREAK (Fast Retina Keypoint): Một thuật toán phát hiện và mô tả đặc trưng lấy cảm hứng từ cách hoạt động của võng mạc, có khả năng chịu được sự thay đổi về xoay và tỷ lệ.
- KAZE (Key points from Accelerated Segment Test): Sử dụng các bộ lọc Hessian để phát hiện các điểm đặc trưng và tạo ra các mô tả dựa trên thông tin tỷ lệ, mang lại khả năng mạnh mẽ trong việc xử lý các thay đổi.
- AKAZE (Accelerated KAZE): Một phiên bản nhanh hơn của KAZE, vẫn giữ được khả năng phát hiện các đặc trưng mạnh mẽ dưới các điều kiện khác nhau.
- BRISK (Binary Robust Invariant Scalable Keypoints): Một thuật toán phát hiện và mô tả đặc trưng nhị phân nhanh chóng, có khả năng chịu được sự thay đổi về xoay và tỷ lệ.

# Nhóm 3: Các Kỹ Thuật Xử Lý Ảnh Cổ Điển (Classical Image Processing Techniques)

- Viola-Jones (chủ yếu cho phát hiện khuôn mặt): Mặc dù chủ yếu được biết đến với việc phát hiện khuôn mặt thẳng đứng, nhưng về lý thuyết, có thể được mở rộng để phát hiện các khuôn mặt nghiêng ở một mức độ nhất định bằng cách huấn luyện với nhiều góc độ khác nhau.
- HOG (Histogram of Oriented Gradients): Trích xuất các đặc trưng dựa trên hướng của gradient trong các vùng cục bộ của hình ảnh. Hữu ích cho việc phát hiện các đối tượng có hình dạng và cấu trúc nhất định, và có thể chịu được một số biến thể về hướng.
- Aggregate Channel Features (ACFs): Một framework tổng quát cho việc xây dựng các bộ phát hiện đối tượng bằng cách tổng hợp các phản hồi từ nhiều kênh đặc trưng khác nhau. Có thể được thiết kế để nhạy cảm với các đối tượng ở nhiều hướng.
- Template matching: So sánh một mẫu (template) của đối tượng không nghiêng với các vùng khác nhau trong ảnh. Có thể phát hiện đối tượng nghiêng nếu mẫu cũng được xoay theo các góc độ khác nhau để so sánh.
- Color-based matching: Sử dụng thông tin màu sắc để tìm kiếm các vùng trong ảnh có màu sắc tương tự như đối tượng mục tiêu. Ít nhạy cảm với độ nghiêng nếu màu sắc là đặc trưng chính của đối tượng.
- Shape-based recognition: Phân tích hình dạng của các đối tượng trong ảnh. Có thể được sử dụng để phát hiện các đối tượng nghiêng nếu thuật toán đủ mạnh mẽ để xử lý các biến dạng về hình dạng do góc nhìn gây ra.
- Hough transform for line detection: Phát hiện các đường thẳng trong ảnh. Nếu đối tượng có các cạnh thẳng, bạn có thể sử dụng Hough transform để xác định góc nghiêng của các cạnh này.
- Hough transform for circle detection: Phát hiện các hình tròn trong ảnh. Ít trực tiếp liên quan đến việc phát hiện đối tượng nghiêng trừ khi đối tượng có hình dạng tròn và bạn muốn xem xét sự biến dạng của hình tròn thành elip do góc nhìn.
- Canny edge detection: Một thuật toán phổ biến để phát hiện các cạnh trong ảnh. Các cạnh được phát hiện có thể là bước đầu tiên để sử dụng Hough transform hoặc các kỹ thuật phân tích hình dạng khác để xác định độ nghiêng.
- Sobel (edge detection): Một toán tử khác để phát hiện cạnh, tính toán đạo hàm bậc nhất của cường độ ảnh theo hướng ngang và dọc. Tương tự như Canny, có thể là bước tiền xử lý để phát hiện độ nghiêng.
- Laplacian of Gaussian (LoG): Một toán tử phát hiện blob và cạnh. Có thể hữu ích để xác định các điểm hoặc vùng quan tâm, nhưng không trực tiếp cung cấp thông tin về độ nghiêng.
- thuật toán matching robust như RANSAC (RANdom SAmple Consensus) 

# Tiền xử lý ảnh:
- Cải thiện độ tương phản và độ sáng: Sử dụng các kỹ thuật như Histogram Equalization, Contrast Limited Adaptive Histogram Equalization (CLAHE) để làm rõ các chi tiết trong điều kiện sáng tối.
- Giảm nhiễu: Áp dụng các bộ lọc làm mịn như Gaussian blur hoặc Median filter để giảm nhiễu mà không làm mất quá nhiều chi tiết, đặc biệt hữu ích trong điều kiện độ nét thấp.
- Tăng độ phân giải (Super-Resolution): Nếu có thể, sử dụng các thuật toán super-resolution (mặc dù có thể tốn kém về mặt tính toán) để tăng độ phân giải của ảnh trước khi đưa vào mô hình phát hiện.

# Đặc tính ảnh:
## Heatmap
 1. Center-based Heatmap: Tập trung vào trung tâm ảnh. Dùng khi bạn muốn xem mức độ "quan trọng" giả định ở giữa ảnh.
 2. Saliency Map: Dựa trên mô hình thị giác máy tính để tìm ra những vùng "nổi bật với con người" trong ảnh. Giúp xác định vùng thu hút ánh nhìn nhất (theo mô hình AI).
 3. Object Detection Heatmap: Dùng AI để xác định và tạo heatmap theo vị trí các vật thể được phát hiện (như người, xe, v.v.).
 4. Edge-based Heatmap: Tạo heatmap dựa trên biên cạnh (edges) – thường làm nổi bật hình dạng vật thể, đường viền.
 5. Color Intensity Heatmap: Tạo heatmap theo mức độ sáng/tối, độ bão hòa màu. Thích hợp khi bạn quan tâm đến ánh sáng hoặc mức độ tương phản. 