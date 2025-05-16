import instaloader
import os
from urllib.parse import urlparse

def extract_username_from_story_url(url):
    parsed = urlparse(url)
    path_parts = parsed.path.strip("/").split("/")
    if "stories" in path_parts:
        return path_parts[path_parts.index("stories") + 1]
    else:
        raise ValueError("URL bukan story Instagram yang valid. Format yang benar: https://www.instagram.com/stories/username/...")

def login_instagram():
    print("=== Login Instagram ===")
    username = input("Masukkan username Instagram Anda: ")
    password = input("Masukkan password Instagram Anda (akan terlihat): ")

    L = instaloader.Instaloader()
    try:
        print("\n🔐 Login ke Instagram...")
        L.login(username, password)
        print("✅ Login berhasil tanpa 2FA.")
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        print("📱 Akun Anda menggunakan verifikasi dua langkah (2FA).")
        two_factor_code = input("Masukkan kode 2FA dari aplikasi/authenticator Anda: ")
        try:
            L.two_factor_login(two_factor_code)
            print("✅ Login berhasil dengan 2FA.")
        except Exception as e:
            print("❌ Gagal login dengan 2FA:", e)
            return None, None
    except Exception as e:
        print("❌ Gagal login:", e)
        return None, None

    # Simpan sesi login
    L.save_session_to_file(filename=f"{username}-session")
    return L, username

def load_session():
    print("🔄 Mengecek sesi login yang tersimpan...")
    for file in os.listdir():
        if file.endswith("-session"):
            username = file.replace("-session", "")
            print(f"✅ Sesi login ditemukan untuk akun: {username}")
            L = instaloader.Instaloader()
            try:
                L.load_session_from_file(username, filename=file)
                return L, username
            except Exception as e:
                print("❌ Gagal memuat sesi:", e)
    return None, None

def logout(username):
    session_file = f"{username}-session"
    if os.path.exists(session_file):
        os.remove(session_file)
        print(f"🚪 Anda telah keluar. Sesi untuk '{username}' telah dihapus.")
    else:
        print("⚠️ Tidak ada sesi yang tersimpan.")

def download_story(L, target_username):
    print(f"\n🔽 Mengunduh story dari akun: {target_username}")
    try:
        profile = instaloader.Profile.from_username(L.context, target_username)
        downloaded = False
        for story in L.get_stories(userids=[profile.userid]):
            for item in story.get_items():
                L.download_storyitem(item, target=target_username)
                downloaded = True

        if downloaded:
            print("✅ Story berhasil diunduh.\n")
        else:
            print("⚠️ Tidak ada story yang tersedia untuk akun ini.\n")
    except Exception as e:
        print("❌ Gagal mengunduh story:", e)

def main():
    print("=== Instagram Story Downloader Advanced ===\n")
    
    # Cek apakah ada sesi login
    L, username = load_session()

    if not L:
        L, username = login_instagram()
        if not L:
            return

    while True:
        print("\nMenu:")
        print("1. Unduh story dari link")
        print("2. Logout akun")
        print("3. Keluar program")
        choice = input("Pilih opsi [1/2/3]: ")

        if choice == "1":
            story_url = input("Masukkan URL story Instagram: ")
            try:
                target_username = extract_username_from_story_url(story_url)
                download_story(L, target_username)
            except Exception as e:
                print("❌ Error:", e)

        elif choice == "2":
            logout(username)
            break

        elif choice == "3":
            print("👋 Keluar dari program.")
            break

        else:
            print("⚠️ Pilihan tidak valid.")

if __name__ == "__main__":
    main()
