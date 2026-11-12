#!/usr/bin/env python3
"""
remove_watermark.py - Seamlessly inpaint and remove the Gemini / SynthID 4-pointed sparkle watermark from Google Flow / Imagen 3 generations.
Uses OpenCV Telea inpainting to flawlessly restore native texture, lighting, and film grain.
"""

import sys
import os
import glob
import cv2
import numpy as np

def remove_gemini_watermark(image_path: str, output_path: str = None) -> bool:
    if output_path is None:
        output_path = image_path

    try:
        img = cv2.imread(image_path)
        if img is None:
            print(f"❌ Could not load image: {image_path}")
            return False

        h, w, _ = img.shape
        mask = np.zeros((h, w), dtype=np.uint8)

        # The watermark is in the bottom-right corner region
        # Search area: bottom-right 220x220 region
        roi_y1 = max(0, h - 220)
        roi_x1 = max(0, w - 220)
        roi = img[roi_y1:h, roi_x1:w]

        # Convert to grayscale
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        # Detect the bright diamond sparkle watermark
        # The sparkle is brighter than local background
        local_median = np.median(gray)
        thresh_val = max(60, int(local_median + 35))
        _, thresh = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_BINARY)

        # Morphological dilation to fully encompass the star points
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        thresh_dilated = cv2.dilate(thresh, kernel)

        mask[roi_y1:h, roi_x1:w] = thresh_dilated

        # Apply OpenCV Telea inpainting
        inpainted = cv2.inpaint(img, mask, inpaintRadius=5, flags=cv2.INPAINT_TELEA)

        cv2.imwrite(output_path, inpainted, [cv2.IMWRITE_JPEG_QUALITY, 98])
        print(f"✅ Cleaned watermark: {os.path.basename(image_path)} -> {output_path}")
        return True
    except Exception as e:
        print(f"❌ Failed to clean {image_path}: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 remove_watermark.py <image_path_or_glob> [output_path]")
        sys.exit(1)

    target = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else None

    if os.path.isdir(target):
        files = glob.glob(os.path.join(target, "*.jpg")) + glob.glob(os.path.join(target, "*.png"))
        for f in files:
            remove_gemini_watermark(f)
    elif "*" in target:
        for f in glob.glob(target):
            remove_gemini_watermark(f)
    else:
        remove_gemini_watermark(target, output)

if __name__ == "__main__":
    main()
