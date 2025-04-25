# Research Overview: Object Detection

## 1. Introduction to Object Detection

Object detection is a critical area within computer vision focused on identifying and locating specific objects within digital images or videos.[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17] Unlike image classification, which assigns a single label to an entire image, object detection provides a more detailed understanding by outlining the positions of individual objects using bounding boxes.[3, 12] This fundamental capability is essential for various advanced computer vision tasks, including instance segmentation, object tracking, and image captioning.[8, 18] The ultimate goal is to enable AI systems to interpret visual scenes with a level of sophistication similar to human vision.[1, 4]

The progress in object detection has significantly enhanced the ability of machines to understand visual information, moving from simple recognition to comprehending spatial context. This advancement is crucial for a wide array of real-world applications across numerous domains.[3, 7, 8, 9, 10, 11, 13, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64] By automating tasks previously requiring human intervention, improving accuracy in critical applications, and offering real-time insights, object detection has become indispensable in various industries.[28, 36]

## 2. Core Functionalities: Classification and Localization

The primary functions of object detection are object classification and object localization.[3, 5, 9, 65, 66] **Object classification** involves determining the category or label of each detected object within an image.[1, 2, 3, 9, 12, 65, 66] This requires training models to recognize visual patterns characteristic of different object classes, such as distinguishing between cars, people, and dogs.[2, 3, 4, 5, 7, 10] Modern approaches, especially those using deep learning, employ Convolutional Neural Networks (CNNs) to automatically learn these features from large datasets.[3, 4, 5, 10, 11, 19, 21]

**Object localization** focuses on pinpointing the spatial extent of each detected object.[2, 3, 5, 9, 10, 11, 12, 15, 18, 65, 66] This is typically achieved by generating a bounding box, a rectangle tightly enclosing the object.[2, 3, 5, 7, 9, 12, 65, 67] The box's location and size are defined by its coordinates (e.g., top-left corner's x and y, width, and height).[3] Many systems also predict a confidence score for each detection, indicating the model's certainty.[3, 5, 7]

The strength of object detection lies in the **simultaneous execution of both classification and localization**.[2, 3, 9, 12, 65, 67, 66] This integrated approach provides a comprehensive understanding of a visual scene, identifying objects and their precise spatial context.[3, 5, 9] Contemporary deep learning-based systems often use unified frameworks performing both tasks in a single pass, enhancing efficiency for real-time applications.[2, 3, 9, 12, 65, 67] The ability to recognize what is in an image and where it is located is fundamental to the broad utility of object detection.[3, 5, 9]

## 3. Historical Development of Object Detection

Object detection has evolved significantly from traditional methods to the dominance of deep learning.[5, 68, 69, 70, 71, 72] **Traditional methods**, used before the deep learning revolution, relied on handcrafted features and heuristic algorithms.[5, 11, 28] **Template matching**, an early technique, involved sliding a template across an image to find similar patterns.[73, 74] However, it struggled with variations in scale, orientation, and lighting.[73]

**Feature-based detection** became more robust, extracting features like edges, corners, and textures to represent objects.[4, 5, 6, 11, 12, 14, 19, 20, 22, 24, 26, 27, 56, 59, 74, 75, 76, 68, 77, 69, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90] Notable algorithms include **Scale-Invariant Feature Transforms (SIFT)** (1999), which detect features invariant to scale, rotation, and illumination. The **Histogram of Oriented Gradients (HOG)** (2005) counts gradient orientations and was popular for pedestrian detection.[4, 5, 12, 14, 22, 26, 27, 56, 59, 74, 75, 76, 69, 78, 81, 83, 88, 89, 90, 91] The **Viola-Jones algorithm** (2001) used Haar-like features and AdaBoost for rapid object detection, especially faces.[4, 5, 12, 20, 24, 26, 27, 77, 69, 78, 83, 88, 90, 91, 70] These methods often used classifiers like Support Vector Machines (SVMs).[4, 5, 6, 19, 22, 27, 74, 69, 78, 79, 81, 83, 92, 93] The **sliding window approach** systematically scanned images at different scales but was computationally expensive.[12, 14, 15, 19, 77, 88, 94, 95]

The field shifted dramatically with the **rise of deep learning** after 2012.[20, 68, 69, 70, 71, 72, 96, 97, 98] AlexNet's success in the 2012 ImageNet competition demonstrated the power of deep learning and Convolutional Neural Networks (CNNs) for image recognition.[20, 68, 69, 70, 71, 72] Deep learning's ability to automatically learn features from raw data eliminated the need for manual feature engineering.[4, 10, 19, 21, 71, 72]

Following this, several deep learning architectures emerged. **Region-Based CNNs (R-CNN family)**, including R-CNN, Fast R-CNN, Faster R-CNN, and Mask R-CNN, used a two-stage approach: generating region proposals and then classifying them using CNNs. **Single-Stage Detectors**, like YOLO and SSD, directly predict bounding boxes and class probabilities in one pass, prioritizing speed. More recently, **Transformer-Based Models** have been adapted for object detection.[24, 27] This evolution reflects a continuous pursuit of better accuracy, efficiency, and adaptability.

## 4. Categories of Object Detection Methodologies

Object detection methods are mainly divided into two categories: region-based (two-stage) and single-stage detectors.

**Region-Based Methods (Two-Stage Detectors)** involve two sequential stages. The first stage generates **region proposals**, candidate bounding boxes likely to contain objects. Later architectures, like Faster R-CNN, integrated this using **Region Proposal Networks (RPNs)**.[67, 88, 89, 99, 100, 101] The second stage classifies objects within these regions and refines their locations.[3, 5, 9, 10, 11, 21, 23, 24, 25, 27, 74, 78, 79, 80, 83, 88, 89, 92, 93, 71, 102, 99, 103, 104, 105, 100, 96, 106, 107, 108, 109, 101, 110, 111, 112, 113, 114, 115, 116, 66] Examples include R-CNN, Fast R-CNN, Faster R-CNN, and Mask R-CNN. These methods generally offer higher accuracy, especially for small objects and complex scenes. However, the two-stage process leads to slower inference speeds due to the computational cost of processing numerous proposals.

**Single-Stage Detectors** directly predict bounding boxes and class probabilities in a single pass, eliminating the region proposal step. They treat object detection as a regression problem. Prominent examples are YOLO and SSD. Their main advantage is significantly faster and more efficient operation, suitable for real-time applications.[3, 106, 117, 113, 114, 115, 116] Their architecture and training are generally simpler.[113] Historically, they faced challenges in achieving the same accuracy as two-stage detectors, especially for small objects and precise localization.

## 5. Prominent Deep Learning Architectures

Deep learning has led to several influential architectures for object detection.

**R-CNN (Regions with CNN features)** (2014) was one of the first successful applications of CNNs to object detection. It used selective search to generate around 2000 region proposals.[9, 17, 20, 23, 79, 88, 89, 92, 93, 103, 108, 118, 119] Each proposal was resized and fed into a pre-trained CNN (e.g., AlexNet) to extract features.[9, 20, 23, 79, 88, 89, 92, 93, 103, 108, 119] These features were then classified using an SVM, and a bounding box regressor refined the localization.[9, 23, 69, 79, 88, 89, 92, 93, 103, 108, 119] R-CNN's innovation was using CNNs, significantly improving accuracy.[23, 67, 89, 92, 108, 119] However, it was computationally expensive as the CNN ran on each proposal [79, 89, 93, 107, 110, 118], and it wasn't end-to-end trainable [79, 89, 108], leading to slow inference.[20, 77, 79, 89, 118]

**Fast R-CNN** (2015) improved upon R-CNN by processing the entire input image once through the CNN to get a feature map. Region proposals were still generated externally (e.g., Selective Search).[20, 67, 79, 88, 93, 103] An RoI pooling layer extracted fixed-size feature vectors for each proposal from this shared map. Fast R-CNN replaced the SVM with a softmax layer and also performed bounding box regression.[67, 69, 79, 88, 89, 92, 93] Its main advantage was faster speed by sharing computations , and it enabled end-to-end training.[92] However, it still relied on selective search, a bottleneck.

**Faster R-CNN** (2015) further enhanced efficiency by integrating region proposal generation into the network. It introduced a **Region Proposal Network (RPN)** that efficiently predicts objectness scores and bounding box adjustments for predefined anchor boxes.[67, 88, 89, 93, 99, 120] These proposals are then used by a Fast R-CNN detector for classification and final regression.[67, 88, 89, 93, 99, 120] Faster R-CNN achieved near real-time detection by making region proposal learnable and more efficient [20, 67, 69, 79, 88, 89, 93, 111, 120], and it was end-to-end trainable.[69, 79, 101, 120] While a significant improvement, it could still be slow with many proposals [111] and might struggle with very small objects.[79, 101]

**YOLO (You Only Look Once)** (2015) took a different approach by treating object detection as a single regression problem. It divides the input image into a grid, and each cell predicts a fixed number of bounding boxes and their class probabilities in one pass.[27, 67, 79, 110, 115] YOLO is known for its very fast, real-time capabilities [5, 21, 24, 25, 26, 27, 67, 77, 69, 79, 88, 90, 72, 121, 100, 96, 106, 110, 111, 112, 117, 113, 114, 115, 122] and can process up to 45 frames per second. Its single-stage approach allows it to consider more context.[115] However, earlier versions had lower accuracy than some two-stage methods [27, 67, 96, 106, 115] and struggled with small or closely packed objects. The YOLO family has been continuously developed with improved versions (v2, v3, v4, v5, v6, v7, v8, v10, v11).[5, 8, 24, 25, 26, 27, 67, 73, 110, 114]

**SSD (Single Shot MultiBox Detector)** (2016) is another single-stage detector balancing speed and accuracy.[24, 25, 123] Similar to YOLO, it directly predicts bounding boxes and class probabilities in one pass.[3, 4, 5, 8, 9, 10, 20, 21, 24, 25, 26, 27, 39, 78, 79, 88, 71, 100, 96, 106, 110, 123, 112, 117, 113, 114, 115, 124, 116] A key feature is using feature maps at multiple scales to detect objects of various sizes.[9, 24, 25] It also uses default (anchor) boxes with different aspect ratios at each location.[78, 112, 114] By avoiding region proposal and pooling layers, SSD achieves faster inference than R-CNN [78], making it suitable for mobile and embedded applications.[24, 117, 114] However, it can struggle with very small objects compared to some two-stage approaches.[114, 125]

## 6. Real-World Applications of Object Detection

Object detection's ability to identify and locate objects has led to its widespread use across many applications.

In **Autonomous Driving**, it's crucial for vehicles to perceive their environment by identifying pedestrians, other vehicles, obstacles, traffic signs, and lane markings. Companies like Tesla and Waymo use it for features like automatic emergency braking and lane keeping assist.[3, 4, 27, 29, 30, 60, 103] Algorithms like YOLO and Faster R-CNN are commonly used.[27, 30, 67, 103]

**Surveillance and Security** systems use object detection in security alarms to detect intruders, monitor crowds, identify abandoned objects, and enhance monitoring efficiency.[3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 31, 32, 34, 36, 42, 46, 49, 52, 56, 67, 79, 92, 94, 107, 117, 97, 126, 127, 128, 129] Applications include facial recognition, license plate recognition, and real-time detection of anomalies.[5, 8, 9, 10, 13, 16, 18, 20, 22, 24, 27, 28, 31, 32, 67, 69, 128, 129]

In **Medical Imaging**, object detection assists in diagnosing diseases by detecting tumors, lesions, fractures, and other indicators in scans like CTs, MRIs, and X-rays.[3, 5, 8, 10, 13, 17, 19, 20, 21, 23, 24, 27, 28, 29, 33, 34, 35, 36, 37, 50, 59, 60, 61, 62, 63, 64, 67, 92, 94, 130, 97, 126, 131, 132, 133, 134, 135, 118] It improves diagnostic accuracy and speeds up image analysis, aiding in early diagnosis and treatment planning.[23, 28, 33, 34, 35, 36, 37, 61, 63, 64, 92, 135, 118]

Other applications include: **Retail** for automated checkout, inventory management, and customer behavior analysis.[5, 7, 8, 10, 21, 22, 23, 24, 25, 28, 29, 37, 41, 42, 43, 51, 54, 62, 136, 127, 128, 129] **Manufacturing** for quality control, predictive maintenance, and automated assembly.[3, 5, 7, 8, 10, 11, 19, 20, 21, 22, 23, 24, 27, 28, 36, 37, 38, 39, 40, 51, 52, 54, 108, 137, 138, 128] **Agriculture** for crop monitoring, yield estimation, pest and disease detection, and weed management.[3, 5, 7, 8, 10, 11, 19, 21, 22, 23, 24, 27, 28, 29, 44, 45, 46, 47, 48, 51, 52, 53, 54, 65, 67, 139, 133, 127, 128] **Robotics** for autonomous navigation, object interaction, and quality inspections. **Transportation** for traffic monitoring, vehicle counting, safety compliance, and infrastructure inspection.[5, 7, 8, 17, 21, 23, 24, 27, 28, 55, 56, 57, 58, 59, 67, 71, 140]

The wide adoption of object detection highlights its versatility and potential to significantly improve automation, efficiency, and safety.[3, 5, 7, 8, 9, 10, 11, 19, 20, 21, 22, 23, 24, 27, 28, 55, 56, 58, 59, 92, 94, 130, 117, 125, 140, 127, 128, 129]

## 7. Key Challenges and Limitations

Despite significant progress, object detection still faces several challenges.

**Handling Small Objects** remains difficult due to their limited pixel representation.[3, 12, 25, 27, 79, 90, 94, 95, 102, 100, 110, 112, 113, 114, 115, 116, 125, 141, 136, 126, 142, 131, 143] Features at coarser resolutions may miss necessary details.[79, 95, 101, 125, 142, 131]

**Occlusions**, where objects are partially or fully hidden, pose another major challenge. They disrupt learned visual patterns.[144]

Achieving **Real-Time Processing** with high accuracy is a constant balancing act.[3, 4, 5, 8, 9, 21, 24, 25, 26, 27, 55, 67, 77, 79, 86, 88, 90, 70, 94, 95, 72, 121, 102, 100, 96, 106, 110, 111, 145, 123, 112, 117, 113, 114, 115, 116, 66, 125, 122, 146, 147, 148, 120, 143, 149, 135] High-accuracy models can be computationally expensive.[8, 150]

**Variations in Object Appearance** due to changes in size, shape, orientation, lighting, and viewpoint are significant challenges.[12, 21, 29, 61, 63, 79, 88, 130, 151, 140, 146, 127, 147, 134, 152, 153, 154, 138, 155, 98] Deformable objects like humans and animals add complexity.[10, 12, 151, 140, 146, 127, 134, 152, 154, 138, 118]

**Cluttered Backgrounds** can also significantly hinder performance. Similarities between foreground and background features make it difficult to isolate objects.[119, 128, 156]

## 8. Current Trends and Future Directions

Object detection is a continuously evolving field.[33, 73, 104, 105, 123, 152]

**Transformer-Based Models** are increasingly being adopted.[3, 24, 141, 152] Models like DETR use attention mechanisms to capture global context, potentially overcoming limitations of CNNs.[3, 24, 122, 141] Vision Transformers (ViTs) are also being used.[58, 122]

**Efficient Detection Techniques** are crucial for deploying models on resource-limited devices.[4, 8, 24, 25, 27, 79, 80, 94, 71, 102, 110, 117, 114, 135, 98] Techniques like model compression and quantization are being explored.[80, 141, 135] Examples include MobileNet and EfficientDet.[8, 25, 27, 73]

**Open World Object Detection (OWOD) and Incremental Learning** are emerging areas.[152, 150, 157] OWOD aims to recognize novel objects not in the initial training set.[150, 157] Incremental learning allows models to continuously learn new classes without retraining from scratch.[150, 157]

Other trends include **anchor-free detection methods** like FCOS [112, 155], **Graph Neural Networks (GNNs)** for modeling object relationships [111], **multi-modal approaches** fusing data from various sensors [30, 56, 135], and **self-supervised learning** to use unlabeled data.[25, 27, 63]

## 9. Comparison and Contrast of Evaluation Metrics

Performance of object detection models is evaluated using several metrics.[35, 38, 97]

**mAP (mean Average Precision)** is widely used, calculated as the average of Average Precision (AP) for each class, where AP is the area under the precision-recall curve.[3, 6, 12, 18, 87, 94, 71, 125, 97, 141, 126, 119] Higher mAP indicates better overall performance.[12, 18, 97]

**Precision** measures the proportion of correctly detected objects out of all predicted positives.[18, 38] **Recall** measures the proportion of correctly detected objects out of all actual objects.[18, 38]

**Intersection over Union (IoU)** measures the overlap between the predicted and ground truth bounding boxes.[6, 12, 16, 18, 23, 38, 89, 94, 108, 97, 136, 142, 131, 137, 135] A threshold (often 0.5) determines a true positive.[6, 16, 18, 23, 97, 136, 137, 135]

The **F1 Score** is the harmonic mean of precision and recall, useful for imbalanced datasets.[18, 38, 148]

The **Confusion Matrix** provides a detailed breakdown of predictions into True Positives, False Positives, False Negatives, and True Negatives.[18, 38, 97]

## 10. Conclusion

Object detection has advanced significantly, driven by deep learning and increasing data and computational power. It has become a vital technology impacting numerous real-world applications. While challenges remain in areas like small object detection and handling occlusions, ongoing research in transformer models, efficient techniques, and open-world learning promises further advancements. Evaluation metrics like mAP and IoU are crucial for measuring progress. The continuous innovation in this field underscores its importance in the future of computer vision.

---

# Các Phương Pháp Phát Hiện Đối Tượng Hình Dạng Cố Định Trong Ảnh Bị Suy Giảm

## 1. Giới thiệu

### Định nghĩa bài toán

Báo cáo này tập trung vào bài toán phát hiện một đối tượng đã biết trước với hình dạng cố định trong môi trường chụp ảnh có thể bị nhiễu, mờ hoặc nghiêng, nhưng ít bị chồng chéo. Thách thức cốt lõi nằm ở việc đạt được khả năng phát hiện đáng tin cậy một đối tượng cụ thể khi chất lượng hình ảnh bị suy giảm do các yếu tố phổ biến như nhiễu, mờ và các biến dạng hình học như độ nghiêng. Giả định về hình dạng đối tượng cố định là rất quan trọng vì nó cho phép khai thác các phương pháp phát hiện dựa trên hình dạng. Điều kiện ít bị chồng chéo giúp đơn giản hóa bài toán bằng cách giảm độ phức tạp trong việc phân tách nhiều đối tượng hoặc phân biệt đối tượng mục tiêu với các vật thể gây cản trở.[1]

### Tầm quan trọng của việc phát hiện đối tượng mạnh mẽ trong môi trường thách thức

Trong nhiều ứng dụng thực tế, việc thu được hình ảnh chất lượng cao không phải lúc nào cũng khả thi. Ví dụ, trong kiểm soát chất lượng công nghiệp, các đối tượng có thể được kiểm tra trong điều kiện ánh sáng khác nhau hoặc bằng camera có thể gây nhiễu. Trong lĩnh vực robot học, hình ảnh có thể bị mờ do chuyển động của robot hoặc các yếu tố môi trường. Các hệ thống giám sát có thể ghi lại cảnh quay trong điều kiện thời tiết bất lợi hoặc với camera bị rung. Do đó, các kỹ thuật phát hiện đối tượng mạnh mẽ có khả năng hoạt động chính xác bất chấp những thách thức này là rất cần thiết cho độ tin cậy và tính thực tế của các ứng dụng thị giác máy tính. Các kỹ thuật cổ điển, mặc dù đôi khi bị che mờ bởi sự tiến bộ của học sâu, nhưng vẫn mang lại những lợi thế đáng kể về hiệu quả tính toán, khả năng diễn giải và khả năng hoạt động hiệu quả với dữ liệu huấn luyện hạn chế, khiến chúng phù hợp với nhiều tình huống.[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

### Tập trung vào các kỹ thuật thị giác máy tính cổ điển

Báo cáo này sẽ tập trung vào các phương pháp thị giác máy tính đã được thiết lập, không dựa vào học sâu, để giải quyết bài toán phát hiện đối tượng cụ thể của người dùng. Chúng ta sẽ khám phá các kỹ thuật khớp mẫu, các phương pháp dựa trên đặc trưng, các thuật toán học máy cổ điển và các bước tiền xử lý ảnh thiết yếu. Mục tiêu là cung cấp một sự hiểu biết toàn diện về các nguyên tắc cơ bản và các công cụ thực tế có sẵn để phát hiện đối tượng mạnh mẽ trong các điều kiện hình ảnh bị suy giảm, cung cấp một giải pháp thay thế hoặc bổ sung cho các giải pháp dựa trên học sâu.[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

## 2. Khớp mẫu để phát hiện đối tượng

### Các nguyên tắc cốt lõi của khớp mẫu

Khớp mẫu là một kỹ thuật cơ bản trong thị giác máy tính, trong đó một hình ảnh nhỏ (mẫu) đại diện cho đối tượng quan tâm được trượt trên một hình ảnh lớn hơn (hình ảnh nguồn).[23, 24, 25, 26, 27, 28] Tại mỗi vị trí, một điểm số tương tự được tính toán để xác định mức độ khớp giữa mẫu và vùng tương ứng của hình ảnh nguồn.[23, 24, 25, 26, 27, 28] Vị trí có điểm số tương tự cao nhất (hoặc thấp nhất đối với một số số liệu dựa trên khoảng cách) cho biết vị trí có khả năng nhất của đối tượng.[23, 24, 25, 26, 27, 28] OpenCV cung cấp hàm `cv::matchTemplate()`, một công cụ được sử dụng rộng rãi để triển khai kỹ thuật này.[23, 24, 25, 26, 27, 28, 29] Hàm này cung cấp một số phương pháp so sánh, mỗi phương pháp có độ nhạy khác nhau đối với các đặc điểm hình ảnh khác nhau.

### Các biến thể của khớp mẫu

#### Tương quan chéo chuẩn hóa để bất biến chiếu sáng

Tương quan chéo chuẩn hóa (NCC) là một phương pháp ưu tiên khi xử lý các biến thể tiềm năng trong điều kiện ánh sáng giữa mẫu và hình ảnh nguồn.[28, 29, 30, 31, 32, 33, 34, 35] NCC đạt được tính bất biến chiếu sáng bằng cách chuẩn hóa cả mẫu và vùng cục bộ của hình ảnh nguồn đang được so sánh. Quá trình chuẩn hóa này bao gồm việc trừ đi cường độ pixel trung bình và chia cho độ lệch chuẩn, làm cho phép đo độ tương tự ít bị ảnh hưởng bởi những thay đổi đồng nhất về độ sáng hoặc độ tương phản. Kết quả của NCC thường là một giá trị nằm trong khoảng từ -1 đến 1, trong đó giá trị gần 1 cho thấy mức độ tương tự cao, cho thấy sự khớp mạnh mẽ.[33, 35]

#### Kỹ thuật bất biến xoay và tỷ lệ trong khớp mẫu

Một hạn chế đáng kể của khớp mẫu tiêu chuẩn là độ nhạy của nó đối với các phép biến đổi hình học, đặc biệt là xoay và tỷ lệ của đối tượng trong hình ảnh nguồn so với mẫu.[36, 37, 38, 39, 40, 41, 42, 43, 44] Có một số kỹ thuật có thể được sử dụng để giải quyết hạn chế này:

*   **Tìm kiếm theo lưới:** Kỹ thuật này bao gồm việc tạo nhiều phiên bản của mẫu, mỗi phiên bản được xoay theo một góc khác nhau trong một phạm vi được xác định trước và được thu phóng đến các kích thước khác nhau trong một phạm vi được chỉ định.[36, 38, 39] Sau đó, khớp mẫu được thực hiện bằng cách sử dụng từng mẫu đã được biến đổi này so với hình ảnh nguồn. Điểm số tương tự cao nhất trên tất cả các phép biến đổi cho biết sự khớp tiềm năng tốt nhất, cùng với góc xoay và hệ số tỷ lệ tương ứng. Mặc dù đơn giản về mặt khái niệm, phương pháp này có thể tốn kém về mặt tính toán, đặc biệt nếu cần khám phá một phạm vi lớn các góc và tỷ lệ với độ chi tiết cao.[39]
*   **Căn chỉnh dựa trên đặc trưng:** Một cách tiếp cận thay thế là trích xuất các đặc trưng riêng biệt (chẳng hạn như các điểm khóa bằng cách sử dụng các thuật toán như SIFT, SURF hoặc ORB) từ cả mẫu và hình ảnh nguồn.[37, 45, 46, 47, 48] Bằng cách khớp các đặc trưng này, có thể ước tính phép biến đổi hình học (bao gồm xoay, tỷ lệ và dịch chuyển) căn chỉnh tốt nhất các đặc trưng của mẫu với các đặc trưng của hình ảnh nguồn. Sau đó, phép biến đổi ước tính này có thể được áp dụng cho mẫu hoặc vùng tương ứng trong hình ảnh nguồn trước khi thực hiện khớp mẫu tiêu chuẩn. Phương pháp này thường mạnh mẽ hơn đối với các tắc nghẽn một phần và các phép biến đổi phức tạp so với tìm kiếm theo lưới.
*   **Khớp mẫu bất biến:** Các thuật toán khớp mẫu chuyên dụng hơn nhằm đạt được tính bất biến đối với xoay và tỷ lệ trực tiếp mà không cần các phép biến đổi rõ ràng. Các phương pháp này thường sử dụng các kỹ thuật như trích xuất các biên dạng xuyên tâm của mẫu hoặc sử dụng các phép biến đổi Fourier-Mellin để thu được các biểu diễn vốn đã bất biến đối với những thay đổi hình học này.[37, 38, 49, 50] Tuy nhiên, các thuật toán này có thể không có sẵn trong các thư viện tiêu chuẩn như OpenCV và có thể yêu cầu các triển khai chuyên biệt.

### Độ mạnh mẽ của khớp mẫu đối với nhiễu và mờ

Các phương pháp khớp mẫu truyền thống có thể khá nhạy cảm với sự hiện diện của nhiễu và mờ trong hình ảnh nguồn, vì những suy giảm này có thể làm thay đổi cường độ và độ dốc pixel mà quá trình khớp dựa vào.[40, 51] Có một số chiến lược có thể được sử dụng để tăng cường độ mạnh mẽ của khớp mẫu trong các điều kiện này:

*   **Tiền xử lý:** Áp dụng các kỹ thuật tiền xử lý hình ảnh thích hợp thường là cách hiệu quả nhất để giảm thiểu tác động của nhiễu và mờ.[52, 53, 54, 55, 56, 57, 58] Ví dụ, nếu nhiễu chủ yếu là nhiễu Gaussian, việc áp dụng bộ lọc làm mờ Gaussian có thể giúp làm mịn nhiễu trong khi vẫn giữ được cấu trúc tổng thể của đối tượng. Nếu nhiễu là nhiễu muối tiêu, bộ lọc trung vị thường hiệu quả hơn trong việc loại bỏ nhiễu mà không làm mờ các cạnh quá nhiều.
*   **Các biện pháp tương tự chuyên dụng:** Một số số liệu tương tự vốn đã mạnh mẽ hơn đối với nhiễu so với các số liệu khác. Ví dụ, Tương quan bất đối xứng (ASC) đã được thiết kế đặc biệt để có khả năng phục hồi tốt hơn đối với nhiễu cực độ trong các tình huống khớp mẫu.[30, 31]
*   **Làm mờ hình học:** Một kỹ thuật thú vị khác là áp dụng "làm mờ hình học" cho mẫu. Phương pháp này giới thiệu độ mờ thay đổi theo không gian tỷ lệ với khoảng cách từ tâm của mẫu. Ý tưởng là làm cho quá trình khớp mẫu mạnh mẽ hơn đối với các biến dạng hình học, bao gồm cả những biến dạng có thể phát sinh từ độ mờ.[59]

### Kết luận

Khớp mẫu là một kỹ thuật phát hiện đối tượng cơ bản có thể hiệu quả trong các điều kiện nhất định. Các biến thể như NCC giúp giải quyết các thay đổi về ánh sáng, và các kỹ thuật như tìm kiếm theo lưới hoặc căn chỉnh dựa trên đặc trưng có thể được sử dụng để xử lý các thay đổi về xoay và tỷ lệ. Tuy nhiên, độ mạnh mẽ của khớp mẫu đối với nhiễu và mờ thường cần được tăng cường thông qua các bước tiền xử lý thích hợp và có thể lựa chọn các biện pháp tương tự chuyên dụng.

## 3. Trích xuất đặc trưng hình dạng để phát hiện đối tượng mạnh mẽ

### Các phương pháp dựa trên đường viền

#### Thuật toán trích xuất đường viền

Các phương pháp dựa trên đường viền tập trung vào hình dạng hoặc đường bao của các đối tượng. Một bước đầu tiên phổ biến trong các phương pháp này là trích xuất đường viền từ hình ảnh. Thuật toán phát hiện cạnh Canny là một kỹ thuật được sử dụng rộng rãi cho mục đích này, nổi tiếng với khả năng phát hiện chính xác một loạt các cạnh trong hình ảnh đồng thời tương đối mạnh mẽ đối với nhiễu.[54, 55] OpenCV cung cấp hàm `cv::Canny()` để triển khai thuật toán này. Sau khi các cạnh được phát hiện, các thuật toán trích xuất đường viền, chẳng hạn như những thuật toán được triển khai bởi `cv::findContours()` trong OpenCV, có thể được sử dụng để xác định các đường cong khép kín đại diện cho ranh giới của các đối tượng trong hình ảnh.

#### Các bộ mô tả hình dạng và các thuộc tính bất biến của chúng

Sau khi trích xuất các đường viền, các bộ mô tả hình dạng có thể được sử dụng để mô tả các đặc điểm thiết yếu của hình dạng theo cách bất biến đối với các phép biến đổi nhất định.

*   **Các moment Hu:** Đây là một tập hợp bảy moment thống kê được tính toán từ các moment trung tâm của một hình dạng. Một đặc tính quan trọng của các moment Hu là chúng bất biến đối với phép dịch chuyển, tỷ lệ và xoay, khiến chúng rất hữu ích để nhận dạng các đối tượng bất kể vị trí, kích thước và hướng của chúng trong hình ảnh.[60] Các moment này có thể được tính toán bằng cách sử dụng các hàm có sẵn trong các thư viện xử lý ảnh.
*   **Ngữ cảnh hình dạng:** Đây là các bộ mô tả hình dạng phức tạp hơn nắm bắt sự phân bố của các điểm đường viền khác so với một điểm tham chiếu trên đường viền. Chúng được xây dựng bằng cách tạo ra một biểu đồ tọa độ cực log về vị trí tương đối của các điểm đường viền khác. Ngữ cảnh hình dạng được biết đến là khá mạnh mẽ đối với các phép biến đổi không cứng nhắc và có thể xử lý một mức độ tắc nghẽn nhất định, khiến chúng phù hợp cho các tác vụ khớp hình dạng phức tạp hơn.[60]

### Các phương pháp dựa trên điểm khóa

#### Các bộ dò tìm đặc trưng mạnh mẽ

Các phương pháp dựa trên điểm khóa tập trung vào việc xác định các điểm riêng biệt hoặc "đặc trưng" trong hình ảnh có khả năng phục hồi tốt trước các phép biến đổi và suy giảm khác nhau. Một số bộ dò tìm đặc trưng phổ biến bao gồm:

*   **SIFT (Scale-Invariant Feature Transform - Biến đổi đặc trưng bất biến tỷ lệ):** Được phát triển bởi David Lowe, SIFT là một thuật toán mạnh mẽ phát hiện các điểm khóa trong hình ảnh bất biến đối với tỷ lệ và xoay, và bất biến một phần đối với các thay đổi về ánh sáng và phép chiếu affine hoặc 3D.[60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81] Nó tạo ra một bộ mô tả 128 chiều cho mỗi điểm khóa được phát hiện, nắm bắt thông tin hình ảnh cục bộ xung quanh nó.[62, 76]
*   **SURF (Speeded-Up Robust Features - Các đặc trưng mạnh mẽ được tăng tốc):** Lấy cảm hứng từ SIFT, SURF được thiết kế để trở thành một giải pháp thay thế nhanh hơn trong khi vẫn duy trì hiệu suất tốt về khả năng phục hồi đối với tỷ lệ và xoay.[60, 61, 64, 65, 67, 69, 70, 71, 72, 73, 75, 76, 77, 78] Nó sử dụng bộ mô tả 64 chiều và tận dụng hình ảnh tích phân để tăng tốc quá trình phát hiện và mô tả đặc trưng, thường nhanh hơn SIFT.[69, 76]
*   **ORB (Oriented FAST and Rotated BRIEF - BRIEF được định hướng và xoay):** ORB là một thuật toán gần đây hơn được phát triển bởi OpenCV Labs như một giải pháp thay thế miễn phí cho SIFT và SURF, vốn được cấp bằng sáng chế.[60, 61, 63, 68, 69, 73, 75, 76, 77, 78, 79] Nó kết hợp bộ dò tìm điểm khóa FAST với bộ mô tả BRIEF, kết hợp các cải tiến để đạt được tính bất biến xoay. ORB đặc biệt hiệu quả và phù hợp cho các ứng dụng có tài nguyên tính toán hạn chế.[60, 76]

#### Kỹ thuật khớp đặc trưng

Sau khi các đặc trưng được phát hiện và mô tả trong cả mẫu (đại diện cho đối tượng đã biết) và hình ảnh nguồn, bước tiếp theo là khớp các đặc trưng này để tìm các điểm tương ứng. Các kỹ thuật khớp phổ biến bao gồm:

*   **Khớp thô bạo:** Đây là một phương pháp đơn giản, trong đó bộ mô tả của mỗi đặc trưng trong một hình ảnh được so sánh với bộ mô tả của tất cả các đặc trưng trong hình ảnh kia bằng cách sử dụng một số liệu khoảng cách. Bộ mô tả tương tự nhất (dựa trên khoảng cách) được coi là một sự khớp. Đối với SIFT và SURF, khoảng cách Euclidean thường được sử dụng, trong khi đối với ORB (tạo ra các bộ mô tả nhị phân), khoảng cách Hamming được sử dụng.[82] OpenCV cung cấp lớp `cv::BFMatcher` cho mục đích này.
*   **Khớp dựa trên FLANN (Fast Library for Approximate Nearest Neighbors - Thư viện nhanh cho hàng xóm gần đúng nhất):** Đối với các tập hợp đặc trưng lớn hơn, khớp dựa trên FLANN có thể nhanh hơn đáng kể so với khớp thô bạo. FLANN sử dụng một cấu trúc lập chỉ mục để tìm kiếm hiệu quả các hàng xóm gần đúng nhất, tăng tốc quá trình khớp.[82] OpenCV cung cấp lớp `cv::FlannBasedMatcher` cho việc này.

### Kết luận

Trích xuất đặc trưng hình dạng cung cấp một cách tiếp cận mạnh mẽ để phát hiện đối tượng trong các điều kiện thách thức. Các phương pháp dựa trên đường viền sử dụng các bộ mô tả như moment Hu để đạt được tính bất biến đối với các phép biến đổi, trong khi các phương pháp dựa trên điểm khóa như SIFT, SURF và ORB có khả năng phục hồi tốt trước nhiễu, mờ và các thay đổi về góc nhìn. Việc lựa chọn phương pháp phụ thuộc vào các đặc điểm cụ thể của đối tượng và loại suy giảm hình ảnh dự kiến.

## 4. Các thuật toán và bộ lọc học máy cổ điển để phát hiện đối tượng

### Các phương pháp dựa trên bộ lọc

#### Bộ lọc phát hiện cạnh

Các kỹ thuật lọc hình ảnh có thể được sử dụng để làm nổi bật các đặc điểm cụ thể trong hình ảnh có thể hỗ trợ phát hiện đối tượng. Ví dụ, các bộ lọc phát hiện cạnh như Sobel và Laplacian làm nổi bật các vùng trong hình ảnh có sự thay đổi cường độ đáng kể, thường tương ứng với ranh giới hoặc cạnh của đối tượng.[53, 54, 55, 58] Việc làm nổi bật các đặc trưng liên quan đến hình dạng này có thể giúp xác định vị trí của đối tượng trong hình ảnh.

#### Bộ lọc giảm nhiễu và làm sắc nét ảnh

Như đã thảo luận trước đó, các bộ lọc giảm nhiễu như bộ lọc Gaussian (cho nhiễu Gaussian) và bộ lọc trung vị (cho nhiễu muối tiêu) có thể được áp dụng như một bước tiền xử lý để cải thiện chất lượng hình ảnh và tăng độ chính xác của các thuật toán phát hiện đối tượng tiếp theo.[53, 54, 55, 56, 57, 58] Tương tự, các kỹ thuật làm sắc nét ảnh có thể nâng cao các cạnh và chi tiết, có khả năng làm cho đối tượng dễ phát hiện hơn trong hình ảnh bị mờ.[53, 55, 57, 58]

### Các phương pháp thống kê

#### Phát hiện đối tượng bằng cách kiểm định giả thuyết thống kê

Một cách tiếp cận chính thức hơn để phát hiện đối tượng sử dụng các phương pháp thống kê liên quan đến việc kiểm định giả thuyết.[83] Phương pháp này thường bắt đầu bằng cách thu thập một số lượng lớn các phép đo hình ảnh (đặc trưng) đa dạng từ các ví dụ huấn luyện dương tính về đối tượng. Đối với mỗi đặc trưng, hàm mật độ xác suất được ước tính dựa trên sự phân bố của đặc trưng đó trên các ví dụ huấn luyện dương tính. Tại thời gian chạy, đối với một vùng ứng viên trong hình ảnh, một kiểm định giả thuyết được thực hiện cho mỗi đặc trưng đã chọn để xác định xem giá trị đặc trưng quan sát được có nhất quán với phân phối đã học từ đối tượng hay không. Một đối tượng được phát hiện nếu một số lượng đủ các kiểm định này vượt qua, cung cấp bằng chứng thống kê về sự hiện diện của đối tượng.

#### Các bộ phân loại học máy cổ điển với các đặc trưng thủ công

Các thuật toán học máy cổ điển, chẳng hạn như Máy vectơ hỗ trợ (SVM), có thể được sử dụng để phát hiện đối tượng khi kết hợp với các đặc trưng được thiết kế cẩn thận. Ví dụ, bộ mô tả Biểu đồ độ dốc hướng (HOG), nắm bắt sự phân bố của các độ dốc cường độ cục bộ, đã rất thành công khi được sử dụng với bộ phân loại SVM để phát hiện đối tượng, đặc biệt là cho các tác vụ như phát hiện người đi bộ.[26, 60, 65, 84] Trong cách tiếp cận này, các đặc trưng HOG được trích xuất từ các vùng hình ảnh, và SVM được huấn luyện để phân loại các vùng này là chứa đối tượng hay không.

### Kết luận

Các bộ lọc hình ảnh và các phương pháp thống kê cung cấp các công cụ hữu ích để phát hiện đối tượng trong các điều kiện nhiễu và mờ. Các bộ lọc có thể làm nổi bật các đặc trưng quan trọng hoặc giảm nhiễu, trong khi các phương pháp thống kê và các bộ phân loại học máy cổ điển cho phép học các mẫu từ dữ liệu và đưa ra quyết định về sự hiện diện của đối tượng. Sự kết hợp của các kỹ thuật này có thể dẫn đến các hệ thống phát hiện đối tượng mạnh mẽ.

## 5. Xử lý các biến thể về góc nhìn và độ nghiêng trong phát hiện đối tượng

### Các phép biến đổi hình học

#### Phép biến đổi affine

Phép biến đổi affine là các phép biến đổi tuyến tính bảo toàn tính song song của các đường thẳng. Chúng có thể mô hình hóa hiệu quả những thay đổi về vị trí (phép tịnh tiến), kích thước (phép tỷ lệ) và hướng (phép xoay) của đối tượng trong mặt phẳng hình ảnh.[85, 86, 87] Phép biến đổi trượt là một loại phép biến đổi affine khác có thể giải thích một mức độ nào đó những thay đổi về góc nhìn.

#### Phép biến đổi phối cảnh

Phép biến đổi phối cảnh tổng quát hơn phép biến đổi affine và có thể mô hình hóa những thay đổi về hình dạng của đối tượng khi quan điểm của camera thay đổi trong không gian 3D.[85, 87] Chúng giải thích hiệu ứng phối cảnh, trong đó các đối tượng xuất hiện nhỏ hơn khi chúng ở xa hơn.

### Kỹ thuật hiệu chỉnh độ nghiêng và căn chỉnh hình ảnh

#### Xoay hình ảnh dựa trên ước tính góc nghiêng

Nếu có thể ước tính góc nghiêng hoặc góc xoay của đối tượng trong hình ảnh, thì toàn bộ hình ảnh (hoặc vùng chứa đối tượng) có thể được xoay theo một góc bằng và ngược dấu để hiệu chỉnh hướng của nó.[84, 88, 89] Các kỹ thuật như Phương pháp biên dạng chiếu, phân tích hình chiếu cường độ pixel ở các góc khác nhau, có thể được sử dụng để ước tính góc nghiêng của văn bản hoặc đối tượng trong hình ảnh.[84] OpenCV cung cấp các hàm như `cv::getRotationMatrix2D()` để tính toán ma trận xoay và `cv::warpAffine()` để thực hiện phép xoay.

#### Biến dạng hình học để căn chỉnh

Các phép biến đổi hình học phức tạp hơn, chẳng hạn như biến dạng affine hoặc phối cảnh, có thể được áp dụng cho hình ảnh hoặc mẫu để căn chỉnh chúng bất chấp sự khác biệt về góc nhìn hoặc độ nghiêng.[85, 90, 91] Điều này thường đòi hỏi phải ước tính các tham số của phép biến đổi, có thể được thực hiện bằng cách khớp các đặc trưng giữa các điểm tương ứng trong hai chế độ xem. Các hàm `cv::warpAffine()` và `cv::warpPerspective()` của OpenCV có thể được sử dụng cho các mục đích này.

#### Căn chỉnh dựa trên đặc trưng

Như đã đề cập trước đó, việc khớp các đặc trưng (ví dụ: các điểm khóa SIFT, SURF, ORB) giữa chế độ xem tham chiếu của đối tượng (mẫu) và chế độ xem bị nghiêng trong hình ảnh nguồn có thể cung cấp một tập hợp các điểm tương ứng.[37, 45, 46, 47, 48] Các điểm tương ứng này sau đó có thể được sử dụng để ước tính phép biến đổi hình học (ví dụ: bằng cách sử dụng các phương pháp như tìm phép homography) căn chỉnh hai chế độ xem.

### Trích xuất đặc trưng bất biến góc nhìn

Một cách tiếp cận khác để xử lý các biến thể về góc nhìn là sử dụng các kỹ thuật trích xuất đặc trưng vốn ít nhạy cảm hơn với những thay đổi này.[66, 92] Ví dụ, các bộ mô tả đặc trưng như SIFT được thiết kế để bất biến đối với một số mức độ thay đổi về góc nhìn, bao gồm xoay và tỷ lệ. Bằng cách dựa vào các loại đặc trưng này, có thể giảm nhu cầu hiệu chỉnh độ nghiêng hoặc căn chỉnh hình ảnh rõ ràng trong một số trường hợp.

### Kết luận

Việc xử lý các biến thể về góc nhìn và độ nghiêng thường liên quan đến việc áp dụng các phép biến đổi hình học để điều chỉnh hướng của hình ảnh hoặc sử dụng các đặc trưng ít bị ảnh hưởng bởi những thay đổi này. Việc lựa chọn kỹ thuật phụ thuộc vào bản chất và mức độ của sự thay đổi góc nhìn hoặc độ nghiêng.

## 6. So sánh hiệu suất của các phương pháp khác nhau

### Phân tích các ưu điểm và nhược điểm

*   **Khớp mẫu:** Mặc dù đơn giản và nhanh chóng để phát hiện các đối tượng khớp chính xác, nhưng nó lại chịu nhiều ảnh hưởng của nhiễu, mờ và các phép biến đổi hình học như độ nghiêng hoặc xoay.[40, 41] Hiệu suất của nó giảm nhanh chóng khi đối tượng trong cảnh khác biệt dù chỉ một chút so với mẫu về các yếu tố này.
*   **Các phương pháp dựa trên đặc trưng (SIFT, SURF, ORB):** Các phương pháp này thường mạnh mẽ hơn nhiều đối với các thay đổi về tỷ lệ, xoay (độ nghiêng có thể được coi là một dạng xoay trong mặt phẳng hình ảnh) và góc nhìn.[60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81] Chúng cũng có khả năng phục hồi tốt hơn một mức độ nào đó đối với nhiễu và mờ so với khớp mẫu. Tuy nhiên, chúng có thể tốn kém hơn về mặt tính toán, đặc biệt là SIFT và SURF, và có thể gặp khó khăn với các đối tượng thiếu các đặc trưng cục bộ riêng biệt.
*   **Học máy cổ điển (SVM với HOG):** Khi được huấn luyện trên một tập dữ liệu bao gồm các biến thể về độ nghiêng, nhiễu và mờ, cách tiếp cận này có thể mang lại sự cân bằng tốt giữa độ mạnh mẽ và hiệu quả để phát hiện các danh mục đối tượng cụ thể.[26, 60, 65, 84] Tuy nhiên, hiệu suất của nó phụ thuộc rất nhiều vào chất lượng và sự đa dạng của dữ liệu huấn luyện.

### Các yếu tố ảnh hưởng đến hiệu suất

Mức độ nhiễu, mờ và độ nghiêng hiện diện trong hình ảnh sẽ là yếu tố quyết định chính ảnh hưởng đến độ chính xác phát hiện của tất cả các phương pháp. Mức độ suy giảm càng cao, hiệu suất thường càng giảm. Độ phức tạp về hình dạng và kết cấu của đối tượng cũng đóng một vai trò quan trọng. Các đối tượng có nhiều đặc trưng thường dễ phát hiện hơn bằng các phương pháp dựa trên đặc trưng, trong khi khớp mẫu hoạt động tốt nhất cho các đối tượng có mẫu trực quan rõ ràng.

### Tiềm năng kết hợp các kỹ thuật khác nhau

Một chiến lược đầy hứa hẹn có thể là kết hợp các kỹ thuật khác nhau. Ví dụ, có thể sử dụng các bước tiền xử lý để giảm nhiễu và mờ, sau đó áp dụng phương pháp khớp mẫu bất biến xoay hoặc phương pháp dựa trên đặc trưng để phát hiện. Đối với các ứng dụng cụ thể, việc huấn luyện một bộ phân loại học máy cổ điển trên các đặc trưng được trích xuất từ các hình ảnh đã được tiền xử lý và tăng cường dữ liệu để bao gồm các biến thể về độ nghiêng, nhiễu và mờ cũng có thể hiệu quả.

### Kết luận

Việc lựa chọn phương pháp phát hiện đối tượng cổ điển tối ưu phụ thuộc vào các đặc điểm cụ thể của đối tượng, các loại và mức độ suy giảm hình ảnh dự kiến, cũng như các tài nguyên tính toán có sẵn. Các nghiên cứu so sánh thường cho thấy sự đánh đổi giữa độ mạnh mẽ, độ chính xác và tốc độ cho các kỹ thuật khác nhau.[51, 67, 69, 70, 71, 72, 73, 74, 93, 94, 95, 96]

## 7. Kỹ thuật tiền xử lý ảnh để cải thiện độ chính xác

### Phương pháp giảm nhiễu

*   **Bộ lọc Gaussian:** Hiệu quả trong việc giảm nhiễu Gaussian, thường gặp trong ảnh do nhiễu cảm biến hoặc nhiễu điện. Nó hoạt động bằng cách tích chập ảnh với hạt nhân Gaussian, làm mờ ảnh để giảm các thành phần nhiễu tần số cao.[53, 54, 55, 56, 57, 58]
*   **Bộ lọc trung vị:** Đặc biệt hữu ích để loại bỏ nhiễu xung, còn được gọi là nhiễu muối tiêu, biểu hiện dưới dạng các pixel đen trắng ngẫu nhiên. Bộ lọc trung vị thay thế giá trị của mỗi pixel bằng giá trị trung vị của các pixel lân cận, loại bỏ hiệu quả các giá trị ngoại lai mà không làm mờ đáng kể các cạnh.[53, 54, 55, 56, 57, 58]
*   **Bộ lọc song phương:** Một bộ lọc phi tuyến tính giúp giảm nhiễu đồng thời bảo toàn các cạnh. Nó xem xét cả khoảng cách không gian và sự khác biệt về cường độ giữa các pixel, đảm bảo rằng chỉ các pixel có cường độ tương tự mới đóng góp vào việc làm mịn một pixel nhất định.[53, 54, 55, 56, 57, 58]

### Loại bỏ mờ và làm sắc nét ảnh

*   **Kỹ thuật deconvolution:** Các phương pháp này cố gắng đảo ngược quá trình làm mờ bằng cách sử dụng kiến thức về hạt nhân làm mờ (nếu biết) hoặc bằng cách ước tính nó từ hình ảnh.[53, 55, 57, 58]
*   **Mặt nạ làm sắc nét không rõ nét:** Một kỹ thuật làm sắc nét phổ biến giúp tăng cường các cạnh bằng cách tăng độ tương phản giữa các pixel ở hai bên cạnh. Nó bao gồm việc tạo ra một phiên bản bị mờ của hình ảnh, trừ nó khỏi bản gốc và sau đó thêm một phiên bản đã được chia tỷ lệ của sự khác biệt trở lại bản gốc.[53, 55, 57, 58]
*   **Bộ lọc thông cao:** Các bộ lọc này nhấn mạnh các thành phần tần số cao của hình ảnh, tương ứng với các cạnh và chi tiết nhỏ, do đó làm sắc nét hình ảnh.[53, 55, 57, 58]

### Hiệu chỉnh độ nghiêng và căn chỉnh hình ảnh

*   **Xoay hình ảnh:** Nếu có thể ước tính góc nghiêng (ví dụ: bằng cách sử dụng phép biến đổi Hough để phát hiện đường thẳng hoặc Phương pháp biên dạng chiếu), hình ảnh có thể được xoay để căn chỉnh đối tượng với hướng tiêu chuẩn.[84, 88, 89]
*   **Biến dạng affine hoặc phối cảnh:** Đối với các biến thể về độ nghiêng hoặc góc nhìn phức tạp hơn, có thể sử dụng các phép biến đổi affine hoặc phối cảnh để biến dạng hình ảnh thành một chế độ xem chính tắc. Điều này thường yêu cầu xác định các điểm tương ứng giữa hình ảnh bị biến dạng và hình ảnh hoặc mô hình tham chiếu.[88, 89, 91]

### Tăng cường độ tương phản

*   **Cân bằng biểu đồ:** Phân phối lại cường độ pixel trong hình ảnh để sử dụng toàn bộ phạm vi giá trị có thể, thường dẫn đến tăng độ tương phản toàn cục và làm cho các chi tiết dễ nhìn thấy hơn.[54, 97]
*   **Kéo giãn độ tương phản:** Chia tỷ lệ tuyến tính cường độ pixel thành một phạm vi mới, thường từ giá trị tối thiểu đến giá trị tối đa có thể, có thể tăng cường độ tương phản trong các hình ảnh có phạm vi cường độ hẹp.[54, 97]

### Kết luận

Một chuỗi các bước tiền xử lý được lên kế hoạch kỹ lưỡng, phù hợp với các suy giảm hình ảnh dự kiến, có thể cải thiện đáng kể độ chính xác và độ mạnh mẽ của các thuật toán phát hiện đối tượng cổ điển. Thứ tự và lựa chọn các bước này là rất quan trọng để có hiệu suất tối ưu.

## 8. Thư viện và công cụ mã nguồn mở

### Tổng quan về OpenCV

OpenCV là một thư viện mã nguồn mở mạnh mẽ và được sử dụng rộng rãi, cung cấp một tập hợp phong phú các hàm để triển khai nhiều kỹ thuật phát hiện đối tượng cổ điển được thảo luận trong báo cáo này.[23, 24, 25, 26, 27, 28, 29, 68, 75, 76, 77, 78, 79, 80, 81, 82, 98, 99] Nó hỗ trợ nhiều ngôn ngữ lập trình, bao gồm Python, C++ và Java, khiến nó trở thành một lựa chọn linh hoạt cho các nhà nghiên cứu và nhà phát triển.

### Các chức năng liên quan đến phát hiện đối tượng

*   **Khớp mẫu:** OpenCV cung cấp hàm `cv::matchTemplate()` để thực hiện khớp mẫu với nhiều phương pháp so sánh khác nhau, bao gồm NCC và SSD.[23, 24, 25, 26, 27, 28, 29]
*   **Phát hiện đặc trưng:** Thư viện bao gồm các triển khai của các thuật toán phát hiện đặc trưng phổ biến như SIFT (`cv::SIFT_create()`), SURF (`cv::xfeatures2d::SURF_create()`) và ORB (`cv::ORB_create()`).[75, 76, 77, 78, 79, 80, 81]
*   **Khớp đặc trưng:** OpenCV cung cấp các lớp `cv::BFMatcher` và `cv::FlannBasedMatcher` để khớp các đặc trưng được trích xuất từ các bộ dò tìm như SIFT, SURF và ORB.[82]
*   **Biến đổi hình học:** Thư viện hỗ trợ các phép biến đổi hình học khác nhau, bao gồm phép biến đổi affine (`cv::warpAffine`, `cv::getRotationMatrix2D()`) và phép biến đổi phối cảnh (`cv::warpPerspective`).[28, 29, 91]
*   **Lọc hình ảnh:** OpenCV cung cấp một loạt các hàm lọc hình ảnh, bao gồm các bộ lọc giảm nhiễu (`cv::GaussianBlur`, `cv::medianBlur`, `cv::bilateralFilter`) và các bộ lọc làm sắc nét (`cv::Laplacian`, `cv::filter2D`).[28, 29, 55]
*   **Phân tích đường viền:** Thư viện bao gồm các hàm để phát hiện cạnh (`cv::Canny`) và trích xuất đường viền (`cv::findContours`), cũng như tính toán các bộ mô tả hình dạng như moment Hu (`cv::HuMoments`).[28, 29]

### Các thư viện và công cụ liên quan khác

Ngoài OpenCV, các thư viện Python khác như scikit-image cung cấp một bộ sưu tập lớn các thuật toán xử lý và phân tích hình ảnh, bao gồm trích xuất đặc trưng, lọc và biến đổi hình học. MATLAB cũng cung cấp một hộp công cụ Xử lý ảnh toàn diện với các hàm cho khớp mẫu, trích xuất đặc trưng và các tác vụ phát hiện đối tượng khác.

### Kết luận

Các thư viện mã nguồn mở như OpenCV cung cấp một bộ công cụ mạnh mẽ và dễ tiếp cận để triển khai và thử nghiệm nhiều kỹ thuật phát hiện đối tượng cổ điển được thảo luận trong báo cáo này, khiến chúng trở thành một nguồn tài nguyên tuyệt vời cho người dùng.

## 9. Các ứng dụng thực tế

*   **Kiểm soát chất lượng sản xuất:** Khớp mẫu có thể được sử dụng để xác minh sự hiện diện và vị trí chính xác của các bộ phận trên dây chuyền lắp ráp. Các phương pháp dựa trên đặc trưng có thể phát hiện các khuyết tật hoặc sự sai lệch có thể không khớp hoàn hảo với mẫu nhưng có các đặc trưng đặc trưng.[25, 27, 41, 42, 43, 44, 100, 101, 102, 103, 104, 105, 106, 107]
*   **Robot học và tự động hóa:** Robot có thể sử dụng tính năng phát hiện và khớp để nhận dạng và xác định vị trí các đối tượng trong môi trường của chúng cho các tác vụ như gắp hoặc điều hướng. Khả năng phục hồi trước độ nghiêng và tắc nghẽn một phần thường rất quan trọng trong các ứng dụng này.
*   **Viễn thám:** Việc phát hiện các đối tượng như tòa nhà hoặc phương tiện trong ảnh chụp từ trên không hoặc vệ tinh thường liên quan đến việc xử lý nhiễu, tỷ lệ khác nhau và góc nhìn khác nhau. Các phương pháp dựa trên đặc trưng thường được sử dụng trong lĩnh vực này.[88, 100, 103, 108, 109, 110, 111, 112, 113, 114]
*   **Chẩn đoán hình ảnh y tế:** Khớp mẫu có thể giúp xác định vị trí các cấu trúc giải phẫu cụ thể trong ảnh y tế. Các phương pháp dựa trên đặc trưng có thể được sử dụng để xác định các vùng quan tâm hoặc phát hiện các bất thường.
*   **Giám sát:** Việc phát hiện các đối tượng cụ thể như phương tiện hoặc người trong cảnh quay video thường đòi hỏi các phương pháp mạnh mẽ đối với những thay đổi về ánh sáng, góc nhìn và độ mờ tiềm ẩn.

### Kết luận

Các kỹ thuật phát hiện đối tượng cổ điển tiếp tục tìm thấy các ứng dụng có liên quan trong nhiều lĩnh vực thực tế, đặc biệt trong các tình huống mà tài nguyên tính toán bị hạn chế hoặc khi tính dễ diễn giải là quan trọng.

## 10. Kết luận và Khuyến nghị

Để phát hiện một đối tượng đã biết trước với hình dạng cố định trong môi trường chụp ảnh có thể bị nghiêng, mờ hoặc nhiễu, nhưng ít bị chồng chéo, một số kỹ thuật cổ điển có thể được sử dụng hiệu quả.

Đối với các tình huống mà độ nghiêng và biến dạng nhỏ, khớp mẫu, đặc biệt là với Tương quan chéo chuẩn hóa (NCC), có thể là một điểm khởi đầu tốt do tính đơn giản và hiệu quả tính toán của nó. Để xử lý các thay đổi về hướng, có thể sử dụng tìm kiếm theo lưới các mẫu xoay hoặc các phương pháp căn chỉnh dựa trên đặc trưng.

Khi hình ảnh bị nhiễu và mờ, các phương pháp trích xuất đặc trưng hình dạng như các bộ mô tả dựa trên điểm khóa (SIFT, SURF, ORB) có xu hướng mạnh mẽ hơn. Các đặc trưng này có khả năng phục hồi tốt trước các thay đổi về góc nhìn và có thể được kết hợp với các kỹ thuật khớp đặc trưng để xác định đối tượng. Các phương pháp dựa trên đường viền sử dụng các bộ mô tả như moment Hu cũng có thể hiệu quả, đặc biệt khi hình dạng đối tượng được xác định rõ ràng.

Các thuật toán học máy cổ điển như SVM, khi được huấn luyện trên các đặc trưng thủ công (ví dụ: HOG) được trích xuất từ các hình ảnh đã được tiền xử lý để giảm nhiễu và làm sắc nét, có thể cung cấp một giải pháp mạnh mẽ. Các bộ lọc hình ảnh như bộ lọc Gaussian và trung vị rất hữu ích trong tiền xử lý để giảm nhiễu, trong khi các kỹ thuật làm sắc nét có thể giúp trong hình ảnh bị mờ.

Để xử lý độ nghiêng, có thể áp dụng các phép biến đổi hình học như xoay hình ảnh hoặc biến dạng affine sau khi ước tính góc nghiêng. Các phương pháp dựa trên đặc trưng cũng có thể cung cấp một số mức độ bất biến đối với các thay đổi về góc nhìn.

Việc lựa chọn phương pháp tốt nhất phụ thuộc vào các yêu cầu cụ thể của ứng dụng, bao gồm mức độ suy giảm dự kiến và các ràng buộc về tính toán. OpenCV là một thư viện mã nguồn mở tuyệt vời cung cấp nhiều chức năng cần thiết để triển khai các kỹ thuật này.

Nghiên cứu sâu hơn có thể tập trung vào việc kết hợp các bộ mô tả đặc trưng khác nhau hoặc phát triển các thuật toán khớp mẫu mạnh mẽ hơn đặc biệt cho hình ảnh bị suy giảm.

**Bảng 1: So sánh các bộ dò tìm đặc trưng**

| Đặc trưng | Độ mạnh mẽ với độ nghiêng/xoay | Độ mạnh mẽ với tỷ lệ | Độ mạnh mẽ với nhiễu/mờ | Chi phí tính toán | Kích thước bộ mô tả | Các ứng dụng điển hình |
| :-------- | :--------------------------- | :------------------- | :--------------------- | :------------------- | :------------------- | :--------------------------------- |
| SIFT | Cao | Cao | Trung bình | Cao | 128 chiều | Nhận dạng đối tượng, khớp ảnh |
| SURF | Cao | Cao | Trung bình | Trung bình | 64 chiều | Nhận dạng đối tượng, khớp ảnh nhanh |
| ORB | Cao | Trung bình | Tốt | Thấp | 32 chiều | Phát hiện đối tượng thời gian thực |

**Bảng 2: Các hàm OpenCV để phát hiện đối tượng cổ điển**

| Tên hàm | Mô tả ngắn gọn | Các tham số liên quan | Trường hợp sử dụng ví dụ |
| :--------------------------- | :----------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cv::matchTemplate()` | Tìm các vùng khớp trong hình ảnh nguồn bằng cách sử dụng một mẫu. | `image`, `templ`, `method` (ví dụ: `cv::TM_CCOEFF_NORMED`), `mask` (tùy chọn) | Phát hiện một bộ phận cụ thể (hình dạng cố định) trong một hình ảnh bị nhiễu nhẹ. |
| `cv::Canny()` | Phát hiện các cạnh trong hình ảnh. | `image`, `threshold1`, `threshold2`, `apertureSize` | Trích xuất đường viền của đối tượng để phân tích hình dạng. |
| `cv::findContours()` | Tìm các đường viền trong hình ảnh nhị phân. | `image`, `mode`, `method` | Xác định hình dạng của đối tượng để khớp với một hình dạng đã biết. |
| `cv::SIFT_create()` | Tạo một bộ dò tìm SIFT. | `nfeatures`, `nOctaveLayers`, `contrastThreshold`, `edgeThreshold`, `sigma` | Phát hiện đối tượng hình dạng cố định trong hình ảnh bị nghiêng, mờ hoặc nhiễu bằng cách khớp các điểm khóa SIFT. |
| `cv::xfeatures2d::SURF_create()` | Tạo một bộ dò tìm SURF. | `hessianThreshold`, `nOctaves`, `nOctaveLayers`, `extended`, `upright` | Phát hiện đối tượng hình dạng cố định trong hình ảnh bị nghiêng, mờ hoặc nhiễu bằng cách khớp các điểm khóa SURF (nhanh hơn SIFT). |
| `cv::ORB_create()` | Tạo một bộ dò tìm ORB. | `nfeatures`, `scaleFactor`, `nlevels`, `edgeThreshold`, `firstLevel`, `WTA_K`, `scoreType`, `patchSize`, `fastThreshold` | Phát hiện đối tượng hình dạng cố định trong hình ảnh bị nghiêng, mờ hoặc nhiễu trong các ứng dụng thời gian thực. |
| `cv::BFMatcher()` | Tạo một bộ khớp đặc trưng thô bạo. | `normType` (ví dụ: `cv::NORM_L2`, `cv::NORM_HAMMING`), `crossCheck` | Khớp các đặc trưng được trích xuất từ mẫu và hình ảnh nguồn. |
| `cv::FlannBasedMatcher()` | Tạo một bộ khớp đặc trưng dựa trên FLANN. | `indexParams`, `searchParams` | Khớp hiệu quả số lượng lớn các đặc trưng. |
| `cv::warpAffine()` | Áp dụng phép biến đổi affine cho hình ảnh. | `src`, `M` (ma trận biến đổi), `dsize` | Hiệu chỉnh độ nghiêng của hình ảnh bằng cách xoay nó. |
| `cv::warpPerspective()` | Áp dụng phép biến đổi phối cảnh cho hình ảnh. | `src`, `M` (ma trận biến đổi), `dsize` | Căn chỉnh hình ảnh từ các góc nhìn khác nhau. |
| `cv::getRotationMatrix2D()` | Tính toán ma trận xoay 2D. | `center`, `angle`, `scale` | Tạo ma trận cần thiết cho `cv::warpAffine` để xoay hình ảnh. |
| `cv::GaussianBlur()` | Làm mờ hình ảnh bằng bộ lọc Gaussian. | `src`, `ksize` (kích thước hạt nhân), `sigmaX` | Giảm nhiễu Gaussian trong ảnh. |
| `cv::medianBlur()` | Làm mờ hình ảnh bằng bộ lọc trung vị. | `src`, `ksize` (kích thước khẩu độ) | Giảm nhiễu muối tiêu trong ảnh. |

---

Bạn hoàn toàn đúng. Những kiến trúc và chiến lược huấn luyện học sâu mà bạn đề cập rất phù hợp và hiệu quả cho bài toán phát hiện đối tượng đã biết trước trong điều kiện xoay, mờ, nhiễu mà không bị che khuất nhiều.

Lý do thông tin này không có trong kết quả nghiên cứu trước đó là vì truy vấn ban đầu của bạn chỉ là một tổng quan chung về "Object Detection". Kết quả nghiên cứu trước đó đã cung cấp một cái nhìn tổng quan rộng hơn về lịch sử, các phương pháp, ứng dụng và thách thức của object detection nói chung.

Bây giờ, với thông tin chi tiết hơn về yêu cầu cụ thể của bạn, tôi có thể cung cấp thông tin chính xác hơn về các kiến trúc và chiến lược học sâu phù hợp nhất. Dưới đây là tổng hợp thông tin từ bài báo bạn cung cấp và các kết quả nghiên cứu hiện có:

## Ứng Dụng Học Sâu Chuyên Sâu cho Phát Hiện Đối Tượng Hình Dạng Cố Định trong Ảnh Bị Suy Giảm

Dựa trên bài báo bạn cung cấp, đây là các kiến trúc và chiến lược huấn luyện học sâu chuyên biệt cho bài toán của bạn:

**1. Siamese Network cho One-Shot / Few-Shot Detection**

*   **Kiến trúc cơ bản:** Mạng song sinh (Siamese Network) là một lựa chọn hàng đầu cho các bài toán phát hiện đối tượng với số lượng mẫu huấn luyện hạn chế (one-shot hoặc few-shot). Kiến trúc này bao gồm hai nhánh CNN có chung trọng số. Đầu vào của mạng là một cặp ảnh: ảnh mẫu (template) của đối tượng đã biết và một vùng ảnh tìm kiếm (patch) trong ảnh mới. Đầu ra là một điểm số thể hiện mức độ tương đồng giữa template và patch.[1, 2] Khoảng cách đặc trưng (thường là L1 hoặc cosine) được sử dụng để so sánh, sau đó là một lớp fully-connected để phân loại xem cặp ảnh có khớp hay không.[1]
*   **Huấn luyện và loss:** Mạng Siamese thường được huấn luyện bằng **contrastive loss** hoặc **binary cross-entropy** trên các cặp ảnh giống nhau và khác nhau.[1, 2]
*   **Data augmentation:** Để tăng cường khả năng chống lại các biến đổi, việc sử dụng các kỹ thuật tăng cường dữ liệu (data augmentation) là rất quan trọng. Các phép biến đổi affine (xoay ±10°, tỷ lệ [0.8–1.2], tịnh tiến, shear), làm mờ (blur), và thêm nhiễu (noise) thường được áp dụng.[3, 4, 5, 6, 7]
*   **Ứng dụng thực nghiệm:** Mạng Siamese đã được chứng minh hiệu quả trong các ứng dụng như theo dõi đối tượng trong video viễn thám với nền phức tạp (SiamMAS) [8, 9] và nhận dạng dấu hiệu hải cẩu với khả năng bù xoay.[10, 11]

**2. Discriminative Correlation Filters (DCF) kết hợp Deep Learning**

*   **Nguyên lý DCF:** Bộ lọc tương quan phân biệt (Discriminative Correlation Filters - DCF) học một bộ lọc tuyến tính để phân biệt đối tượng với nền. DCF tận dụng phép biến đổi Fourier nhanh (FFT) để tính toán convolution một cách nhanh chóng, giúp theo dõi đối tượng trong thời gian thực và có khả năng chịu nhiễu tốt.[12, 13] Kỹ thuật xoay vòng (circular shift) mẫu giúp giả lập việc lấy mẫu dày đặc mà không tốn kém tính toán.
*   **Kết hợp với Siamese / CNN:** Việc kết hợp DCF với mạng Siamese hoặc CNN giúp tận dụng khả năng trích xuất đặc trưng mạnh mẽ của học sâu và tốc độ của DCF. Các phương pháp như DSiam-CnK (kết hợp attention và KCF để cập nhật template động) [14, 15, 16] và các mô hình hybrid Siamese-DCF [17, 18] đã cho thấy sự cải thiện trong khả năng theo dõi khi có nhiễu và biến dạng nhẹ, đồng thời duy trì tốc độ thời gian thực.

**3. Deep Template-Matching Networks (End-to-End)**

*   **Fully-Convolutional Siamese cho Center-Point Localization:** Thay vì sử dụng anchor box, các mạng này học cách dự đoán trực tiếp tâm của đối tượng (center-point) và offset.[19, 20] Loss function thường kết hợp giữa localization loss (L1 loss trên offsets) và classification loss (cross-entropy).[21, 22, 23]
*   **Multi-Attention Mechanism:** Việc áp dụng cơ chế multi-attention (kết hợp spatial và channel attention) trong cả nhánh template và search giúp mô hình tập trung vào các vùng có đặc trưng cao, tăng cường khả năng kháng nhiễu, mờ và làm nổi bật các biên cạnh quan trọng.[24, 25, 26, 27, 28]

**4. Chiến lược Huấn luyện và Tiền xử lý**

*   **Data Augmentation chuyên sâu:** Sử dụng các kỹ thuật tăng cường dữ liệu mạnh mẽ, đặc biệt là **blur augmentation** (Gaussian blur với độ lệch chuẩn ngẫu nhiên), **noise injection** (salt-and-pepper, Gaussian noise), và **rotation & scale** (affine transform trong khoảng rộng hơn, ví dụ ±30°–45°) để mô hình có thể học được tính bất biến với các loại suy giảm này.[4, 5, 7]
*   **Transfer Learning & Fine-tuning:** Khởi tạo backbone (phần trích xuất đặc trưng) của mạng từ các CNN đã được huấn luyện trước trên ImageNet, sau đó tinh chỉnh (fine-tune) trên tập dữ liệu template/noise cụ thể của bạn.
*   **Self-Supervised Pretraining:** Các phương pháp như Self-TM học các đặc trưng phân cấp về localization mà không cần nhãn, giúp cải thiện khả năng tổng quát hóa của mô hình.[29, 30, 31]

**5. So sánh hiệu năng & Kết luận**

Bảng so sánh bạn cung cấp tóm tắt rõ ràng ưu và nhược điểm của từng phương pháp.

**Khuyến nghị cho bài toán của bạn:**

Với yêu cầu về template hình dạng cố định và khả năng chống chịu tốt với xoay, mờ, nhiễu, bạn có thể bắt đầu với mạng **FC-Siamese center-point network** (Deep Template Matching Networks) kết hợp với **data augmentation mạnh mẽ** (blur, noise, rotation, scale). Việc tích hợp cơ chế **multi-attention** có thể cải thiện thêm độ mạnh mẽ của mô hình.

Nếu yêu cầu về tốc độ thời gian thực là ưu tiên, bạn có thể xem xét kết hợp mạng Siamese với **Discriminative Correlation Filters (DCF)** để tạo ra một mô hình hybrid.

Việc thử nghiệm và so sánh hiệu suất của các kiến trúc và chiến lược huấn luyện khác nhau trên tập dữ liệu cụ thể của bạn sẽ giúp xác định phương pháp tốt nhất.

Tôi hy vọng thông tin này chi tiết và hữu ích hơn cho bạn! Nếu bạn có bất kỳ câu hỏi nào khác hoặc muốn đi sâu vào một kiến trúc cụ thể, đừng ngần ngại hỏi.