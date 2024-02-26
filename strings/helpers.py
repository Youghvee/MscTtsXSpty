#
# Copyright (C) 2021-2022 by bee, < https://github.com/bee >.
# All rights reserved.


HELP_1 = """✅**<u>Perintah Admin:</u>**

**c** adalah singkatan dari pemutaran saluran.

/pause atau /cpause - Menjeda musik yang sedang diputar.
/resume atau /cresume- Melanjutkan musik yang dijeda.
/mute atau /cmute- Mematikan musik yang diputar.
/unmute atau /cunmute- Mengaktifkan musik yang dimatikan.
/skip atau /cskip- Lewati musik yang sedang diputar.
/stop atau /cstop- Menghentikan pemutaran musik.
/shuffle atau /cshuffle- Secara acak mengacak daftar putar yang antri.


HELP_2 = """✅<u>**Perintah Auth:**</u>

/auth [Nama Pengguna] - Tambahkan pengguna ke DAFTAR AUTH grup.
/unauth [Nama Pengguna] - Menghapus pengguna dari DAFTAR AUTH grup.
/authusers - Periksa DAFTAR AUTH grup."""

HELP_3 = """✅<u>**Perintah Bot:**</u>

/stats - Dapatkan Top 10 Tracks Global Stats, Top 10 Users of bot, Top 10 Chats on bot, Top 10 Played in a chat, dll.
/sudolist - Periksa Pengguna Sudo dari Bot Musik Musikku
/lyrics [Music Name] - Mencari Lirik untuk Musik tertentu di web.
/song [Nama Trek] atau [Tautan YT] - Unduh trek apa pun dari youtube dalam format mp3 atau mp4.
/verify : Verifikasikan diri kamu agar bisa menjalankan musik"""
/restart - Mulai ulang Bot.
/update - Perbarui Bot.
/speedtest - Periksa kecepatan server
/maintenance - [enable / disable]
/logger [enable / disable] - Bot mencatat kueri yang dicari di grup logger.
/get_log [Jumlah Baris] - Dapatkan log bot Anda dari heroku atau vps. Bekerja untuk keduanya.

PERINTAH STATUS:
/activevoice - Periksa obrolan suara aktif di bot.
/activevideo - Periksa panggilan video aktif di bot.
/stats - Periksa Statistik Bot

**c** adalah singkatan dari pemutaran saluran.
/queue atau /cqueue- Periksa Daftar Antrian Musik."""

HELP_4 = """✅<u>**Perintah Ban:**</u>

**FUNGSI CHAT DAFTAR HITAM:**
/blacklistchat [CHAT_ID] - Masukkan semua chat ke dalam daftar hitam agar tidak menggunakan Bot Musik
/whitelistchat [CHAT_ID] - Masukkan semua chat yang masuk daftar hitam ke dalam daftar putih dari penggunaan Bot Musik
/blacklistedchat - Periksa semua obrolan yang masuk daftar hitam.

**FUNGSI YANG DIBLOKIR:**
/block [Nama Pengguna atau Balasan ke pengguna] - Mencegah pengguna menggunakan perintah bot.
/unblock [Nama Pengguna atau Balasan ke pengguna] - Menghapus pengguna dari Daftar Blokir Bot.
/blockedusers - Periksa Daftar Pengguna yang diblokir

**FUNGSI GBAN:**
/gban [Nama Pengguna atau Balasan ke pengguna] - Blokir pengguna dari obrolan yang dilayani bot dan hentikan dia menggunakan bot Anda.
/ungban [Nama Pengguna atau Balasan ke pengguna] - Hapus pengguna dari Daftar Bot yang diblokir dan izinkan dia menggunakan bot Anda
/gbannedusers - Periksa Daftar Pengguna yang Diblokir"""

HELP_6 = """**✅<u>Perintah Extra:</u>**

Pengaturan Grup:
/settings - Dapatkan pengaturan grup lengkap dengan tombol sebaris.

🔗 Opsi di Pengaturan:
1️⃣ Anda dapat mengatur Kualitas Audio yang ingin Anda streaming pada obrolan suara.
2️⃣ Anda dapat mengatur Kualitas Video yang ingin Anda streaming pada obrolan suara.
3️⃣ Mode Bersih: Jika diaktifkan, hapus pesan bot dari grup Anda untuk memastikan obrolan Anda tetap bersih dan bagus.
4️⃣ Command Clean : Saat diaktifkan, Bot akan segera menghapus perintah yang dieksekusi (/play, /stop dll).
5️⃣ Pengaturan Putar:

/playmode - Dapatkan panel pengaturan permainan lengkap dengan tombol di mana Anda dapat mengatur pengaturan permainan grup Anda.
Pilihan dalam mode bermain:
1️⃣ Mode Pencarian [Langsung atau Sebaris] - Mengubah mode pencarian Anda saat Anda memberikan / mode putar.
2️⃣ Perintah Admin [Semua Orang atau Admin] - Jika semua orang, siapa pun yang ada di grup Anda akan dapat menggunakan perintah admin (seperti /lewati dll.)
3️⃣ Jenis Putar [Semua Orang atau Admin] - Jika admin, hanya admin yang ada di grup yang dapat memutar musik di obrolan suara.
"""

HELP_7 = """✅<u>**Perintah Stats:**</u>

**📊 PERINTAH STATISTIK:**
/activevoice - Periksa obrolan suara aktif di bot.
/activevideo - Periksa panggilan video aktif di bot.
/stats - Periksa Statistik Bot.
"""
HELP_8 = """✅<u>**Perintah sudo:**</u>

**TAMBAH & HAPUS PENGGUNA SUDO :**
/addsudo [Nama pengguna atau Balas ke pengguna]
/delsudo [Nama pengguna atau Balas ke pengguna]
"""
HELP_9 = """✅<u>**Perintah mainkan/play:**</u>

**Perintah Putar:**
Perintah yang Tersedia = play, vplay, cplay
Perintah ForcePlay = playforce, vplayforce, cplayforce

c adalah singkatan dari pemutaran saluran.
v singkatan dari pemutaran video.
force berarti permainan kekuatan.

/play atau /vplay atau /cplay - Bot akan mulai memutar kueri yang Anda berikan di obrolan suara atau Streaming tautan langsung di obrolan suara.
/playforce atau /vplayforce atau /cplayforce - Force Play menghentikan trek yang sedang diputar di obrolan suara dan mulai memutar trek yang dicari secara instan tanpa mengganggu/menghapus antrean.
/channelplay [Nama pengguna atau id obrolan] atau [Nonaktifkan] - Hubungkan saluran ke grup dan streaming musik di obrolan suara saluran dari grup Anda.

***Daftar Putar Server Bot:**
/playlist - Periksa Daftar Putar Tersimpan Anda di Server.
/deleteplaylist - Hapus semua musik yang tersimpan di playlist Anda
/play - Mulai mainkan Daftar Putar Tersimpan Anda dari Server.
 """
HELP_10 = """✅<u>**Printah broadcast:**</u>

**FUNGSI PENYIARAN:**
/broadcast [Pesan atau Balas Pesan] - Menyiarkan pesan apa pun ke Obrolan yang Disajikan Bot.

**pilihan untuk siaran:**
-pin : Ini akan menyematkan pesan Anda
-pinloud : Ini akan menyematkan pesan Anda dengan pemberitahuan keras
-user : Ini akan menyiarkan pesan Anda ke pengguna yang telah memulai bot Anda.
-assistant : Ini akan menyiarkan pesan Anda dari akun asisten bot Anda.
-nobot : Ini akan memaksa bot Anda untuk tidak menyiarkan pesan

Contoh: /broadcast -user -assistant -pin Halo Pengujian
"""
