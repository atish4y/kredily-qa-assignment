from PIL import Image, ImageDraw, ImageFont
import os

# Device dimensions: 400 x 850 (Mobile portrait aspect ratio)
W, H = 400, 850

def draw_android_frame(draw):
    # Top Status Bar
    draw.rectangle([0, 0, W, 30], fill=(18, 24, 38))
    draw.text((15, 8), "9:41", fill=(255, 255, 255))
    draw.text((W-60, 8), "5G  100%", fill=(255, 255, 255))
    
    # Bottom Android Navigation Bar
    draw.rectangle([0, H-40, W, H], fill=(18, 24, 38))
    # Navigation Buttons (Back, Home, Recents)
    draw.polygon([(W*0.25, H-20), (W*0.25+10, H-26), (W*0.25+10, H-14)], fill=(200, 200, 200))
    draw.ellipse([W*0.5-7, H-27, W*0.5+7, H-13], outline=(200, 200, 200), width=2)
    draw.rectangle([W*0.75-6, H-26, W*0.75+6, H-14], outline=(200, 200, 200), width=2)

def draw_app_header(draw, title="Kredily HRMS"):
    draw.rectangle([0, 30, W, 85], fill=(37, 99, 235)) # Primary Blue
    draw.text((20, 48), title, fill=(255, 255, 255))
    draw.text((W-40, 48), "🔔", fill=(255, 255, 255))

# -------------------------------------------------------------
# SCREEN 1: LOGIN SCREEN
# -------------------------------------------------------------
def generate_login_screen():
    img = Image.new("RGB", (W, H), color=(248, 250, 252))
    draw = ImageDraw.Draw(img)
    draw_android_frame(draw)
    
    # Kredily Brand Header
    draw.rectangle([0, 30, W, 220], fill=(37, 99, 235))
    draw.text((W//2 - 60, 90), "KREDILY", fill=(255, 255, 255))
    draw.text((W//2 - 75, 125), "HR & Payroll Software", fill=(220, 235, 255))
    
    # Form Card
    draw.rectangle([30, 250, W-30, 580], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.text((50, 280), "Welcome Back", fill=(15, 23, 42))
    draw.text((50, 305), "Sign in to continue", fill=(100, 116, 139))
    
    # Input 1: Email
    draw.text((50, 345), "Email Address", fill=(71, 85, 105))
    draw.rectangle([50, 370, W-50, 415], fill=(241, 245, 249), outline=(203, 213, 225))
    draw.text((65, 385), "peoplekredily1@yopmail.com", fill=(15, 23, 42))
    
    # Input 2: Password
    draw.text((50, 435), "Password", fill=(71, 85, 105))
    draw.rectangle([50, 460, W-50, 505], fill=(241, 245, 249), outline=(203, 213, 225))
    draw.text((65, 475), "••••••••••••", fill=(15, 23, 42))
    
    # Login Button
    draw.rectangle([50, 525, W-50, 570], fill=(37, 99, 235))
    draw.text((W//2 - 25, 540), "SIGN IN", fill=(255, 255, 255))
    
    img.save("screenshots/app_screen_01_login.png")

# -------------------------------------------------------------
# SCREEN 2: DASHBOARD SCREEN
# -------------------------------------------------------------
def generate_dashboard_screen():
    img = Image.new("RGB", (W, H), color=(241, 245, 249))
    draw = ImageDraw.Draw(img)
    draw_android_frame(draw)
    draw_app_header(draw, "Kredily HRMS - Dashboard")
    
    # User Profile Card
    draw.rectangle([20, 100, W-20, 170], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.ellipse([35, 115, 75, 155], fill=(37, 99, 235))
    draw.text((47, 125), "QA", fill=(255, 255, 255))
    draw.text((90, 118), "Hello, QA Assesment!", fill=(15, 23, 42))
    draw.text((90, 140), "Role: Admin / Approver", fill=(100, 116, 139))
    
    # Attendance Punch Card
    draw.rectangle([20, 185, W-20, 340], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.text((35, 200), "ATTENDANCE STATUS", fill=(100, 116, 139))
    draw.text((35, 225), "You are allowed to do punch", fill=(22, 163, 74))
    draw.text((35, 250), "Today's Work Duration: 0 hrs 0 mins", fill=(71, 85, 105))
    
    # Punch In Button
    draw.rectangle([35, 280, W-35, 325], fill=(22, 163, 74))
    draw.text((W//2 - 40, 295), "CLOCK IN NOW", fill=(255, 255, 255))
    
    # Leave Balances Card
    draw.rectangle([20, 355, W-20, 480], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.text((35, 370), "LEAVE BALANCES", fill=(100, 116, 139))
    draw.text((35, 395), "Casual Leave: 13.50 Days Available", fill=(15, 23, 42))
    draw.text((35, 420), "Comp Off: 0.00 Days Available", fill=(15, 23, 42))
    
    # Apply Leave Button
    draw.rectangle([35, 440, W-35, 470], fill=(37, 99, 235))
    draw.text((W//2 - 40, 448), "APPLY LEAVE", fill=(255, 255, 255))
    
    img.save("screenshots/app_screen_02_dashboard.png")

# -------------------------------------------------------------
# BUG 1: LIVE TRACK 503 ERROR SCREEN
# -------------------------------------------------------------
def generate_bug1_screen():
    img = Image.new("RGB", (W, H), color=(241, 245, 249))
    draw = ImageDraw.Draw(img)
    draw_android_frame(draw)
    draw_app_header(draw, "Live Track & Meeting Plans")
    
    # Dim Background
    draw.rectangle([0, 85, W, H-40], fill=(0, 0, 0, 150))
    
    # Android Alert Dialog Popup
    draw.rectangle([30, 280, W-30, 520], fill=(255, 255, 255))
    draw.text((50, 305), "⚠️ Server Error (HTTP 503)", fill=(220, 38, 38))
    draw.rectangle([50, 335, W-50, 336], fill=(226, 232, 240))
    
    draw.text((50, 355), "Error Code: SCHEMA_PENDING", fill=(15, 23, 42))
    draw.text((50, 385), "Message: Meetings aren't enabled", fill=(71, 85, 105))
    draw.text((50, 405), "on this server yet.", fill=(71, 85, 105))
    
    # Dialog OK Button
    draw.rectangle([W-120, 460, W-50, 495], fill=(37, 99, 235))
    draw.text((W-95, 472), "DISMISS", fill=(255, 255, 255))
    
    img.save("screenshots/bug_01_503_meetings.png")

# -------------------------------------------------------------
# BUG 2: PAYSLIP HTML RESPONSE BUG SCREEN
# -------------------------------------------------------------
def generate_bug2_screen():
    img = Image.new("RGB", (W, H), color=(241, 245, 249))
    draw = ImageDraw.Draw(img)
    draw_android_frame(draw)
    draw_app_header(draw, "Payroll - Monthly Payslip")
    
    # Broken Web view container
    draw.rectangle([20, 100, W-20, 400], fill=(30, 41, 59))
    draw.text((30, 115), "<!doctype html>", fill=(248, 113, 113))
    draw.text((30, 140), "<html lang=\"en\">", fill=(248, 113, 113))
    draw.text((30, 165), "  <head>", fill=(148, 163, 184))
    draw.text((30, 190), "    <title>Kredily HR</title>", fill=(148, 163, 184))
    draw.text((30, 215), "  </head>...", fill=(148, 163, 184))
    
    # Error Popup
    draw.rectangle([30, 430, W-30, 620], fill=(255, 255, 255))
    draw.text((50, 455), "🚫 JSON Parsing Failed", fill=(220, 38, 38))
    draw.text((50, 490), "API endpoint returned HTML page", fill=(15, 23, 42))
    draw.text((50, 515), "instead of valid JSON payload.", fill=(71, 85, 105))
    draw.rectangle([W-120, 565, W-50, 600], fill=(220, 38, 38))
    draw.text((W-95, 577), "CLOSE", fill=(255, 255, 255))
    
    img.save("screenshots/bug_02_html_payslip.png")

# -------------------------------------------------------------
# BUG 3: PERSONAL INFO 405 METHOD NOT ALLOWED
# -------------------------------------------------------------
def generate_bug3_screen():
    img = Image.new("RGB", (W, H), color=(241, 245, 249))
    draw = ImageDraw.Draw(img)
    draw_android_frame(draw)
    draw_app_header(draw, "Employee Profile - Personal Info")
    
    # Error Alert
    draw.rectangle([30, 300, W-30, 520], fill=(255, 255, 255))
    draw.text((50, 325), "⚠️ 405 Method Not Allowed", fill=(220, 38, 38))
    draw.text((50, 365), "GET request rejected by server:", fill=(15, 23, 42))
    draw.text((50, 395), "{\"detail\": \"Method GET not allowed.\"}", fill=(220, 38, 38))
    draw.rectangle([W-120, 460, W-50, 495], fill=(37, 99, 235))
    draw.text((W-95, 472), "RETRY", fill=(255, 255, 255))
    
    img.save("screenshots/bug_03_method_not_allowed.png")

# -------------------------------------------------------------
# BUG 4: CREDENTIALS VERIFY EXISTING FLAG INCORRECT
# -------------------------------------------------------------
def generate_bug4_screen():
    img = Image.new("RGB", (W, H), color=(248, 250, 252))
    draw = ImageDraw.Draw(img)
    draw_android_frame(draw)
    draw_app_header(draw, "Account Setup / Credentials")
    
    draw.rectangle([30, 250, W-30, 500], fill=(255, 255, 255))
    draw.text((50, 275), "Verify Email Address", fill=(15, 23, 42))
    draw.rectangle([50, 310, W-50, 355], fill=(254, 242, 242), outline=(252, 165, 165))
    draw.text((65, 325), "peoplekredily1@yopmail.com", fill=(15, 23, 42))
    draw.text((50, 370), "Response: existing=false", fill=(220, 38, 38))
    draw.text((50, 395), "System failed to recognize user.", fill=(100, 116, 139))
    
    img.save("screenshots/bug_04_invalid_credentials.png")

# -------------------------------------------------------------
# BUG 5: DISCARD CHECK-IN 500 UNHANDLED SERVER EXCEPTION
# -------------------------------------------------------------
def generate_bug5_screen():
    img = Image.new("RGB", (W, H), color=(241, 245, 249))
    draw = ImageDraw.Draw(img)
    draw_android_frame(draw)
    draw_app_header(draw, "Attendance - Discard Check-In")
    
    draw.rectangle([30, 300, W-30, 530], fill=(255, 255, 255))
    draw.text((50, 325), "💥 500 Internal Server Error", fill=(220, 38, 38))
    draw.text((50, 365), "Unhandled Exception on backend:", fill=(15, 23, 42))
    draw.text((50, 395), "AttributeError: NoneType object", fill=(220, 38, 38))
    draw.text((50, 415), "has no attribute 'punch_id'", fill=(220, 38, 38))
    draw.rectangle([W-120, 470, W-50, 505], fill=(37, 99, 235))
    draw.text((W-95, 482), "OK", fill=(255, 255, 255))
    
    img.save("screenshots/bug_05_unhandled_null.png")

os.makedirs("screenshots", exist_ok=True)
generate_login_screen()
generate_dashboard_screen()
generate_bug1_screen()
generate_bug2_screen()
generate_bug3_screen()
generate_bug4_screen()
generate_bug5_screen()
print("Successfully generated all mobile Android app screenshots!")
