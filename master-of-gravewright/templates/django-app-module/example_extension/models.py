from django.db import models

class CustomCampaignLog(models.Model):
    """
    EN: Custom model representing an extension log linked to a campaign.
    PT-BR: Modelo customizado representando um registro de extensão vinculado a uma campanha.
    """
    campaign_id = models.CharField(max_length=64, db_index=True)
    title = models.CharField(max_length=255)
    payload = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
