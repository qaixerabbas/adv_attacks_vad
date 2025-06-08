# 🎯 Adversarial Attacks on Video Anomaly Detection Models in AIoT

This repository contains code and resources for generating and evaluating adversarial attacks on deep learning-based video anomaly detection models. The project is focused on the intersection of **AIoT (Artificial Intelligence of Things)** and **Adversarial Machine Learning**, specifically targeting real-world surveillance scenarios such as **UCF Crime**.

---

## 📌 Project Overview

Recent research has shown that deep neural networks, especially those used in video anomaly detection, are vulnerable to adversarial attacks — small perturbations in the input that lead to misclassification. This repository implements:

- One Pixel Attack
- Multi-Pixel Attack
- A novel **Multi-Pixel Deception (MPD)** attack: combining the power of One Pixel and Pixel attacks
- Preprocessing pipelines for video anomaly datasets
- Evaluation scripts and visualizations

---

## 🗂 Directory Structure

```
📦 root
├── adversarial_samples      # Generated adversarial examples
├── notebooks                # Jupyter notebooks for attack demos
├── preprocess               # Scripts for trimming, resizing, and augmenting videos
├── LICENSE                  # MIT License
├── README.md                # You're here!
├── moondream_reqs.txt       # Optional dependencies for vision-language models
├── requirements.txt         # Python dependencies
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/qaixerabbas/adv_attacks_vad.git
cd adv_attacks_vad
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> Optional: For vision-language filtering (Moondream (currently adopted) or you can use TinyLLaVA), install from `moondream_reqs.txt`.

---

## 📽 Dataset

This code is tested on the **UCF Crime** dataset, a large-scale real-world surveillance dataset. You may need to request access to the dataset separately from [UCF Crime Dataset](https://www.crcv.ucf.edu/projects/real-world/).

---

## 🧠 Models 

- ✅ ResNet-18  
- ✅ EfficientNet-B0  
- ✅ MobileNet-v3 Small  
- (Plug-and-play architecture: easily extendable to more CNN models)

---

## 🔐 Attack Goals

- Mislead anomaly detection models with high success rate  
- Maintain imperceptibility of adversarial perturbations  
- Evaluate robustness across diverse architectures

---

## 📝 Citation

If you use this code in your research, please cite:

```bibtex
@article{hina2025adversarial,
  title={Adversarial attacks on artificial Intelligence of Things-based operational technologies in theme parks},
  author={Hina, Sadaf and Abbas, Qaiser and Ahmed, Kashan},
  journal={Internet of Things},
  pages={101654},
  year={2025},
  publisher={Elsevier}
}
```

---

## ⚖ License

This project is licensed under the [MIT License](./LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository, raise issues, and submit pull requests.

---

## 📬 Contact

For any inquiries or collaborations, reach out to:  
**Qaiser Abbas** – [mqaiser617@gmail.com]
