mishtee_css = """
/* Import premium fonts */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Inter:wght@300;400&display=swap');

/* Main Container: Off-White Background */
.gradio-container {
    background-color: #FAF9F6 !important;
    font-family: 'Inter', sans-serif !important;
    color: #333333 !important;
}

/* Headings: Spaced-out Serif */
h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    letter-spacing: 0.05em !important;
    font-weight: 400 !important;
    text-transform: uppercase !important;
    border-bottom: 1px solid #333333;
    padding-bottom: 0.5rem;
    margin-bottom: 2rem !important;
}

/* Sharp Edges and Thin Borders */
button, input, textarea, .form, .block {
    border-radius: 0px !important;
    border: 1px solid #333333 !important;
    box-shadow: none !important;
}

/* Buttons: Sober Terracotta */
button.primary {
    background-color: #C06C5C !important;
    color: white !important;
    border: none !important;
    font-family: 'Playfair Display', serif !important;
    letter-spacing: 0.1em !important;
    transition: opacity 0.3s ease;
}

button.primary:hover {
    opacity: 0.9;
    background-color: #C06C5C !important;
}

/* Tables: Lightweight Sans-Serif */
table, thead, tbody, tr, td, th {
    font-family: 'Inter', sans-serif !important;
    font-weight: 300 !important;
    font-size: 0.9rem !important;
    border-collapse: collapse !important;
}

/* Layout Padding and Whitespace */
.gap {
    gap: 40px !important;
}

.block {
    padding: 20px !important;
    margin-bottom: 20px !important;
}

/* Remove default Gradio highlights */
.selected {
    border: 1px solid #C06C5C !important;
}
"""
