import React, { useState } from "react";
import Navbar from "../components/Navbar";
import ChatWindow from "../components/ChatWindow";

const Home = () => {
  const [uploadedFileName, setUploadedFileName] = useState(null);
  const [documentId, setDocumentId] = useState();
  const [messages, setMessages] = useState();

  return (
    <div className="h-screen flex flex-col">
      <Navbar
        uploadedFileName={uploadedFileName}
        setUploadedFileName={setUploadedFileName}
        setDocumentId={setDocumentId}
        setMessages={setMessages}
      />
      <div className="flex-grow">
        <ChatWindow
          setMessages={setMessages}
          documentId={documentId}
          messages={messages}
        />
      </div>
    </div>
  );
};

export default Home;
