const path = require('path');

module.exports = {
    entry: {
        analysis: path.join(__dirname, "core", "ui", "analysis.tsx"),
        tools: path.join(__dirname, "core", "ui", "tools.tsx"),
    },
    output: {
        filename: '[name].js',
        path: path.resolve(__dirname, "core", "static", "js"),
    },
    module: {
    rules: [
      {
        test: /\.?ts|tsx$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react', '@babel/preset-typescript']
          }
        }
      },
    ]
  },
}