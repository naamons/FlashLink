import streamlit as st
import time

# Set the page configuration
st.set_page_config(
    page_title="FlashLink: TriCore ECU Reader/Writer",
    page_icon="🔌",
    layout="centered",
)

# Initialize session state variables
if 'started' not in st.session_state:
    st.session_state['started'] = False

# Define the steps with their descriptions and durations (in seconds)
steps = [
    {"description": "Initializing ECU Interface...", "duration": 10},
    {"description": "Establishing Communication Protocols...", "duration": 10},
    {"description": "Reading Sector 1/2...", "duration": 10},
    {"description": "Reading Sector 2/2...", "duration": 10},
    {"description": "Verifying Data Integrity...", "duration": 10},
    {"description": "Resetting ECU Interface...", "duration": 10},
]

total_steps = len(steps)
total_duration = sum(step["duration"] for step in steps)  # 60 seconds

# Function to start the ECU reading process
def start_process():
    st.session_state['started'] = True

# Function to reset the app
def reset_app():
    st.session_state['started'] = False
    st.experimental_rerun()

# Main Application Logic
def main():
    st.title("🔌 FlashLink: TriCore ECU Reader/Writer App")
    
    # Sidebar Controls
    st.sidebar.header("⚙️ Controls")
    if st.sidebar.button("🔄 Reset App"):
        reset_app()
    
    if not st.session_state['started']:
        st.header("🔍 Step 1: Identify ECU")
        st.write("Click the button below to start the ECU reading process.")
        if st.button("Start ECU Reading"):
            start_process()
    else:
        # Placeholders for spinner, progress, and step description
        spinner_placeholder = st.empty()
        progress_placeholder = st.empty()
        step_placeholder = st.empty()
        
        # Initialize progress
        progress_bar = progress_placeholder.progress(0)
        
        for idx, step in enumerate(steps):
            # Display large spinning icon using an emoji with increased font size
            spinner_placeholder.markdown(
                f"<div style='font-size:100px;'>🔄</div>",
                unsafe_allow_html=True
            )
            
            # Update step description
            step_placeholder.markdown(f"**{step['description']}**")
            
            # Simulate step duration
            for second in range(step['duration']):
                # Calculate progress
                current_progress = ((idx * step['duration']) + second + 1) / total_duration
                progress_bar.progress(current_progress)
                time.sleep(1)
            
            # Update progress to the end of the current step
            current_progress = ((idx + 1) * step['duration']) / total_duration
            progress_bar.progress(current_progress)
            
            # Clear the step description for the next step
            step_placeholder.empty()
        
        # After all steps are completed
        spinner_placeholder.empty()
        progress_placeholder.progress(1.0)
        step_placeholder.markdown("**✅ ECU Reading Complete!**")
        st.info("📤 Information has been successfully read from the ECU.")

# Run the main function
if __name__ == "__main__":
    main()
