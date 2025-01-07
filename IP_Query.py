import tkinter as tk
from tkinter import messagebox
import requests

def query_ip():
    ip_address = entry.get().strip()
    if not validate_ip(ip_address):
        result_label.config(text="Bu IP Adresi Hatalı!", fg="red", bg="black")
        return

    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}").json()
        if response['status'] == 'success':
            country = response.get('country', 'Bilinmiyor')
            city = response.get('city', 'Bilinmiyor')
            lat = response.get('lat', 'Bilinmiyor')
            lon = response.get('lon', 'Bilinmiyor')
            isp = response.get('isp', 'Bilinmiyor')

            result_label.config(
                text=f"IP Adresi: {ip_address}\nÜlke: {country}\nŞehir: {city}\nEnlem: {lat}\nBoylam: {lon}\nISP: {isp}",
                fg="white", bg="green"
            )
        else:
            result_label.config(text="Bu IP Adresi Hatalı!", fg="red", bg="black")
    except Exception as e:
        result_label.config(text="Bir hata oluştu!", fg="red", bg="black")


def validate_ip(ip):
    """IP adresinin geçerli olup olmadığını kontrol eder."""
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(part) <= 255 for part in parts)
    except ValueError:
        return False

def animate_text():
    """Basit bir animasyon örneği."""
    current_text = animated_label.cget("text")
    new_text = current_text[1:] + current_text[0]
    animated_label.config(text=new_text)
    root.after(200, animate_text)

# Pencere oluşturma
root = tk.Tk()
root.title("IP Sorgulama Uygulaması")
root.geometry("400x400")
root.configure(bg="darkgray")

# Başlık animasyonu
animated_label = tk.Label(root, text="*** IP Sorgulama Uygulaması ***", font=("Arial", 14), fg="blue", bg="darkgray")
animated_label.pack(pady=10)
animate_text()

# IP adresi girişi
entry_label = tk.Label(root, text="IP Adresi Giriniz:", font=("Arial", 12), bg="darkgray", fg="black")
entry_label.pack()
entry = tk.Entry(root, font=("Arial", 12), width=30, bg="lightyellow", fg="black")
entry.pack(pady=5)

# Sorgulama butonu
query_button = tk.Button(root, text="Tıkla", font=("Arial", 12), command=query_ip, bg="blue", fg="black", activebackground="darkblue", activeforeground="white")
query_button.pack(pady=10)

# Sonuç etiketi
result_label = tk.Label(root, text="", font=("Arial", 12), bg="darkgray", fg="black", wraplength=380, justify="left")
result_label.pack(pady=10)

# Ana döngü
root.mainloop()
