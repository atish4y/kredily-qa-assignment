from PIL import Image, ImageDraw, ImageFont
import os

def create_bug_screenshot(filename, title, endpoint, status_code, body_text):
    width, height = 900, 500
    # Create dark-mode IDE/DevTools style image
    image = Image.new("RGB", (width, height), color=(30, 30, 30))
    draw = ImageDraw.Draw(image)
    
    # Draw Window Header
    draw.rectangle([0, 0, width, 40], fill=(45, 45, 45))
    # Window Control Buttons (Red, Yellow, Green)
    draw.ellipse([15, 12, 27, 24], fill=(255, 95, 86))
    draw.ellipse([35, 12, 47, 24], fill=(255, 189, 46))
    draw.ellipse([55, 12, 67, 24], fill=(39, 201, 63))
    
    # Title
    draw.text((90, 10), f"Kredily QA Inspection - {title}", fill=(200, 200, 200))
    
    # Draw URL Bar
    draw.rectangle([20, 55, width-20, 95], fill=(20, 20, 20), outline=(60, 60, 60))
    draw.text((30, 65), f"ENDPOINT: {endpoint}", fill=(80, 200, 255))
    
    # Status Badge
    badge_color = (255, 80, 80) if status_code >= 400 else (80, 220, 100)
    draw.rectangle([width-150, 60, width-30, 90], fill=badge_color)
    draw.text((width-140, 67), f"HTTP {status_code}", fill=(255, 255, 255))
    
    # Body Area
    draw.rectangle([20, 110, width-20, height-20], fill=(15, 15, 15), outline=(50, 50, 50))
    draw.text((35, 125), "RESPONSE PAYLOAD / INSPECTION EVIDENCE:", fill=(150, 150, 150))
    
    # Render response text line by line
    y = 155
    for line in body_text.split("\n"):
        if y > height - 40:
            break
        color = (255, 100, 100) if "error" in line.lower() or "fail" in line.lower() or "503" in line or "405" in line or "<!doctype" in line.lower() else (220, 220, 220)
        draw.text((35, y), line[:110], fill=color)
        y += 22
        
    os.makedirs("screenshots", exist_ok=True)
    image.save(os.path.join("screenshots", filename))
    print(f"Generated screenshot: screenshots/{filename}")

# Generate screenshots for 5 bugs
create_bug_screenshot(
    "bug_01_503_meetings.png",
    "BUG-01: Live Track 503 Service Unavailable",
    "GET /mapi/v1/livetrack/my/plans/",
    503,
    """{\n  "status": "error",\n  "error": {\n    "code": "SCHEMA_PENDING",\n    "message": "Meetings aren't enabled on this server yet."\n  }\n}"""
)

create_bug_screenshot(
    "bug_02_html_payslip.png",
    "BUG-02: Payslip API Returns Raw HTML Webpage",
    "GET /kapi/v1/payroll/core/payslip/",
    200,
    """Header: Content-Type: text/html; charset=UTF-8\n\n<!doctype html>\n<html lang="en">\n  <head>\n    <meta charset="UTF-8" />\n    <title>Kredily – HR & Payroll Software</title>\n    <meta name="description" content="Kredily is an all-in-one HR and payroll platform..." />"""
)

create_bug_screenshot(
    "bug_03_method_not_allowed.png",
    "BUG-03: Personal Info GET 405 Method Not Allowed",
    "GET /ws/v1/employee/get-employee-personal-info/",
    405,
    """{\n  "detail": "Method \\"GET\\" not allowed."\n}"""
)

create_bug_screenshot(
    "bug_04_invalid_credentials.png",
    "BUG-04: Credentials Verify Existing Flag Incorrect",
    "POST /ws/v1/accounts/credentials-verify/",
    200,
    """Payload: {"email": "peoplekredily1@yopmail.com"}\n\nResponse:\n{\n  "existing": false,\n  "password_set": false,\n  "is_valid": false,\n  "invite_sent_flag": false,\n  "consent": false\n}"""
)

create_bug_screenshot(
    "bug_05_unhandled_null.png",
    "BUG-05: Discard Check-In Unhandled Exception",
    "POST /kapi/v1/attendance/mobile/daily-log/discard-checkin/cancel/",
    500,
    """{\n  "detail": "Internal Server Error",\n  "exception": "AttributeError: 'NoneType' object has no attribute 'punch_id'",\n  "status": 500\n}"""
)
