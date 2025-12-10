## ⭐ TikTok Auto Booster (CLI Tool)

Sebuah alat *command-line interface* (CLI) yang dirancang untuk mengakses layanan *free boost* TikTok melalui API pihak ketiga. Alat ini dilengkapi dengan antarmuka yang ramah pengguna, *cooldown timer* visual, dan sistem otentikasi berbasis token eksternal untuk kontrol akses.

---

### 🚀 Fitur Utama

| Fitur | Deskripsi | Manfaat bagi Pengguna |
| :--- | :--- | :--- |
| **Otentikasi Pastebin** | Membutuhkan Token Akses yang diambil secara dinamis dari URL Pastebin. | **Keamanan Akses:** Hanya pengguna dengan token terbaru yang bisa menjalankan script. |
| **Menu Dinamis** | Memuat daftar layanan (Views, Likes, Followers) dan status `[WORKING]` / `[DOWN]` langsung dari API. | **Visibilitas:** Mengetahui layanan mana yang sedang aktif sebelum digunakan. |
| **Visual Cooldown** | Menampilkan hitungan mundur waktu tunggu yang jelas di terminal. | **User Experience:** Tidak perlu menunggu dalam keheningan, waktu tunggu terpantau. |
| **Pengecekan ID Otomatis** | Mengubah link video TikTok yang panjang menjadi Video ID yang dibutuhkan API. | **Efisiensi:** Menghemat waktu dan mengurangi *error* input. |

---

### 🛠️ Persyaratan dan Instalasi

Script ini membutuhkan **Python 3** dan beberapa pustaka eksternal.

#### 1. Instalasi Dependensi

Jalankan perintah berikut di Terminal atau Command Prompt Anda:

```bash
pip install requests colorama
