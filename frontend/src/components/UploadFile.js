import React, { useState } from "react";
import axios from "axios";

const UploadFile = () => {
    const [file, setFile] = useState(null);
    const [result, setResult] = useState(null);

    const handleFileUpload = async () => {
        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await axios.post("http://localhost:8000/upload/", formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            });

            setResult(response.data); // Save backend response (plot_path and matched_count)
        } catch (error) {
            console.error("Error uploading file:", error.response?.data || error.message);
            alert("File upload failed! Please check the file format and try again.");
        }
    };

    return (
        <div>
            <h1>Gene Variant Analysis</h1>
            <input type="file" onChange={(e) => setFile(e.target.files[0])} />
            <button onClick={handleFileUpload}>Upload</button>

            {result && (
                <div>
                    <h3>Matched Count: {result.matched_count}</h3>
                    <img
                        src={`http://localhost:8000/static/${result.plot_path}`} // Render plot dynamically
                        alt="Gene Comparison Plot"
                        style={{ width: "80%", marginTop: "20px" }}
                    />
                </div>
            )}
        </div>
    );
};

export default UploadFile;