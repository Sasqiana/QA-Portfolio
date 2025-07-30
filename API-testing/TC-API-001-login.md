# TC-API-001: Login With Valid Credential (Access Denied)

**Endpoint:** https://dummyjson.com/auth/login`

**Method:** POST

**Request Body:**
```json
{
  "username": "kminchelle",
  "password": "0lelplR"
}

```

**Expected Result:**
- Status Code: `200 OK`
- Response Body:
```json

  "id": 15
  "username": "kminchelle",
  "email": "kminchelle@example.com",
  "token": "..."

```
**Actual Result:**
- Status Code: `401 Unauthorized`
- Response Body:
```json
{
  "message": "Access Token is required"
}
```
- Dari sisi teknis:
Endpoint /auth/login menolak request karena meminta token terlebih dahulu, padahal seharusnya login adalah proses awal untuk mendapatkan token, bukan sebaliknya.

- Dari sisi pengguna:
Pengguna tidak dapat melakukan login meskipun telah mengisi username dan password dengan benar. Hal ini menyebabkan fungsi login gagal sepenuhnya, dan dapat dianggap sebagai bug fungsional yang menghambat akses user ke sistem.

---

**Attachment:**
![API login](../documentations/TC-API-001.png)
