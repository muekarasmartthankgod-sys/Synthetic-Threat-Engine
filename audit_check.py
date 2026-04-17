from ultralytics import YOLO
from google import genai
import os

# --- CONFIGURATION ---
API_KEY = "YOUR_GEMINI_API_KEY"
WEIGHTS_PATH = 'weights/best.pt' # Path to your private weights
IMAGE_TO_TEST = 'synthetic_audit_sample.png'

client = genai.Client(api_key=API_KEY)

def run_conformity_audit(image_path, manifest_item="truck tyre"):
    if not os.path.exists(WEIGHTS_PATH):
        print("❌ Error: weights/best.pt not found. Ensure your private weights are in the folder.")
        return

    # 1. Vision Logic (YOLOv8)
    # Critical: Use imgsz=640 to match training scale
    model = YOLO(WEIGHTS_PATH)
    results = model.predict(image_path, conf=0.25, imgsz=640, verbose=False)
    
    detections = [model.names[int(box.cls)] for box in results[0].boxes]
    found_summary = ", ".join(detections) if detections else "nothing detected"

    # 2. Strategic Reasoning Logic (Gemini)
    prompt = f"""
    SYSTEM: Senior Nigeria Customs Auditor.
    TASK: Compare physical detections vs. manifest declarations.
    
    MANIFEST SAYS: {manifest_item}
    VISION DETECTED: {found_summary}
    
    ACTION:
    1. Declare CONFORMITY or NON-CONFORMITY.
    2. Provide a brief Customs Risk Analysis.
    """

    response = client.models.generate_content(model="gemini-1.5-flash", contents=prompt)

    # 3. Final Report
    print("\n" + "="*45)
    print("CUSTOMS CONFORMITY AUDIT REPORT")
    print("="*45)
    print(f"IMAGE: {image_path}")
    print(f"PHYSICAL EVIDENCE: {found_summary}")
    print("-" * 45)
    print(response.text)

if __name__ == "__main__":
    run_conformity_audit(IMAGE_TO_TEST)
