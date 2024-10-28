import React, { useState, useEffect, useRef } from "react";
import Message from "./Message";
import { IoMdSend } from "react-icons/io";
import axios from "axios";

const ChatWindow = ({ documentId, setMessages, messages }) => {
  const [input, setInput] = useState("");
  const [isGeneratingResponse, setIsGeneratingResponse] = useState(false);
  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async () => {
    if (!input.trim() || !documentId) return;

    const userMessage = { role: "user", content: input };
    setMessages((prevMessages) => [...prevMessages, userMessage]);
    setIsGeneratingResponse(true);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/questions/ask-question/",
        {
          document_id: documentId,
          question: input,
        }
      );

      const responseMessage = {
        role: "model",
        content: response.data.answer,
      };
      setMessages((prevMessages) => [...prevMessages, responseMessage]);
    } catch (error) {
      console.error("Error generating response:", error);
    } finally {
      setIsGeneratingResponse(false);
    }

    setInput("");
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !isGeneratingResponse) {
      handleSendMessage();
    }
  };

  return (
    <div className="flex flex-col h-full p-2 lg:p-6 bg-gray-100 overflow-auto">
      <div className="flex-grow mb-4 space-y-4">
        {messages?.map((message, index) => (
          <Message key={index} message={message} />
        ))}
        <div ref={messagesEndRef} />
      </div>
      <div
        className="flex items-center sticky bottom-0 z-10 bg-gray-100"
        style={{ zIndex: 100 }}
      >
        <div
          className={`flex flex-grow px-2 justify-between items-center shadow-[rgba(0, 0, 0, 0.24) 0px 3px 8px] rounded-lg border-gray-300 ${
            isGeneratingResponse ? "bg-gray-200" : "bg-white"
          }`}
        >
          <input
            ref={inputRef}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyPress}
            placeholder="Send a message..."
            className={`flex flex-grow px-2 py-2 justify-between items-center shadow-[rgba(0, 0, 0, 0.24) 0px 3px 8px] rounded-lg border-gray-300 ${
              isGeneratingResponse ? "bg-gray-200" : "bg-white"
            }`}
            disabled={isGeneratingResponse}
          />
          <button
            onClick={handleSendMessage}
            disabled={isGeneratingResponse}
            className={`ml-2 p-2 rounded-full ${
              isGeneratingResponse ? "cursor-not-allowed text-gray-400" : ""
            }`}
          >
            <IoMdSend />
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatWindow;
