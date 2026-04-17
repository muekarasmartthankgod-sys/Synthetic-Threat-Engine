# 🧩 Synthetic-Threat-Engine
**Physics-Informed Data Augmentation & Multimodal Customs Audit AI**

Developed by **Smart Thankgod**, Nigeria Customs Service. UK Border Force trained Image analyst 
*MSc Computer Science (by Research), University of York. 

## 📖 Project Overview
The **Synthetic-Threat-Engine** addresses the "Data Scarcity" bottleneck in border security. It provides a specialized pipeline to generate high-fidelity "Digital Twins" of smuggling scenarios by mathematically interleaving contraband into real-world cargo backgrounds. 

This repository demonstrates the full lifecycle: from **Synthetic Generation** to **Automated Conformity Auditing** using YOLOv8 and Large Language Models (LLMs).

## 🛠️ Core Modules

### 1. The Generation Engine (Sim-to-Real)
To simulate a concealment scenario, the engine utilizes **Radiometric Density Matching**. Rather than a simple overlay, it calculates the pixel-wise attenuation of an X-ray beam:
- **Interleaving:** Blends threat templates into background NII scans.
- **Physics Modeling:** Applies a density coefficient ($\alpha = 0.85$ for rubber) to ensure the threat "sinks" into the cargo.
- **U-Net Style Masking:** Soft-edge blurring prevents the AI from detecting artificial digital boundaries.

### 2. The Multimodal Audit Bridge
The system functions as a **Decision Intelligence (DI)** platform:
- **Vision Intelligence:** Employs YOLOv8 (trained on real-world NCS data) to identify physical goods.
- **Strategic Reasoning:** Uses Gemini AI to cross-reference visual detections against manifest declarations.

## 🚀 Performance
- **Validation:** 93.12% Confidence score on synthetic truck tyre injections.
- **Inference:** ~3.0ms per scan, supporting high-volume port operations.

## 🔒 Security Notice
The proprietary weights (`best.pt`) used for these tests were trained on sensitive Nigeria Customs Service data and are **not included** in this public repository to maintain national security protocols.
