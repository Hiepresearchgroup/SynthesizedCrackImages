import requests
import re

url = "https://vnueduvn-my.sharepoint.com/:f:/g/personal/hieus_lecong_vnu_edu_vn/EoMKqKzNpmNFtrSHZkU_NB4Be6LQDFE7f0ycBqPz-T7Vfg?e=eghXIg"

resp = requests.get(url, allow_redirects=True, stream=True, timeout=60)
resp.raise_for_status()


fname = None
cd = resp.headers.get('content-disposition')
if cd:
    m = re.search(r'filename\*=UTF-8\'\'(.+)|filename="(.+)"', cd)
    if m:
        fname = m.group(1) or m.group(2)

if not fname:
    fname = "downloaded_file.html"  # fallback (nếu chỉ là trang html)

with open(fname, "wb") as f:
    for chunk in resp.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

print("✅ Saved as", fname)
