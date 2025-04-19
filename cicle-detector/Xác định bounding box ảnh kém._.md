# **Các Phương Pháp Xác Định Bounding Box cho Ảnh Độ Nét Thấp, Thay Đổi Độ Sáng và Góc Nhìn**

**1\. Giới Thiệu:**

Bài toán xác định vị trí của một vật thể có hình dạng cố định trong ảnh số đặt ra nhiều thách thức khi chất lượng ảnh suy giảm do độ phân giải thấp, sự thay đổi về độ sáng và độ tương phản, cũng như sự khác biệt về góc nhìn dẫn đến hiện tượng vật thể bị nghiêng. Những yếu tố này có thể làm giảm đáng kể hiệu suất của các thuật toán phát hiện đối tượng truyền thống. Để giải quyết vấn đề này, cần có một cách tiếp cận toàn diện, kết hợp nhiều kỹ thuật xử lý ảnh và thị giác máy tính khác nhau để tăng cường chất lượng ảnh, trích xuất các đặc trưng mạnh mẽ và cuối cùng là xác định chính xác vị trí của vật thể thông qua bounding box. Báo cáo này sẽ trình bày tổng quan về các phương pháp tiềm năng, bao gồm tiền xử lý ảnh, kỹ thuật template matching, trích xuất đặc trưng, học sâu và các phương pháp kết hợp, cùng với các chỉ số đánh giá hiệu suất liên quan.

**2\. Các Kỹ Thuật Tiền Xử Lý Ảnh để Cải Thiện Chất Lượng Ảnh:**

Để chuẩn bị cho các bước phát hiện đối tượng tiếp theo, việc cải thiện chất lượng ảnh đầu vào là vô cùng quan trọng, đặc biệt đối với ảnh có độ phân giải thấp và độ tương phản kém. Các kỹ thuật tiền xử lý có thể giúp giảm nhiễu, tăng cường độ tương phản và làm nổi bật các đặc trưng quan trọng của vật thể.1

* **Các Phương Pháp Giảm Nhiễu:**  
  * **Bộ lọc trung vị (Median Filter):** Đặc biệt hiệu quả trong việc loại bỏ nhiễu dạng "muối tiêu" (salt-and-pepper noise) thường xuất hiện trong quá trình thu thập hoặc truyền tải ảnh.3 Bộ lọc này hoạt động bằng cách thay thế giá trị của mỗi pixel bằng giá trị trung vị của các pixel lân cận, giúp bảo toàn các cạnh của vật thể tốt hơn so với các bộ lọc tuyến tính khác.6 Trong trường hợp ảnh có nhiễu "muối tiêu" như được đề cập trong 3, bộ lọc trung vị được khuyến nghị sử dụng thay vì bộ lọc Gaussian. Hiệu quả của bộ lọc trung vị trong việc loại bỏ nhiễu xung (impulse noise) với ít làm mờ ảnh cũng được ghi nhận.4  
  * **Bộ lọc Gaussian:** Thích hợp để giảm nhiễu Gaussian, một loại nhiễu thường xuất hiện do các yếu tố ngẫu nhiên trong quá trình thu nhận ảnh.3 Bộ lọc này sử dụng hàm Gaussian để tính toán trọng số cho các pixel lân cận, tạo ra hiệu ứng làm mờ nhẹ, giúp giảm nhiễu. Tuy nhiên, cần lưu ý rằng việc sử dụng bộ lọc Gaussian có thể làm mờ các chi tiết quan trọng, đặc biệt trong ảnh có độ phân giải thấp.8  
  * **Các Phương Pháp Lọc Không Gian Khác:** Ngoài bộ lọc trung vị và Gaussian, còn có nhiều phương pháp lọc không gian khác có thể được sử dụng để giảm nhiễu, tùy thuộc vào đặc điểm của nhiễu trong ảnh.5  
* **Các Kỹ Thuật Tăng Cường Độ Tương Phản:**  
  * **Cân bằng histogram (Histogram Equalization):** Phương pháp này phân phối lại các mức cường độ pixel để cải thiện độ tương phản tổng thể của ảnh, đặc biệt hiệu quả khi các giá trị cường độ tập trung trong một phạm vi hẹp.3 Kỹ thuật này có thể làm cho vật thể trở nên rõ ràng hơn so với nền. Tuy nhiên, cần lưu ý rằng cân bằng histogram có thể khuếch đại nhiễu và bỏ qua các chi tiết cục bộ.11  
  * **Giãn tương phản (Contrast Stretching):** Tương tự như cân bằng histogram, giãn tương phản mở rộng phạm vi giá trị pixel để tăng độ tương phản, đặc biệt hữu ích cho ảnh có giá trị cường độ tập trung.1  
  * **Cân bằng histogram thích ứng (Adaptive Histogram Equalization \- AHE) và Cân bằng histogram thích ứng giới hạn tương phản (Contrast Limited AHE \- CLAHE):** Các phương pháp này tăng cường độ tương phản cục bộ bằng cách áp dụng cân bằng histogram cho các vùng nhỏ của ảnh. CLAHE giới hạn mức độ khuếch đại tương phản để giảm thiểu nhiễu.11 CLAHE đặc biệt phù hợp với trường hợp độ sáng thay đổi trên ảnh.3  
  * **Hiệu chỉnh Gamma (Gamma Correction):** Điều chỉnh độ sáng tổng thể của ảnh và có thể làm cho các pixel sáng hơn hoặc tối hơn.4  
* **Kỹ Thuật Tăng Độ Phân Giải (Super-Resolution):**  
  * **Nội suy (Interpolation):** Các phương pháp truyền thống như nội suy lân cận gần nhất (Nearest-Neighbor), nội suy song tuyến (Bilinear), nội suy hai lần lập phương (Bicubic) và nội suy Lanczos có thể được sử dụng để tăng kích thước ảnh.2 Tuy nhiên, các phương pháp này có thể gây ra hiện tượng mờ hoặc răng cưa.29  
  * **Siêu phân giải dựa trên học sâu (Deep Learning-based Super-Resolution):** Các mô hình học sâu như EDSR và SRCNN có khả năng khôi phục các chi tiết tốt hơn từ ảnh có độ phân giải thấp, nhưng đòi hỏi dữ liệu huấn luyện và tài nguyên tính toán lớn.2  
* **Các Thuật Toán Làm Nét Ảnh (Image Sharpening Algorithms):**  
  * **Mặt nạ làm nét không sắc (Unsharp Masking):** Tăng cường các cạnh và chi tiết nhỏ bằng cách trừ một phiên bản mờ của ảnh gốc.13  
  * **Các Kỹ Thuật Làm Nét Khác:** Các toán tử như Roberts, Sobel và Laplacian cũng có thể được sử dụng để làm nổi bật các cạnh.36

Việc lựa chọn kỹ thuật tiền xử lý phù hợp phụ thuộc vào loại nhiễu, mức độ tương phản và độ phân giải của ảnh, cũng như hình dạng và đặc điểm của vật thể cần phát hiện.42 Cần thử nghiệm và đánh giá hiệu quả của từng kỹ thuật để tìm ra phương pháp tốt nhất cho từng trường hợp cụ thể.

**Bảng 1: Tổng quan về các kỹ thuật tiền xử lý ảnh**

| Kỹ thuật | Mục đích chính | Ưu điểm | Nhược điểm |
| :---- | :---- | :---- | :---- |
| Bộ lọc trung vị | Giảm nhiễu "muối tiêu" | Bảo toàn cạnh tốt | Có thể làm mất chi tiết nhỏ |
| Bộ lọc Gaussian | Giảm nhiễu Gaussian | Làm mờ nhẹ, thường dùng trước các kỹ thuật khác | Có thể làm mờ chi tiết quan trọng |
| Cân bằng histogram | Tăng cường độ tương phản toàn cục | Đơn giản, hiệu quả khi cường độ tập trung | Có thể khuếch đại nhiễu, bỏ qua chi tiết cục bộ |
| Giãn tương phản | Tăng cường độ tương phản toàn cục | Hiệu quả khi cường độ tập trung trong một phạm vi hẹp | Tương tự cân bằng histogram |
| AHE/CLAHE | Tăng cường độ tương phản cục bộ | Phù hợp với ánh sáng thay đổi, CLAHE giảm nhiễu | Phức tạp hơn cân bằng histogram toàn cục |
| Hiệu chỉnh Gamma | Điều chỉnh độ sáng tổng thể | Đơn giản, có thể làm sáng hoặc tối ảnh | Không cải thiện độ tương phản cục bộ |
| Nội suy | Tăng độ phân giải | Đơn giản, dễ thực hiện | Có thể gây mờ, răng cưa |
| Siêu phân giải học sâu | Tăng độ phân giải | Khôi phục chi tiết tốt hơn | Đòi hỏi dữ liệu huấn luyện và tài nguyên tính toán |
| Mặt nạ làm nét không sắc | Tăng cường cạnh và chi tiết nhỏ | Làm nổi bật đường viền | Có thể khuếch đại nhiễu, tạo halo |
| Các kỹ thuật làm nét khác | Tăng cường cạnh | Nhấn mạnh đường biên của vật thể | Có thể nhạy cảm với nhiễu |

**3\. Kỹ Thuật Phát Hiện Đối Tượng Dựa Trên Mẫu (Template Matching):**

Template matching là một kỹ thuật cơ bản trong thị giác máy tính, được sử dụng để tìm kiếm các phần của ảnh đầu vào khớp với một ảnh mẫu (template) cho trước.43 Kỹ thuật này hoạt động bằng cách trượt ảnh mẫu trên ảnh đầu vào và tính toán một độ đo tương tự tại mỗi vị trí. Vị trí có độ tương tự cao nhất được coi là vị trí tìm thấy đối tượng.

* **Các Phương Pháp Template Matching trong OpenCV:** OpenCV cung cấp nhiều phương pháp template matching khác nhau, bao gồm 52:  
  * **TM\_SQDIFF và TM\_SQDIFF\_NORMED:** Tính tổng bình phương sai khác giữa ảnh mẫu và vùng ảnh. Giá trị nhỏ nhất chỉ ra sự khớp tốt nhất.  
  * **TM\_CCORR và TM\_CCORR\_NORMED:** Tính tương quan chéo giữa ảnh mẫu và vùng ảnh. Giá trị lớn nhất chỉ ra sự khớp tốt nhất.  
  * **TM\_CCOEFF và TM\_CCOEFF\_NORMED:** Tính hệ số tương quan giữa ảnh mẫu và vùng ảnh. Giá trị lớn nhất gần 1 chỉ ra sự khớp tốt nhất. Các phương pháp có hậu tố "\_NORMED" thường được ưu tiên hơn vì chúng đã được chuẩn hóa, giúp giảm độ nhạy cảm với sự thay đổi độ sáng và độ tương phản.43 Đặc biệt, normalized cross-correlation (NCC) được chứng minh là bất biến với những thay đổi về độ sáng toàn cục.47  
* **Xử Lý Biến Thể về Độ Sáng và Độ Tương Phản:** Các phương pháp template matching chuẩn hóa (như TM\_CCORR\_NORMED, TM\_CCOEFF\_NORMED, NCCOEFF) có khả năng xử lý tốt hơn sự thay đổi về độ sáng và độ tương phản so với các phương pháp không chuẩn hóa.43  
* **Xử Lý Biến Thể về Độ Nghiêng:** Template matching truyền thống rất nhạy cảm với sự thay đổi về góc nhìn và độ nghiêng.43 Để xử lý vấn đề này, có thể áp dụng các cách tiếp cận sau:  
  * **Xoay ảnh mẫu:** Tạo nhiều phiên bản của ảnh mẫu đã được xoay ở các góc độ khác nhau và thực hiện template matching với từng phiên bản.67  
  * **Sử dụng các đặc trưng bất biến với phép xoay:** Các phương pháp trích xuất đặc trưng như SIFT, SURF và ORB (sẽ được thảo luận trong phần sau) có khả năng đối phó với sự thay đổi về góc nhìn tốt hơn.  
  * **Template matching dựa trên hình dạng (Grayscale-based Matching):** Một số thuật toán template matching nâng cao có thể xử lý sự thay đổi về hướng.47  
  * **Chuyển đổi sang tọa độ cực:** Chuyển đổi ảnh và mẫu sang hệ tọa độ cực có thể biến đổi phép xoay thành phép tịnh tiến, giúp việc tìm kiếm trở nên dễ dàng hơn.67  
  * **Sử dụng các hàm phân biệt tổng hợp (Synthetic Discriminant Functions):** Tạo một mẫu tổng hợp từ các phiên bản đã xoay của ảnh mẫu.67  
* **Xử Lý Biến Thể về Độ Phân Giải Thấp:** Template matching rất nhạy cảm với sự khác biệt về kích thước giữa ảnh mẫu và đối tượng trong ảnh.43 Để giải quyết vấn đề này, có thể sử dụng kỹ thuật **template matching đa tỷ lệ (Multi-Scale Template Matching)**.70 Kỹ thuật này bao gồm việc tạo ra nhiều phiên bản của ảnh hoặc ảnh mẫu ở các tỷ lệ khác nhau và thực hiện template matching trên tất cả các tỷ lệ này.

Mặc dù template matching là một phương pháp đơn giản và dễ thực hiện, nhưng nó có nhiều hạn chế, đặc biệt khi đối tượng có sự thay đổi đáng kể về độ sáng, góc nhìn hoặc bị che khuất.43

**Bảng 2: So sánh các phương pháp template matching**

| Phương pháp | Độ nhạy sáng | Độ nhạy tương phản | Độ nhạy xoay | Chi phí tính toán |
| :---- | :---- | :---- | :---- | :---- |
| TM\_SQDIFF | Cao | Cao | Cao | Thấp |
| TM\_SQDIFF\_NORMED | Thấp | Thấp | Cao | Trung bình |
| TM\_CCORR | Cao | Cao | Cao | Thấp |
| TM\_CCORR\_NORMED | Thấp | Thấp | Cao | Trung bình |
| TM\_CCOEFF | Trung bình | Trung bình | Cao | Trung bình |
| TM\_CCOEFF\_NORMED | Thấp | Thấp | Cao | Trung bình |

**4\. Thuật Toán Trích Xuất Đặc Trưng (Feature Extraction):**

Để vượt qua những hạn chế của template matching, đặc biệt là khả năng xử lý sự thay đổi về ánh sáng và góc nhìn, các thuật toán trích xuất đặc trưng có thể được sử dụng.45 Các thuật toán này tìm kiếm các điểm hoặc vùng đặc biệt trong ảnh (được gọi là các đặc trưng hoặc điểm quan tâm) mà ít bị ảnh hưởng bởi các biến đổi như thay đổi độ sáng, góc nhìn và tỷ lệ.

* **Các Thuật Toán Trích Xuất Đặc Trưng Phổ Biến:**  
  * **SIFT (Scale-Invariant Feature Transform):** Là một thuật toán mạnh mẽ, bất biến với tỷ lệ, xoay và có khả năng chịu được một số thay đổi về ánh sáng.61 SIFT phát hiện các điểm quan tâm bằng cách tìm cực trị cục bộ trong không gian tỷ lệ và mô tả chúng bằng histogram của hướng gradient cục bộ.  
  * **SURF (Speeded-Up Robust Features):** Nhanh hơn SIFT và cũng có khả năng chịu được một số biến đổi.61 SURF sử dụng ma trận Hessian để phát hiện điểm quan tâm và các đặc trưng Haar wavelet để mô tả chúng.  
  * **ORB (Oriented FAST and Rotated BRIEF):** Hiệu quả về mặt tính toán và bất biến với phép xoay.61 ORB sử dụng FAST để phát hiện điểm quan tâm và BRIEF để mô tả chúng, đồng thời thêm khả năng bất biến với phép xoay bằng cách tính toán hướng của các điểm này.  
  * **Các Thuật Toán Khác:** Ngoài SIFT, SURF và ORB, còn có nhiều thuật toán trích xuất đặc trưng khác như AKAZE, BRISK và FREAK, mỗi thuật toán có những ưu nhược điểm riêng về độ mạnh mẽ và hiệu quả tính toán.80  
* **Xác Định Vị Trí Đối Tượng Bằng Cách So Khớp Đặc Trưng:** Sau khi trích xuất các đặc trưng từ cả ảnh mẫu và ảnh đầu vào, bước tiếp theo là so khớp các đặc trưng này để tìm ra sự tương ứng giữa chúng.80 Các thuật toán so khớp đặc trưng như Brute-Force hoặc FLANN (Fast Library for Approximate Nearest Neighbors) thường được sử dụng cho mục đích này.81 Sau khi tìm được các cặp đặc trưng tương ứng, có thể sử dụng các kỹ thuật như RANSAC (RANdom SAmple Consensus) để loại bỏ các điểm ngoại lai và ước tính một phép biến đổi hình học (ví dụ: phép homography) để xác định vị trí và hướng của đối tượng trong ảnh.  
* **Sử Dụng Ràng Buộc Hình Dạng (Shape Constraints):** Khi đối tượng có hình dạng cố định, thông tin này có thể được sử dụng như một ràng buộc để cải thiện độ chính xác của việc so khớp đặc trưng và xác định vị trí đối tượng.98 Các phương pháp như shape context matching có thể so sánh hình dạng dựa trên sự phân bố tương đối của các điểm trên đường viền đối tượng.101

**Bảng 3: So sánh các thuật toán trích xuất đặc trưng**

| Thuật toán | Bất biến tỷ lệ | Bất biến xoay | Chịu sáng | Chi phí tính toán |
| :---- | :---- | :---- | :---- | :---- |
| SIFT | Có | Có | Tốt | Cao |
| SURF | Có | Có | Tốt | Trung bình |
| ORB | Gần đúng | Có | Khá | Thấp |
| AKAZE | Có | Có | Tốt | Trung bình |
| BRISK | Có | Có | Khá | Thấp |
| FREAK | Có | Có | Khá | Thấp |

**5\. Mô Hình Học Sâu (Deep Learning) cho Phát Hiện Đối Tượng:**

Trong những năm gần đây, các mô hình học sâu, đặc biệt là các mạng nơ-ron tích chập (Convolutional Neural Networks \- CNNs), đã đạt được những thành công vượt trội trong lĩnh vực phát hiện đối tượng.87 Các mô hình này có khả năng học các đặc trưng phức tạp từ dữ liệu ảnh, giúp chúng trở nên mạnh mẽ hơn trong việc xử lý các điều kiện ảnh chất lượng kém và các biến thể khác nhau.

* **Các Kiến Trúc Học Sâu Phổ Biến cho Phát Hiện Đối Tượng:** Các kiến trúc như R-CNN, Fast R-CNN, Faster R-CNN, YOLO và SSD đã được phát triển để giải quyết bài toán phát hiện đối tượng với độ chính xác và tốc độ khác nhau.87  
* **Xử Lý Ảnh Độ Phân Giải Thấp:** Việc phát hiện đối tượng trong ảnh có độ phân giải thấp là một thách thức do thiếu thông tin chi tiết.32 Các kỹ thuật như **knowledge distillation** (chuyển giao kiến thức từ một mô hình được huấn luyện trên ảnh độ phân giải cao sang mô hình trên ảnh độ phân giải thấp) và các kiến trúc mạng đặc biệt (ví dụ: sử dụng Feature Pyramid Networks \- FPN) có thể giúp cải thiện hiệu suất.32 Một số nghiên cứu còn tập trung vào việc huấn luyện các mô hình có khả năng ưa thích các thông tin tần số không gian thấp, vì chúng có thể mang lại sự mạnh mẽ hơn trong nhận dạng đối tượng.110  
* **Xử Lý Sự Thay Đổi về Độ Sáng và Góc Nghiêng:** Các mô hình học sâu có thể được huấn luyện để trở nên bất biến với sự thay đổi về độ sáng và góc nghiêng thông qua việc sử dụng **data augmentation** (tăng cường dữ liệu bằng cách tạo ra các phiên bản biến đổi của ảnh huấn luyện, ví dụ: thay đổi độ sáng, xoay ảnh).42 Ngoài ra, một số kiến trúc mạng được thiết kế đặc biệt để học các đặc trưng bất biến với phép xoay.116 Các nghiên cứu cũng chỉ ra rằng sự bất biến với các biến đổi như xoay có thể xuất hiện tự nhiên trong các mạng nơ-ron được khởi tạo ngẫu nhiên.113  
* **Phát Hiện Đối Tượng Nhỏ:** Nếu vật thể có kích thước nhỏ trong ảnh độ phân giải thấp, các kỹ thuật đặc biệt cho phát hiện đối tượng nhỏ trong học sâu, chẳng hạn như sử dụng FPN hoặc các phương pháp dựa trên tiling, có thể cần thiết.32  
* **Học Chuyển Giao (Transfer Learning):** Việc sử dụng các mô hình đã được huấn luyện trước trên các bộ dữ liệu lớn (ví dụ: ImageNet, COCO) và sau đó tinh chỉnh chúng trên bộ dữ liệu ảnh cụ thể của người dùng có thể giúp giảm nhu cầu về dữ liệu huấn luyện và cải thiện hiệu suất, đặc biệt khi dữ liệu ảnh chất lượng kém và bị nghiêng là hạn chế.34

**Bảng 4: So sánh các mô hình học sâu cho phát hiện đối tượng**

| Mô hình | Ưu điểm | Nhược điểm | Khả năng xử lý độ phân giải thấp | Khả năng xử lý độ sáng thay đổi | Khả năng xử lý vật thể nghiêng |
| :---- | :---- | :---- | :---- | :---- | :---- |
| R-CNN Family | Độ chính xác cao (thường là các mô hình 2 giai đoạn) | Tốc độ chậm hơn | Thường cần độ phân giải đủ | Cần huấn luyện với dữ liệu đa dạng | Cần huấn luyện với dữ liệu đa dạng |
| YOLO Family | Tốc độ nhanh, phù hợp cho ứng dụng thời gian thực (thường là mô hình 1 giai đoạn) | Độ chính xác có thể thấp hơn R-CNN trong một số trường hợp | Các phiên bản mới cải thiện | Tốt khi huấn luyện đúng cách | Tốt khi huấn luyện đúng cách |
| SSD | Cân bằng giữa tốc độ và độ chính xác (mô hình 1 giai đoạn) | Có thể gặp khó khăn với các đối tượng nhỏ | Tương tự YOLO | Tốt khi huấn luyện đúng cách | Tốt khi huấn luyện đúng cách |
| Các mô hình khác | Nhiều kiến trúc khác nhau với các ưu nhược điểm riêng |  | Tùy thuộc kiến trúc | Tùy thuộc kiến trúc | Tùy thuộc kiến trúc |

**6\. Thư Viện và Công Cụ Phần Mềm Mã Nguồn Mở:**

Có nhiều thư viện và công cụ phần mềm mã nguồn mở cung cấp các chức năng và mô hình được thiết kế cho việc phát hiện đối tượng trong ảnh có độ phân giải thấp và các biến thể khác:

* **OpenCV (Open Source Computer Vision Library):** Cung cấp một bộ công cụ toàn diện cho xử lý ảnh và thị giác máy tính, bao gồm các hàm cho tiền xử lý ảnh, template matching và trích xuất đặc trưng (SIFT, SURF, ORB).1  
* **scikit-image:** Một thư viện Python khác cho xử lý ảnh và phân tích, cung cấp nhiều thuật toán và công cụ hữu ích.50  
* **TensorFlow và Keras:** Các framework học sâu phổ biến, cung cấp API để xây dựng và huấn luyện các mô hình phát hiện đối tượng.105 TensorFlow Hub và Keras Applications cung cấp các mô hình đã được huấn luyện trước có thể được sử dụng cho học chuyển giao.  
* **PyTorch:** Một framework học sâu khác, được biết đến với tính linh hoạt và dễ sử dụng, cũng cung cấp các công cụ và mô hình cho phát hiện đối tượng.82 PyTorch Hub cũng cung cấp các mô hình tiền huấn luyện.

**7\. Phương Pháp Kết Hợp Nhiều Kỹ Thuật:**

Để tăng độ chính xác và độ tin cậy của việc xác định bounding box trong trường hợp ảnh có độ phân giải thấp, ánh sáng thay đổi và đối tượng bị nghiêng, việc kết hợp nhiều kỹ thuật khác nhau có thể mang lại hiệu quả cao.79

* **Kết Hợp Tiền Xử Lý và Template Matching:** Sử dụng các kỹ thuật tiền xử lý để cải thiện chất lượng ảnh (ví dụ: giảm nhiễu, tăng cường độ tương phản) trước khi áp dụng template matching có thể làm tăng đáng kể độ chính xác.127  
* **Kết Hợp Template Matching và Học Sâu:** Template matching có thể được sử dụng để tạo ra các vùng đề xuất (region proposals), sau đó được phân loại bằng mô hình học sâu. Ngược lại, các đặc trưng học được từ mô hình học sâu có thể được sử dụng trong quy trình template matching để tăng cường khả năng phân biệt.79  
* **Sử Dụng Đặc Trưng Học Sâu trong Template Matching:** Các đặc trưng trích xuất từ các lớp sâu của mạng nơ-ron tích chập có thể chứa thông tin ngữ nghĩa phong phú và có khả năng bất biến với nhiều biến đổi. Sử dụng các đặc trưng này trong template matching có thể cải thiện đáng kể độ mạnh mẽ của phương pháp.137  
* **Kết Hợp Feature Matching và Học Sâu:** Feature matching có thể cung cấp thông tin về hình dạng và cấu trúc, bổ sung cho thông tin ngữ nghĩa từ các mô hình học sâu.

**8\. Chỉ Số Đánh Giá Hiệu Suất:**

Để so sánh hiệu quả của các phương pháp khác nhau trong trường hợp ảnh có độ phân giải thấp, ánh sáng thay đổi và đối tượng bị nghiêng, cần sử dụng các chỉ số đánh giá hiệu suất phù hợp.106

* **Các Chỉ Số Phổ Biến:**  
  * **Precision (Độ chính xác):** Tỷ lệ các bounding box được dự đoán là đúng so với tổng số bounding box được dự đoán.  
  * **Recall (Độ bao phủ):** Tỷ lệ các bounding box đúng được dự đoán so với tổng số bounding box đúng trong ảnh.  
  * **F1-Score:** Trung bình điều hòa của precision và recall.  
  * **Average Precision (AP):** Tính độ chính xác trung bình trên các ngưỡng khác nhau của độ tin cậy.  
  * **Mean Average Precision (mAP):** Giá trị AP trung bình trên tất cả các lớp đối tượng (trong trường hợp có nhiều lớp).  
* **Đánh Giá Phát Hiện Đối Tượng Nghiêng:** Đối với các đối tượng bị nghiêng, các chỉ số đánh giá đặc biệt có thể cần thiết để đánh giá độ chính xác của bounding box xoay.135  
* **Đánh Giá trên Ảnh Độ Phân Giải Thấp:** Cần lưu ý rằng độ phân giải thấp có thể ảnh hưởng đến độ chính xác của việc định vị bounding box, do đó có thể ảnh hưởng đến các chỉ số đánh giá dựa trên Intersection over Union (IoU).139

**9\. Kết Luận và Khuyến Nghị:**

Việc xác định bounding box cho một vật thể có hình dạng cố định trong ảnh có độ nét thấp, thay đổi độ sáng và có thể nghiêng là một bài toán phức tạp đòi hỏi sự kết hợp của nhiều kỹ thuật. Dựa trên phân tích trên, có thể đưa ra một số khuyến nghị sau:

* **Bắt đầu với các kỹ thuật tiền xử lý:** Áp dụng các phương pháp giảm nhiễu (ví dụ: bộ lọc trung vị cho nhiễu "muối tiêu", bộ lọc Gaussian cho nhiễu Gaussian) và tăng cường độ tương phản (ví dụ: CLAHE cho độ sáng thay đổi). Nếu độ phân giải quá thấp, hãy cân nhắc sử dụng các phương pháp nội suy cơ bản để tăng kích thước ảnh, nhưng cần lưu ý đến khả năng làm mờ.  
* **Thử nghiệm với Template Matching:** Nếu sự thay đổi về góc nghiêng không quá lớn, template matching chuẩn hóa (ví dụ: TM\_CCORR\_NORMED) có thể là một lựa chọn đơn giản và hiệu quả, đặc biệt khi kết hợp với việc xoay ảnh mẫu ở một số góc độ nhất định và sử dụng template matching đa tỷ lệ.  
* **Khám phá các phương pháp trích xuất đặc trưng:** Đối với sự thay đổi đáng kể về góc nhìn và độ sáng, các thuật toán như SIFT, SURF hoặc ORB có thể cung cấp kết quả mạnh mẽ hơn. So khớp các đặc trưng này và sử dụng các ràng buộc về hình dạng có thể giúp xác định vị trí đối tượng chính xác hơn.  
* **Cân nhắc sử dụng học sâu:** Nếu có đủ dữ liệu huấn luyện, các mô hình học sâu có khả năng học các đặc trưng phức tạp và trở nên rất mạnh mẽ trong việc xử lý các biến thể khác nhau. Học chuyển giao từ các mô hình đã được huấn luyện trước có thể là một cách tiếp cận hiệu quả.  
* **Kết hợp các kỹ thuật:** Một giải pháp hybrid, chẳng hạn như sử dụng tiền xử lý để tăng cường chất lượng ảnh trước khi áp dụng template matching hoặc sử dụng template matching để tạo vùng đề xuất cho một mô hình học sâu, có thể mang lại kết quả tốt nhất.  
* **Đánh giá hiệu suất một cách khách quan:** Sử dụng các chỉ số đánh giá phù hợp (bao gồm cả các chỉ số cho phát hiện đối tượng nghiêng nếu cần) để so sánh hiệu quả của các phương pháp khác nhau trên bộ dữ liệu ảnh cụ thể của người dùng.

Việc lựa chọn phương pháp tốt nhất sẽ phụ thuộc vào các đặc điểm cụ thể của bộ dữ liệu ảnh, yêu cầu về độ chính xác và tốc độ, cũng như tài nguyên tính toán có sẵn. Do đó, việc thử nghiệm và đánh giá kỹ lưỡng các phương pháp khác nhau là rất quan trọng để đạt được kết quả tối ưu.

