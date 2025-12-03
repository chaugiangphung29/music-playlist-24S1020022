# playlist.py
songs = []

def add_song():
    """Thêm bài hát vào playlist với kiểm tra nhập liệu."""
    try:
        title = input("Nhập tên bài hát: ").strip()
        if not title:
            print("Tên bài hát không được rỗng. Hủy thao tác.")
            return

        artist = input("Nhập tên ca sĩ: ").strip()
        if not artist:
            print("Tên ca sĩ không được rỗng. Hủy thao tác.")
            return

        # Lấy thời lượng, đảm bảo là số nguyên dương
        while True:
            dur_str = input("Nhập thời lượng (giây): ").strip()
            if dur_str == "":
                print("Thời lượng không được để trống. Hủy thao tác.")
                return
            try:
                duration = int(dur_str)
                if duration <= 0:
                    print("Vui lòng nhập thời lượng là số nguyên dương.")
                    continue
                break
            except ValueError:
                print("Thời lượng phải là một số nguyên (ví dụ: 240). Thử lại.")

        song = {
            "title": title,
            "artist": artist,
            "duration": duration
        }

        songs.append(song)
        print(f"Đã thêm: {title} - {artist} ({duration}s)")

    except KeyboardInterrupt:
        print("\nHủy thao tác thêm bài hát (Ctrl+C).")
        return

def view_playlist():
    """Hiển thị toàn bộ playlist (nếu có)."""
    if not songs:
        print("Playlist trống.")
        return

    print("\n--- DANH SÁCH PHÁT ---")
    total = 0
    for idx, song in enumerate(songs, start=1):
        print(f"{idx}. {song['title']} - {song['artist']} ({song['duration']}s)")
        total += song['duration']
    print(f"Tổng số bài: {len(songs)} | Tổng thời lượng: {total}s")

def search_by_artist():
    """Tìm và hiển thị bài hát theo tên ca sĩ (so sánh không phân biệt hoa thường)."""
    try:
        name = input("Nhập tên ca sĩ cần tìm: ").strip()
        if not name:
            print("Tên ca sĩ không được rỗng.")
            return

        found = [song for song in songs if name.lower() in song["artist"].lower()]

        if not found:
            print("Không tìm thấy bài hát nào.")
            return

        print(f"\n--- KẾT QUẢ TÌM: '{name}' ---")
        for idx, song in enumerate(found, start=1):
            print(f"{idx}. {song['title']} - {song['artist']} ({song['duration']}s)")

    except KeyboardInterrupt:
        print("\nHủy thao tác tìm kiếm (Ctrl+C).")
        return

def main():
    try:
        while True:
            print("\n--- MUSIC PLAYLIST MANAGER ---")
            print("1. Thêm bài hát")
            print("2. Xem danh sách phát")
            print("3. Tìm bài hát theo ca sĩ")
            print("4. Thoát")

            choice = input("Chọn chức năng: ").strip()

            if choice == '1':
                add_song()
            elif choice == '2':
                view_playlist()
            elif choice == '3':
                search_by_artist()
            elif choice == '4':
                print("Kết thúc chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn 1-4.")
    except KeyboardInterrupt:
        print("\nKết thúc chương trình (Ctrl+C). Bye!")

if __name__ == "__main__":
    main()
def add_song():
    title = input("Nhập tên bài hát: ")
    artist = input("Nhập tên ca sĩ: ")
    duration = int(input("Nhập thời lượng (giây): "))

    song = {
        "title": title,
        "artist": artist,

        "duration": duration
    }

    songs.append(song)
    print("Đã thêm bài hát vào playlist.")
def view_playlist():
    if not songs:
        print("Playlist trống.")
        return

    print("\n--- DANH SÁCH PHÁT ---")
    for idx, song in enumerate(songs, start=1):
        print(f"{idx}. {song['title']} - {song['artist']} ({song['duration']}s)")
def search_by_artist():
    name = input("Nhập tên ca sĩ cần tìm: ")

    found = [song for song in songs if name.lower() in song["artist"].lower()]

    if not found:
        print("Không tìm thấy bài hát nào.")
        return

    print("\n--- KẾT QUẢ TÌM KIẾM ---")
    for idx, song in enumerate(found, start=1):
        print(f"{idx}. {song['title']} - {song['artist']} ({song['duration']}s)")

