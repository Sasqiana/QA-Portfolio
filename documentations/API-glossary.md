# API Testing Glossary (Postman)

Daftar istilah penting seputar API testing menggunakan Postman.

---

### 1. Endpoint
URL tujuan API yang digunakan untuk mengakses resource/data.
Contoh: `https://dummyjson.com/products`

### 2. Method
Jenis permintaan yang dikirim:
- `GET`: ambil data
- `POST`: kirim data baru
- `PUT`: update seluruh data
- `PATCH`: update sebagian data
- `DELETE`: hapus data

### 3. Request
Permintaan yang dikirim dari Postman ke server, terdiri dari method, URL, header, dan body.

### 4. Response
Balasan dari server berupa status code, body, dan informasi lain.

### 5. Status Code
Kode yang menunjukkan hasil request:
- `200 OK`: berhasil
- `201 Created`: data berhasil dibuat
- `400 Bad Request`: request salah
- `401 Unauthorized`: butuh otentikasi
- `404 Not Found`: data tidak ditemukan
- `500 Internal Server Error`: error dari server

### 6. Params (Query Parameters)
Digunakan untuk mengirim data tambahan dalam URL.
Contoh: `?limit=10&skip=5`

### 7. Headers
Informasi tambahan dalam request, seperti format data (`Content-Type`) atau token akses (`Authorization`).

### 8. Body
Data yang dikirim dalam request, terutama pada method POST/PUT.
Format umum: JSON.
> Contoh:
```json
{
  "title": "Product A",
  "price": 150
}
```
### 9. Collection
Kumpulan request API yang dikelompokkan dalam satu file Postman.

### 10. Test Script (Tests tab)
Kode untuk memverifikasi response API secara otomatis menggunakan JavaScript.
> Contoh:
```js
pm.test("Status code is 200", function () {
  pm.response.to.have.status(200);
});
```
### 11. Environment
Tempat menyimpan variabel global seperti URL dasar (`base_url`) atau token.

### 12. Authorization
Pengaturan akses ke API, seperti Bearer Token, API Key, Basic Auth, dll.

---
> Notes:

File ini disusun sebagai dokumentasi istilah penting dalam API testing untuk mendukung pemahaman dalam portfolio QA. Disusun dari hasil belajar mandiri dan praktik langsung di Postman.

