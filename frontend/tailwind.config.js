/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        // Surface values come from CSS variables so the theme (Midnight /
        // Graphite) can switch at runtime without touching components.
        surface: {
          DEFAULT: 'rgb(var(--surface-0) / <alpha-value>)',
          raised: 'rgb(var(--surface-1) / <alpha-value>)',
          overlay: 'rgb(var(--surface-2) / <alpha-value>)',
          border: 'rgb(var(--surface-border) / <alpha-value>)',
        },
        accent: {
          DEFAULT: 'rgb(var(--accent) / <alpha-value>)',
          soft: '#1e3a8a',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'Segoe UI', 'sans-serif'],
        mono: ['JetBrains Mono', 'Consolas', 'monospace'],
      },
      maxWidth: { content: '1440px' },
    },
  },
  plugins: [],
}
