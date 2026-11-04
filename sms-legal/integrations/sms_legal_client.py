"""
SMS Legal Python Client
Universal SDK for SMS Legal / SMS Gateway API.
Compatible with Python 3.8+.
"""

import re
import urllib.request
import urllib.parse
import json
from typing import List, Union, Dict, Any, Optional

class SmsLegalClient:
    BASE_URL = "https://v1.smsgateway.com.br/api/"

    def __init__(self, token: str, timeout: int = 30):
        self.token = token.strip()
        self.timeout = timeout

    @staticmethod
    def _sanitize_phone(phone: str) -> str:
        return re.sub(r"\D+", "", phone)

    def _request(self, endpoint: str, params: Dict[str, Any], method: str = "GET") -> Dict[str, Any]:
        merged = {k: v for k, v in params.items() if v is not None}
        merged["token"] = self.token
        encoded = urllib.parse.urlencode(merged)

        headers = {
            "User-Agent": "SmsLegal-PythonClient/1.0.0",
            "Accept": "application/json, text/plain, */*"
        }

        if method.upper() == "POST":
            full_url = f"{self.BASE_URL}{endpoint}"
            data = encoded.encode("utf-8")
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            req = urllib.request.Request(full_url, data=data, headers=headers, method="POST")
        else:
            full_url = f"{self.BASE_URL}{endpoint}?{encoded}"
            req = urllib.request.Request(full_url, headers=headers, method="GET")

        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                raw = resp.read().decode("utf-8")
                try:
                    return json.loads(raw)
                except Exception:
                    return {"raw": raw.strip(), "statusCode": resp.status}
        except Exception as e:
            return {"error": True, "message": f"Erro de conexão: {str(e)}"}

    def enviar_texto(self, to: str, msg: str) -> Dict[str, Any]:
        return self._request("send-sms-texto.php", {
            "to": self._sanitize_phone(to),
            "msg": msg
        }, method="POST")

    def enviar_lote(self, recipients: Union[List[str], str], msg: str) -> Dict[str, Any]:
        if isinstance(recipients, list):
            to_str = ",".join([self._sanitize_phone(r) for r in recipients])
        else:
            to_str = recipients
        return self._request("send-sms-texto-lote.php", {
            "to": to_str,
            "msg": msg
        }, method="POST")

    def agendar(self, recipients: Union[List[str], str], msg: str, dtenvio: str) -> Dict[str, Any]:
        if isinstance(recipients, list):
            to_str = ",".join([self._sanitize_phone(r) for r in recipients])
        else:
            to_str = recipients
        return self._request("agendar-sms.php", {
            "to": to_str,
            "msg": msg,
            "dtenvio": dtenvio
        }, method="POST")

    def consultar_status(self, idsms: str) -> Dict[str, Any]:
        return self._request("status.php", {"idsms": idsms}, method="GET")

    def consultar_creditos(self) -> Dict[str, Any]:
        return self._request("creditos.php", {}, method="GET")

    def consultar_respostas(self, qt: int = 50) -> Dict[str, Any]:
        return self._request("respostas.php", {"qt": qt}, method="GET")

    def consultar_numero(self, phone: str) -> Dict[str, Any]:
        return self._request("consultar-numero.php", {
            "nr": self._sanitize_phone(phone)
        }, method="GET")

    def enviar_voz(self, to: str, msg: str, from_id: str) -> Dict[str, Any]:
        return self._request("send-sms-voz.php", {
            "to": self._sanitize_phone(to),
            "msg": msg,
            "from": from_id
        }, method="POST")

    def enviar_audio(self, to: str, idaudio: str, from_id: str) -> Dict[str, Any]:
        return self._request("send-sms-audio.php", {
            "to": self._sanitize_phone(to),
            "idaudio": idaudio,
            "from": from_id
        }, method="POST")

