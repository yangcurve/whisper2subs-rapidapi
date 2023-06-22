import requests

from whisper2subs.transcribe import TranscribeResult


def deepl_translate(
    transcribed_audio: TranscribeResult, output_language: str, api_key: str
) -> TranscribeResult:
    url = "https://deepl-translator.p.rapidapi.com/translate"

    for i, x in enumerate(transcribed_audio["segments"], 0):
        payload = {
            "text": x["text"],
            "source": "EN",
            "target": output_language.upper(),
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "deepl-translator.p.rapidapi.com",
        }
        response = requests.post(url, json=payload, headers=headers)
        try:
            result = response.json()["text"]
        except:
            result = ""

        transcribed_audio["segments"][i]["text"] = result

    return transcribed_audio
