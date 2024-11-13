import React, { useState, useEffect, PureComponent } from "react";
import { createRoot } from "react-dom/client";

import {
  PieChart,
  Pie,
  ResponsiveContainer,
  Tooltip,
  LineChart,
  Line,
  XAxis,
  YAxis,
} from "recharts";

import { Property } from "./types";

// Render your React component instead
const root = createRoot(document.getElementById("toolsapp"));

const data = [
  { high: 1.45, low: 1.4, year: 2023 },
  { high: 1.52, low: 1.44, year: 2024 },
  { high: 1.6, low: 1.48, year: 2025 },
  { high: 1.67, low: 1.52, year: 2026 },
  { high: 1.76, low: 1.57, year: 2027 },
  { high: 1.85, low: 1.62, year: 2028 },
];

function App() {
  return (
    <>
      <LineChart width={900} height={500} data={data}>
        <Line dataKey="high" fill="#8884d8" />
        <Line dataKey="low" fill="#82ca9d" />
        <XAxis dataKey="year" />
        <YAxis />
        <Tooltip />
      </LineChart>
    </>
  );
}

root.render(<App />);
