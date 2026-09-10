# Foundry VTT Knowledge Base: Getting Started & Hosting

> Source: [https://foundryvtt.com/kb/](https://foundryvtt.com/kb/)

## 1. Hosting Architecture
Foundry Virtual Tabletop is self-hosted. You can host:
- **Local Application:** Run directly on your desktop (Windows / macOS / Linux). Players connect via your Public IP / Port 30000 with UPnP or manual Port Forwarding.
- **Dedicated Cloud Server:** Node.js server hosted on VPS (Ubuntu, Debian, AWS, DigitalOcean, Oracle Cloud, Docker).
- **Partner Hosting Services:** Forge, Molten Hosting, etc.

## 2. Network Configuration & SSL
- **Port:** Default is `30000` TCP.
- **SSL (HTTPS/WSS):** Required for WebRTC Audio/Video features. Use Reverse Proxy (Nginx / Caddy / Cloudflare) with Let's Encrypt certificates.
