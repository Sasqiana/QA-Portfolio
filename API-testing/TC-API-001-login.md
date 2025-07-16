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
**Functional Bug**: login tidak bisa dijalankan karena flow tidak logis

**Attachment:**
![API login](../documentations/)
