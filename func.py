# func.py

import pyautogui
import pytesseract
import time
from PIL import ImageGrab
import re

def get_time_from_screen(region):
    """
    region: (left, top, width, height) şeklinde zamanın yazdığı ekran bölgesi
    ekran görüntüsünden dakika:saniye formatında zamanı okur ve toplam saniye cinsinden döner
    """
    screenshot = ImageGrab.grab(bbox=region)
    text = pytesseract.image_to_string(screenshot)
    print(f"OCR çıktısı: '{text.strip()}'")

    match = re.search(r"(\d+)\s*\.?\s*dk\s+(\d+)\s*sn", text)
    if match:
        minutes = int(match.group(1))
        seconds = int(match.group(2))
        print(f"Okunan süre: {minutes} dakika, {seconds} saniye")
        return minutes * 60 + seconds
    else:
        print("Süre bulunamadı, 0 döndü")
        return 0

def wait_for_seconds(seconds):
    """
    seconds: beklenilecek süre (saniye cinsinden)
    verilen süre kadar bekler
    """
    half_mins = seconds // 30
    for _ in range(half_mins + 3):
        click_position(93, 745)
        time.sleep(45)

def scroll_down(amount):
    """
    amount: kaç birim scroll yapılacağı (örneğin -500 aşağı kaydırmak için)
    ekranda scroll işlemi yapar
    """
    pyautogui.scroll(amount)

def click_position(x, y):
    """
    x: tıklanacak konumun x koordinatı
    y: tıklanacak konumun y koordinatı
    verilen konuma tıklar
    """
    pyautogui.moveTo(x, y)
    pyautogui.click()

def run_loop(time_region, scroll_amount, first_click_pos, second_click_pos):
    """
    time_region: zamanın yazdığı ekran bölgesi (left, top, width, height)
    scroll_amount: scroll yapılacak miktar
    first_click_pos: ilk tıklama konumu (x, y)
    second_click_pos: ikinci tıklama konumu (x, y)
    bu işlemleri sonsuz döngüyle tekrarlar: zaman al -> bekle -> scroll -> tıkla -> bekle -> tıkla
    """
    wait_for_seconds(5)
    while True:
        wait_time = get_time_from_screen(time_region)
        wait_for_seconds(wait_time)
        scroll_down(scroll_amount)
        time.sleep(10)
        click_position(*first_click_pos)
        click_position(*second_click_pos)
