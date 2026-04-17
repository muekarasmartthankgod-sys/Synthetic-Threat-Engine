import cv2
import numpy as np

def generate_synthetic_threat(background_path, threat_path, output_name):
    # 1. Load images in Grayscale (X-ray standard)
    bg = cv2.imread(background_path, cv2.IMREAD_GRAYSCALE)
    threat = cv2.imread(threat_path, cv2.IMREAD_GRAYSCALE)
    
    # 2. Pre-processing
    bg = cv2.resize(bg, (256, 256))
    threat = cv2.resize(threat, (80, 80)) 

    # 3. Create a soft mask for natural blending
    mask = cv2.GaussianBlur(threat, (5, 5), 0)
    _, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)

    # 4. Radiometric Interleaving (Physics-based blending)
    # Final = Background * (1 - (Threat_Density * Alpha))
    alpha = 0.85 
    y1, y2, x1, x2 = 100, 180, 100, 180 # Center coordinates
    roi = bg[y1:y2, x1:x2].astype(float)
    threat_norm = threat.astype(float) / 255.0
    
    # Apply density attenuation
    blended_roi = roi * (1.0 - (threat_norm * alpha))
    
    # 5. Finalize Image
    bg[y1:y2, x1:x2] = blended_roi.astype(np.uint8)
    final_scan = cv2.GaussianBlur(bg, (3, 3), 0) # Add scanner noise
    
    cv2.imwrite(output_name, final_scan)
    print(f"✅ Created: {output_name}")

if __name__ == "__main__":
    # Ensure you have these files in your folder
    generate_synthetic_threat('container_bg.png', 'tyre_template.png', 'synthetic_audit_sample.png')
