import streamlit as st
import paho.mqtt.client as mqtt
import json

# Cấu hình MQTT
MQTT_SERVER = "192.168.1.100"
TOPIC_CMD = "farm/scales/C_0001/cmd"

st.set_page_config(page_title="IoT Scale Admin", layout="centered")

st.title("🚜 Farm Scale Dashboard")
st.subheader("Cấu hình thiết bị: C_0001")

# Kết nối MQTT (phần xử lý ngầm)
client = mqtt.Client()
client.connect(MQTT_SERVER, 1883, 60)

# Giao diện điều khiển
col1, col2 = st.columns(2)

with col1:
    new_calib = st.number_input("Hệ số Calibration", value=109230.0)
    if st.button("Cập nhật Calib"):
        payload = json.dumps({"calib": new_calib})
        client.publish(TOPIC_CMD, payload)
        st.success(f"Đã gửi Calib: {new_calib}")

with col2:
    new_sleep = st.number_input("Thời gian ngủ (giây)", value=5, step=1)
    if st.button("Cập nhật Sleep"):
        payload = json.dumps({"sleep_time": new_sleep})
        client.publish(TOPIC_CMD, payload)
        st.success(f"Đã gửi Sleep: {new_sleep}s")

st.divider()

if st.button("🚨 THỰC HIỆN TARE (RESET 0)", use_container_width=True):
    client.publish(TOPIC_CMD, json.dumps({"tare": 1}))
    st.warning("Đã gửi lệnh Tare!")
