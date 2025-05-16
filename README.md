# Instagram Story Downloader

Program Python sederhana dan aman untuk mengunduh Instagram Stories dari akun mana pun yang Anda inginkan.

Alat ini mendukung login dengan username dan password, termasuk akun dengan autentikasi dua faktor (2FA).  
Sesi login Anda akan disimpan sehingga Anda tidak perlu login setiap saat, dan Anda dapat logout untuk menghapus sesi tersebut.

---

## Fitur

- Login ke Instagram dengan username & password
- Mendukung Autentikasi Dua Faktor (2FA) menggunakan aplikasi autentikator (Google Authenticator, Authy, dll)
- Otomatis menyimpan sesi login ke file sehingga tidak perlu login ulang
- Opsi logout untuk menghapus sesi dan memaksa login ulang
- Unduh Instagram Stories langsung dari URL story
- Antarmuka terminal yang mudah digunakan

---

## Persyaratan

- Python 3.6 atau lebih baru
- Library Python `instaloader` (`pip install instaloader`)

---

## Instalasi

1. Clone repositori ini atau unduh sebagai ZIP dan ekstrak:

    ```bash
    git clone https://github.com/username/instagram-story-downloader.git
    cd instagram-story-downloader
    ```

---

## Cara Penggunaan

- Jika belum pernah login, program akan meminta username dan password Instagram Anda.
- Jika akun Anda menggunakan 2FA, masukkan kode dari aplikasi autentikator saat diminta.
- Setelah login berhasil, masukkan URL Instagram Story yang ingin diunduh.
- Story yang diunduh akan disimpan di folder dengan nama username target.
- Untuk logout, pilih opsi logout untuk menghapus sesi Anda.

**Contoh URL:**  
`https://www.instagram.com/stories/username/1234567890/`  
Program akan mengambil username dari URL dan mengunduh story yang tersedia ke folder utama.

---

## Tips & Catatan

- Pastikan username dan password Anda benar.
- Kode 2FA bersifat sensitif waktu; gunakan kode terbaru dari aplikasi autentikator Anda.
- Sesi login disimpan dalam file `username-session` di folder program. Jangan bagikan file ini.
- Jika mengalami error saat login, coba logout terlebih dahulu untuk menghapus sesi lama, lalu login kembali.
- Hanya story aktif (belum kadaluarsa) yang dapat diunduh.
- Gunakan secara bertanggung jawab dan jangan mengunduh konten tanpa izin pemiliknya.


---

## Lisensi
Project ini bersifat open source dan dapat digunakan secara gratis.
Gunakan sesuai kebijakan Instagram dan hukum yang berlaku.

---

## Kontak
Jika ada pertanyaan, kamu bisa hubungi:

Email: maiekerurahadian@gmail.com