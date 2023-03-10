/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/**/*.{html,js}',
],
  theme: {
    extend: {
      colors: {
        'background-color': '#000',
        'primary-color': '#81ff33',
        'secondary-color': '#d1ff00',
        'highlight-color': '#fff',
      },
      fontFamily: {
        'clash-display-regular': ['Clash Display Regular'],
        'clash-display-bold': ['Clash Display Bold'],
        'clash-display-extralight': ['Clash Display Extralight'],
        'clash-display-light': ['Clash Display Light'],
        'clash-display-medium': ['Clash Display Medium'],
        'clash-display-semi-bold': ['Clash Display Semi Bold'],

    },
  },
  plugins: [],
}
}
