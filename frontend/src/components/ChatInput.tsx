import { FormEvent, useState } from "react";

type ChatInputProps = {
  onSend: (message: string) => void;
  disabled?: boolean;
};

export default function ChatInput({ onSend, disabled = false }: ChatInputProps) {
  const [value, setValue] = useState("");

  function handleSubmit(event: FormEvent) {
    event.preventDefault();

    const message = value.trim();

    if (!message || disabled) {
      return;
    }

    onSend(message);
    setValue("");
  }

  return (
    <form className="chat-input-form" onSubmit={handleSubmit}>
      <input
        className="chat-input"
        type="text"
        value={value}
        disabled={disabled}
        placeholder="Écrivez votre question..."
        onChange={(event) => setValue(event.target.value)}
      />

      <button className="send-button" type="submit" disabled={disabled || !value.trim()}>
        Envoyer
      </button>
    </form>
  );
}