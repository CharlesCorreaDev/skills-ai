# Manual Mestre de Kubernetes (K8s) ☸️ Da Máquina Local à Multi-Cloud

> **Fonte Canônica:** [github.com/kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) • [kubernetes.io/docs](https://kubernetes.io/docs/)  
> **Objetivo:** Fornecer o roteiro passo a passo para criar, configurar e orquestrar clusters de Kubernetes tanto **localmente** (K3s, Kind, Minikube, Podman Play) quanto nas principais **Nuvens Públicas e Provedores**:
> - **Nuvem Pública:** Azure (AKS), Google Cloud (GKE), AWS (EKS), Oracle Cloud (OKE).
> - **Provedores Acessíveis & VPS:** DigitalOcean (DOKS), Hostinger (VPS K3s/Rancher) e Cloudflare (BFF / Edge Tunnel).

---

## 💻 PARTE 1: Kubernetes Local (Ambiente de Desenvolvimento Rápido)

Para testar pods, deployments e services sem gastar dinheiro na nuvem:

### 1. Kind (Kubernetes in Docker/Kiri/Podman) - O Mais Recomendado 🌟
O Kind roda nós do Kubernetes como contêineres:
```bash
# Instalação: brew install kind / winget install Kubernetes.kind
# Criar cluster com 1 control-plane e 2 workers:
cat <<EOF > kind-config.yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
- role: worker
EOF

kind create cluster --name dev-cluster --config kind-config.yaml
kubectl cluster-info --context kind-dev-cluster
```

### 2. K3s (Kubernetes Leve mantido pela Rancher/SUSE) 🪶
Ideal para máquinas com pouca RAM e servidores VPS modestos:
```bash
# Instalação com 1 comando no Linux/WSL2 (apenas ~512MB RAM):
curl -sfL https://get.k3s.io | sh -
# Verificar nós:
sudo k3s kubectl get nodes
```

### 3. Minikube
```bash
minikube start --driver=docker --memory=4096 --cpus=2
minikube dashboard
```

### 4. Podman Nativo (`podman play kube`)
Dispensar totalmente a instalação de um cluster e subir arquivos YAML de Pods diretamente:
```bash
podman play kube deployment.yaml
```

---

## ☁️ PARTE 2: Clusters de Kubernetes Gerenciados nas Nuvens Públicas

---

### 🔷 1. Microsoft Azure: Azure Kubernetes Service (AKS)
```bash
# 1. Login e criação de Resource Group:
az login
az group create --name rg-kubernetes --location eastus

# 2. Criar cluster AKS gerenciado:
az aks create \
  --resource-group rg-kubernetes \
  --name aks-prod-cluster \
  --node-count 2 \
  --node-vm-size Standard_B2s \
  --enable-managed-identity \
  --generate-ssh-keys

# 3. Baixar credenciais para o kubectl:
az aks get-credentials --resource-group rg-kubernetes --name aks-prod-cluster
kubectl get nodes
```

---

### 🌐 2. Google Cloud: Google Kubernetes Engine (GKE)
O GKE é a referência de mercado, já que o Kubernetes foi criado pelo Google:
```bash
# 1. Autenticação e definição de projeto:
gcloud auth login
gcloud config set project MEU_PROJETO_ID
gcloud config set compute/zone us-central1-a

# 2. Criar cluster GKE Autopilot (Totalmente gerenciado e autoescalável):
gcloud container clusters create-auto gke-prod-cluster --region us-central1

# Ou modo Standard com nós e2-standard-2:
gcloud container clusters create gke-standard-cluster --num-nodes=2 --machine-type=e2-standard-2

# 3. Conectar kubectl:
gcloud container clusters get-credentials gke-prod-cluster --region us-central1
```

---

### 🟧 3. AWS (Amazon Web Services): Amazon EKS (Elastic Kubernetes Service)
A forma mais ágil de criar clusters no EKS é utilizando a CLI oficial `eksctl`:
```bash
# Instalar eksctl e criar cluster com 2 nós t3.medium:
eksctl create cluster \
  --name eks-prod-cluster \
  --region us-east-1 \
  --nodegroup-name standard-nodes \
  --node-type t3.medium \
  --nodes 2 \
  --nodes-min 1 \
  --nodes-max 3 \
  --managed

# O kubeconfig é configurado automaticamente:
kubectl get nodes
```

---

### 🔴 4. Oracle Cloud Infrastructure (OCI): Oracle Container Engine (OKE)
A Oracle oferece um tier gratuito generoso (Always Free com processadores ARM Ampere até 4 OCPUs e 24GB RAM):
```bash
# 1. Instalar OCI CLI: oci setup config
# 2. Criar via OCI Console ou CLI:
oci ce cluster create \
  --compartment-id <COMPARTMENT_OCID> \
  --name oke-prod-cluster \
  --vcn-id <VCN_OCID> \
  --kubernetes-version v1.31.0

# 3. Gerar kubeconfig:
oci ce cluster create-kubeconfig --cluster-id <CLUSTER_OCID> --file ~/.kube/config
```

---

## 🌊 PARTE 3: Kubernetes Acessível & Provedores VPS

---

### 🦈 1. DigitalOcean: DigitalOcean Kubernetes (DOKS)
Excelente custo-benefício para startups e projetos médios:
```bash
# Instalar doctl:
doctl auth init

# Criar cluster com 2 nós básicos de $12/mês:
doctl kubernetes cluster create doks-prod-cluster \
  --region nyc1 \
  --version latest \
  --size s-2vcpu-2gb \
  --count 2

# Obter kubeconfig:
doctl kubernetes cluster kubeconfig save doks-prod-cluster
```

---

### 🏢 2. Hostinger (VPS K3s / Rancher / Kubernetes Self-Hosted)
A Hostinger oferece VPS KVM de alto desempenho a preços competitivos. Para rodar Kubernetes lá com máxima eficiência:

#### Passo 1: Provisionar VPS KVM com Ubuntu 24.04 LTS
Acesse o painel da Hostinger e crie um VPS KVM (mínimo recomendado: KVM 2 com 2 vCPUs e 8GB RAM).

#### Passo 2: Instalar K3s no Nó Master (Server):
```bash
ssh root@SEU_IP_HOSTINGER
# Instalação leve com flannel e sem servicelb para máxima economia de RAM:
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--disable traefik" sh -

# Pegar o Token do cluster para adicionar novos nós futuramente:
cat /var/lib/rancher/k3s/server/node-token

# Copiar o kubeconfig para sua máquina local:
cat /etc/rancher/k3s/k3s.yaml
```

#### Passo 3: Conectar seu computador local ao cluster da Hostinger:
Na sua máquina, edite o arquivo copiado substituindo `127.0.0.1` pelo IP público do VPS da Hostinger:
```bash
export KUBECONFIG=~/.kube/hostinger-k3s.yaml
kubectl get nodes
```

---

### ☁️ 3. Cloudflare (Cloudflare Tunnels + Ingress Seguro para Kubernetes)
A Cloudflare não hospeda nós de computação Kubernetes diretamente, mas é a **camada definitiva de proteção, DDoS, SSL/TLS e Ingress** para expor qualquer cluster (local, Hostinger ou Cloud) para a internet sem abrir portas no roteador/firewall via **Cloudflare Tunnel (`cloudflared`)**:

```yaml
# manifesto: cloudflared-k8s.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cloudflared
  namespace: default
spec:
  replicas: 2
  selector:
    matchLabels:
      app: cloudflared
  template:
    metadata:
      labels:
        app: cloudflared
    spec:
      containers:
      - name: cloudflared
        image: cloudflare/cloudflared:latest
        args:
        - tunnel
        - --no-autoupdate
        - run
        - --token
        - "SEU_CLOUDFLARE_TUNNEL_TOKEN_AQUI"
```
Aplique no cluster:
```bash
kubectl apply -f cloudflared-k8s.yaml
```
*Seu cluster passa a responder instantaneamente pelo seu domínio na Cloudflare (ex: `api.minhaempresa.com`), com proteção WAF, cache global de borda e SSL gratuito sem precisar de Load Balancers caros!*

---

## 📋 Resumo Comparativo: Onde Criar seu Kubernetes?

| Provedor / Tipo | Custo Inicial | Complexidade | Recomendado Para |
| :--- | :--- | :--- | :--- |
| **Kind / K3s Local** | Gratuito | Mínima | Desenvolvimento local, testes em CI/CD |
| **Azure (AKS)** | Médio/Alto | Baixa (Gerenciado) | Aplicações integradas ao ecossistema Microsoft |
| **Google Cloud (GKE)** | Médio/Alto | Baixa (Autopilot) | Padrão ouro da indústria, alta resiliência |
| **AWS (EKS)** | Médio/Alto | Média | Empresas já hospedadas na infraestrutura AWS |
| **Oracle Cloud (OKE)** | Gratuito / Baixo | Média | Aproveitar o Tier Always Free de 24GB RAM |
| **DigitalOcean (DOKS)** | Baixo (~$24/mês) | Mínima | Startups e projetos com orçamento previsível |
| **Hostinger (K3s em VPS)** | Baixo (~$6 a $12/mês) | Média (Self-hosted) | Máximo poder de hardware pelo menor preço |
| **Cloudflare** | Gratuito / Baixo | Baixa | Borda, segurança, WAF e exposição sem abrir portas |

