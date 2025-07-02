
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Streamlit arka planı ve başlık rengi
st.markdown("""
    <style>
    .stApp { background-color: #fff; }
    .stButton>button { background-color: #f8bbd0; color: white; font-weight: bold; border-radius: 8px; border: none; }
    h1, h2, h3, h4, h5, h6, .stMarkdown, .stText, .stCaption, .stLegend { color: #f8bbd0 !important; }
    .legend-text { color: #f8bbd0 !important; font-size: 18px; }
    </style>
""", unsafe_allow_html=True)


st.set_page_config(page_title="Normal Fault Simulation", layout="wide")
st.title("What is this normal fault really?")


# Parameters
width = 8
height = 4
margin = 0.2
layer_colors = ['#ffd1dc', '#b0eacb', '#fff9b1']  # Pink, green, yellow (Pinkstone, Greenstone, Yellowstone)
layer_names = ['Pinkstone', 'Greenstone', 'Yellowstone']
fault_angle_deg = 135  # 135 degrees (from top right to bottom left)
fault_angle_rad = np.deg2rad(fault_angle_deg)
fault_x = width/2 + 1.0  # x where fault meets the top (slightly right of center)
slip = 1.0     # slip distance along fault


# Button for movement
if 'moved' not in st.session_state:
    st.session_state.moved = False

if st.button("Click here to see!"):
    st.session_state.moved = not st.session_state.moved


# Calculate fault geometry
fault_top = (fault_x, margin)
fault_bottom = (fault_x - (height - 2*margin) / np.tan(np.pi - fault_angle_rad), height - margin)



# Reverse movement direction (on first click, block moves down)
# Block is flat at first, moves down on click, returns up on second click
if st.session_state.moved:
    dx = -slip * np.cos(fault_angle_rad)
    dy = -slip * np.sin(fault_angle_rad)
else:
    dx = 0
    dy = 0

fig, ax = plt.subplots(figsize=(width, height))
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_aspect('equal')
ax.axis('off')

# Draw layers (left and right of fault)

# Fay boyunca kırılma ile tabaka çizimi

# --- YENİ: Katmanları ve hareketi tam olarak tarif ettiğiniz gibi çiz ---

layer_thickness = (height - 2*margin) / 3
for i in range(3):
    y_top = margin + i * layer_thickness
    y_bot = y_top + layer_thickness

    # Fay düzleminin eğimi
    m = (fault_bottom[1] - fault_top[1]) / (fault_bottom[0] - fault_top[0])
    # Fay ile tabaka üst ve altının kesişim x koordinatları
    x_fault_top = (y_top - fault_top[1]) / m + fault_top[0]
    x_fault_bot = (y_bot - fault_top[1]) / m + fault_top[0]

    if not st.session_state.moved:
        # 1st STATE: All layers flat and continuous
        poly = [
            (margin, y_top),
            (width - margin, y_top),
            (width - margin, y_bot),
            (margin, y_bot)
        ]
        ax.add_patch(Polygon(poly, closed=True, facecolor=layer_colors[i], edgecolor='gray'))
    else:
        # 2nd STATE: East block moves down along the fault
        # West block (left of the fault)
        left_poly = [
            (margin, y_top),
            (x_fault_top, y_top),
            (x_fault_bot, y_bot),
            (margin, y_bot)
        ]
        ax.add_patch(Polygon(left_poly, closed=True, facecolor=layer_colors[i], edgecolor='gray'))

        # East block (right of the fault) - shifted down
        right_poly = [
            (x_fault_top + dx, y_top + dy),
            (width - margin + dx, y_top + dy),
            (width - margin + dx, y_bot + dy),
            (x_fault_bot + dx, y_bot + dy)
        ]
        ax.add_patch(Polygon(right_poly, closed=True, facecolor=layer_colors[i], edgecolor='gray'))

# Draw fault plane
ax.plot([fault_top[0], fault_bottom[0]], [fault_top[1], fault_bottom[1]], color='#b85c2b', lw=3, ls='--', zorder=10)





# Legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='none', marker='s', markersize=15, markerfacecolor=layer_colors[0], label=layer_names[0]),
    Line2D([0], [0], color='none', marker='s', markersize=15, markerfacecolor=layer_colors[1], label=layer_names[1]),
    Line2D([0], [0], color='none', marker='s', markersize=15, markerfacecolor=layer_colors[2], label=layer_names[2]),
    Line2D([0], [0], color='#f8bbd0', lw=3, ls='--', label='Fault plane')
]
leg = ax.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1.02, 0.5), frameon=True)
for text in leg.get_texts():
    text.set_color('#f8bbd0')

st.pyplot(fig)
