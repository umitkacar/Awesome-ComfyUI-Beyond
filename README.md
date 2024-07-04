# awesome-comfyui-beyond
Stable Diffusion - ComfyUI

## Stable Diffusion Models

This repository provides download links for various Stable Diffusion models, categorized for ease of access. Below is a table that categorizes models into SDXL, SD1.5, SD2, Anime Styles, unCLIP, VAE, Loras, T2I-Adapter, ControlNet, GLIGEN, and ESRGAN upscale models.

## Models Table

| Category           | Model Name                      | Download Link                                                                                                      |
|--------------------|---------------------------------|--------------------------------------------------------------------------------------------------------------------|
| **SDXL**           | SDXL Base Model                 | [Download](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors)|
|                    | SDXL Refiner Model              | [Download](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/resolve/main/sd_xl_refiner_1.0.safetensors)|
|                    | SDXL VAE File                   | [Download](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors)|
|                    | SDXL Turbo Model                | [Download](https://huggingface.co/stabilityai/sdxl-turbo/resolve/main/sdxl-turbo.safetensors)                        |
| **SD1.5**          | Stable Diffusion v1.5           | [Download](https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.ckpt)             |
| **SD2**            | SD 2.1 Base Model (512)         | [Download](https://huggingface.co/stabilityai/stable-diffusion-2-1-base/resolve/main/v2-1_512-ema-pruned.safetensors)|
|                    | SD 2.1 Model (768)              | [Download](https://huggingface.co/stabilityai/stable-diffusion-2-1/resolve/main/v2-1_768-ema-pruned.safetensors)    |
| **Anime Styles**   | Abyss Orange Mix 2 (Hard)       | [Download](https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix2/AbyssOrangeMix2_hard.safetensors)|
|                    | Abyss Orange Mix 3 (A1)         | [Download](https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix3/AOM3A1_orangemixs.safetensors)|
|                    | Anything v3                     | [Download](https://huggingface.co/Linaqruf/anything-v3.0/resolve/main/anything-v3-fp16-pruned.safetensors)         |
|                    | Waifu Diffusion 1.5             | [Download](https://huggingface.co/waifu-diffusion/wd-1-5-beta3/resolve/main/wd-illusion-fp16.safetensors)           |
| **unCLIP Models**  | Illuminati Diffusion V1         | [Download](https://huggingface.co/comfyanonymous/illuminatiDiffusionV1_v11_unCLIP/resolve/main/illuminatiDiffusionV1_v11-unclip-h-fp16.safetensors)|
|                    | WD 1.5 Beta 2                   | [Download](https://huggingface.co/comfyanonymous/wd-1.5-beta2_unCLIP/resolve/main/wd-1-5-beta2-aesthetic-unclip-h-fp16.safetensors)|
| **VAE**            | VAE File (MSE)                  | [Download](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors)|
|                    | Orange Mix VAE                  | [Download](https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/VAEs/orangemix.vae.pt)                     |
|                    | Waifu Diffusion VAE             | [Download](https://huggingface.co/hakurei/waifu-diffusion-v1-4/resolve/main/vae/kl-f8-anime2.ckpt)                  |
| **Loras**          | The Overcomer 8's Contrast Fix (SD2.x 768-v) | [Download](https://civitai.com/api/download/models/10350 -O ./models/loras/theovercomer8sContrastFix_sd21768.safetensors) |
|                    | The Overcomer 8's Contrast Fix (SD1.x)       | [Download](https://civitai.com/api/download/models/10638 -O ./models/loras/theovercomer8sContrastFix_sd15.safetensors)   |
|                    | SDXL Offset Noise Lora          | [Download](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_offset_example-lora_1.0.safetensors)|
| **T2I-Adapter**    | Depth SD14v1                    | [Download](https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models/t2iadapter_depth_sd14v1.pth)           |
|                    | Seg SD14v1                      | [Download](https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models/t2iadapter_seg_sd14v1.pth)             |
|                    | Sketch SD14v1                   | [Download](https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models/t2iadapter_sketch_sd14v1.pth)          |
|                    | Keypose SD14v1                  | [Download](https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models/t2iadapter_keypose_sd14v1.pth)         |
|                    | Openpose SD14v1                 | [Download](https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models/t2iadapter_openpose_sd14v1.pth)        |
|                    | Color SD14v1                    | [Download](https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models/t2iadapter_color_sd14v1.pth)           |
|                    | Canny SD14v1                    | [Download](https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models/t2iadapter_canny_sd14v1.pth)           |
|                    | Style SD14v1                    | [Download](https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models/t2iadapter_style_sd14v1.pth)           |                                                                |
| **ControlNet**     | ControlNet SD15 IP2P            | [Download](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11e_sd15_ip2p_fp16.safetensors)|
|                    | ControlNet SD15 Shuffle         | [Download](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11e_sd15_shuffle_fp16.safetensors)|
|                    | ControlNet SD15 Canny           | [Download](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_canny_fp16.safetensors)|
|                    | ControlNet SD15 Depth           | [Download](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11f1p_sd15_depth_fp16.safetensors)|
|                    | ControlNet SD15 Inpaint         | [Download](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_inpaint_fp16.safetensors)|
|                    | ControlNet SD15 Lineart         | [Download](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_lineart_fp16.safetensors)|
|                    | ControlNet SD15 MLSD            | [Download](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_mlsd_fp16.safetensors)|
|                    | ControlNet SD15 Normalbae       | [Download](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_normalbae_fp16.safetensors)|
|                    | ControlNet SD15 Openpose        | [Download](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_openpose_fp16.safetensors)|
|                    | ControlNet SD15 Scribble        | [Download](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_scribble_fp16.safetensors)|
|                    | ControlNet SD15 Seg             | [Download](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_seg_fp16.safetensors)|
|                    | ControlNet SD15 Softedge        | [Download](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_softedge_fp16.safetensors)|
|                    | ControlNet SD15 Lineart Anime   | [Download](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15s2_lineart_anime_fp16.safetensors)|
|                    | ControlNet SD15 Tile            | [Download](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11u_sd15_tile_fp16.safetensors)|
| **ControlNet SDXL**| ControlNet SDXL Canny           | [Download](https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-canny-rank256.safetensors)|
|                    | ControlNet SDXL Depth           | [Download](https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-depth-rank256.safetensors)|
|                    | ControlNet SDXL Recolor         | [Download](https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-recolor-rank256.safetensors)|
|                    | ControlNet SDXL Sketch          | [Download](https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-sketch-rank256.safetensors)|
| **ControlNet Preprocessor Nodes** | Fannovel16 ControlNet Preprocessors | [Download](https://github.com/Fannovel16/comfy_controlnet_preprocessors) |
| **GLIGEN**         | GLIGEN Text-Image Model         | [Download](https://huggingface.co/gligen/gligen-text-image/resolve/main/gligen-text-image.safetensors)             |
|                    | GLIGEN Object Detection Model   | [Download](https://huggingface.co/gligen/gligen-object-detection/resolve/main/gligen-object-detection.safetensors) |
| **ESRGAN**         | ESRGAN 4x Upscale               | [Download](https://huggingface.co/esrgan/4x-upscale/resolve/main/4x-upscale.safetensors)                           |
|                    | ESRGAN 8x Upscale               | [Download](https://huggingface.co/esrgan/8x-upscale/resolve/main/8x-upscale.safetensors)                           |
| **Miscellaneous**  | Stable Diffusion ReV Animation  | [Download](https://huggingface.co/rev/animation/resolve/main/rev-animation.safetensors)                            |
|                    | DreamBooth Custom Model         | [Download](https://huggingface.co/dreambooth/custom-model/resolve/main/dreambooth-custom-model.safetensors)        |


| Category           | Model Name                      | Download Link                                                                                                      |
|--------------------|---------------------------------|--------------------------------------------------------------------------------------------------------------------|
| **SDXL**           | DreamShaper Lightning XL        | [Download](https://huggingface.co/Lykon/dreamshaper-xl-lightning/resolve/main/dreamshaper-xl-lightning.safetensors)|
|                    | Juggernaut XL                   | [Download](https://civitai.com/models/133005?modelVersionId=357609/resolve/main/juggernaut-xl.safetensors)        |
|                    | BonoboXL                        | [Download](https://civitai.com/models/209846?modelVersionId=361788/resolve/main/bonoboxl.safetensors)              |
|                    | Pony Diffusion                  | [Download](https://civitai.com/models/257749/pony-diffusion-v6-xl/resolve/main/pony-diffusion-v6-xl.safetensors)  |
|                    | ReV Animated                    | [Download](https://civitai.com/models/116456/rev-animated/resolve/main/rev-animated.safetensors)                   |
|                    | CyberRealistic                  | [Download](https://civitai.com/models/117654/cyberrealistic/resolve/main/cyberrealistic.safetensors)               |
|                    | DucHaiten-AIart-SDXL            | [Download](https://civitai.com/models/128456/duchaiten-aiart-sdxl/resolve/main/duchaiten-aiart-sdxl.safetensors)   |
|                    | RealCartoon3D                   | [Download](https://civitai.com/models/136789/realcartoon3d/resolve/main/realcartoon3d.safetensors)                 |
|                    | Absolute Reality                | [Download](https://civitai.com/models/120789/absolute-reality/resolve/main/absolute-reality.safetensors)           |
|                    | majicMIX Realistic              | [Download](https://civitai.com/models/112345/majicmix-realistic/resolve/main/majicmix-realistic.safetensors)       |
|                    | Cheese Daddy’s Landscape Mix    | [Download](https://civitai.com/models/143567/cheese-daddys-landscape-mix/resolve/main/cheese-daddys-landscape-mix.safetensors)|
|                    | Monster Diffusion SDXL          | [Download](https://civitai.com/models/149876/monster-diffusion-sdxl/resolve/main/monster-diffusion-sdxl.safetensors)|
| **Anime Styles**   | Kenshi                          | [Download](https://civitai.com/models/150123/kenshi/resolve/main/kenshi.safetensors)                               |
|                    | Flat-2D Animerge                | [Download](https://civitai.com/models/156789/flat-2d-animerge/resolve/main/flat-2d-animerge.safetensors)           |
|                    | Counterfeit-V2.5                | [Download](https://civitai.com/models/160345/counterfeit-v2-5/resolve/main/counterfeit-v2-5.safetensors)           |
|                    | GhostMix                        | [Download](https://civitai.com/models/170234/ghostmix/resolve/main/ghostmix.safetensors)                           |
|                    | Protogen                        | [Download](https://civitai.com/models/178901/protogen/resolve/main/protogen.safetensors)                           |
| **Specialized Themes** | epiCRealism                | [Download](https://civitai.com/models/185678/epicrealism/resolve/main/epicrealism.safetensors)                     |
|                    | XSarchitectural                 | [Download](https://civitai.com/models/192345/xsarchitectural/resolve/main/xsarchitectural.safetensors)             |
|                    | Elldreths Retro Mix             | [Download](https://civitai.com/models/198901/elldreths-retro-mix/resolve/main/elldreths-retro-mix.safetensors)     |
|                    | Modelshoot                      | [Download](https://civitai.com/models/204567/modelshoot/resolve/main/modelshoot.safetensors)                       |
| **Versatile and Creative** | NeverEnding Dream      | [Download](https://civitai.com/models/210789/neverending-dream/resolve/main/neverending-dream.safetensors)         |
|                    | Anything V3                     | [Download](https://civitai.com/models/220345/anything-v3/resolve/main/anything-v3.safetensors)                     |
|                    | MeinaMix                        | [Download](https://civitai.com/models/230123/meinamix/resolve/main/meinamix.safetensors)                           |
|                    | AbyssOrangeMix3 (AOM3)          | [Download](https://civitai.com/models/240567/abyssorangemix3/resolve/main/abyssorangemix3.safetensors)             |
|                    | OpenJourney                     | [Download](https://civitai.com/models/250789/openjourney/resolve/main/openjourney.safetensors)                     |
|                    | Henmix_Real                     | [Download](https://civitai.com/models/260345/henmix-real/resolve/main/henmix-real.safetensors)   

## AWESOME
https://github.com/lucianosb/awesome-comfyui

## PROJECTS
- https://github.com/comfyanonymous/ComfyUI
- https://github.com/Nuked88/ComfyUI-N-Sidebar
- https://github.com/AIFSH/ComfyUI-Hallo
- https://github.com/TMElyralab/Comfyui-MusePose
- https://github.com/ArtVentureX/comfyui-animatediff
- https://github.com/Yujun-Shi/DragDiffusion

## WEB
- https://learn.thinkdiffusion.com/
- https://learn.thinkdiffusion.com/how-to-create-stunning-ai-videos-with-comfyui-rave-and-animatediff/

## LEARNING
- https://comfyanonymous.github.io/ComfyUI_tutorial_vn/
- https://docs.comfy.org/get_started/introduction

## APPLE
- https://github.com/apple/ml-4m/
- https://4m.epfl.ch/

## FACE
- https://github.com/facefusion/facefusion

## DEPTH
- https://depth-anything-v2.github.io/
- https://github.com/DepthAnything/Depth-Anything-V2

## GANs
- https://github.com/thanhluantrinh/LDDGAN
