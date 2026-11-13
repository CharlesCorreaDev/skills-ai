#!/usr/bin/env python3
"""
Code Mode Diagnostics
Checks Node.js, Python, uv and sandbox runtimes available on the host machine.
"""

import sys
import shutil
import subprocess

def check_command(cmd, name):
    path = shutil.which(cmd)
    if path:
        try:
            ver = subprocess.run([cmd, "--version"], capture_output=True, text=True, timeout=5)
            version_str = ver.stdout.strip() or ver.stderr.strip()
            print(f"✅ [OK] {name}: {version_str} ({path})")
            return True
        except Exception:
            print(f"✅ [OK] {name}: Found at {path}")
            return True
    else:
        print(f"⚠️ [NOT FOUND] {name} is not on system PATH.")
        return False

def main():
    print("=" * 65)
    print("  ⚡ CODE MODE BUILDER — RUNTIME DIAGNOSTICS")
    print("=" * 65)
    print("\n🔍 Checking Language Runtimes & Package Managers:")
    
    node_ok = check_command("node", "Node.js (V8 Runtime)")
    py_ok = check_command("python", "Python 3")
    uv_ok = check_command("uv", "Astral uv")
    cargo_ok = check_command("cargo", "Rust Cargo")
    docker_ok = check_command("docker", "Docker Engine (Container Isolation)")
    
    print("\n📦 Verdict / Veredito:")
    if node_ok or py_ok:
        print("🎉 [READY] O ambiente possui os requisitos mínimos para executar Code Mode.")
    else:
        print("❌ [INCOMPLETE] Instale Node.js ou Python para habilitar sandboxes de Code Mode.")

if __name__ == "__main__":
    main()
