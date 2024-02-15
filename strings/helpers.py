#
# Copyright (C) 2021-2022 by kenkansaja@Github, < https://github.com/kenkansaja >.
#
# This file is part of < https://github.com/kenkansaja/Musikku > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/kenkansaja/Musikku/blob/master/LICENSE >
#
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

<u>**Lewati Spesifik:*</u>
/skip atau /cskip [Nomor(contoh: 3)]
    - Melompati musik ke nomor antrian yang ditentukan. Contoh: /skip 3 akan melewatkan musik ke musik antrian ketiga dan akan mengabaikan musik 1 dan 2 dalam antrian.

✅<u>**Pemutaran Putaran:*</u>
/loop atau /cloop [aktifkan/nonaktifkan] atau [Angka antara 1-10]
    - Saat diaktifkan, bot memutar musik yang sedang diputar menjadi 1-10 kali pada obrolan suara. Default untuk 10 kali.

✅<u>**Pengguna Auth:*</u>
Pengguna Auth dapat menggunakan perintah admin tanpa hak admin di obrolan Anda.

/auth [Nama Pengguna] - Tambahkan pengguna ke DAFTAR AUTH grup.
/unauth [Nama Pengguna] - Menghapus pengguna dari DAFTAR AUTH grup.
/authusers - Periksa DAFTAR AUTH grup."""


HELP_2 = """✅<u>**Perintah Mainkan:**</u>

**cplay** atau **cstream **singkatan dari channel play.
**vplay** adalah singkatan dari pemutaran video.

/play atau /vplay atau /cplay - Bot akan mulai memainkan kueri yang Anda berikan pada obrolan suara.

/stream atau /cstream - Streaming tautan langsung di obrolan suara.

/channelplay [Nama pengguna atau id obrolan] atau [Nonaktifkan] - Hubungkan saluran ke grup dan streaming musik di obrolan suara saluran dari grup Anda.


**<u>Daftar Putar Server Bot:</u>**
/playlist - Periksa Daftar Putar Tersimpan Anda Di Server.
/deleteplaylist - Hapus semua musik yang disimpan di daftar putar Anda
/play - Mulai mainkan Daftar Putar Tersimpan Anda dari Server."""


HELP_3 = """✅<u>**Perintah Bot:**</u>

/stats - Dapatkan Top 10 Tracks Global Stats, Top 10 Users of bot, Top 10 Chats on bot, Top 10 Played in a chat, dll.

/sudolist - Periksa Pengguna Sudo dari Bot Musik Musikku

/lyrics [Music Name] - Mencari Lirik untuk Musik tertentu di web.

/song [Nama Trek] atau [Tautan YT] - Unduh trek apa pun dari youtube dalam format mp3 atau mp4.

**c** adalah singkatan dari pemutaran saluran.
/queue atau /cqueue- Periksa Daftar Antrian Musik."""

HELP_4 = """✅<u>**Perintah Ekstra:**</u>
/start - Mulai Bot Musik.
/help - Dapatkan Menu Helper Perintah dengan penjelasan rinci tentang perintah.
/ping- Ping Bot dan periksa Ram, Cpu dll statistik Bot.

<u>**Setelan Grup:*</u>
/settings - Dapatkan pengaturan grup lengkap dengan tombol sebaris

**Opsi di Pengaturan:**

1️⃣ Anda dapat mengatur **Kualitas Audio** yang ingin Anda streaming di obrolan suara.

2️⃣ Anda dapat mengatur **Kualitas Video** yang ingin Anda streaming di obrolan suara.

3️⃣ **Pengguna Auth**: Anda dapat mengubah mode perintah admin dari sini ke semua orang atau hanya admin. Jika semua orang, siapa pun yang ada di grup Anda dapat menggunakan perintah admin (seperti /skip, /stop dll)

4️⃣ **Mode Bersih **: Saat diaktifkan, hapus pesan bot setelah 5 menit dari grup Anda untuk memastikan obrolan Anda tetap bersih dan baik.

5️⃣ **Command Clean** : Saat diaktifkan, Bot akan segera menghapus perintah yang dijalankannya (/play, /pause, /shuffle, /stop dll).

6️⃣ **Pengaturan Putar**:

/playmode - Dapatkan panel pengaturan pemutaran lengkap dengan tombol di mana Anda dapat mengatur pengaturan pemutaran grup Anda.

<u>Opsi dalam mode putar:</u>

1️⃣ **Mode Pencarian** [ Direct or Inline] - Mengubah mode pencarian saat Anda memberikan mode /play.

2️⃣ **Mode Putar** [ Grup atau Saluran] - Mengubah mode Putar Anda ke saluran atau grup dan streaming musik hanya di sana.

3️⃣ **Tipe Putar** [ Semua Orang atau Admin] - Jika admin, hanya admin yang ada di grup yang dapat memutar musik di obrolan suara."""

HELP_5 = """🔰**<u>TAMBAH & HAPUS PENGGUNA SUDO :</u>**
/addsudo [Nama pengguna atau Balas ke pengguna]
/delsudo [Nama pengguna atau Balas ke pengguna]

**<u>HEROKU:</u>**
/usage - Penggunaan Dyno.

**<u>VARS KONFIGURASI:</u>**
/get_var - Dapatkan config var dari Heroku atau .env.
/del_var - Hapus semua var di Heroku atau .env.
/set_var [Var Name] [Value] - Atur Var atau Perbarui Var di heroku atau .env. Pisahkan Var dan Nilainya dengan spasi.

**<u>PERINTAH BOT:</u>**
/restart - Mulai ulang Bot.
/update - Perbarui Bot.
/speedtest - Periksa kecepatan server
/maintenance - [enable / disable]
/logger [enable / disable] - Bot mencatat kueri yang dicari di grup logger.
/get_log [Jumlah Baris] - Dapatkan log bot Anda dari heroku atau vps. Bekerja untuk keduanya.

**<u>PERINTAH STATUS:</u>**
/activevoice - Periksa obrolan suara aktif di bot.
/activevideo - Periksa panggilan video aktif di bot.
/stats - Periksa Statistik Bot

️**<u>FUNGSI BLACKLIST CHAT:</u>**
/blacklistchat [CHAT_ID] - Daftar hitam obrolan apa pun dari menggunakan Bot Musik
/whitelistchat [CHAT_ID] - Daftar putih obrolan apa pun yang masuk daftar hitam dari menggunakan Bot Musik
/blacklistedchat - Periksa semua obrolan yang masuk daftar hitam.

**<u>FUNGSI TERBLOKIR:</u>**
/block [Nama Pengguna atau Balas ke pengguna] - Mencegah pengguna menggunakan perintah bot.
/unblock [Nama Pengguna atau Balas ke pengguna] - Hapus pengguna dari Daftar Blokir Bot.
/blockedusers - Periksa Daftar Pengguna yang diblokir

**<u>FUNGSI GBAN:</u>**
/gban [Nama Pengguna atau Balas ke pengguna] - Gban pengguna dari obrolan yang dilayani bot dan hentikan dia menggunakan bot Anda.
/ungban [Nama Pengguna atau Balas ke pengguna] - Hapus pengguna dari Daftar gbanned Bot dan izinkan dia menggunakan bot Anda
/gbannedusers - Periksa Daftar Pengguna Gbanned

**<u>FUNGSI PANGGILAN VIDEO:</u>**
/set_video_limit [Jumlah Obrolan] - Tetapkan Jumlah Obrolan maksimum yang diizinkan untuk Panggilan Video dalam satu waktu. Default untuk 3 obrolan.
/videomode [download|m3u8] - Jika mode unduh diaktifkan, Bot akan mengunduh video alih-alih memutarnya dalam bentuk M3u8. Secara default ke M3u8. Anda dapat menggunakan mode unduhan saat kueri apa pun tidak diputar dalam mode m3u8.

️**<u>FUNGSI BOT PRIVATE:</u>**
/authorize [CHAT_ID] - Izinkan obrolan untuk menggunakan bot Anda.
/unauthorize [CHAT_ID] - Melarang obrolan menggunakan bot Anda.
/authorized - Periksa semua obrolan bot Anda yang diizinkan.

**<u>FUNGSI PENYIARAN:</u>**
/broadcast [Pesan atau Balas Pesan] - Menyiarkan pesan apa pun ke Obrolan yang Dilayani Bot.

<u>opsi untuk siaran:</u>
**-pin** : Ini akan menyematkan pesan Anda
**-pinloud** : Ini akan menyematkan pesan Anda dengan pemberitahuan keras
**-user** : Ini akan menyiarkan pesan Anda ke pengguna yang telah memulai bot Anda.
**-assistant** : Ini akan menyiarkan pesan Anda dari akun asisten bot Anda.
**-nobot** : Ini akan memaksa bot Anda untuk tidak menyiarkan pesan

**Contoh:** `/broadcast -user -assistant -pin Hello Testing`

"""
HELP_7 = """<u>ʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ ғɪɴᴅ ɴᴇᴡ ғᴇᴀᴛᴜʀᴇs:</u>

/alive : ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴄʜᴇᴄᴋ ᴀʟᴇxᴀ ᴍᴜsɪᴄ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ
/id : ᴛᴏ ᴄʜᴇᴋ ᴜsᴇʀ ᴀɴᴅ ᴄʜᴀᴛ ɪᴅ
/gcast -user -assistant -pin ᴛᴇsᴛɪɴɢ ʙʀᴏᴀᴅᴄᴀsᴛ`
/verify : ᴠᴇʀɪꜰʏ ʏᴏᴜʀsᴇʟꜰ ᴀᴛ ᴅᴀᴛᴀʙᴀsᴇ
"""
HELP_8 = """<u>ꜰᴇᴀᴛᴜʀᴇ ꜰᴏʀ ʙʀᴏᴀᴅᴄᴀsᴛ sᴜʙsᴄʀɪᴘᴛɪᴏɴ:</u>

ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ʙᴜʏ ᴍᴏɴᴛʜʟʏ ᴀɴᴅ ᴡᴇᴇᴋʟʏ ʙʀᴏᴀᴅᴄᴀsᴛ sᴜʙsᴄʀɪᴘᴛɪᴏɴ ꜰʀᴏᴍ ᴜs. ᴡᴇ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ 3 ʙʀᴏᴀᴅᴄᴀsᴛ ꜰᴏʀ ᴡᴇᴇᴋʟʏ ᴀɴᴅ 14 ʙʀᴏᴀᴅᴄᴀsᴛ ꜰᴏʀ ᴍᴏɴᴛʜʟʏ sᴜʙsᴄʀɪᴘᴛɪᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʟɪᴍɪᴛ ᴏꜰ sᴇɴᴅɪɴɢ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀꜰᴛᴇʀ ᴛᴡᴏ ᴅᴀʏs.

ᴏɴʟʏ ᴏᴡɴᴇʀ
/addweekly [ᴜsᴇʀ ɪᴅ] : ᴀᴅᴅ ᴜsᴇʀ ᴛᴏ ᴡᴇᴇᴋʟʏ ʙʀᴏᴀᴅᴄᴀsᴛ sᴜʙsᴄʀɪᴘᴛɪᴏɴ.
/addmonthly [ᴜsᴇʀ ɪᴅ] : ᴀᴅᴅ ᴜsᴇʀ ᴛᴏ ᴍᴏɴᴛʜʟʏ ʙʀᴏᴀᴅᴄᴀsᴛ sᴜʙsᴄʀɪᴘᴛɪᴏɴ.  
/removesub [ᴜsᴇʀ ɪᴅ] : ʀᴇᴍᴏᴠᴇ ᴜsᴇʀ ꜰʀᴏᴍ ʙʀᴏᴀᴅᴄᴀsᴛ sᴜʙsᴄʀɪᴘᴛɪᴏɴ.
/checksubscription [ᴜsᴇʀ ɪᴅ] : ᴄʜᴇᴋ ᴜsᴇʀ sᴜʙsᴄʀɪᴘᴛɪᴏɴ ʀᴇᴍᴀɪɴɪɴɢ ᴅᴀʏs ᴀɴᴅ ʙʀᴏᴀᴅᴄᴀsᴛ.
/substats : ᴄʜᴇᴄᴋ ᴛᴏᴛᴀʟ ɴᴜᴍʙᴇʀ sᴜʙsᴄʀɪᴘᴛɪᴏɴ ᴡɪᴛʜ ᴛʜᴇɪʀ ɪᴅs ᴀɴᴅ sᴜʙsᴄʀɪᴘᴛɪᴏɴ ᴛʏᴘᴇ ᴀʟᴏɴɢ ᴡɪᴛʜ ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴜᴛ.
/subscription_alert : ᴛᴏ sᴇɴᴅ ᴀʟᴇʀᴛ ᴍᴇssᴀɢᴇ ᴛᴏ sᴜʙsᴄʀɪʙᴇʀ ᴡɪᴛʜ ʀᴇᴍᴀɪɴɪɴɢ ᴅᴀʏs  ᴀʟᴏɴɢ ᴡɪᴛʜ ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴜᴛ.

ᴀɴʏᴏɴᴇ ᴄᴀɴ ᴜsᴇ
/mysubscription : ʏᴏᴜ ᴄᴀɴ ᴄʜᴇᴋ ʏᴏᴜʀ sᴜʙsᴄʀɪᴘᴛɪᴏɴ ᴡɪᴛʜ ʀᴇᴍᴀɪɴɪɴɢ ᴅᴀʏs ᴀɴᴅ ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴜɴᴛ.
/paidbroadcast : sᴇɴᴅ ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜsᴇʀ ᴀɴᴅ ɢʀᴏᴜᴘs ᴀᴛ ᴀ ᴛɪᴍᴇ ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ᴀ ᴀᴄᴛɪᴠᴇ sᴜʙsᴄʀɪᴘᴛɪᴏɴ.
ᴘᴏᴡʀᴇᴅ 
<u>Thank you for your help, greetings team: </u>
1. @Arlo4u
2. @Usern4meDoesNotExist404
3. @Usern4meDoestExist404
4. @Hfivxssub
Channels : @TeamAllBots 
"""
