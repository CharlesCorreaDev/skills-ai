---
name: image-to-prompt
description: Reverse-engineers any input image into highly detailed, photorealistic, or artistic generative text prompts in both English and Portuguese (PT-BR). Deconstructs art style, stroke techniques, era/epoch, clothing, fabrics, color palettes, camera lenses, lighting, facial physiognomy, micro-expressions, hairstyles, background depth, and negative prompts for image/video generative AI models (Sora, Nano Banana, Midjourney, DALL-E 3, SDXL, Flux, Imagen 3, ComfyUI). Use when the user wants to analyze an image and generate a reproduction prompt via Antigravity, Claude Code, Copilot CLI, Hermes Agent, Orca, Gemini, Kilo, NVIDIA, or Ollama.
---

# Image to Prompt 🖼️➡️✍️

---

## 🇺🇸 English

### 📌 Overview & Mental Model
**Image to Prompt** is an advanced reverse-engineering skill for AI coding agents and vision models. It analyzes any uploaded or local image file and produces comprehensive, high-fidelity generative prompts formatted for state-of-the-art AI image and video generators (such as **Sora, Nano Banana, Midjourney v6, DALL-E 3, Stable Diffusion / SDXL, Flux, Google Imagen 3, and ComfyUI**).

Rather than producing a brief description, the skill extracts the complete artistic, physical, and photographic DNA of the image across 9 granular dimensions:

1. **Art Style & Medium:** Digital painting, oil on canvas, 3D Octane / Unreal Engine 5 render, cinematic 35mm analog photograph, anime cel-shaded, watercolor, concept art.
2. **Era & Aesthetic:** Victorian gothic, 1980s retro synthwave, Cyberpunk 2077, medieval fantasy, solarpunk, contemporary hyperrealism.
3. **Subject & Facial Physiognomy:** Facial structure, skin texture, ethnicity, eye color, micro-expressions, gaze direction, emotional tone.
4. **Hair & Grooming:** Hair cut, texture, color gradients, individual flyaway strands, styling, facial hair.
5. **Clothing, Textures & Accessories:** Garment types, fabric materials (distressed leather, velvet, silk, cyberware, tactical armor), embroidery, jewelry.
6. **Lighting & Atmosphere:** Volumetric god rays, golden hour, chiaroscuro shadow contrast, neon rim lighting, subsurface scattering.
7. **Camera Angle & Lens Optics:** Focal length (e.g., 85mm f/1.4 portrait, 24mm wide angle), Dutch angle, close-up framing, depth of field, optical bokeh.
8. **Background & Environment:** Atmospheric particles, dust, rain, fog, foreground elements, background architectural/natural setting.
9. **Parameters & Negative Prompt:** Aspect ratio (`--ar 16:9`, `--ar 1:1`), stylized flags, and negative prompts (artifacts, extra fingers, text blur, overexposure).

---

### 📋 Standard Output Template for the Agent

When activated on an image, the AI agent must output:

```markdown
### 🎨 Reverse-Engineered Prompt / Prompt de Engenharia Reversa

#### 🇺🇸 English Prompt (Optimized for Midjourney / SDXL / Flux / Sora / Nano Banana)
> [Complete detailed descriptive prompt in English covering subject, artistic medium, clothing, lighting, camera specs, environment, and quality parameters]

#### 🇧🇷 Prompt em Português (Brasil) (Otimizado para Modelos Multilíngues / DALL-E 3)
> [Prompt descritivo completo em português cobrindo sujeito, traços artísticos, vestimentas, iluminação, especificações de câmera, cenário e parâmetros de qualidade]

#### 🔍 Technical Breakdown / Decomposição dos Elementos
- **Estilo & Técnica / Style & Medium:** ...
- **Época & Estética / Era & Vibe:** ...
- **Fisionomia & Expressão / Physiognomy & Expression:** ...
- **Penteado / Hairstyle:** ...
- **Vestuário & Acessórios / Clothing & Accessories:** ...
- **Iluminação & Cores / Lighting & Palette:** ...
- **Câmera & Enquadramento / Camera & Framing:** ...
- **Plano de Fundo / Background Environment:** ...
- **Negative Prompt (O que evitar):** `deformed, blurry, extra limbs, bad anatomy, mutated hands, low resolution, watermark, noise`
```

---

### 🛠️ CLI Usage
```bash
# Check environment
python scripts/check_env.py

# Technical image metadata & aspect ratio inspection
python scripts/analyze_image.py "path/to/image.png"

# Output metadata in JSON format
python scripts/analyze_image.py "path/to/image.jpg" --json
```

---

### 🛡️ Autonomous Error Recovery & Self-Healing Protocol (For AI Agents)

When an AI Agent encounters errors during skill installation, execution, or environment setup:
1. **Root Cause Diagnosis & Self-Correction:** The agent MUST analyze the underlying cause of failure (missing packages, permissions, OS binary gaps, charset issues) and iteratively attempt self-correction until the skill performs its intended purpose.
2. **Permission Gate for Extra / System Software:** If resolving an issue requires installing system binaries (`pandoc`, `libreoffice`, `tesseract`), elevated global packages, or configuring API keys, the agent MUST explicitly explain the situation to the developer/operator and request authorization before proceeding.
3. **Configuration Report & Verification:** Upon approval, the agent must clearly state what was installed and configured, then immediately execute an end-to-end test or ask the operator for sample inputs to validate that the skill is 100% operational.

---

## 🇧🇷 Português (Brasil)

### 📌 Visão Geral & Modelo Mental
A skill **Image to Prompt** é um motor avançado de engenharia reversa visual para Agentes de IA e modelos de visão computacional. Ela analisa qualquer arquivo de imagem local ou enviado pelo usuário e gera prompts de texto ultra-detalhados e fiéis, formatados para os principais geradores de imagens e vídeos do mercado (**Sora, Nano Banana, Midjourney v6, DALL-E 3, Stable Diffusion / SDXL, Flux, Google Imagen 3 e ComfyUI**).

Em vez de produzir apenas uma legenda superficial, a skill decompõe o DNA visual completo da imagem em 9 dimensões detalhadas:

1. **Estilo Artístico & Meio:** Pintura digital, óleo sobre tela, render 3D em Octane / Unreal Engine 5, foto analógica 35mm, anime cel-shaded, aquarela, concept art.
2. **Época & Estética:** Gótico vitoriano, anos 80 synthwave retrô, Cyberpunk 2077, fantasia medieval, solarpunk, fotorrealismo contemporâneo.
3. **Fisionomia & Expressão:** Estrutura facial, textura de pele, etnia, cor dos olhos, micro-expressões, olhar e emoção transmitida.
4. **Penteado & Cabelo:** Corte, textura, gradientes de cor, fios soltos ao vento, barba/estilização.
5. **Vestuário, Tecidos & Acessórios:** Tipo de roupa, materiais (couro desgastado, seda, veludo, implantes cibernéticos, armaduras táticas), costuras e joias.
6. **Iluminação & Atmosfera:** Raios volumétricos (god rays), luz dourada (golden hour), contraste claro-escuro (chiaroscuro), luz de contorno neon, dispersão subsuperficial (subsurface scattering).
7. **Câmera & Óptica:** Distância focal (ex: lente 85mm f/1.4 para retratos, 24mm grande-angular), ângulo holandês, plano fechado/médio, desfoque de fundo (bokeh).
8. **Plano de Fundo & Cenário:** Partículas no ar, chuva, neblina, poeira suspensa, composição em camadas de primeiro plano e fundo.
9. **Parâmetros & Negative Prompt:** Aspect ratio (`--ar 16:9`, `--ar 1:1`), tags de estilo e termos negativos para evitar artefatos e anomalias.

---

### 🛠️ Uso via CLI
```bash
# Verificar ambiente
python scripts/check_env.py

# Analisar metadados e aspectos técnicos da imagem
python scripts/analyze_image.py "caminho/para/imagem.png"

# Obter resposta técnica estruturada em JSON
python scripts/analyze_image.py "caminho/para/imagem.jpg" --json
```

---

### 🛡️ Protocolo de Auto-Correção e Recuperação de Erros (Para Agentes de IA)

Sempre que o Agente de IA encontrar falhas na instalação, execução ou configuração de ambiente da skill:
1. **Diagnóstico de Causa Raiz e Auto-Correção:** O agente DEVE analisar a causa exata do erro (dependências ausentes, permissões, ferramentas de SO, encoding de caracteres) e tentar se auto-corrigir iterativamente até que a skill esteja funcionando perfeitamente conforme seu propósito.
2. **Solicitação de Permissão para Instalações Extras:** Se a correção exigir a instalação de binários de sistema (`pandoc`, `libreoffice`, `tesseract`), pacotes globais ou configuração de chaves de API, o agente DEVE explicar o diagnóstico com clareza e solicitar a permissão explícita do desenvolvedor/operador antes de instalar.
3. **Relatório de Configuração e Validação:** Após a confirmação, o agente deve informar detalhadamente o que foi instalado e configurado para resolver o problema e executar imediatamente um teste de validação (ou solicitar ao operador os dados/arquivos necessários para testar a skill).
