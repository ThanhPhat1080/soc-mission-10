#!/usr/bin/env python3
"""Nhúng lại ảnh images/giahan-head.jpg và images/hamy-head.jpg vào các file HTML.
Chạy lại mỗi khi bạn thay hai ảnh này:  python3 tools/embed-faces.py"""
import re, base64, subprocess, tempfile, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def data_uri(name):
    out = tempfile.mktemp(suffix=".jpg")
    subprocess.check_call(["sips", "-Z", "400", "-s", "format", "jpeg", "-s", "formatOptions", "80",
                           os.path.join(ROOT, "images", name), "--out", out], stdout=subprocess.DEVNULL)
    b = base64.b64encode(open(out, "rb").read()).decode(); os.remove(out)
    return "data:image/jpeg;base64," + b
URI = {"giahan": data_uri("giahan-head.jpg"), "hamy": data_uri("hamy-head.jpg")}
for f in ("index.html", "slideshow-soc10.html", "mission10.html"):
    p = os.path.join(ROOT, f); s = open(p, encoding="utf-8").read()
    for k, u in URI.items():
        s, n = re.subn(r'("%s": ?")data:image/[a-z]+;base64,[A-Za-z0-9+/=]+(")' % k, lambda m: m.group(1) + u + m.group(2), s)
        print(f, k, "đã thay" if n else "KHÔNG TÌM THẤY")
    open(p, "w", encoding="utf-8").write(s)
