import requests
import csv

# Fungsi untuk membaca API Key dari file .txt
def get_api_key_from_file(file_path):
    with open(file_path, 'r') as file:
        api_key = file.readline().strip()  # Membaca baris pertama dan menghapus spasi
        return api_key

# Ambil API Key dari file apikey.txt
api_key = get_api_key_from_file('apikey.txt')

# Meminta input dari pengguna untuk kata kunci dan jumlah data
keyword = input("Masukkan kata kunci pencarian: ")
num = input("Masukkan jumlah data yang diinginkan: ")

url = 'https://unofficial-pinterest-api.p.rapidapi.com/pinterest/pins/relevance'
querystring = {"keyword": keyword, "num": num}

headers = {
    'x-rapidapi-host': 'unofficial-pinterest-api.p.rapidapi.com',
    'x-rapidapi-key': api_key
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    data = response.json().get('data', [])
    
    # Menyimpan output ke dalam file CSV
    with open('url_printerest_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Nomor', 'Link'])  # Menulis header
        
        for index, item in enumerate(data, start=1):
            link = f"https://id.pinterest.com/pin/{item.get('id')}"
            writer.writerow([index, link])  # Menulis nomor dan link ke dalam CSV

    print("Output telah disimpan ke dalam file 'url_printerest_data.csv'.")
else:
    print("Request failed with status code:", response.status_code)
