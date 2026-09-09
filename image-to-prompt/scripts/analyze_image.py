#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utilitário de análise de imagem e extração de atributos visuais para a Skill 'image-to-prompt'.
Lê dimensões, proporção, paleta de cores dominante, metadados EXIF e formata informações técnicas.
"""

import sys
import os
import base64
import json
from pathlib import Path

# Garantir UTF-8 nas saídas de console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

try:
    from PIL import Image, ImageStat
except ImportError:
    print("❌ Erro: Biblioteca 'Pillow' não encontrada. Execute 'pip install Pillow'.")
    sys.exit(1)

def get_aspect_ratio_label(width, height):
    ratio = width / height
    if abs(ratio - 1.0) < 0.05:
        return "1:1 (Quadrado / Square)"
    elif abs(ratio - (16 / 9)) < 0.08:
        return "16:9 (Widescreen Paisagem / Landscape)"
    elif abs(ratio - (9 / 16)) < 0.08:
        return "9:16 (Vertical Story / Portrait)"
    elif abs(ratio - (4 / 3)) < 0.08:
        return "4:3 (Fotografia Padrão / Standard Photo)"
    elif abs(ratio - (3 / 4)) < 0.08:
        return "3:4 (Retrato / Portrait)"
    elif abs(ratio - (21 / 9)) < 0.1:
        return "21:9 (Cinematográfico Ultrawide / Anamorphic)"
    elif ratio > 1:
        return f"{ratio:.2f}:1 (Paisagem / Landscape)"
    else:
        return f"1:{1/ratio:.2f} (Retrato / Portrait)"

def analyze_image(image_path: str, output_json: bool = False):
    img_path = Path(image_path).resolve()
    if not img_path.exists():
        print(f"❌ Erro: Imagem não encontrada em '{img_path}'")
        return False

    try:
        with Image.open(img_path) as img:
            width, height = img.size
            format_name = img.format or "Desconhecido"
            mode = img.mode
            aspect_label = get_aspect_ratio_label(width, height)
            
            # Análise de luminosidade e estatísticas de cor
            stat = ImageStat.Stat(img.convert('RGB'))
            mean_brightness = sum(stat.mean) / 3.0
            lighting_mood = "Clara / Alta exposição (High Key)" if mean_brightness > 170 else ("Escura / Sombria (Low Key / Chiaroscuro)" if mean_brightness < 85 else "Equilibrada (Balanced Natural)")
            
            # Cores dominantes simplificadas
            small_img = img.convert('RGB').resize((1, 1), Image.Resampling.LANCZOS)
            dom_r, dom_g, dom_b = small_img.getpixel((0, 0))
            hex_color = f"#{dom_r:02x}{dom_g:02x}{dom_b:02x}"
            
            # Codificação Base64 para interoperabilidade com APIs Vision
            with open(img_path, "rb") as f:
                b64_data = base64.b64encode(f.read()).decode('utf-8')
            mime_type = f"image/{format_name.lower()}" if format_name != "JPEG" else "image/jpeg"

            data = {
                "file_name": img_path.name,
                "file_path": str(img_path),
                "dimensions": {"width": width, "height": height},
                "aspect_ratio": aspect_label,
                "color_mode": mode,
                "format": format_name,
                "lighting_mood": lighting_mood,
                "dominant_tint_hex": hex_color,
                "base64_uri": f"data:{mime_type};base64,{b64_data[:60]}...[TRUNCATED]",
                "instructions_for_ai": "Utilize os dados técnicos e a análise visual do modelo para gerar o prompt descritivo detalhado em EN e PT-BR."
            }

            if output_json:
                print(json.dumps(data, indent=2, ensure_ascii=False))
            else:
                print("=========================================================")
                print(f"🎨 Análise Técnica da Imagem: {img_path.name}")
                print("=========================================================")
                print(f"📐 Dimensões       : {width} x {height} px")
                print(f"🖼️ Proporção (AR)  : {aspect_label}")
                print(f"💡 Iluminação Base : {lighting_mood} (Média: {mean_brightness:.1f}/255)")
                print(f"🎨 Tom Médio (Hex) : {hex_color} (RGB: {dom_r}, {dom_g}, {dom_b})")
                print(f"📄 Formato         : {format_name} ({mode})")
                print("=========================================================")
                print("\n💡 Pronto para análise visual e engenharia reversa de prompt pelo Agente de IA.")
                
            return True
    except Exception as e:
        print(f"❌ Erro ao processar a imagem: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python analyze_image.py <caminho_da_imagem> [--json]")
        sys.exit(1)
        
    path_arg = sys.argv[1]
    is_json = "--json" in sys.argv
    analyze_image(path_arg, is_json)
