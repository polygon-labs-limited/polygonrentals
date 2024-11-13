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

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Render your React component instead
const root = createRoot(document.getElementById("reactapp"));

function App() {
  const [data, setData] = useState([]);
  const [properties, setProperties] = useState([]);
  const [portfolioValue, setPortfolioValue] = useState([]);

  const s: string = "0";

  console.log("hello", s);

  useEffect(() => {
    fetch("/api", {
      method: "get",
      credentials: "same-origin",
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        setData(data);

        let d = data.reduce((accumulator, currentValue) => {
          if (accumulator[currentValue.city]) {
            accumulator[currentValue.city] += currentValue.value;
          } else {
            accumulator[currentValue.city] = currentValue.value;
          }
          return accumulator;
        }, {});

        let c = data.reduce((accumulator, currentValue) => {
          return accumulator + currentValue.value;
        }, 0);

        setPortfolioValue(c);

        const colors = ["red", "green", "blue"];

        let _d = Object.keys(d).map((key, index) => {
          return {
            title: key,
            name: key,
            key: key,
            value: Math.ceil((d[key] / c) * 100),
            color: `hsl(147, 50%, ${Math.ceil((d[key] / c) * 100)}%)`,
          };
        });

        console.log(_d);

        setProperties(_d);
      })
      .catch(function (ex) {
        console.log("parsing failed", ex);
      });
  }, []);

  console.log("properties", properties);

  return (
    <>
      <PieChart width={800} height={400}>
        <Pie dataKey="value" data={properties} fill="#8884d8" />
        <Tooltip />
      </PieChart>
      <LineChart width={900} height={500} data={data}>
        <Line dataKey="value" fill="#8884d8" />
        <XAxis dataKey="address" />
        <YAxis />
      </LineChart>
    </>
  );
}

root.render(<App />);
