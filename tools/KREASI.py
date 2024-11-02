import streamlit as st
import numpy as np

# Fungsi untuk menghasilkan layout maze berdasarkan level
def generate_maze(level):
    if level == 1:
        return np.array([[0, 0, 0, 1, 0],
                         [1, 1, 0, 1, 0],
                         [0, 0, 0, 0, 0],
                         [0, 1, 1, 1, 0],
                         [0, 0, 0, 0, 0]])
    elif level == 2:
        return np.array([[0, 1, 0, 0, 0],
                         [0, 1, 1, 1, 0],
                         [0, 0, 0, 1, 0],
                         [1, 1, 0, 0, 0],
                         [0, 0, 0, 1, 0]])
    elif level == 3:
        return np.array([[0, 0, 0, 0, 0],
                         [1, 1, 1, 1, 0],
                         [0, 0, 0, 1, 0],
                         [0, 1, 0, 1, 0],
                         [0, 0, 0, 0, 0]])
    elif level == 4:
        return np.array([[0, 1, 1, 1, 0],
                         [0, 0, 0, 1, 0],
                         [1, 1, 0, 1, 0],
                         [0, 0, 0, 0, 0],
                         [0, 1, 1, 1, 0]])
    else:
        # Untuk level lebih tinggi, kembalikan maze sederhana
        return np.zeros((5, 5), dtype=int)

# Posisi awal dan akhir
start_pos = (0, 0)

# Fungsi untuk menampilkan labirin dengan posisi pemain
def display_maze(player_pos, maze, end_pos):
    maze_display = maze.copy()
    maze_display[player_pos] = 2  # 2 adalah posisi pemain
    maze_display[end_pos] = 3     # 3 adalah posisi tujuan

    for row in maze_display:
        st.write(" ".join(["🟦" if cell == 1 else "🔲" if cell == 0 else "🔴" if cell == 2 else "🏁" for cell in row]))

# Fungsi untuk memindahkan pemain dengan pengecekan validitas
def move_player(player_pos, direction, maze):
    x, y = player_pos
    new_pos = player_pos  # Posisi baru defaultnya adalah posisi sekarang

    # Menentukan posisi baru berdasarkan arah
    if direction == "Up" and x > 0 and maze[x - 1, y] == 0:
        new_pos = (x - 1, y)
    elif direction == "Down" and x < maze.shape[0] - 1 and maze[x + 1, y] == 0:
        new_pos = (x + 1, y)
    elif direction == "Left" and y > 0 and maze[x, y - 1] == 0:
        new_pos = (x, y - 1)
    elif direction == "Right" and y < maze.shape[1] - 1 and maze[x, y + 1] == 0:
        new_pos = (x, y + 1)
    
    return new_pos  # Kembalikan posisi baru

# Inisialisasi level dan status permainan
if "level" not in st.session_state:
    st.session_state.level = 1
if "player_pos" not in st.session_state:
    st.session_state.player_pos = start_pos
if "maze" not in st.session_state:
    st.session_state.maze = generate_maze(st.session_state.level)  # Ukuran maze berdasarkan level
if "game_won" not in st.session_state:
    st.session_state.game_won = False

# Posisi akhir
end_pos = (4, 4)  # Posisi akhir tetap di sudut kanan bawah

# Judul permainan
st.title("Maze Game Gaussian")

# Teks instruksi
st.write("Navigate through the maze to reach the 🏁 goal!")

# Tombol navigasi
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("⬆️ Up"):
        st.session_state.player_pos = move_player(st.session_state.player_pos, "Up", st.session_state.maze)
with col2:
    if st.button("⬇️ Down"):
        st.session_state.player_pos = move_player(st.session_state.player_pos, "Down", st.session_state.maze)
with col3:
    if st.button("⬅️ Left"):
        st.session_state.player_pos = move_player(st.session_state.player_pos, "Left", st.session_state.maze)
with col4:
    if st.button("➡️ Right"):
        st.session_state.player_pos = move_player(st.session_state.player_pos, "Right", st.session_state.maze)

# Tampilkan labirin
display_maze(st.session_state.player_pos, st.session_state.maze, end_pos)

# Cek apakah pemain mencapai tujuan
if st.session_state.player_pos == end_pos:
    st.success("Selamat! Anda sudah sampai tujuan! 🎉")
    st.session_state.game_won = True  # Setel status kemenangan

    # Tombol untuk bermain ulang atau ke level berikutnya
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Main lagi?"):
            st.session_state.player_pos = start_pos  # Reset posisi pemain
            st.session_state.game_won = False  # Reset status kemenangan
            st.session_state.maze = generate_maze(st.session_state.level)  # Reset maze
    with col2:
        if st.button("Level Selanjutnya"):
            st.session_state.level += 1  # Naik level
            st.session_state.player_pos = start_pos  # Reset posisi pemain
            st.session_state.game_won = False  # Reset status kemenangan
            st.session_state.maze = generate_maze(st.session_state.level)  # Buat maze baru
