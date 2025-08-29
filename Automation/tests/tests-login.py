from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time

#inisialisasi browser Chrome
driver = webdriver.Chrome()

# buka halaman login
driver.get("https://www.saucedemo.com/")

# tunggu beberapa detik agar halaman sepenuhnya dimuat
time.sleep(2)

# cari elemen username dan password
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")

# masukkan username dan password
username.send_keys("standard_user")
password.send_keys("secret_sauce")

# klik tombol login
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

time.sleep(5)

# verifikasi apakah login berhasil
expected_url = "https://www.saucedemo.com/inventory.html"
if driver.current_url == expected_url:
    print("Login berhasil!")
else:
    print("Login gagal!")

# tutup browser
driver.quit()
