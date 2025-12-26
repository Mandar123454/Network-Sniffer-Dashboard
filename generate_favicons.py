#!/usr/bin/env python3
"""
Generate favicon PNG files from SVG
Run this script to create favicon_32.png, favicon_64.png, and favicon_256.png
"""

import io
from pathlib import Path

# Try importing PIL for image creation
try:
    from PIL import Image, ImageDraw
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("⚠️  PIL not available. Install with: pip install Pillow")

def create_favicon_png(size):
    """Create a PNG favicon of the specified size with spy badge design."""
    
    if not PIL_AVAILABLE:
        print(f"❌ Cannot create favicon_{size}.png without PIL")
        return False
    
    # Create image with transparent background
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Colors
    cyan = (0, 255, 255, 255)  # #0fff
    dark = (0, 16, 31, 255)     # #00101f
    light_cyan = (74, 212, 255, 255)  # #4ad4ff
    
    # Scale factor for the design
    scale = size / 512
    
    # Draw head (top part)
    head_left = int(256 * scale - 78 * scale)
    head_top = int(0)
    head_right = int(256 * scale + 78 * scale)
    head_bottom = int(69 * scale)
    
    draw.rectangle([head_left, head_top, head_right, head_bottom], fill=cyan)
    
    # Draw body (main part)
    body_left = int(120 * scale)
    body_top = int(122 * scale)
    body_right = int(392 * scale)
    body_bottom = int(223 * scale)
    
    draw.rectangle([body_left, body_top, body_right, body_bottom], fill=dark, outline=cyan, width=max(1, int(10 * scale)))
    
    # Draw left eye
    left_eye_x = int(180 * scale)
    left_eye_y = int(300 * scale)
    eye_radius = int(42 * scale)
    
    draw.ellipse(
        [left_eye_x - eye_radius, left_eye_y - eye_radius,
         left_eye_x + eye_radius, left_eye_y + eye_radius],
        fill=light_cyan
    )
    
    # Draw right eye
    right_eye_x = int(330 * scale)
    right_eye_y = int(300 * scale)
    
    draw.ellipse(
        [right_eye_x - eye_radius, right_eye_y - eye_radius,
         right_eye_x + eye_radius, right_eye_y + eye_radius],
        fill=light_cyan
    )
    
    # Save the image
    static_dir = Path(__file__).parent / 'static'
    static_dir.mkdir(exist_ok=True)
    
    output_path = static_dir / f'favicon_{size}.png'
    img.save(output_path, 'PNG')
    print(f"✅ Created {output_path.name}")
    return True

def main():
    """Generate all favicon sizes."""
    print("🔨 Generating favicon PNG files...")
    print()
    
    sizes = [32, 64, 256]
    success = True
    
    for size in sizes:
        if not create_favicon_png(size):
            success = False
    
    print()
    if success:
        print("✅ All favicons created successfully!")
        print("\nPlace these files in /static/:")
        print("  - favicon_32.png")
        print("  - favicon_64.png")
        print("  - favicon_256.png")
    else:
        print("⚠️  Install Pillow for PNG generation: pip install Pillow")

if __name__ == '__main__':
    main()
