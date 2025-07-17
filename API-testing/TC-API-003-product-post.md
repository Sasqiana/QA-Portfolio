# TC-API-003: Add New Product (POST)

**Endpoint:** https://dummyjson.com/products/add

**Method:** POST

**Request Header:** Content-Type: application/json

**Request Body:**

```json
{
  "title": "QA Test Product",
  "description": "This is a product added via API testing",
  "price": 199,
  "brand": "QA Brand",
  "category": "smartphones"
}

```

**Expected Result:**
- Status Code: `201 Created`
- Response Body: Data yang berhasil ditambahkan dalam format raw json

**Actual Result:**
- Passed, as expected data berhasil ditambahkan dan status code sesuai yaitu `201 Created`
  
**Attachment:**
![Add new data](../documentations/)
