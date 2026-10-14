import urllib.request
import io
import os
from PIL import Image
from rembg import remove

image_mapping = {
    # --- Projects Gallery ---
    "assets/images/project_3.jpg": ("photo-1590486803833-1c5dc8ddd4c8", 600, 400, False),
    "assets/images/project_4.jpg": ("photo-1585704032915-c3400ca199e7", 600, 400, False),
    "assets/images/project_5.jpg": ("photo-1581244277943-fe4a9c777189", 600, 400, False),
    "assets/images/project_6.jpg": ("photo-1517646287270-a5a9ca602e5c", 600, 400, False),
    "assets/images/project_7.jpg": ("photo-1505798577917-a65157d3320a", 600, 400, False),
    "assets/images/project_8.jpg": ("photo-1552321554-5fefe8c9ef14", 600, 400, False),
    "assets/images/project_9.jpg": ("photo-1621905251189-08b45d6a269e", 600, 400, False),

    # --- Services 2 ---
    "assets/images/service2_1.jpg": ("photo-1607472586893-edb57bdc0e39", 500, 350, False),
    "assets/images/service2_2.jpg": ("photo-1581244277943-fe4a9c777189", 500, 350, False),
    "assets/images/service2_3.jpg": ("photo-1581092160607-ee22621dd758", 500, 350, False),
    "assets/images/service2_4.jpg": ("photo-1584622650111-993a426fbf0a", 500, 350, False),
    "assets/images/service2_5.jpg": ("photo-1600585154340-be6161a56a0c", 500, 350, False),
    "assets/images/service2_6.jpg": ("photo-1621905252507-b35492cc74b4", 500, 350, False),
    "assets/images/service2_7.jpg": ("photo-1517646287270-a5a9ca602e5c", 500, 350, False),
    "assets/images/service2_8.jpg": ("photo-1505798577917-a65157d3320a", 500, 350, False),

    # --- Case Study ---
    "assets/images/case_study_1.jpg": ("photo-1584622650111-993a426fbf0a", 800, 440, False),
    "assets/images/case_study_2.jpg": ("photo-1542013936693-884638332954", 400, 400, False),
    "assets/images/case_study_3.jpg": ("photo-1507652313519-d4e9174996dd", 400, 400, False),
    "assets/images/case_study_4.jpg": ("photo-1552321554-5fefe8c9ef14", 800, 480, False),

    # --- Repair & Service 1 ---
    "assets/images/repair_top_1.jpg": ("photo-1621905251189-08b45d6a269e", 600, 440, False),
    "assets/images/repair_top_2.jpg": ("photo-1607472586893-edb57bdc0e39", 500, 440, False),
    "assets/images/repair_benefit.jpg": ("photo-1505798577917-a65157d3320a", 500, 360, False),
    "assets/images/repair_sidebar_widget.jpg": ("photo-1621905252507-b35492cc74b4", 300, 250, False),
    "assets/images/service1_expertise.jpg": ("photo-1581092335397-9583fe92d232", 600, 450, False),
    "assets/images/service_tab_kitchen.jpg": ("photo-1600585154340-be6161a56a0c", 600, 400, False),

    # --- Shop Products ---
    "assets/images/shop_item_1.jpg": ("photo-1585338107529-13afc5f02586", 400, 400, False),
    "assets/images/shop_item_2.jpg": ("photo-1581244277943-fe4a9c777189", 400, 400, False),
    "assets/images/shop_item_3.jpg": ("photo-1572981779307-38b8cabb2407", 400, 400, False),
    "assets/images/shop_item_4.jpg": ("photo-1504307651254-35680f356dfd", 400, 400, False),
    "assets/images/shop_item_5.jpg": ("photo-1530124566582-a618bc2615dc", 400, 400, False),
    "assets/images/shop_item_6.jpg": ("photo-1585704032915-c3400ca199e7", 400, 400, False),

    # --- Price Cards ---
    "assets/images/price_1.jpg": ("photo-1585704032915-c3400ca199e7", 360, 220, False),
    "assets/images/price_2.jpg": ("photo-1621905252507-b35492cc74b4", 360, 220, False),
    "assets/images/price_3.jpg": ("photo-1607472586893-edb57bdc0e39", 360, 220, False),
    "assets/images/price_4.jpg": ("photo-1542013936693-884638332954", 360, 220, False),
    "assets/images/price_5.jpg": ("photo-1581244277943-fe4a9c777189", 360, 220, False),
    "assets/images/price_6.jpg": ("photo-1505798577917-a65157d3320a", 360, 220, False),
    "assets/images/price_7.jpg": ("photo-1517646287270-a5a9ca602e5c", 360, 220, False),
    "assets/images/price_8.jpg": ("photo-1621905251189-08b45d6a269e", 360, 220, False),
    "assets/images/price_9.jpg": ("photo-1581092160607-ee22621dd758", 360, 220, False),
    "assets/images/price_10.jpg": ("photo-1590486803833-1c5dc8ddd4c8", 360, 220, False),
    "assets/images/price_11.jpg": ("photo-1506744038136-46273834b3fb", 360, 220, False),

    # --- Blog ---
    "assets/images/blog_main_1.jpg": ("photo-1621905251189-08b45d6a269e", 900, 550, False),
    "assets/images/blog_main_2.jpg": ("photo-1505798577917-a65157d3320a", 900, 550, False),
    "assets/images/blog_main_3.jpg": ("photo-1517646287270-a5a9ca602e5c", 900, 550, False),
    "assets/images/blog_main_4.jpg": ("photo-1585704032915-c3400ca199e7", 900, 550, False),
    "assets/images/blog_single_featured.jpg": ("photo-1621905251189-08b45d6a269e", 900, 550, False),
    "assets/images/blog_thumb_1.jpg": ("photo-1581244277943-fe4a9c777189", 120, 110, False),
    "assets/images/blog_thumb_2.jpg": ("photo-1584622650111-993a426fbf0a", 120, 110, False),
    "assets/images/blog_thumb_3.jpg": ("photo-1542013936693-884638332954", 120, 110, False),
    "assets/images/blog_thumb_4.jpg": ("photo-1505798577917-a65157d3320a", 120, 110, False),

    # --- Home & About ---
    "assets/images/home_certified_1.jpg": ("photo-1581092335397-9583fe92d232", 500, 350, False),
    "assets/images/home_certified_2.jpg": ("photo-1521791136064-7986c2920216", 500, 350, False),
    "assets/images/home_certified_3.jpg": ("photo-1560518883-ce09059eeffa", 500, 350, False),
    "assets/images/about_mission.jpg": ("photo-1586528116311-ad8dd3c8310d", 600, 400, False),
    "assets/images/about_plumber.jpg": ("photo-1621905252507-b35492cc74b4", 600, 500, False),
    "assets/images/author_avatar.png": ("photo-1573496359142-b8d87734a5a2", 160, 160, False),

    # --- Team Members & Characters (Transparent Cutouts) ---
    "assets/images/team_tim_cock.png": ("photo-1507003211169-0a1dd7228f2d", 400, 480, True),
    "assets/images/team_rock_lelu.png": ("photo-1500648767791-00dcc994a43e", 400, 480, True),
    "assets/images/team_michale_rock.png": ("photo-1472099645785-5658abf4ff4e", 400, 480, True),
    "assets/images/team_rock_lelu_2.png": ("photo-1519085360753-af0119f7cbe7", 400, 480, True),
    "assets/images/service_tab_plumber.png": ("photo-1504307651254-35680f356dfd", 450, 550, True),
    "assets/images/emergency_plumber.png": ("photo-1507003211169-0a1dd7228f2d", 350, 420, True),
    "assets/images/footer_plumber.png": ("photo-1500648767791-00dcc994a43e", 350, 450, True),
}

print(f"Starting upgrade of {len(image_mapping)} images...")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for target_path, (pid, w, h, is_cutout) in image_mapping.items():
    try:
        url = f"https://images.unsplash.com/{pid}?auto=format&fit=crop&w={w}&h={h}&q=85"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as response:
            data = response.read()

        img = Image.open(io.BytesIO(data))

        os.makedirs(os.path.dirname(target_path), exist_ok=True)

        if is_cutout:
            cutout = remove(img)
            cutout.save(target_path, "PNG")
            print(f"[CUTOUT OK] {target_path}")
        else:
            if target_path.lower().endswith(".jpg"):
                img = img.convert("RGB")
                img.save(target_path, "JPEG", quality=90)
            else:
                img.save(target_path, "PNG")
            print(f"[PHOTO OK] {target_path}")

    except Exception as e:
        print(f"[FAILED] {target_path}: {e}")

print("Image upgrade complete!")
