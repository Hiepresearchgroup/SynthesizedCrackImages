# SynthesizedCrackImages
Synthesizing Semantic Crack Images Using Propagation Simulations and GANs
![Demo](/model_comparison_cumulative.gif)
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
