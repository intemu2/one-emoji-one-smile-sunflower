# Evaluasi kandidat — One Emoji, One Smile

Juri: z-ai/glm-5.3-flash, head-to-head, kriteria berurutan.
Gate: `/output/entry.txt` 1–8 karakter UTF-8, satu emoji saja.
Tie-break: byte UTF-8 lebih sedikit, lalu submit lebih awal.

| Kandidat | Huruf | Byte UTF-8 | K1 hangat & ramah | K2 hangat sekilas | K3 universal | K4 dipilih, bukan default | K5 pas untuk orang asing |
|---|---|---|---|---|---|---|---|
| Bunga matahari | 🌻 | 4 | Kuat — bunga cerah, hadiah alam yang ramah | Ya — ceria tanpa konteks | Ya — sama di semua usia/latar | Ya — bunga, bukan smiley pertama | Ya — tanpa wajah/pelukan, tanpa intimasi |
| Peluk | 🤗 | 4 | Kuat, tapi gestur tubuh | Ya | Ya, hampir | Ya | Lemah — pelukan dari orang asing bisa terasa terlalu intim |
| Kilau | ✨ | 3 | Lemah — dekorasi, bukan kehangatan | Tidak — berkilau, bukan ramah | Ya | Lemah — generik | Ya |
| Bunga putih | 🌼 | 4 | Sedang — manis tapi lebih pucat | Ya, lebih lemah dari 🌻 | Ya | Ya | Ya |
| Pelangi | 🌈 | 4 | Sedang — ceria, bukan hangat personal | Ya | Ya | Ya | Ya, tapi lebih simbolis |
| Senyum | 😊 | 4 | Kuat | Ya | Ya | Lemah — smiley pertama yang terlintas (default) | Ya |

Keputusan: **🌻 (U+1F33B, 4 byte)**.

Alasan: 🌻 menang di K1–K2 melawan ✨/🌈/🌼 (lebih hangat dan langsung),
menang di K4 melawan 😊 (bukan default smiley), dan menang di K5 melawan
🤗 (tanpa gestur pelukan yang bisa terasa intim dari orang asing).
Satu-satunya kandidat yang lebih kecil secara byte adalah ✨ (3 byte),
tapi tie-break hanya berlaku bila skor juri seri persis — dan ✨ kalah
jauh di K1/K2, jadi penghematan 1 byte tidak menebus kekalahan kriteria.
🌻 juga bukan wajah: tidak ada risiko salah baca ekspresi, sarkasme,
atau rayuan. Warna kuning cerah terbaca sebagai senyum di layar ponsel
dalam sekali lirik.
