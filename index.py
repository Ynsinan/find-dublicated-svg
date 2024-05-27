import cairosvg
import os
import cv2
from skimage.metrics import structural_similarity as ssim

def svg_to_png(svg_path, png_path):
    try:
        if os.path.basename(svg_path) == '.DS_Store':
            return
        if os.path.getsize(svg_path) > 0:  # Check if the file is not empty
            cairosvg.svg2png(url=svg_path, write_to=png_path)
        else:
            print(f"SVG file is empty: {svg_path}")
    except Exception as e:
        print(f"Error processing SVG file: {svg_path}, Error: {e}")

def compare_images(image1_path, image2_path):
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    if image1 is None:
        print(f"Could not read image: {image1_path}")
        return
    if image2 is None:
        print(f"Could not read image: {image2_path}")
        return

    image1 = cv2.resize(image1, (300, 300))
    image2 = cv2.resize(image2, (300, 300))

    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    score, _ = ssim(gray1, gray2, full=True)
    return score

def find_duplicates(folder_path):
    duplicates = []
    image_files = os.listdir(folder_path)

    for i, img1_name in enumerate(image_files):
        if not img1_name.endswith('.svg'):
            continue
        img1_path = os.path.join(folder_path, img1_name)
        svg_to_png(img1_path, 'temp1.png')
        
        for img2_name in image_files[i+1:]:
            if not img2_name.endswith('.svg'):
                continue
            img2_path = os.path.join(folder_path, img2_name)
            svg_to_png(img2_path, 'temp2.png')

            similarity_score = compare_images('temp1.png', 'temp2.png')
            if similarity_score is not None and similarity_score == 1:
                duplicates.append((img1_path, img2_path))

    return duplicates
    
if __name__ == "__main__":
    folder_path = os.path.join(os.getcwd(), 'icons')
    duplicate_pairs = find_duplicates(folder_path)
    if duplicate_pairs:
        with open('duplicate_log.txt', 'w') as f:
            f.write("Duplicate image pairs:\n")
            for pair in duplicate_pairs:
                f.write(f"These files are identical: {' '.join(pair)}\n")
        print("Duplicate image pairs logged in duplicate_log.txt")
    else:
        print("No duplicate image pairs found.")