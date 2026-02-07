# SynthesizedCrackImages
Synthesizing Semantic Crack Images Using Propagation Simulations and GANs
Demo 1

![Demo](/model_comparison_cumulative.gif)

Qualitative comparison of model outputs under varying levels of input noise for synthesized semantic crack images using propagation simulations and GANs.
## 💾 Dataset

The comprehensive dataset used in this study consists of **90,000 images** and is available for download. The dataset is organized into two main parts:

### Summary of the Analyzed Datasets

| Dataset         | Size   | Note |
|-----------------|--------|------|
| CFD10k          | 9,440  | Augmented from the CFD dataset |
| ControlNet10k   | 10,000 | Synthesized using ControlNet and Stable Diffusion |
| Pix2pixHD10k    | 10,000 | Synthesized using Pix2pixHD |
| Pix2pixHD10k_nn | 10,000 | Synthesized without additive noise using Pix2pixHD |
| DP-GAN10k       | 10,000 | Synthesized using DP-GAN |
| DP-GAN10k_nn    | 10,000 | Synthesized without additive noise using DP-GAN |
| OASIS10k        | 10,000 | Synthesized using OASIS |
| OASIS10k_nn     | 10,000 | Synthesized without additive noise using OASIS |

**➡️ Download the dataset link in file pdf here:** [SynthesizedCrackImages Dataset](SynthesizedCrackImages.pdf)

```bash
# Run the script download the dataset with:
python download_dataset.py
```
## Pretrained Models
[![Download for Pretrained](https://img.shields.io/badge/Download%20for%20Windows-%F0%9F%92%BB-blue?style=for-the-badge)](https://github.com/Hiepresearchgroup/SynthesizedCrackImages/releases/tag/v1.0)

The following pretrained models are released via GitHub Releases.
Each model corresponds to a specific image synthesis framework used in this work.

### 🔹 OASIS
- **Generator:** `best_G.pth`
- **Discriminator:** `best_D.pth`

### 🔹 pix2pixHD
- **Generator:** `latest_net_G.pth`
- **Discriminator:** `latest_net_D.pth`

### 🔹 DP-GAN
- **Generator:** `best_G_DPGAN.pth`
- **Discriminator:** `best_D_DPGAN.pth`
- 
All files are provided in **PyTorch (`.pth`) format** for **research and academic use only**. 
	
**Citation**
```
@article{dinh2025simcrackgan,
  title     = {Synthesizing Semantic Crack Images Using Propagation Simulations and GANs},
  author    = {Dinh, Tran Hiep and Le, Cong Hieu and Lin, Chin-Teng and Trung, Nguyen Linh},
  journal   = {IEEE Transactions on Instrumentation and Measurement},
  note      = {under review},
  year      = {2025}
}
```
**Background: Crack Tip Simulation**
To ensure the synthesized cracks adhere to physical laws rather than just visual imitation, this work builds upon our previous research in fracture mechanics. A critical component of this approach is the modeling of the crack tip—the precise location where material separation occurs and propagation direction is determined.
By utilizing the Extended Finite Element Method (X-FEM) coupled with the Level Set Method (LSM), we developed an automated pipeline to simulate realistic propagation paths and extract precise crack tip coordinates. These physical simulations provide the structural "skeleton" for the semantic masks used in our GAN training. For a detailed explanation of the automatic simulation and crack tip extraction methodology, please refer to our foundational paper below.

```
@article{Dinh2023Toward,
	author = {Dinh, Tran Hiep and Anh, Vu Thi Thuy and Nguyen, TruongGiang and Hieu Le, Cong and Trung, Nguyen Linh and Duc, Nguyen Dinh and Lin, Chin-Teng},
	journal = {IEEE Transactions on Instrumentation and Measurement},
	year = {2023},
	pages = {1--15},
	publisher = {{Institute of Electrical and Electronics Engineers (IEEE)}},
	title = {Toward vision-based concrete crack detection: Automatic simulation of real-world cracks},
	volume = {72},
}
```
