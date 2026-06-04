import requests

from app.config import settings


class LangflowClient:
    def generate(self, message: str, session_id: str) -> str:
        if not settings.langflow_flow_id:
            raise RuntimeError("LANGFLOW_FLOW_ID is not configured")

        headers = {"Content-Type": "application/json"}

        if settings.langflow_api_key:
            headers["x-api-key"] = settings.langflow_api_key

        response = requests.post(
            f"{settings.langflow_base_url}/api/v1/run/{settings.langflow_flow_id}",
            headers = headers,
            json    = {
                "input_value": message,
                "input_type" : "chat",
                "output_type": "chat",
                "session_id" : session_id,
            },
            timeout = 120)

        response.raise_for_status()
        return self._extract_text(response.json())


    def _extract_text(self, data: dict) -> str:
        try:
            return data["outputs"][0]["outputs"][0]["results"]["message"]["text"]
        except (KeyError, IndexError, TypeError):
            pass

        text = self._find_text(data)

        if text is None:
            return str(data)

        return text


    def _find_text(self, value) -> str | None:
        if isinstance(value, dict):
            if isinstance(value.get("text"), str):
                return value["text"]

            message = value.get("message")
            if isinstance(message, dict) and isinstance(message.get("text"), str):
                return message["text"]

            for child in value.values():
                text = self._find_text(child)
                if text is not None:
                    return text

        if isinstance(value, list):
            for child in value:
                text = self._find_text(child)
                if text is not None:
                    return text

        return None