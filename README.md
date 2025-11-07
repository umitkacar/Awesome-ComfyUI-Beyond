# AWESOME COMFYUI BEYOND

> The ultimate curated collection of ComfyUI resources for 2024-2025. From cutting-edge video generation to 3D creation, this is your comprehensive guide to the ComfyUI ecosystem.

**Last Updated:** November 2024 | **Maintained by:** [umitkacar](https://github.com/umitkacar)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![GitHub stars](https://img.shields.io/github/stars/umitkacar/Awesome-ComfyUI-Beyond?style=social)

---

## 📋 Table of Contents

- [🚀 What's New in 2024-2025](#-whats-new-in-2024-2025)
- [⚡ Essential Setup](#-essential-setup)
- [🎬 Video Generation](#-video-generation)
- [🎭 Face & Portrait](#-face--portrait)
- [🎨 Image Enhancement](#-image-enhancement)
- [🏗️ 3D Generation](#️-3d-generation)
- [🔧 Workflow Tools](#-workflow-tools)
- [📦 Model Support](#-model-support)
- [🎓 Learning Resources](#-learning-resources)
- [⭐ Top Community Resources](#-top-community-resources)

---

## 🚀 What's New in 2024-2025

### ComfyUI V1 Desktop App (October 2024)
The game-changing update that makes ComfyUI accessible to everyone:
- ✅ **One-Click Installation** - No more Python environment headaches
- ✅ **Model Library** - Browse and drag-drop models with ease
- ✅ **Workflow Browser** - Save and manage workflows efficiently
- ✅ **Automatic Updates** - Stay on the stable release track
- ✅ **Custom Node Registry (CNR)** - 600+ nodes, 2000+ versions

**Download:** [ComfyUI Desktop](https://www.comfy.org/download)

### Major Breakthroughs

🎬 **Video Generation Revolution**
- **HunyuanVideo** - Tencent's 13B parameter model (CVPR 2025)
- **LTX Video** - First real-time video generation (24FPS, faster than playback!)
- **Mochi** - Genmo's 10B model with best text-to-video quality

🎨 **Next-Gen Image Models**
- **Flux.1** - Black Forest Labs' breakthrough models (Dev & Schnell)
- **Kolors** - Bilingual (Chinese/English) text-to-image excellence
- **Stable Diffusion 3.5** - Latest from Stability (Oct 2024)

🏗️ **3D Content Creation**
- **Trellis** - Unified 3D asset generation (Radiance Fields, Gaussians, Meshes)
- **DepthCrafter** - Consistent video depth estimation (CVPR 2025 Highlight)

---

## ⚡ Essential Setup

### Must Install First!

#### 1. ComfyUI Manager
**The single most important extension**
- https://github.com/Comfy-Org/ComfyUI-Manager
- Install, update, and manage all custom nodes
- Automatic dependency resolution
- Model browser and downloader

#### 2. Workspace Manager
**Organize your creative chaos**
- https://github.com/11cafe/comfyui-workspace-manager
- Version control for workflows (git-like)
- Manage workflows, models, and images
- Sync across devices

### Core Custom Nodes (Install These Next)

**Image Processing Essentials:**
- https://github.com/ltdrdata/ComfyUI-Impact-Pack - Face detailing, segmentation, regional prompting
- https://github.com/cubiq/ComfyUI_IPAdapter_plus - IPAdapter Plus with 37 specialized nodes
- https://github.com/cubiq/ComfyUI_essentials - Quality-of-life improvements and missing features

**Workflow Enhancement:**
- https://github.com/ltdrdata/was-node-suite-comfyui - WAS Node Suite (hundreds of essential nodes)
- https://github.com/jags111/efficiency-nodes-comfyui - Streamline your workflows
- https://github.com/pythongosssss/ComfyUI-Custom-Scripts - UI/UX improvements
- https://github.com/rgthree/rgthree-comfy - Power Prompt, Fast Groups, utilities

**ControlNet & Preprocessing:**
- https://github.com/Fannovel16/comfyui_controlnet_aux - 65+ ControlNet preprocessors
- https://github.com/florestefano1975/comfyui-portrait-master - Advanced portrait control

---

## 🎬 Video Generation

### State-of-the-Art Models (2024-2025)

#### HunyuanVideo (Tencent)
**Best for:** Professional video production
- https://github.com/kijai/ComfyUI-HunyuanVideoWrapper
- 13B parameters, DiT architecture
- 5-second videos, extendable
- **VRAM:** Runs on 8GB minimum
- **Status:** Native ComfyUI support (Dec 2024)

#### LTX Video (Lightricks)
**Best for:** Real-time generation
- https://github.com/Lightricks/ComfyUI-LTXVideo
- First real-time DiT video model
- 24FPS at 768x512, faster than playback
- Supports up to 60 seconds
- **Models:** Standard (13B) & Distilled (4-8 steps only)

#### Mochi (Genmo)
**Best for:** Text-to-video quality
- https://github.com/kijai/ComfyUI-MochiWrapper
- https://github.com/logtd/ComfyUI-MochiEdit - Video editing
- 10B parameters, best T2V quality
- **VRAM:** 20GB required

#### CogVideoX (Tsinghua University)
**Best for:** Image-to-video
- https://github.com/kijai/ComfyUI-CogVideoXWrapper
- Best I2V quality
- Chinese prompt optimization
- **VRAM:** 5-6GB sampling, 13-14GB VAE decode

### Video Tools & Utilities
- https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite - Essential video processing
- https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved - Advanced AnimateDiff features
- https://github.com/kijai/ComfyUI-LivePortraitKJ - Live portrait animation

---

## 🎭 Face & Portrait

### Face Swapping & Identity

#### PuLID (2024)
**Best for:** Lightning-fast consistent faces
- https://github.com/cubiq/PuLID_ComfyUI
- Tuning-free ID customization
- **PuLID Flux II** - No model pollution
- Generate in under 10 seconds
- **Comparison:** Most versatile, good balance

#### InstantID
**Best for:** Highest quality face swapping
- https://github.com/cubiq/ComfyUI_InstantID
- https://github.com/nosiu/comfyui-instantId-faceswap
- **Best Practice:** Combine with FaceDetailer + IP-Adapter
- Most resource-intensive but best results
- SDXL only

#### IPAdapter FaceID V2 (2024)
**Best for:** Integration flexibility
- https://github.com/cubiq/ComfyUI_IPAdapter_plus
- **Update:** Kolors FaceIDv2 added (Aug 2024)
- Weight parameter: -1 to 5.0
- Requires InsightFace + LoRA

### Face Enhancement
- https://github.com/ltdrdata/ComfyUI-Impact-Pack - FaceDetailer for automatic refinement
- https://github.com/Gourieff/comfyui-reactor-node - ReActor face swap
- https://github.com/facefusion/facefusion - FaceFusion standalone tool

---

## 🎨 Image Enhancement

### Background Removal

#### BiRefNet (2024)
**The new standard for background removal**
- https://github.com/ZhengPeng7/BiRefNet - Original (CAAI AIR'24)
- https://github.com/1038lab/ComfyUI-RMBG - Multi-model integration
- **Models:** General, HR (2048x2048), Lite, Portrait
- Best hair detail preservation
- Commercially usable

### Upscaling

#### SUPIR (2024)
**Professional-grade upscaling**
- https://github.com/kijai/ComfyUI-SUPIR
- Comparable to Magnific, Topaz
- 8GB VRAM capable
- Two models: SUPIR-v0Q (quality) & SUPIR-v0F (detail preservation)

#### AuraSR
**GAN-based enhancement**
- https://github.com/alexisrolland/AuraSR-ComfyUI
- GigaGAN architecture
- Supports RGBA transparency
- Sensitive to compression

### Relighting & Effects

#### IC-Light (2024)
**Professional lighting control**
- https://github.com/kijai/ComfyUI-IC-Light
- https://github.com/huchenlei/ComfyUI-IC-Light-Native
- Text & background-conditioned relighting
- Video relighting support
- V1: Commercial use | V2: Non-commercial

### Inpainting

#### PowerPaint V2 (2024)
**Advanced inpainting solution**
- https://github.com/nullquant/ComfyUI-BrushNet
- BrushNet + PowerPaint integration
- Object removal with SAM
- Any SD 1.5 → Inpainting model

#### ControlNet Union (2024)
**Unified control solution**

**For Flux:**
- https://github.com/XLabs-AI/x-flux-comfyui
- 7 control modes: canny, tile, depth, blur, pose, gray, low quality
- Native ComfyUI support

**For SDXL:**
- Includes ALL control types in one model
- Promax: +Tile Variation, Deblur, Super-resolution
- Massive storage savings

### Depth Estimation

#### DepthCrafter (CVPR 2025 Highlight)
- https://github.com/akatz-ai/ComfyUI-DepthCrafter-Nodes
- Consistent long depth sequences
- No optical flow/camera pose needed
- Non-commercial academic use

---

## 🏗️ 3D Generation

### Trellis (2024)
**Unified 3D Asset Generation**
- https://github.com/if-ai/ComfyUI-IF_Trellis
- https://github.com/smthemex/ComfyUI_TRELLIS
- **Output Formats:** Radiance Fields, 3D Gaussians, Meshes
- **Input:** Text or image prompts
- SLAT (Structured 3D Latents) representation
- Editable 3D assets
- **VRAM:** 8GB minimum

### 3D Processing Suite
- https://github.com/MrForExample/ComfyUI-3D-Pack - Comprehensive 3D processing (3DGS, NeRF)

### Research Models
- https://github.com/apple/ml-4m - Apple's 4M multimodal model
- https://4m.epfl.ch - Interactive demos

---

## 🔧 Workflow Tools

### Productivity & Organization

**Real-time Monitoring:**
- https://github.com/crystian/ComfyUI-Crystools - CPU, GPU, memory monitoring

**Workflow Optimization:**
- https://github.com/chrisgoringe/cg-use-everywhere - Use Everywhere nodes
- https://github.com/BadCafeCode/masquerade-nodes-comfyui - Advanced masking

**Prompting:**
- https://github.com/ZHO-ZHO-ZHO/ComfyUI-SDXL-Prompt-Styler - Pre-set styles library
- https://github.com/twri/sdxl_prompt_styler - Alternative templates
- https://github.com/pythongosssss/ComfyUI-WD14-Tagger - Image analysis → prompt suggestions

**Image Analysis:**
- https://github.com/SLAPaper/ComfyUI-Image-Selector - Advanced selection
- https://github.com/chflame163/ComfyUI_LayerStyle - Photoshop-like layers

---

## 📦 Model Support

### Latest Models (2024-2025)

#### Flux.1 (Black Forest Labs) - August 2024
**Native ComfyUI Support** - Built-in nodes: FluxGuidance, ModelSamplingFlux
- **Flux.1 Dev** - [Download](https://huggingface.co/black-forest-labs/FLUX.1-dev)
  - High-quality guidance-distilled model
- **Flux.1 Schnell** - [Download](https://huggingface.co/black-forest-labs/FLUX.1-schnell)
  - Fast "Turbo" model (4-8 steps)

**Extensions:**
- https://github.com/XLabs-AI/x-flux-comfyui - LoRA & ControlNet integration

#### Stable Diffusion 3 / 3.5 (Stability) - 2024
- **SD3 Medium** - [Download](https://huggingface.co/stabilityai/stable-diffusion-3-medium)
- **SD3.5 Large** (Oct 2024) - [Download](https://huggingface.co/stabilityai/stable-diffusion-3.5-large)
- **SD3.5 Medium** - [Download](https://huggingface.co/stabilityai/stable-diffusion-3.5-medium)

#### Kolors (Kuaishou) - July 2024
**Bilingual text-to-image excellence**
- https://github.com/Kwai-Kolors/Kolors
- https://github.com/MinusZoneAI/ComfyUI-Kolors-MZ
- Trained on billions of text-image pairs
- Chinese & English support

### Classic Models

<details>
<summary><b>SDXL Models (Click to expand)</b></summary>

| Model Name | Download Link |
|------------|---------------|
| SDXL Base | [Download](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors) |
| SDXL Refiner | [Download](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/resolve/main/sd_xl_refiner_1.0.safetensors) |
| DreamShaper Lightning XL | [Download](https://huggingface.co/Lykon/dreamshaper-xl-lightning/resolve/main/DreamShaperXL_Lightning.safetensors) |
| SDXL Turbo | [Download](https://huggingface.co/stabilityai/sdxl-turbo/resolve/main/sdxl-turbo.safetensors) |

</details>

<details>
<summary><b>SD 1.5 & SD 2.x Models (Click to expand)</b></summary>

| Model Name | Download Link |
|------------|---------------|
| SD v1.5 | [Download](https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.ckpt) |
| SD 2.1 Base (512) | [Download](https://huggingface.co/stabilityai/stable-diffusion-2-1-base/resolve/main/v2-1_512-ema-pruned.safetensors) |
| SD 2.1 (768) | [Download](https://huggingface.co/stabilityai/stable-diffusion-2-1/resolve/main/v2-1_768-ema-pruned.safetensors) |

</details>

### Specialized Integrations
- https://github.com/city96/ComfyUI_ExtraModels - Extra model format support
- https://github.com/Acly/krita-ai-diffusion - Krita integration
- https://krita.org - Krita (open-source digital painting)

---

## 🎓 Learning Resources

### Official Documentation
- https://docs.comfy.org/get_started/introduction - Official ComfyUI Docs (2024)
- https://blog.comfy.org - ComfyUI Official Blog
- https://github.com/comfyanonymous/ComfyUI_examples - Official example workflows
- https://github.com/Comfy-Org/workflow_templates - Built-in template workflows

### Workflow Collections

**Professional Workflows:**
- https://github.com/cubiq/ComfyUI_Workflows - Well-documented, educational workflows
- https://github.com/comfy-deploy/comfyui-workflows - Cloud & local compatible
- https://github.com/C0nsumption/Consume-ComfyUI-Workflows - Building block workflows

**Community Platforms:**
- https://openart.ai/workflows/academy - OpenArt Academy
- https://openart.ai/workflows/templates - Searchable templates
- https://comfyworkflows.com - Community workflow sharing
- https://www.runcomfy.com/comfyui-workflows - 200+ curated workflows

### Video Tutorials & Courses
- https://www.youtube.com/@OlivioSarikas/playlists - Olivio Sarikas (comprehensive)
- https://learn.thinkdiffusion.com - ThinkDiffusion platform
- https://fastcampus.com/en/products/data_online_comfyui - FastCampus Course ($215)

### Cloud Platforms
- https://www.comflowy.com - No setup, 100+ extensions pre-installed
- https://www.runcomfy.com - Pre-configured nodes & models

---

## ⭐ Top Community Resources

### Most Starred Repositories (2024)

**Top Workflow Collections:**
1. **ZHO-ZHO-ZHO/ComfyUI-Workflows-ZHO** (6.9k ⭐)
   - https://github.com/ZHO-ZHO-ZHO/ComfyUI-Workflows-ZHO
   - Comprehensive Chinese/English workflows
   - Regular updates with latest features

2. **ComfyUI-HunyuanVideoWrapper** (2.6k ⭐)
   - https://github.com/kijai/ComfyUI-HunyuanVideoWrapper
   - Latest video generation tech

3. **ComfyUI-AdvancedLivePortrait** (2.5k ⭐)
   - https://github.com/PowerHouseMan/ComfyUI-AdvancedLivePortrait
   - Advanced portrait animation

**Essential Reading:**
- https://github.com/liusida/top-100-comfyui - Auto-updated top 100 repos
- https://github.com/ComfyUI-Workflow/awesome-comfyui - Curated node collection

### Specialized Extensions

**Vision & Language Models:**
- https://github.com/spacepxl/ComfyUI-Florence-2 - Microsoft Florence-2
- https://github.com/kijai/ComfyUI-Florence2 - Alternative implementation
- https://github.com/if-ai/ComfyUI-IF_AI_tools - LLM integration
- https://github.com/gokayfem/ComfyUI_VLM_nodes - Vision Language Models

**Segmentation:**
- https://github.com/storyicon/comfyui_segment_anything - Segment Anything Model (SAM)
- https://github.com/DepthAnything/Depth-Anything-V2 - Depth Anything V2

**Utilities:**
- https://github.com/Acly/comfyui-tooling-nodes - Professional tooling
- https://github.com/Acly/comfyui-inpaint-nodes - Advanced inpainting
- https://github.com/BadCafeCode/apitools-comfyui - API integration

**Animation & Motion:**
- https://github.com/ArtVentureX/comfyui-animatediff - AnimateDiff
- https://github.com/Yujun-Shi/DragDiffusion - DragDiffusion
- https://github.com/TMElyralab/Comfyui-MusePose - MusePose
- https://github.com/tencent/MimicMotion - MimicMotion
- https://github.com/AIFSH/ComfyUI-Hallo - Hallo

**Other Tools:**
- https://github.com/spacepxl/ComfyUI-StyleGan - StyleGAN
- https://github.com/thanhluantrinh/LDDGAN - LDDGAN
- https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node - Blender integration
- https://github.com/Nuked88/ComfyUI-N-Sidebar - Enhanced sidebar
- https://github.com/vivax3794/ComfyUI-Sub-Nodes - Subnode functionality

---

## 🤝 Contributing

Contributions are welcome! If you know of amazing ComfyUI resources:

1. Fork this repository
2. Add your resource to the appropriate section
3. Include a brief description
4. Create a pull request

**Guidelines:**
- Must be ComfyUI-related
- Working links only
- Brief, clear descriptions
- Fits existing categories or propose new ones

---

## 📝 Important Notes

### Model Downloads
Some models require:
- Hugging Face account + license agreement
- Civitai account
- Sufficient disk space and VRAM

**Always check system requirements before downloading!**

### Commercial Use
Verify licensing before commercial use:
- ✅ Flux.1, Kolors, SDXL - Commercial friendly
- ✅ BiRefNet, IC-Light V1 - Commercial use allowed
- ⚠️ IC-Light V2, DepthCrafter - Non-commercial only
- ⚠️ Trellis, some research models - Check individual licenses

---

## 🔗 Other Awesome Resources

- [ComfyUI Official](https://github.com/comfyanonymous/ComfyUI) - The source
- [ComfyUI-Manager Registry](https://github.com/ltdrdata/ComfyUI-Manager) - Official registry
- [Awesome ComfyUI](https://github.com/lucianosb/awesome-comfyui) - Comprehensive list
- [ComfyUI Workflow Collection](https://github.com/ComfyUI-Workflow/awesome-comfyui) - Workflow-focused

---

## 💡 Quick Start Guide

**Never used ComfyUI?** Start here:

1. **Install:** Download [ComfyUI Desktop V1](https://www.comfy.org/download)
2. **Manager:** Install ComfyUI Manager (essential!)
3. **Learn:** Watch [Olivio Sarikas tutorials](https://www.youtube.com/@OlivioSarikas)
4. **Practice:** Try [official example workflows](https://github.com/comfyanonymous/ComfyUI_examples)
5. **Explore:** Browse [OpenArt templates](https://openart.ai/workflows/templates)

---

## ⭐ Star History

If this repository helped you, please star it! It helps others discover these resources.

---

**This is a living document.** ComfyUI evolves rapidly - this list is continuously updated with cutting-edge developments.

**Questions?** Open an issue or contribute your findings!

