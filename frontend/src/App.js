import React, { useState } from "react";
import Heatmap from "./components/Heatmap";
import { uploadCSV } from "./services/api";

function App() {
  const [heatmapData, setHeatmapData] = useState(null);

  const handleFileChange = async (e) => {
    const file = e.target.files[0];
    const result = await uploadCSV(file);
    setHeatmapData(result.heatmap_data);
  };

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Gene Profile Matcher</h1>
      <input type="file" accept=".csv" onChange={handleFileChange} />
      {heatmapData && <Heatmap data={heatmapData} />}
    </div>
  );
}

export default App;
