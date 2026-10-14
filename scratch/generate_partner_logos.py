from PIL import Image, ImageDraw, ImageFont

def generate_partner_logos():
    # 1200x120 RGBA transparent strip
    width, height = 1200, 120
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    try:
        font_main = ImageFont.truetype("arialbd.ttf", 26)
        font_sub = ImageFont.truetype("arial.ttf", 12)
    except:
        font_main = font_sub = ImageFont.load_default()
        
    partners = [
        ("KOHLER", "THE BOLD LOOK"),
        ("MOEN", "BUY IT FOR LOOKS"),
        ("DELTA", "FAUCET COMPANY"),
        ("GROHE", "PURE FREUDE AN WASSER"),
        ("TOTO", "PERFECTION BY DESIGN")
    ]
    
    spacing = width // len(partners)
    
    for i, (name, tag) in enumerate(partners):
        cx = i * spacing + spacing // 2
        cy = height // 2
        
        # Draw subtle geometric icon
        # For Kohler: stylized K box
        # For Moen: circle M
        # For Delta: Triangle delta
        # For Grohe: wave lines
        # For Toto: minimalist clean box
        
        # Draw Brand Name
        bbox = draw.textbbox((0, 0), name, font=font_main)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        
        # Subtle charcoal gray #64748b with slight transparency
        draw.text((cx - tw//2, cy - 16), name, fill=(100, 116, 139, 210), font=font_main)
        
        # Draw tagline
        bbox_sub = draw.textbbox((0, 0), tag, font=font_sub)
        sw = bbox_sub[2] - bbox_sub[0]
        draw.text((cx - sw//2, cy + 14), tag, fill=(148, 163, 184, 180), font=font_sub)
        
    img.save("assets/images/partner_logos.png", "PNG")
    print("Created high-res partner_logos.png (1200x120 RGBA)")

if __name__ == "__main__":
    generate_partner_logos()
