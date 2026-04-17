# **🚜 Hệ Thống Cân Điện Tử Thông Minh (IoT Smart Scale)**

Dự án sử dụng ESP8266 kết hợp với cảm biến HX711 để đo lường khối lượng, gửi dữ liệu qua giao thức MQTT và cho phép cấu hình từ xa thông qua Dashboard Streamlit.



### **✨ Tính năng nổi bật**

* **Tiết kiệm năng lượng cực độ:** Sử dụng chế độ Deep Sleep và Transistor ngắt nguồn hoàn toàn cảm biến khi không đo.



* **Cấu hình từ xa:** Thay đổi hệ số Calibration, thời gian ngủ, và lệnh Tare trực tiếp từ Cloud.



* **Lưu trữ thông minh:** Mọi thông số (ID, Calib, Offset) được lưu vào bộ nhớ NVS (Flash), không bị mất khi mất điện hoặc khi đi ngủ.



###### **Chế độ kép:**



* RUN MODE: Thức dậy -> Đo -> Gửi dữ liệu -> Ngủ (Tối ưu pin).



* SETUP MODE: Thức liên tục để hiệu chỉnh và cấu hình qua Serial/App.



### **🛠 Sơ đồ đấu nối (Hardware)**

**Linh kiện			Chân ESP8266			Chú thích**

HX711 DOUT      D2 (GPIO 4)	   Chân dữ lieu

HX711 CLK	D1 (GPIO 5)	   Chân xung nhịp

Switch Setup	D7 (GPIO 13)	   Nối xuống GND để vào Setup Mode

Power Control	D6 (GPIO 12)	   Điều khiển Transistor cấp nguồn





### **🚀 Hướng dẫn cài đặt**



###### **1. Cấu hình ESP8266**

Cài đặt thư viện: HX711, PubSubClient, Preferences, ArduinoJson.



Mở file code Arduino, cập nhật thông tin WiFi và Broker MQTT:



*C++*

*const char\* ssid = "Tên\_WiFi\_Của\_Bạn";*

*const char\* password = "Mật\_Khẩu\_WiFi";*

*const char\* mqtt\_server = "192.168.1.100"; // Broker công cộng*



Nạp code cho ESP8266.



###### **2. Triển khai Dashboard (Streamlit)**

Tạo Repository trên GitHub chứa file app.py và requirements.txt.



Kết nối với Streamlit Cloud.



Đảm bảo biến MQTT\_SERVER trong app.py trùng với biến trong ESP8266.





#### **🕹 Hướng dẫn sử dụng**

###### **Quy trình hiệu chuẩn (Calibration)**

Để cân hoạt động chính xác, bạn cần thực hiện các bước sau tại giao diện Setup Mode (Gạt Switch D7 xuống GND):



* Lấy vạch 0 (Tare): Đảm bảo cân trống. Nhấn nút TARE trên Dashboard hoặc gõ t trên Serial Monitor.
* Xác định hệ số Calib: \* Đặt một vật mẫu (ví dụ: chai nước 500ml) lên cân.



&#x09;Nếu cân hiển thị sai, điều chỉnh số Calibration Factor trên Dashboard cho đến khi cân 	hiện đúng 0.5kg.



&#x09;Nhấn Save để lưu vào bộ nhớ Flash.

###### 

###### **Vận hành thực tế**

Gạt Switch D7 lên mức HIGH (Hở mạch).



Thiết bị sẽ tự động gửi dữ liệu khối lượng lên Server theo chu kỳ sleep\_time đã cài đặt.



Dữ liệu được gửi dưới dạng JSON:



JSON

{"id":"C\_0001", "weight": 1.25, "uptime": 4500}



