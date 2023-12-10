module.exports = {
  rules: [
    {
      test: /\.js$/,
      enforce: "pre",
      use: ["source-map-loader"],
    },
  ],
  ignoreWarnings: [/Failed to parse source map/],
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}