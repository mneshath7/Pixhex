import numpy as np
from scipy.ndimage import gaussian_filter, sobel
from scipy.spatial import Delaunay
from PIL import Image
from matplotlib.image import imread

def tiered_blur_cascade(image):
    """Stage 2: Apply tiered blur cascade."""
    high_blur = gaussian_filter(image, sigma=5)  # High blur
    medium_blur = gaussian_filter(high_blur, sigma=3)  # Medium on high
    low_blur = gaussian_filter(medium_blur, sigma=1)  # Low on medium
    return low_blur  # Final blurred image for further processing

def identify_edit_probable_regions(image, threshold=50):
    """Identify regions likely to be edited, e.g., high-edge areas."""
    # Convert to grayscale if needed
    if len(image.shape) == 3:
        gray = np.mean(image, axis=2)
    else:
        gray = image
    # Edge detection using Sobel
    sx = sobel(gray, axis=0)
    sy = sobel(gray, axis=1)
    edge_mag = np.sqrt(sx**2 + sy**2)
    # Binary mask for high-edge areas
    mask = edge_mag > threshold
    return mask

def embed_anchor_points(image, shift_amount=1):
    """Embed subtle shifts in strings of 3 adjacent pixels in probable regions."""
    # Assume image is RGB numpy array (H, W, 3)
    h, w, _ = image.shape
    mask = identify_edit_probable_regions(image)
    
    # For simplicity, embed in horizontal strings
    for i in range(h):
        for j in range(1, w - 1):  # Avoid edges
            if mask[i, j-1] and mask[i, j] and mask[i, j+1]:  # All 3 in probable region
                # Shift middle pixel's blue channel (least noticeable) by shift_amount
                image[i, j, 2] = (image[i, j, 2] + shift_amount) % 256
    
    return image

def detect_anchor_points(image, shift_amount=1, tolerance=0.5):
    """Detect if embedded shifts are present and consistent."""
    h, w, _ = image.shape
    mask = identify_edit_probable_regions(image)
    suspicious_count = 0
    total_strings = 0
    
    for i in range(h):
        for j in range(1, w - 1):
            if mask[i, j-1] and mask[i, j] and mask[i, j+1]:
                total_strings += 1
                # Check if middle blue is approx left + right avg + shift
                expected = (int(image[i, j-1, 2]) + int(image[i, j+1, 2])) // 2 + shift_amount
                actual = int(image[i, j, 2])
                if abs(actual - expected) > tolerance:
                    suspicious_count += 1
    
    if total_strings == 0:
        return "NO ANCHORS"
    suspicion_rate = suspicious_count / total_strings
    if suspicion_rate > 0.1:  # 10% threshold for suspicion
        return "SUSPICIOUS"
    return "SAFE"

def anchor_point_triangulation(image, num_points=100):
    """Legacy Stage 3: Detect anchor points and perform triangulation (for compatibility)."""
    # Compute edge magnitude using Sobel
    sx = sobel(image, axis=0)
    sy = sobel(image, axis=1)
    edge_mag = np.sqrt(sx**2 + sy**2)
    
    # Select top points with highest edge magnitude as anchors
    flat_indices = np.argsort(edge_mag.ravel())[-num_points:]
    y, x = np.unravel_index(flat_indices, image.shape)
    points = np.column_stack((x, y))
    
    # Perform Delaunay triangulation
    if len(points) < 3:
        raise ValueError("Not enough points for triangulation")
    tri = Delaunay(points)
    return tri, points

def conditional_logic(tri, points, threshold=0.1):
    """Stage 4: Flag based on triangle area variance (legacy)."""
    # Compute triangle areas
    tri_points = points[tri.simplices]
    vec1 = tri_points[:, 1] - tri_points[:, 0]
    vec2 = tri_points[:, 2] - tri_points[:, 0]
    areas = 0.5 * np.abs(np.cross(vec1, vec2))
    
    # Normalize areas
    if np.max(areas) > 0:
        normalized_areas = areas / np.max(areas)
    else:
        normalized_areas = areas
    
    # High variance might indicate irregularity (suspicious)
    area_var = np.var(normalized_areas)
    if area_var > threshold:
        return "SUSPICIOUS"
    return "SAFE"

def turing_pattern_analysis(image, grid_size=20, var_threshold=50):
    """Stage 5: Localized analysis inspired by Turing patterns (simple variance check)."""
    h, w = image.shape[:2]  # Handle RGB or grayscale
    if len(image.shape) == 3:
        image = np.mean(image, axis=2)  # Convert to grayscale for analysis
    suspicions = 0
    for i in range(0, h, grid_size):
        for j in range(0, w, grid_size):
            patch = image[i:i+grid_size, j:j+grid_size]
            if patch.size == 0:
                continue
            patch_var = np.var(patch)
            if patch_var < var_threshold:  # Low variance might indicate synthetic uniformity
                suspicions += 1
    if suspicions > (h * w) / (grid_size ** 2) * 0.2:  # More than 20% suspicious patches
        return "SUSPICIOUS"
    return "SAFE"

def image_forgery_detection_pipeline(image_path, embed=False, use_legacy_triangulation=False):
    """Full pipeline for image manipulation detection, with updated anchor points."""
    # Stage 1: Raw Data Input
    image = np.array(Image.open(image_path).convert('RGB')).astype(float)
    
    if embed:
        embedded_image = embed_anchor_points(image)
        return embedded_image  # Return embedded image as numpy array
    
    # Stage 2: Tiered Blur Cascade
    blurred_image = tiered_blur_cascade(image)
    
    # Stage 3: Anchor Point Triangulation/Detection
    if use_legacy_triangulation:
        tri, points = anchor_point_triangulation(blurred_image)
    else:
        anchor_flag = detect_anchor_points(image)
        if anchor_flag in ["SUSPICIOUS", "NO ANCHORS"]:
            return anchor_flag
    
    # Stage 4: Conditional Logic
    if use_legacy_triangulation:
        flag4 = conditional_logic(tri, points)
        if flag4 == "SUSPICIOUS":
            return flag4
    else:
        # For updated version, skip or integrate additional logic if needed
        pass
    
    # Stage 5: Turing Pattern Analysis
    flag5 = turing_pattern_analysis(image)
    return flag5

# Example usage:
# To embed anchors: embedded = image_forgery_detection_pipeline('path/to/image.jpg', embed=True)
# To detect (updated): result = image_forgery_detection_pipeline('path/to/image.jpg')
# To use legacy: result = image_forgery_detection_pipeline('path/to/image.jpg', use_legacy_triangulation=True)
# print(result)
