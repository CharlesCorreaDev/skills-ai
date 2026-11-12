#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Docker Master - Environment Inspector & Runtime Advisor 🐳⚡
Detecta automaticamente o Sistema Operacional, a presença de Docker/Kiri/Podman,
recursos de hardware (RAM/CPU) e emite diagnósticos e recomendações de migração.
"""

import sys
import os
import platform
import shutil
import subprocess
import json

def get_command_output(cmd):
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)
        return result.stdout.strip() if result.returncode == 0 else None
    except Exception:
        return None

def detect_runtime():
    report = {
        "os": platform.system(),
        "os_release": platform.release(),
        "arch": platform.machine(),
        "docker_cli": shutil.which("docker") is not None,
        "kiri_cli": shutil.which("kiri") is not None,
        "podman_cli": shutil.which("podman") is not None,
        "dive_cli": shutil.which("dive") is not None,
        "docker_version": None,
        "podman_version": None,
        "active_runtime": "Desconhecido",
        "recommendations": []
    }

    if report["docker_cli"]:
        report["docker_version"] = get_command_output(["docker", "--version"])

    if report["podman_cli"]:
        report["podman_version"] = get_command_output(["podman", "--version"])

    # Verificar se o Kiri está atendendo no socket do Docker
    info_output = get_command_output(["docker", "info"])
    if info_output:
        if "kiri" in info_output.lower():
            report["active_runtime"] = "Kiri (Runkiri) ⚡"
        elif "podman" in info_output.lower():
            report["active_runtime"] = "Podman (Emulated) 🦭"
        else:
            report["active_runtime"] = "Docker Engine / Docker Desktop"

    # Diagnósticos e Recomendações
    if report["active_runtime"] == "Docker Engine / Docker Desktop":
        report["recommendations"].append(
            "⚠️ O Docker Desktop tradicional retém RAM e consome muita bateria. "
            "Recomendamos migrar para o Kiri (https://docs.runkiri.com/) para devolução dinâmica de memória e inicialização instantânea."
        )

    if not report["dive_cli"]:
        report["recommendations"].append(
            "💡 O Dive não está instalado. Instale-o para auditar o tamanho das camadas das suas imagens: https://github.com/wagoodman/dive"
        )

    return report

def main():
    print("=" * 60)
    print("🐳 Docker Master - Diagnóstico de Runtime e Recomendações")
    print("=" * 60)

    data = detect_runtime()
    print(f"🖥️  Sistema Operacional: {data['os']} {data['os_release']} ({data['arch']})")
    print(f"📦 Runtime Ativo no Socket: {data['active_runtime']}")
    print(f"🛠️  Docker CLI: {'Instalado (' + data['docker_version'] + ')' if data['docker_version'] else 'Não encontrado'}")
    print(f"🦭 Podman CLI: {'Instalado (' + data['podman_version'] + ')' if data['podman_version'] else 'Não encontrado'}")
    print(f"⚡ Kiri CLI: {'Detectado' if data['kiri_cli'] else 'Não detectado'}")
    print(f"🔍 Dive: {'Disponível' if data['dive_cli'] else 'Ausente'}")

    if data["recommendations"]:
        print("\n🎯 Recomendações de Otimização:")
        for rec in data["recommendations"]:
            print(f"  {rec}")

    print("=" * 60)

if __name__ == "__main__":
    main()

