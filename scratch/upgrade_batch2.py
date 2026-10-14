import os
import io
import urllib.request
from PIL import Image, ImageDraw, ImageFont
from rembg import remove

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def fetch_image(photo_id, w, h):
    url = f"https://images.unsplash.com/{photo_id}?auto=format&fit=crop&w={w}&h={h}&q=88"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as resp:
        return Image.open(io.BytesIO(resp.read()))

def save_jpg(img, path, quality=92):
    img = img.convert("RGB")
    img.save(path, "JPEG", quality=quality)
    print(f"[JPG OK] {path} ({img.size})")

def save_png_cutout(img, path):
    cutout = remove(img)
    cutout.save(path, "PNG")
    print(f"[CUTOUT OK] {path} ({cutout.size}, {cutout.mode})")

# 1. Testimonial Avatars (high-res smiling clients)
try:
    # Warm smiling homeowner
    t1 = fetch_image("photo-1544005313-94ddf0286df2", 240, 240)
    save_jpg(t1, "assets/images/testimonial_1.jpg")
    
    # Warm smiling senior / family homeowner
    t2 = fetch_image("photo-1506794778202-cad84cf45f1d", 240, 240)
    save_jpg(t2, "assets/images/testimonial_2.jpg")
except Exception as e:
    print(f"Error updating testimonials: {e}")

# 2. Blog Thumbnails (Retina quality 320x240)
blog_thumbs = {
    "assets/images/blog_thumb_1.jpg": "photo-1581244277943-fe4a9c777189",
    "assets/images/blog_thumb_2.jpg": "photo-1584622650111-993a426fbf0a",
    "assets/images/blog_thumb_3.jpg": "photo-1542013936693-884638332954",
    "assets/images/blog_thumb_4.jpg": "photo-1505798577917-a65157d3320a",
}
for path, pid in blog_thumbs.items():
    try:
        b_img = fetch_image(pid, 320, 240)
        save_jpg(b_img, path)
    except Exception as e:
        print(f"Error {path}: {e}")

# 3. Blog Top Banner background crop (1600x600 high res blueprint/pipe engineering)
try:
    bg_img = fetch_image("photo-1504307651254-35680f356dfd", 1600, 600)
    save_jpg(bg_img, "assets/images/blog_top_crop.jpg")
except Exception as e:
    print(f"Error blog_top_crop: {e}")

# 4. Service Van cutout for blog banner (white cargo van)
try:
    van_img = fetch_image("photo-1570125909232-eb263c188f7e", 700, 360)
    save_png_cutout(van_img, "assets/images/blog_banner_van.png")
except Exception as e:
    print(f"Error van cutout: {e}")

# 5. Clean transparent Water Splash
try:
    # Water splash against dark/white
    splash_raw = fetch_image("photo-1548839140-29a749e1bc4e", 700, 450)
    save_png_cutout(splash_raw, "assets/images/water_splash.png")
except Exception as e:
    print(f"Error water splash: {e}")

print("Batch 2 completed successfully!")
