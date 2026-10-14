import urllib.request, io
from PIL import Image, ImageDraw, ImageFont

headers = {'User-Agent': 'Mozilla/5.0'}

try:
    # High-resolution architectural aerial / satellite city street grid
    url = "https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?auto=format&fit=crop&w=1200&h=500&q=88"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=12) as resp:
        img = Image.open(io.BytesIO(resp.read())).convert("RGBA")
        
    draw = ImageDraw.Draw(img)
    
    # Draw a stylish location card and pin marker on the map
    cx, cy = 600, 220
    
    # Outer pulse circle
    draw.ellipse([cx-40, cy-40, cx+40, cy+40], fill=(245, 166, 35, 60))
    draw.ellipse([cx-25, cy-25, cx+25, cy+25], fill=(245, 166, 35, 120))
    # Pin head
    draw.ellipse([cx-14, cy-14, cx+14, cy+14], fill="#f5a623", outline="#ffffff", width=3)
    
    # Floating Info Card
    card_w, card_h = 240, 75
    card_x = cx - card_w//2
    card_y = cy - 95
    
    draw.rounded_rectangle([card_x, card_y, card_x+card_w, card_y+card_h], radius=8, 
                           fill=(7, 42, 64, 235), outline=(245, 166, 35, 200), width=2)
                           
    try:
        font_b = ImageFont.truetype("arialbd.ttf", 15)
        font_s = ImageFont.truetype("arial.ttf", 12)
    except:
        font_b = font_s = ImageFont.load_default()
        
    draw.text((card_x + 15, card_y + 12), "PlumberX HQ - NYC", fill="#ffffff", font=font_b)
    draw.text((card_x + 15, card_y + 32), "24/7 Rapid Dispatch Station", fill="#f5a623", font=font_s)
    draw.text((card_x + 15, card_y + 50), "Call: (888) 123-4567", fill="#94a3b8", font=font_s)
    
    final_img = img.convert("RGB")
    final_img.save("assets/images/contact_map.jpg", "JPEG", quality=92)
    print("Created high-res styled contact_map.jpg (1200x500)")
except Exception as e:
    print("Error creating contact map:", e)
