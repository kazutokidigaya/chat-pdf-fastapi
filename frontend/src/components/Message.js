const Message = ({ message }) => {
  const isUser = message.role === "user";

  return (
    <div className="flex items-start space-x-4 p-6">
      <div className="flex-shrink-0">
        {isUser ? (
          <img src={require("../assets/user-logo.png")} alt="User Logo" />
        ) : (
          <img src={require("../assets/chat-logo.png")} alt="Chat Logo" />
        )}
      </div>
      <div className="  rounded-lg ">{message.content}</div>
    </div>
  );
};

export default Message;
