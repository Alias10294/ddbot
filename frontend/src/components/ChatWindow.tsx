import MessageBubble from "./MessageBubble";

export type ChatMessage = {
  id: string;
  role: "user" | "assistant";
  content: string;
};

type ChatWindowProps = {
  messages: ChatMessage[];
  isLoading: boolean;
};

export default function ChatWindow({ messages, isLoading }: ChatWindowProps) {
  return (
    <div className="chat-window">
      {messages.map((message) => (
        <MessageBubble key={message.id} message={message} />
      ))}

      {isLoading && (
        <div className="message-row assistant-row">
          <div className="message-bubble assistant-bubble loading-bubble">
            L'agent rédige une réponse...
          </div>
        </div>
      )}
    </div>
  );
}