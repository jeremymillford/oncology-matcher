import React from "react";
import Plot from "react-plotly.js";

const Heatmap = ({ data }) => {
  const genes = Object.keys(data);
  const values = Object.values(data);
  return (
    <Plot
      data={[
        {
          z: [values],
          x: genes,
          type: "heatmap",
          colorscale: "Viridis",
        },
      ]}
      layout={{ title: "Gene Expression Difference Heatmap" }}
    />
  );
};

export default Heatmap;
