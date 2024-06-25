import streamlit as st
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import time  # Add import for time module

# Initialize session state for login and date/time
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = ""
if 'date' not in st.session_state:
    st.session_state['date'] = None
if 'time' not in st.session_state:
    st.session_state['time'] = None
if 'text_size' not in st.session_state:
    st.session_state['text_size'] = 20
if 'show_additional_info' not in st.session_state:
    st.session_state['show_additional_info'] = False
if 'professional_expert' not in st.session_state:
    st.session_state['professional_expert'] = "Student"  # Default value
if 'show_student_details' not in st.session_state:
    st.session_state['show_student_details'] = False

# Login function
def login(username, password):
    # Simple login logic (username: susmita, password: 12345)
    if username == "susmita" and password == "12345":
        st.session_state['logged_in'] = True
        st.session_state['username'] = username
    else:
        st.error("Incorrect username or password")

# Signup function (for demonstration purposes)
def signup(username, password):
    # Here you would normally save the username and password to a database
    st.success(f"User {username} registered successfully!")

# Page to display student details and data visualization
def student_details():
    st.title("Student Details and Data Visualization")

    # Load the CSV file
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Score': [85, 70, 90, 80]
    })

    # Display the data in a table
    st.subheader("Student Data")
    st.write(df)

    # Data visualization
    st.subheader("Data Visualization")

    # Line chart
    st.write("Line Chart")
    fig, ax = plt.subplots()
    df.plot(kind='line', x='Name', y='Score', ax=ax)
    st.pyplot(fig)

    # Bar chart
    st.write("Bar Chart")
    fig, ax = plt.subplots()
    df.plot(kind='bar', x='Name', y='Score', ax=ax)
    st.pyplot(fig)

    # Pie chart
    st.write("Pie Chart")
    fig, ax = plt.subplots()
    df['Score'].plot(kind='pie', labels=df['Name'], autopct='%1.1f%%', ax=ax)
    st.pyplot(fig)

# Main function to control the app flow
def main():
    st.sidebar.title("Menu")
    menu_option = st.sidebar.selectbox("Select an option", ["Sign In", "Sign Up", "Student Details"])

    if menu_option == "Sign In":
        st.sidebar.title("Login")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        if st.sidebar.button("Login"):
            login(username, password)

    elif menu_option == "Sign Up":
        st.sidebar.title("Sign Up")
        new_username = st.sidebar.text_input("New Username")
        new_password = st.sidebar.text_input("New Password", type="password")
        if st.sidebar.button("Sign Up"):
            signup(new_username, new_password)

    elif menu_option == "Student Details":
        if st.session_state['logged_in']:
            student_details()
        else:
            st.write("Please log in to view student details.")

    st.sidebar.subheader("Professional Expert")
    st.sidebar.radio("Select Expertise", ["Student", "Working", "Others"], key='professional_expert')

    if st.session_state['logged_in']:
        st.title(f"Welcome, {st.session_state['professional_expert']}!")

        st.header("Select Date and Time")
        date = st.date_input("Select a date", datetime.date.today())
        selected_time = st.time_input("Select a time", datetime.datetime.now().time())

        if st.button("Submit Date and Time"):
            st.session_state['date'] = date
            st.session_state['time'] = selected_time
            st.success(f"Date and Time submitted: {date} {selected_time}")

        # Display selected date and time
        if st.session_state['date'] and st.session_state['time']:
            text_size = st.slider("Text Size", 10, 50, st.session_state['text_size'])
            st.session_state['text_size'] = text_size
            st.markdown(f"<h2 style='font-size:{text_size}px;'>Selected Date: {st.session_state['date']}</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='font-size:{text_size}px;'>Selected Time: {st.session_state['time']}</h2>", unsafe_allow_html=True)

        show_info = st.sidebar.checkbox("Show Additional Information", key='show_additional_info')

        if show_info:
            with st.spinner('Loading additional information...'):
                time.sleep(2)  # Simulating a loading time using time module
                st.balloons()
            st.header("Additional Information")
            st.write("The My Account portal helps you to manage your work or school account by setting up and managing your security info, managing your connected organizations and devices, viewing how your organization uses your data.")

    else:
        st.write("Please log in to see the date and time.")

# Custom CSS for background image
page_bg_img = '''
<style>
.stApp {
    background-image: url("https://th.bing.com/th/id/R.64f9aafaff3125789f5f579a156e252c?rik=5AXCG2CLvmklxA&riu=http%3a%2f%2fwww.baltana.com%2ffile%2f7144%2f700x394%2f16%3a9%2fyellow-flower-pics-07434_511174358.jpg&ehk=bKwUpcRb4vyXrQcTelNAL1SV3%2f5mQUj9GA7lpusw3Jw%3d&risl=&pid=ImgRaw&r=0");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
'''

# Inject the CSS into the Streamlit app
st.markdown(page_bg_img, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
