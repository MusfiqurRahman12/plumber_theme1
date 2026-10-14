import os
import re
import glob
from PIL import Image

files = glob.glob('*.html') + glob.glob('css/*.css')
img_refs = set()
for f in files:
    content = open(f, encoding='utf-8').read()
    for match in re.findall(r'assets/images/[\w\.\-]+', content):
        img_refs.add(match)

print(f"Total unique referenced images: {len(img_refs)}")
print(f"{'Image Path':<35} | {'Dimensions':<12} | {'Size KB':<10} | {'Status'}")
print("-" * 75)
for ref in sorted(img_refs):
    if os.path.exists(ref):
        size = os.path.getsize(ref) / 1024
        try:
            im = Image.open(ref)
            dim = f"{im.size[0]}x{im.size[1]}"
            mode = im.mode
        except Exception as e:
            dim = "ERR"
            mode = "ERR"
        # determine if it looks like a low-res crop (< 200px or small size)
        is_low_res = "LOW-RES CROP" if (im.size[0] < 300 and im.size[1] < 300 and size < 15 and "icon" not in ref and "logo" not in ref and "avatar" not in ref) else "OK"
        print(f"{ref:<35} | {dim:<12} | {size:6.1f} KB | {mode} {is_low_res}")
    else:
        print(f"{ref:<35} | MISSING      | -          | NOT FOUND")
