# What is this normal fault realy?

This is an interactive Streamlit web application that visually demonstrates a 2D geological cross-section and the movement of a normal fault.

## Features
- Three colored geological layers: Pinkstone, Greenstone, and Yellowstone
- A diagonal normal fault (135°) dividing the section
- Button to animate the right (east) block moving down along the fault plane
- Clean, modern UI with pastel colors
- All code and visualization runs in your browser using Streamlit

## How to Run
1. Make sure you have Python and Streamlit installed. If not, install Streamlit with:
   ```bash
   pip install streamlit
   ```
2. Save the code as `normal_fault_streamlit.py` in a folder.
3. Open a terminal in that folder and run:
   ```bash
   streamlit run normal_fault_streamlit.py
   ```
4. Your browser will open the app. Click the button to see the normal fault movement.

## Layer Colors (Legend)
- **Pinkstone**: Pink (`#ffd1dc`)
- **Greenstone**: Pastel Green (`#b0eacb`)
- **Yellowstone**: Pastel Yellow (`#fff9b1`)

## How it works
- The first view shows flat, continuous layers.
- When you click the button, the east (right) block moves down along the fault, breaking the layers along the fault plane.
- Click again to return to the original state.

---
Created for educational and demonstration purposes.
