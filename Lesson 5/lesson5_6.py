import machine
import time

# 設定內建 LED
# 注意：Pico W 的內建 LED 腳位名稱為 'LED'，而非舊版 Pico 的 25
led = machine.Pin('LED', machine.Pin.OUT)

while True:
    # --- 第一次閃爍 ---
    led.on()
    time.sleep(0.1)  # 亮 0.1 秒
    led.off()
    time.sleep(0.1)  # 滅 0.1 秒
    
    # --- 第二次閃爍 ---
    led.on()
    time.sleep(0.1)  # 亮 0.1 秒
    led.off()
    
    # --- 等待週期結束 ---
    # 目前已消耗時間：0.1 + 0.1 + 0.1 = 0.3 秒
    # 若要維持每 1 秒一個循環，需等待：1.0 - 0.6 = 0.7秒
    time.sleep(0.7)