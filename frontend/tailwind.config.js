/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  rules: [
    {
      test: /\.js$/,
      enforce: "pre",
      use: ["source-map-loader"],
    },
  ],
  ignoreWarnings: [/Failed to parse source map/],
  plugins: [require("daisyui")],

  daisyui:{
    themes:["lemonade"],
  }
};