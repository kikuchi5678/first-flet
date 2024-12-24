import tkinter as tk
import requests
from PIL import Image, ImageTk  # Pillowライブラリをインポート
import json

# 天気予報 API の URL
API_URL = "https://weather.tsukumijima.net/api/forecast"

# 都市名とそのIDの辞書
city_ids = {
    "札幌": "016010",
    "仙台": "040010",
    "福島": "070010",
    "さいたま": "110010",
    "熊谷": "110020",
    "東京": "130010",
    "静岡": "220010",
    "名古屋": "230010",
    "大阪": "270000",
    "福岡": "400010",
    "那覇": "471010"
}

def fetch_weather():
    # ID 番号を取得
    area_id = entry.get()
    
    # URL に ID 番号を含めてリクエストを送信
    params = {"city": area_id}
    try:
        response = requests.get(API_URL, params=params)
        data = response.json()
        
        # 天気情報の表示
        if "forecasts" in data:
            forecast = data["forecasts"][0]
            weather_info = f"日時: {forecast['dateLabel']}\n"
            weather_info += f"天気: {forecast['telop']}\n"
            weather_info += f"気温: {forecast['temperature']['max']['celsius']}°C ~ {forecast['temperature']['min']['celsius']}°C"
            label_result.config(text=weather_info)
        else:
            label_result.config(text="指定したIDが無効です。")
    
    except requests.exceptions.RequestException as e:
        label_result.config(text=f"エラーが発生しました: {e}")

def update_entry_from_menu(value):
    # メニューから選択された都市IDをエントリーに反映
    entry.delete(0, tk.END)  # 現在の入力を消去
    entry.insert(0, city_ids[value])  # 選択された都市IDを入力欄に設定

# GUI の設定
root = tk.Tk()
root.title("🌦️ 天気予報アプリ 🌤️")
root.geometry("600x700")  # ウィンドウのサイズを変更

# 背景色を設定
root.config(bg="#f0f8ff")  # 明るい青色

# 画像を読み込む (src/assets/forecast1.jpg)
image = Image.open("src/assets/forecast1.jpg")  # 画像ファイルを開く
image = image.resize((300, 300))  # 画像サイズを調整
photo = ImageTk.PhotoImage(image)  # tkinterが扱える形式に変換

# 画像を表示するLabelを追加
label_image = tk.Label(root, image=photo, bg="#f0f8ff")
label_image.grid(row=0, column=0, columnspan=2, pady=20)

# ヘッダーラベル
header_label = tk.Label(root, text="天気予報を取得", font=("Arial", 24, "bold"), bg="#f0f8ff", fg="#4682b4")
header_label.grid(row=1, column=0, columnspan=2, pady=10)

# 都市選択用のラベル
label_city = tk.Label(root, text="都市を選択してください:", font=("Arial", 16), bg="#f0f8ff")
label_city.grid(row=2, column=0, sticky="w", padx=20, pady=10)

# 都市IDを選択するためのOptionMenu
city_menu = tk.StringVar()
city_menu.set("札幌")  # 初期値を設定
dropdown = tk.OptionMenu(root, city_menu, *city_ids.keys(), command=update_entry_from_menu)
dropdown.config(font=("Arial", 14), width=15)
dropdown.grid(row=2, column=1, padx=20, pady=10)

# ID 番号が入力されますラベル
label_id = tk.Label(root, text="ID 番号が入力されます:", font=("Arial", 16), bg="#f0f8ff")
label_id.grid(row=3, column=0, sticky="w", padx=20, pady=10)

# ID 番号を入力するエントリーボックス
entry = tk.Entry(root, font=("Arial", 14), width=20, borderwidth=2, relief="solid")
entry.grid(row=3, column=1, padx=20, pady=10)

# 天気予報を取得するボタン
button = tk.Button(root, text="天気予報を取得", font=("Arial", 16), bg="#4682b4", fg="white", command=fetch_weather)
button.grid(row=4, column=0, columnspan=2, pady=20)

# 結果を表示するラベル
label_result = tk.Label(root, text="結果がここに表示されます", font=("Arial", 16), bg="#f0f8ff", fg="#333333", justify=tk.LEFT)
label_result.grid(row=5, column=0, columnspan=2, pady=20)

# GUI のメインループを開始
root.mainloop()
