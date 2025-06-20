## SD-LG-002: Login dengan Kredensial Invalid

**Pre-condition:**
User berada di halaman login

**Steps:**
1. Kosongkan kolom username
2. Kosongkan kolom password
3. Klik tombol Login atau Enter

**Expected Result:**
Tidak berhasil login dan sistem menampilkan wording berwarna merah "Epic sadface: Username is required".

**Actual Result:**
PASSED, as expected. Sistem menampilkan wording dan tidak berhasil login.

**Post Condition:**
User tetap berada di halaman login

**Documentation:**
![Login Failed](../documentations/)
