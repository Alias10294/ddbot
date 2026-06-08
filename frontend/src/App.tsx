import { useMemo, useState } from "react";
import { sendMessage       } from "./api/chat";
import ChatWindow, { ChatMessage } from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";

function createConversationId(): string {
  return crypto.randomUUID();
}

export default function App() {
  const [conversationId, setConversationId] = useState(createConversationId);
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: crypto.randomUUID(),
      role: "assistant",
      content:
        "Bonjour, je suis l'agent de sensibilisation à la cybersécurité. Posez-moi une question sur les bonnes pratiques, le phishing, les mots de passe ou la sécurité numérique."
    }
  ]);
  const [isLoading, setIsLoading] = useState(false);

  // QUICK REPLIES -- Propositions de questions pré-remplies pour guider l'utilisateur
  const quickReplies = [
    "Comment reconnaître un e-mail de phishing ?",
    "Quelles sont les bonnes pratiques pour un mot de passe fort ?",
    "Quelles sont les actions de l'UPHF en cybersécurité ?"
  ];

  const canSend = useMemo(() => !isLoading, [isLoading]);

  async function handleSend(content: string) {
    const userMessage: ChatMessage = {
      id: crypto.randomUUID(),
      role: "user",
      content
    };

    setMessages((current) => [...current, userMessage]);
    setIsLoading(true);

    try {
      const response = await sendMessage({
        conversation_id: conversationId,
        message: content
      });

      const assistantMessage: ChatMessage = {
        id: crypto.randomUUID(),
        role: "assistant",
        content: response.answer
      };

      setMessages((current) => [...current, assistantMessage]);
    } catch {
      const errorMessage: ChatMessage = {
        id: crypto.randomUUID(),
        role: "assistant",
        content:
          "Impossible de contacter le backend. Vérifiez que FastAPI est lancé sur le port 8000."
      };

      setMessages((current) => [...current, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  }

  function handleNewConversation() {
    setConversationId(createConversationId());
    setMessages([
      {
        id: crypto.randomUUID(),
        role: "assistant",
        content: "Nouvelle conversation démarrée. Quelle est votre question ?"
      }
    ]);
  }

  return (
    <main className="app">
      <aside className="sidebar">
        <div className="sidebar-header">
          <img src="/src/assets/logo.png" alt="Dédé" className="sidebar-logo" />
          <h1>DD Bot</h1>
        </div>
        
        <p>Chatbot de sensibilisation cybersécurité</p>

        <button className="new-chat-button" onClick={handleNewConversation}>
          Nouvelle conversation
        </button>

        <div className="conversation-info">
          <span>Conversation</span>
          <code>{conversationId.slice(0, 8)}</code>
        </div>
      </aside>

      <section className="chat-panel">
        <header className="chat-header">
          <h2>DD Bot</h2>
          <p>Posez une question concernant la cybersécurité. Renseignez-vous à propos de la sécurité numérique mise en place à l'UPHF.</p>
        </header>

        {/* Conteneur intermédiaire pour organiser l'affichage fenêtré */}
        <div className="chat-body">
          <ChatWindow messages={messages} isLoading={isLoading} />
          
          {/* QUICK REPLIES -- S'affichent uniquement s'il n'y a que le message d'accueil et pas de chargement */}
          {messages.length === 1 && !isLoading && (
            <div className="quick-replies-container">
              {quickReplies.map((reply, index) => (
                <button
                  key={index}
                  className="quick-reply-card"
                  onClick={() => handleSend(reply)}
                >
                  {reply}
                </button>
              ))}
            </div>
          )}
        </div>

        <ChatInput onSend={handleSend} disabled={!canSend} />
      </section>
    </main>
  );
}