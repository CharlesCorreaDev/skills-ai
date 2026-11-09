<?php
declare(strict_types=1);

namespace SmsLegal;

/**
 * Cliente PHP oficial para a API SMS Legal / SMS Gateway.
 * Compatível com PHP 7.4, 8.0, 8.1, 8.2, 8.3, 8.4 e 8.5.
 */
class SmsLegalClient
{
    private const BASE_URL = 'https://v1.smsgateway.com.br/api/';

    private string $token;
    private int $timeout;

    /**
     * @param string $token Token de autenticação da API SMS Legal.
     * @param int $timeout Tempo limite da requisição em segundos (padrão 30s).
     */
    public function __construct(string $token, int $timeout = 30)
    {
        $this->token = trim($token);
        $this->timeout = $timeout;
    }

    /**
     * Envia uma mensagem SMS de texto simples para um único número.
     *
     * @param string $to Número com DDI + DDD + Telefone (ex: 5551999999999).
     * @param string $msg Texto da mensagem.
     * @return array Resposta decodificada da API.
     */
    public function enviarTexto(string $to, string $msg): array
    {
        return $this->request('send-sms-texto.php', [
            'to' => $this->sanitizePhone($to),
            'msg' => $msg
        ], 'POST');
    }

    /**
     * Envia uma mensagem SMS em lote para múltiplos números.
     *
     * @param array<string>|string $recipients Lista de números ou string separada por vírgula.
     * @param string $msg Texto da mensagem.
     * @return array Resposta decodificada da API.
     */
    public function enviarLote($recipients, string $msg): array
    {
        $toString = is_array($recipients) ? implode(',', array_map([$this, 'sanitizePhone'], $recipients)) : $recipients;
        return $this->request('send-sms-texto-lote.php', [
            'to' => $toString,
            'msg' => $msg
        ], 'POST');
    }

    /**
     * Agenda o envio de SMS para uma data e hora específicas.
     *
     * @param array<string>|string $recipients Número(s) de destino.
     * @param string $msg Texto da mensagem.
     * @param string $dtenvio Data e hora no formato DD-MM-AAAA HH:MM:SS.
     * @return array Resposta da API.
     */
    public function agendar($recipients, string $msg, string $dtenvio): array
    {
        $toString = is_array($recipients) ? implode(',', array_map([$this, 'sanitizePhone'], $recipients)) : $recipients;
        return $this->request('agendar-sms.php', [
            'to' => $toString,
            'msg' => $msg,
            'dtenvio' => $dtenvio
        ], 'POST');
    }

    /**
     * Consulta o status de entrega de um SMS enviado.
     *
     * @param string $idSms Código retornado na hora do envio.
     * @return array Dados de status da mensagem.
     */
    public function consultarStatus(string $idSms): array
    {
        return $this->request('status.php', [
            'idsms' => $idSms
        ], 'GET');
    }

    /**
     * Consulta o saldo de créditos da conta.
     *
     * @return array Saldo e data de verificação.
     */
    public function consultarCreditos(): array
    {
        return $this->request('creditos.php', [], 'GET');
    }

    /**
     * Captura as respostas de clientes (replies).
     *
     * @param int $qt Quantidade de mensagens (máx 500).
     * @return array Lista de respostas capturadas.
     */
    public function consultarRespostas(int $qt = 50): array
    {
        return $this->request('respostas.php', [
            'qt' => $qt
        ], 'GET');
    }

    /**
     * Consulta operadora, portabilidade e status de ativação do número.
     *
     * @param string $phone Número de telefone com DDI + DDD + Telefone.
     * @return array Detalhes cadastrais e de rede do número.
     */
    public function consultarNumero(string $phone): array
    {
        return $this->request('consultar-numero.php', [
            'nr' => $this->sanitizePhone($phone)
        ], 'GET');
    }

    /**
     * Envia mensagem de voz sintetizada (Text-to-Speech).
     *
     * @param string $to Número de destino.
     * @param string $msg Texto falado.
     * @param string $from ID do Remetente no painel.
     * @return array Resposta da API.
     */
    public function enviarVoz(string $to, string $msg, string $from): array
    {
        return $this->request('send-sms-voz.php', [
            'to' => $this->sanitizePhone($to),
            'msg' => $msg,
            'from' => $from
        ], 'POST');
    }

    /**
     * Envia chamada telefônica com áudio pré-gravado.
     *
     * @param string $to Número de destino.
     * @param string $idAudio ID do áudio cadastrado no painel.
     * @param string $from ID do Remetente no painel.
     * @return array Resposta da API.
     */
    public function enviarAudio(string $to, string $idAudio, string $from): array
    {
        return $this->request('send-sms-audio.php', [
            'to' => $this->sanitizePhone($to),
            'idaudio' => $idAudio,
            'from' => $from
        ], 'POST');
    }

    /**
     * Remove caracteres não numéricos do telefone.
     */
    private function sanitizePhone(string $phone): string
    {
        return preg_replace('/\D+/', '', $phone) ?? '';
    }

    /**
     * Executa a requisição cURL para a API.
     */
    private function request(string $endpoint, array $params, string $method): array
    {
        $params['token'] = $this->token;
        $url = self::BASE_URL . $endpoint;

        $ch = curl_init();
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_TIMEOUT, $this->timeout);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);

        if (strtoupper($method) === 'POST') {
            curl_setopt($ch, CURLOPT_URL, $url);
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($params));
        } else {
            curl_setopt($ch, CURLOPT_URL, $url . '?' . http_build_query($params));
        }

        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $curlError = curl_error($ch);
        curl_close($ch);

        if ($response === false) {
            return [
                'error' => true,
                'message' => 'Erro de conexão cURL: ' . $curlError
            ];
        }

        $decoded = json_decode((string)$response, true);
        if (json_last_error() === JSON_ERROR_NONE) {
            return $decoded;
        }

        return [
            'statusCode' => $httpCode,
            'raw' => trim((string)$response)
        ];
    }
}

