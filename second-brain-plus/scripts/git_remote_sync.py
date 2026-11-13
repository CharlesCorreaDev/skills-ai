#!/usr/bin/env python3
"""
git_remote_sync.py - GitHub CLI (gh) & GitLab CLI (glab) Remote Integration Engine
Motor de Integração e Sincronização Remota com GitHub CLI (gh) e GitLab CLI (glab).

Features:
- CLI discovery & authentication audit (gh auth status, glab auth status).
- Git remote analysis (git remote -v, ahead/behind status, uncommitted changes).
- Visibility audit (Private vs Public repositories).
- Automated repo creation & linking (gh repo create, glab repo create).
- Proactive diagnostics ("precisa de algo a mais?"): .gitignore protection, branch sync, CI automation.

Bilingual support: English (EN) and Portuguese (PT-BR).
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def run_cmd(command: list[str]) -> tuple[int, str, str]:
    """Execute command safely and return (returncode, stdout, stderr)."""
    try:
        proc = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace"
        )
        return proc.returncode, proc.stdout.strip(), proc.stderr.strip()
    except Exception as e:
        return 1, "", str(e)

class GitRemoteManager:
    def __init__(self, repo_dir: Path | None = None):
        self.repo_dir = repo_dir or Path.cwd()
        self.gh_installed = shutil.which("gh") is not None
        self.glab_installed = shutil.which("glab") is not None

    def check_gh_auth(self) -> dict:
        """Check GitHub CLI status."""
        if not self.gh_installed:
            return {"installed": False, "authenticated": False, "account": None, "details": "gh CLI not found on PATH."}
        
        code, out, err = run_cmd(["gh", "auth", "status"])
        full_text = f"{out}\n{err}"
        is_auth = (code == 0) or ("Logged in to" in full_text)
        
        account = None
        for line in full_text.splitlines():
            if "Logged in to" in line and "account" in line:
                account = line.split("account")[-1].strip().split()[0]
                break

        return {
            "installed": True,
            "authenticated": is_auth,
            "account": account,
            "details": full_text.strip()
        }

    def check_glab_auth(self) -> dict:
        """Check GitLab CLI status."""
        if not self.glab_installed:
            return {"installed": False, "authenticated": False, "account": None, "details": "glab CLI not found on PATH."}
        
        code, out, err = run_cmd(["glab", "auth", "status"])
        full_text = f"{out}\n{err}"
        is_auth = (code == 0) or ("Logged in to" in full_text)

        account = None
        for line in full_text.splitlines():
            if "Logged in to" in line:
                account = line.split("as")[-1].strip() if "as" in line else line.strip()
                break

        return {
            "installed": True,
            "authenticated": is_auth,
            "account": account,
            "details": full_text.strip()
        }

    def get_git_remotes(self) -> dict[str, str]:
        """Fetch all git remotes."""
        code, out, _ = run_cmd(["git", "remote", "-v"])
        if code != 0 or not out:
            return {}
        
        remotes = {}
        for line in out.splitlines():
            parts = line.split()
            if len(parts) >= 2:
                name, url = parts[0], parts[1]
                remotes[name] = url
        return remotes

    def audit(self) -> dict:
        """Perform full audit of git remote integration and security status."""
        remotes = self.get_git_remotes()
        gh_info = self.check_gh_auth()
        glab_info = self.check_glab_auth()

        # Check git branch and ahead/behind
        code_branch, current_branch, _ = run_cmd(["git", "branch", "--show-current"])
        current_branch = current_branch if code_branch == 0 else "main"

        # Check uncommitted files
        _, status_out, _ = run_cmd(["git", "status", "--porcelain"])
        uncommitted_count = len([l for l in status_out.splitlines() if l.strip()])

        # Remote visibility and details via gh
        remote_type = "None"
        is_private = None
        repo_name = None

        if "origin" in remotes:
            url = remotes["origin"]
            if "github.com" in url:
                remote_type = "GitHub"
                if gh_info["authenticated"]:
                    code_view, view_out, _ = run_cmd(["gh", "repo", "view", "--json", "isPrivate,nameWithOwner"])
                    if code_view == 0 and "isPrivate" in view_out:
                        import json
                        try:
                            data = json.loads(view_out)
                            is_private = data.get("isPrivate", True)
                            repo_name = data.get("nameWithOwner")
                        except Exception:
                            pass
            elif "gitlab.com" in url or "gitlab" in url:
                remote_type = "GitLab"
                if glab_info["authenticated"]:
                    code_view, view_out, _ = run_cmd(["glab", "repo", "view"])
                    if code_view == 0:
                        is_private = "Private" in view_out
                        repo_name = url.split(":")[-1].replace(".git", "")

        # Check ahead/behind remote
        ahead, behind = 0, 0
        if "origin" in remotes:
            run_cmd(["git", "fetch", "origin", current_branch])
            code_rev, rev_out, _ = run_cmd(["git", "rev-list", "--left-right", "--count", f"HEAD...origin/{current_branch}"])
            if code_rev == 0 and rev_out:
                parts = rev_out.split()
                if len(parts) == 2:
                    ahead, behind = int(parts[0]), int(parts[1])

        # Proactive recommendations ("precisa de algo a mais?")
        recommendations = []
        
        # 1. Secret protection check
        gitignore_path = self.repo_dir / ".gitignore"
        has_env_ignored = False
        if gitignore_path.exists():
            content = gitignore_path.read_text(encoding="utf-8", errors="ignore")
            has_env_ignored = ".env" in content
        else:
            recommendations.append("Criar .gitignore para impedir commit acidental de tokens e segredos.")

        if not has_env_ignored:
            recommendations.append("Adicionar '.env' e 'credentials.json' ao .gitignore para proteção de tokens Notion/Git.")

        # 2. Vault privacy warning
        if remote_type != "None" and is_private is False:
            recommendations.append("⚠️ ATENÇÃO: O repositório remoto está marcado como PÚBLICO. Se seu Second Brain armazena anotações confidenciais, considere torná-lo PRIVADO ou usar um repositório dedicado separado para a pasta .second-brain/.")

        # 3. Uncommitted sync
        if uncommitted_count > 0:
            recommendations.append(f"Existem {uncommitted_count} arquivos modificados não commitados. Execute 'git commit' e sincronize com a nuvem.")

        # 4. Ahead of remote
        if ahead > 0:
            recommendations.append(f"O repositório local está {ahead} commit(s) à frente do remote. Execute 'git push' para manter o backup atualizado.")

        # 5. Behind remote
        if behind > 0:
            recommendations.append(f"O repositório remoto tem {behind} commit(s) novos. Execute 'git pull' para sincronizar alterações remotas.")

        # 6. CI Sync Workflow
        ci_workflow_github = self.repo_dir / ".github" / "workflows" / "second-brain-sync.yml"
        ci_workflow_gitlab = self.repo_dir / ".gitlab-ci.yml"
        if remote_type == "GitHub" and not ci_workflow_github.exists():
            recommendations.append("Adicionar workflow de automação GitHub Actions (.github/workflows/second-brain-sync.yml) para backup e auditoria contínua.")
        elif remote_type == "GitLab" and not ci_workflow_gitlab.exists():
            recommendations.append("Adicionar pipeline GitLab CI (.gitlab-ci.yml) para validação e backup agendado do cofre.")

        return {
            "gh": gh_info,
            "glab": glab_info,
            "remotes": remotes,
            "current_branch": current_branch,
            "remote_type": remote_type,
            "repo_name": repo_name,
            "is_private": is_private,
            "uncommitted_files": uncommitted_count,
            "ahead": ahead,
            "behind": behind,
            "recommendations": recommendations
        }

    def print_audit_report(self):
        """Prints a rich, formatted audit report in Portuguese and English."""
        report = self.audit()

        print("=" * 72)
        print("🌐 GIT REMOTE SYNCHRONIZATION AUDIT / AUDITORIA DE SINCRONIZAÇÃO GIT")
        print("=" * 72)
        
        # CLI Availability
        print("\n🔧 Ferramentas de Linha de Comando (CLIs):")
        gh = report["gh"]
        if gh["installed"]:
            auth_str = f"✅ Autenticado como @{gh['account']}" if gh["authenticated"] else "⚠️ Instalado, mas não autenticado ('gh auth login')"
            print(f"  • GitHub CLI (gh):  {auth_str}")
        else:
            print("  • GitHub CLI (gh):  ❌ Não instalado (Instale via 'winget install GitHub.cli')")

        glab = report["glab"]
        if glab["installed"]:
            auth_str = f"✅ Autenticado como {glab['account']}" if glab["authenticated"] else "⚠️ Instalado, mas não autenticado ('glab auth login')"
            print(f"  • GitLab CLI (glab): {auth_str}")
        else:
            print("  • GitLab CLI (glab): ⚪ Não instalado (Opcional - 'winget install GLab.GLab')")

        # Remote status
        print("\n📦 Repositório Git Local & Remoto:")
        print(f"  • Branch Ativa:     {report['current_branch']}")
        remotes = report["remotes"]
        if remotes:
            for name, url in remotes.items():
                print(f"  • Remote '{name}':    {url}")
        else:
            print("  • Remote 'origin':   ❌ Nenhum remote configurado")

        if report["remote_type"] != "None":
            vis_str = "🔒 Privado (Private)" if report["is_private"] else "🌍 Público (Public)"
            print(f"  • Provedor:         {report['remote_type']} ({report['repo_name'] or 'detectado'})")
            print(f"  • Visibilidade:     {vis_str}")
        
        print(f"  • Arquivos Pendentes: {report['uncommitted_files']}")
        print(f"  • Status de Sincronia: {report['ahead']} à frente (ahead) / {report['behind']} atrás (behind)")

        # Recommendations ("Precisa de algo a mais?")
        print("\n💡 Diagnóstico Proativo — 'Precisa de algo a mais?':")
        recs = report["recommendations"]
        if not recs:
            print("  ✨ Perfeito! O repositório está perfeitamente protegido, sincronizado e configurado.")
        else:
            for idx, r in enumerate(recs, 1):
                print(f"  {idx}. {r}")

        print("=" * 72 + "\n")

    def sync_to_remote(self, commit_message: str = "chore(brain): automated second-brain sync"):
        """Stage, commit, and push changes to the active remote."""
        print(f"🔄 Disparando sincronização Git para o remote...")
        run_cmd(["git", "add", ".second-brain/"])
        code_c, out_c, _ = run_cmd(["git", "commit", "-m", commit_message])
        if code_c == 0:
            print(f"  ✓ Commit realizado: {commit_message}")
        else:
            print("  ℹ️ Nenhuma alteração pendente em .second-brain/ para commitar.")

        code_b, branch, _ = run_cmd(["git", "branch", "--show-current"])
        branch = branch or "main"
        code_p, out_p, err_p = run_cmd(["git", "push", "origin", branch])
        if code_p == 0:
            print(f"  ✅ Push concluído com sucesso para origin/{branch}!")
            return True
        else:
            print(f"  ⚠️ Erro no push: {err_p}")
            return False

    def create_remote_repo(self, provider: str = "github", name: str = "my-second-brain", private: bool = True):
        """Create a new remote repo using gh or glab and set as origin."""
        vis_flag = "--private" if private else "--public"
        if provider.lower() == "github":
            if not self.gh_installed:
                print("❌ GitHub CLI (gh) não está instalado.")
                return False
            print(f"🚀 Criando repositório no GitHub: {name} ({'privado' if private else 'público'})...")
            code, out, err = run_cmd(["gh", "repo", "create", name, vis_flag, "--source=.", "--remote=origin", "--push"])
            if code == 0:
                print(f"✅ Repositório criado e vinculado com sucesso no GitHub: {out}")
                return True
            else:
                print(f"⚠️ Erro ao criar repositório via gh: {err}")
                return False
        elif provider.lower() == "gitlab":
            if not self.glab_installed:
                print("❌ GitLab CLI (glab) não está instalado.")
                return False
            print(f"🚀 Criando repositório no GitLab: {name} ({'privado' if private else 'público'})...")
            code, out, err = run_cmd(["glab", "repo", "create", name, vis_flag])
            if code == 0:
                print(f"✅ Repositório criado no GitLab: {out}")
                return True
            else:
                print(f"⚠️ Erro ao criar repositório via glab: {err}")
                return False
        return False

def main():
    manager = GitRemoteManager()
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd in ["--audit", "audit", "status"]:
            manager.print_audit_report()
            return
        elif cmd in ["--sync", "sync", "push"]:
            msg = sys.argv[2] if len(sys.argv) > 2 else "chore(brain): automated second-brain sync"
            manager.sync_to_remote(msg)
            return
        elif cmd in ["--create", "create"]:
            provider = sys.argv[2] if len(sys.argv) > 2 else "github"
            repo_name = sys.argv[3] if len(sys.argv) > 3 else "second-brain-vault"
            is_private = "--public" not in sys.argv
            manager.create_remote_repo(provider, repo_name, is_private)
            return

    # Default action: run audit
    manager.print_audit_report()

if __name__ == "__main__":
    main()
