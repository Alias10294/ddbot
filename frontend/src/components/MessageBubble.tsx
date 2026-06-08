import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import logoDD from "../assets/logo.png";
import { ChatMessage } from "./ChatWindow";

type MessageBubbleProps = {
  message: ChatMessage;
};

export default function MessageBubble({ message }: MessageBubbleProps) {
  const isUser = message.role === "user";

  return (
    <div className={`message-row ${isUser ? "user-row" : "assistant-row"}`}>
      {/* On affiche l'avatar à gauche pour Dédé, à droite pour l'user */}
      {!isUser && (
        <div className="avatar assistant-avatar">
          <img src={logoDD} alt="Dédé" />
        </div>
      )}

      <div className={`message-bubble ${isUser ? "user-bubble" : "assistant-bubble"}`}>
        {/* Markdown + remarkGfm pour les tableaux */}
        <ReactMarkdown remarkPlugins={[remarkGfm]}>
          {message.content}
        </ReactMarkdown>
      </div>

      {isUser && (
        <div className="avatar user-avatar">
          <span>👤</span>
        </div>
      )}
    </div>
  );
}