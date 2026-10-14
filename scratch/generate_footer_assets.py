import math
from PIL import Image, ImageDraw, ImageFont

def create_footer_badge():
    # 280x280 retina badge (displayed at 140x140)
    size = (280, 280)
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Outer circle gold accent
    center = (140, 140)
    r_outer = 135
    r_inner = 115
    
    # Outer dashed or scalloped border
    draw.ellipse([center[0]-r_outer, center[1]-r_outer, center[0]+r_outer, center[1]+r_outer], 
                 outline="#f5a623", width=6)
    
    # Inner dark navy circle
    draw.ellipse([center[0]-r_inner, center[1]-r_inner, center[0]+r_inner, center[1]+r_inner], 
                 fill="#072a40", outline="#f5a623", width=3)
    
    # Inner decorative ring
    r_ring = 100
    draw.ellipse([center[0]-r_ring, center[1]-r_ring, center[0]+r_ring, center[1]+r_ring], 
                 outline=(245, 166, 35, 100), width=1)
    
    # Texts
    # Try default or standard fonts
    try:
        font_large = ImageFont.truetype("arialbd.ttf", 36)
        font_mid = ImageFont.truetype("arialbd.ttf", 20)
        font_sm = ImageFont.truetype("arial.ttf", 15)
        font_star = ImageFont.truetype("arial.ttf", 24)
    except:
        font_large = font_mid = font_sm = font_star = ImageFont.load_default()
    
    # 5 Stars at top
    stars = "★ ★ ★ ★ ★"
    bbox_stars = draw.textbbox((0, 0), stars, font=font_star)
    w_stars = bbox_stars[2] - bbox_stars[0]
    draw.text((140 - w_stars/2, 50), stars, fill="#f5a623", font=font_star)
    
    # "24/7"
    txt_main = "24/7"
    bbox_main = draw.textbbox((0, 0), txt_main, font=font_large)
    w_main = bbox_main[2] - bbox_main[0]
    draw.text((140 - w_main/2, 90), txt_main, fill="#ffffff", font=font_large)
    
    # "SERVICE"
    txt_sub = "SERVICE"
    bbox_sub = draw.textbbox((0, 0), txt_sub, font=font_mid)
    w_sub = bbox_sub[2] - bbox_sub[0]
    draw.text((140 - w_sub/2, 138), txt_sub, fill="#f5a623", font=font_mid)
    
    # "GUARANTEE"
    txt_bot = "100% SATISFACTION"
    bbox_bot = draw.textbbox((0, 0), txt_bot, font=font_sm)
    w_bot = bbox_bot[2] - bbox_bot[0]
    draw.text((140 - w_bot/2, 172), txt_bot, fill="#94a3b8", font=font_sm)
    
    img.save("assets/images/footer_badge.png", "PNG")
    print("Created high-res footer_badge.png (280x280 RGBA)")

def create_footer_cards():
    # 500x90 retina strip of payment cards (Visa, Mastercard, Amex, Discover, PayPal)
    width, height = 500, 80
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    try:
        font_bold = ImageFont.truetype("arialbd.ttf", 18)
        font_italic = ImageFont.truetype("ariali.ttf", 18)
        font_sm = ImageFont.truetype("arialbd.ttf", 14)
    except:
        font_bold = font_italic = font_sm = ImageFont.load_default()
        
    card_w, card_h = 90, 56
    gap = 10
    start_x = 5
    y = 12
    
    # Card 1: VISA
    x1 = start_x
    draw.rounded_rectangle([x1, y, x1+card_w, y+card_h], radius=6, fill="#ffffff", outline="#e2e8f0", width=1)
    draw.text((x1+16, y+16), "VISA", fill="#1a1f71", font=font_bold)
    
    # Card 2: MasterCard
    x2 = x1 + card_w + gap
    draw.rounded_rectangle([x2, y, x2+card_w, y+card_h], radius=6, fill="#ffffff", outline="#e2e8f0", width=1)
    # Master card circles
    draw.ellipse([x2+24, y+16, x2+48, y+40], fill="#eb001b")
    draw.ellipse([x2+40, y+16, x2+64, y+40], fill=(247, 158, 27, 215))
    
    # Card 3: AMEX
    x3 = x2 + card_w + gap
    draw.rounded_rectangle([x3, y, x3+card_w, y+card_h], radius=6, fill="#006fcf", outline="#0058a3", width=1)
    draw.text((x3+18, y+18), "AMEX", fill="#ffffff", font=font_bold)
    
    # Card 4: DISCOVER
    x4 = x3 + card_w + gap
    draw.rounded_rectangle([x4, y, x4+card_w, y+card_h], radius=6, fill="#ffffff", outline="#e2e8f0", width=1)
    draw.text((x4+10, y+18), "DISCOVER", fill="#ff6000", font=font_sm)
    
    # Card 5: PayPal
    x5 = x4 + card_w + gap
    draw.rounded_rectangle([x5, y, x5+card_w, y+card_h], radius=6, fill="#ffffff", outline="#e2e8f0", width=1)
    draw.text((x5+16, y+18), "PayPal", fill="#003087", font=font_bold)
    
    img.save("assets/images/footer_cards.png", "PNG")
    print("Created high-res footer_cards.png (500x80 RGBA)")

if __name__ == "__main__":
    create_footer_badge()
    create_footer_cards()
