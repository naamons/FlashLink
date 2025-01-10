import streamlit as st
import time

# Set the page configuration
st.set_page_config(
    page_title="FlashLink: TriCore ECU Reader/Writer",
    page_icon="🔌",
    layout="centered",
    initial_sidebar_state="auto",
)

# Initialize session state variables
if 'current_step' not in st.session_state:
    st.session_state['current_step'] = 1  # Start with Step 1

# Define total number of steps
TOTAL_STEPS = 4

# Function to reset the app
def reset_app():
    st.session_state['current_step'] = 1
    st.experimental_rerun()

# Step 1: Identify ECU
def step_identify_ecu():
    with st.spinner('🔄 Identifying ECU...'):
        time.sleep(3)  # Simulate time delay
    st.session_state['current_step'] = 2

# Step 2: Read ECU
def step_read_ecu():
    st.session_state['current_step'] = 2.1  # Intermediate state for reading
    reading_log_placeholder = st.empty()
    progress_bar = st.progress(0)
    steps = [
        "Initializing TriCore ECU interface...",
        "Establishing communication protocols...",
        "Reading sector 1/2...",
        "Sector 1/2 read successfully.",
        "Reading sector 2/2...",
        "Sector 2/2 read successfully.",
        "Verifying data integrity...",
        "Data integrity verified.",
        "Resetting ECU interface...",
        "ECU reset successfully.",
        "Reading complete."
    ]
    total_steps = len(steps)
    log = ">>> TriCore ECU Read Log\n"

    # Define CSS for the scrollable log area and auto-scroll
    scrollable_style = """
    <style>
    .scrollable-log {
        height: 300px;
        overflow-y: scroll;
        background-color: #f5f5f5;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 5px;
        font-family: monospace;
    }
    </style>
    <script>
    function scrollToBottom(id) {
        var element = document.getElementById(id);
        element.scrollTop = element.scrollHeight;
    }
    </script>
    """
    st.markdown(scrollable_style, unsafe_allow_html=True)

    # Unique ID for the log container to target with JavaScript
    log_container_id = "ecu_read_log"

    # Initialize the scrollable log
    reading_log_placeholder.markdown(f"""
    <div id="{log_container_id}" class="scrollable-log">
    ```python
{log}
