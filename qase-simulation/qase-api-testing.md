# Qase Test Run Log – API Testing (DummyJSON)

**Project**: QA Portfolio – DummyJSON API  
**Module**: API-testing  
**Test Run Title**: API Testing Run - DummyJSON  
**Tester**: Sasqiana
**Executed on**: 26 Juli 2025 

---

## Test Case Summary

| TC-ID          | Title                          | Status      | Notes                |Title                                                    |
|----------------|--------------------------------|-------------|----------------------|---------------------------------------------------------|
| TC-API-001     | Login With Valid Credential    | ❌ Failed   | API response: 401    | ![Test Run API](../documentations/Qase-API-test-001.png)|
| TC-API-002     | Get All Products               | ✅ Passed   | Data returned normal | ![Test Run API](../documentations/Qase-API-test-002.png)|
| TC-API-003     | Create New Product (POST)      | ✅ Passed   | Product created      | ![Test Run API](../documentations/Qase-API-test-003.png)|
| TC-API-004     | Update Product (PUT)           | ✅ Passed   | Product updated      | ![Test Run API](../documentations/Qase-API-test-004.png)|
| TC-API-005     | Delete Product (DELETE)        | ✅ Passed   | Product deleted      | ![Test Run API](../documentations/Qase-API-test-005.png)|

---

## Test Result Summary:
- **Total**: 5 test cases  
- **Passed**: 4  
- **Failed**: 1 (login - access denied)  
- **Blocked/Skipped**: 0  

---

📝 **Kesimpulan**:  
Pengujian API DummyJSON berhasil dijalankan dengan total 5 skenario. Semua berhasil **kecuali login**, karena endpoint saat ini tidak mengizinkan akses (kemungkinan tidak aktif atau butuh token). Hal ini dicatat sebagai catatan penting (bukan bug dari kita).

