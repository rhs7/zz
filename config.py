from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
app_id = 21236276
app_hash = "775f8c2f523b73c64a1a2149458480f2"
session = "1BJWap1sBu1KZx1HRnnsZ_SWdF53ehdzANtsEwkeTNiaSgEn9rQJuMVALfshqtfex1WNVaA9A6AzzakKAlbPx6pWR8zHZtVW4NyqO6aSfnZtq5F0TaEngoHiYnybsX1HboIcPHNyB6hPz-nt_2UvzZSV8OLQElF5aa2BL3zjMc9lr81bKfuJj0g2mrePOKjgaOX3glNfDWEZmKqMu4Jtm_opGEerhVyeAlvt4-4CDeD-dRAtgu9ydSSJd5nN1m6cJBKDCFfU-QAelAsMVnH91ZqNnGojTqRgldTeGGMhSJFGX6ub1UbqwTIoWqeYuJHvdESguUM_ZZoG1qeINQlMOej1RKy9coU0="
StrPython = TelegramClient(StringSession(session), app_id, app_hash)
StrPython.start()
