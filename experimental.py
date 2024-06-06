link = "https://m.youtube.com/watch?v=wRaWKfDLj_4&pp=ygUodGVkIGZhaWxvbiBhbmQgZGogY2hhY2hhIHNhIHJhZHlvIHNpbmdrbw%3D%3D"


if "youtube.com/watch?v=" in link:
    start_pos = link.find("youtube.com/watch?v=")
    end_pos = link.find("&")

print(link[start_pos + len("youtube.com/watch?v="):end_pos])