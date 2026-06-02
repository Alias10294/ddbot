export type ChatRequest = {
  conversation_id: string;
  message: string;
};

export type ChatResponse = {
  conversation_id: string;
  answer: string;
};

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000";

export async function sendMessage(request: ChatRequest): Promise<ChatResponse> {
  const response = await fetch(`${API_BASE_URL}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(request)
  });

  if (!response.ok) {
    throw new Error("Erreur lors de la communication avec le backend.");
  }

  return response.json();
}