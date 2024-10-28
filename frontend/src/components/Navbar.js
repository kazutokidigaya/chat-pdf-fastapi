import React, { useRef } from "react";
import { IoAddCircleOutline } from "react-icons/io5";
import axios from "axios";

const Navbar = ({
  setUploadedFileName,
  setDocumentId,
  setMessages,
  uploadedFileName,
}) => {
  const fileInputRef = useRef();

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    if (file) {
      const formData = new FormData();
      formData.append("file", file);

      try {
        const response = await axios.post(
          "https://chat-pdf-fastapi.onrender.com/pdf/upload-pdf/",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );
        console.log("PDF uploaded successfully:", response.data);
        setUploadedFileName(
          file.name.length > 10 ? file.name.slice(0, 12) + "..." : file.name
        );
        setDocumentId(response.data.document_id);
        setMessages([]);
      } catch (error) {
        console.error("Error uploading PDF:", error);
      }
    }
  };

  return (
    <nav className="flex items-center justify-between px-6 py-4 bg-white text-white">
      <div className="font-bold text-lg">
        <img src={require("../assets/main-logo.png")} alt="Main Logo" />
      </div>
      <div className="flex items-center space-x-4 text-[#10a857]">
        {uploadedFileName && (
          <span className="text-sm">{uploadedFileName}</span>
        )}
        <input
          type="file"
          ref={fileInputRef}
          style={{ display: "none" }}
          onChange={handleFileUpload}
        />
        <button
          onClick={() => fileInputRef.current.click()}
          className="flex items-center space-x-2 px-2 py-2 rounded-lg text-black  border border-black hover:text-white hover:bg-black sm:px-8"
        >
          <IoAddCircleOutline size={20} />

          <span className="hidden sm:inline">Upload PDF</span>
        </button>
      </div>
    </nav>
  );
};

export default Navbar;
