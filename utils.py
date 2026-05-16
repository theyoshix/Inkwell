import os
import sys
import base64


def get_asset_path(filename):
    """Gets the absolute path to a file, whether running as a script or a compiled .exe"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, filename)


def load_image_to_base64(filename):
    """Reads a local image and converts it to Base64 in memory."""
    filepath = get_asset_path(filename)
    if not os.path.exists(filepath):
        print(f"[WARNING] Could not find image: {filepath}")
        return ""
    try:
        with open(filepath, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode('utf-8')
            ext = filepath.split('.')[-1].lower()
            mime = "image/jpeg" if ext in ['jpg', 'jpeg'] else "image/png"
            return f"data:{mime};base64,{encoded}"
    except Exception as e:
        print(f"[ERROR] Loading image {filename}: {e}")
        return ""
