/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./*.html",
    "./*.js"
  ],
  darkMode: "class",
  theme: {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "surface-container-lowest": "#ffffff",
                    "on-secondary": "#ffffff",
                    "inverse-on-surface": "#f1f0f5",
                    "error": "#ba1a1a",
                    "tertiary-fixed": "#ffdbcc",
                    "outline-variant": "#c1c6d7",
                    "primary": "#0058bc",
                    "on-primary-container": "#fefcff",
                    "on-background": "#1a1b1f",
                    "surface-bright": "#faf9fe",
                    "surface-dim": "#dad9df",
                    "on-secondary-container": "#646464",
                    "on-tertiary": "#ffffff",
                    "on-secondary-fixed-variant": "#474747",
                    "outline": "#717786",
                    "on-primary-fixed": "#001a41",
                    "on-error-container": "#93000a",
                    "tertiary-fixed-dim": "#ffb595",
                    "on-primary-fixed-variant": "#004493",
                    "surface-container-low": "#f4f3f8",
                    "surface-tint": "#005bc1",
                    "on-surface": "#1a1b1f",
                    "surface-container-highest": "#e3e2e7",
                    "surface": "#faf9fe",
                    "on-tertiary-fixed": "#351000",
                    "secondary-fixed": "#e2e2e2",
                    "primary-container": "#0070eb",
                    "secondary": "#5e5e5e",
                    "surface-container-high": "#e9e7ed",
                    "secondary-container": "#e2e2e2",
                    "error-container": "#ffdad6",
                    "on-error": "#ffffff",
                    "on-primary": "#ffffff",
                    "on-surface-variant": "#414755",
                    "primary-fixed": "#d8e2ff",
                    "surface-variant": "#e3e2e7",
                    "surface-container": "#eeedf3",
                    "inverse-surface": "#2f3034",
                    "inverse-primary": "#adc6ff",
                    "tertiary-container": "#c64f00",
                    "on-secondary-fixed": "#1b1b1b",
                    "on-tertiary-fixed-variant": "#7c2e00",
                    "on-tertiary-container": "#fffbff",
                    "background": "#faf9fe",
                    "tertiary": "#9e3d00",
                    "primary-fixed-dim": "#adc6ff",
                    "secondary-fixed-dim": "#c6c6c6"
            },
            "borderRadius": {
                    "DEFAULT": "0.25rem",
                    "lg": "0.5rem",
                    "xl": "0.75rem",
                    "full": "9999px"
            },
            "spacing": {
                    "margin-desktop": "64px",
                    "section-gap": "120px",
                    "gutter": "24px",
                    "container-max": "1280px",
                    "unit": "8px",
                    "margin-mobile": "20px"
            },
            "fontFamily": {
                    "body-lg": ["Inter"],
                    "display-lg": ["Hanken Grotesk"],
                    "display-lg-mobile": ["Hanken Grotesk"],
                    "headline-md": ["Hanken Grotesk"],
                    "body-md": ["Inter"],
                    "label-caps": ["Geist"],
                    "headline-sm": ["Hanken Grotesk"]
            },
            "fontSize": {
                    "body-lg": ["18px", {"lineHeight": "1.6", "fontWeight": "400"}],
                    "display-lg": ["64px", {"lineHeight": "1.1", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                    "display-lg-mobile": ["40px", {"lineHeight": "1.1", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                    "headline-md": ["32px", {"lineHeight": "1.2", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                    "body-md": ["16px", {"lineHeight": "1.5", "fontWeight": "400"}],
                    "label-caps": ["12px", {"lineHeight": "1", "letterSpacing": "0.05em", "fontWeight": "600"}],
                    "headline-sm": ["24px", {"lineHeight": "1.3", "fontWeight": "600"}]
            }
          },
        },
      }.theme,
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/container-queries')
  ],
}
