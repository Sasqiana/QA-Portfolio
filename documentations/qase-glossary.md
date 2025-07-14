# 📗 Qase.io Glossary for Manual Testing

Dokumentasi istilah penting yang digunakan dalam platform Qase.io untuk pengujian manual, penulisan test case, dan pengelolaan test run.

---

### 1. Project
Tempat untuk mengelola semua test case yang berkaitan dengan satu aplikasi atau sistem. Biasanya 1 project untuk 1 aplikasi.

---

### 2. Test Case
Langkah pengujian terstruktur untuk memverifikasi satu fungsi tertentu.
Biasanya berisi:
- **Title**: Nama test case
- **Precondition**: Syarat sebelum test dijalankan
- **Steps**: Langkah-langkah yang harus dilakukan
- **Expected Result**: Hasil yang diharapkan dari langkah tersebut
- **Postcondition** *(opsional)*: Kondisi setelah pengujian selesai

---

### 3. Test Suite
Kumpulan test case yang dikelompokkan berdasarkan fitur atau modul tertentu.
> Contoh: "Login Module", "Shopping Cart"

---

### 4. Test Run
Eksekusi dari test case yang sudah dibuat.
Di sinilah kamu mencatat apakah test case tersebut **Passed**, **Failed**, **Blocked**, atau **Skipped**.

---

### 5. Test Plan
Rencana pengujian yang bisa terdiri dari beberapa test suite dan test run. Berguna saat testing besar (misal: sebelum release).

---

### 6. Step
Langkah individual dalam sebuah test case. Setiap step biasanya punya:
- **Action** (apa yang dilakukan)
- **Expected Result** (apa yang diharapkan terjadi)

---

### 7. Status
Hasil dari test case saat dijalankan:
- **Passed**: Berhasil sesuai harapan
- **Failed**: Gagal atau error
- **Blocked**: Tidak bisa dijalankan karena ada halangan (misal: bug belum diperbaiki)
- **Skipped**: Dilewati

---

### 8. Severity
Tingkat keparahan dari hasil gagal (jika test case gagal).
Biasanya disesuaikan dengan **bug severity**.

---

### 9. Attachment
Bukti visual berupa screenshot, file, atau dokumen lain yang ditambahkan ke test case atau test run.

---

### 10. Integration
Qase bisa terhubung ke tools lain seperti:
- **Jira** (untuk melaporkan bug)
- **Postman** (untuk testing API)
- **Slack**, **GitHub**, dan lainnya

---

📌 **Catatan**  
File ini disusun sebagai dokumentasi istilah penting dalam penggunaan Qase.io untuk pengujian manual dan pembuatan test case. Digunakan sebagai bagian dari dokumentasi dalam portfolio QA.
