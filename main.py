# main.py

from func import run_loop

# Zaman bilgisi içeren metin kutusu
# 385 393 x1 y1 
# 743 417 x2 y2

# Tıklanacak ilk konum
# 238 750

# Tıklanacak ikinci konum
# 1796 702

def main():
    """
    run_loop fonksiyonunu uygun parametrelerle başlatır
    """
    time_region = (385, 393, 743, 417)     # zaman kutusunun bulunduğu bölge
    scroll_amount = -5000                  # aşağı kaydırma miktarı
    first_click_pos = (238, 750)          # ilk tıklama konumu
    second_click_pos = (1796, 702)        # ikinci tıklama konumu

    run_loop(time_region, scroll_amount, first_click_pos, second_click_pos)

if __name__ == "__main__":
    main()
