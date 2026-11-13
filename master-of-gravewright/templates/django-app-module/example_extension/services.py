"""
Domain Services - Gravewright Architecture Rule
================================================
EN: Domain services own authorization, validation and persistence.
    Views and WebSocket consumers only translate incoming requests and dispatch events.
PT-BR: Serviços de domínio detêm a validação, autorização e persistência.
       Views e WebSockets apenas traduzem requisições e despacham eventos.
"""

from typing import Dict, Any
from .models import CustomCampaignLog

def record_campaign_log(campaign_id: str, title: str, payload: Dict[str, Any]) -> CustomCampaignLog:
    """
    EN: Business logic service to validate and persist a log entry.
    PT-BR: Serviço de lógica de negócio para validar e persistir um log.
    """
    if not campaign_id or not title:
        raise ValueError("campaign_id and title are required")
    
    return CustomCampaignLog.objects.create(
        campaign_id=campaign_id,
        title=title,
        payload=payload
    )
