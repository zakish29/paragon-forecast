import streamlit as st

def run():
    linkedin = 'https://www.linkedin.com/in/zaki-syaiful-hunafa-a6a759b8/'
    github = 'https://github.com/zakish29'

    # Display  bio and icons with links
    st.title('About Me')
    st.write("""
As an experienced Project Manager and Junior Data Scientist, I bring a wealth of expertise and skills to the table. With a proven track record of successfully evaluating and enhancing business systems for top-tier organizations, I am dedicated to driving results and achieving project goals. As a natural leader and effective communicator, I excel at managing cross-functional teams and leveraging my end-to-end IT management knowledge to deliver high-quality work.

In addition to my project management skills, I possess hands-on experience with coding languages such as SQL and Python, as well as visualization tools like Tableau and Google Data Studio. My hands-on experience also covers infrastructure management using Google Cloud Platform, as well as spreadsheet tools like Microsoft Excel and Google Sheets.

My ability to research and analyze complex business processes and procedures, and design and implement solutions, sets me apart from other candidates. I am committed to leveraging my diverse skillset to deliver optimal results and drive business success. Let's work together to achieve your project goals and take your organization to new heights.
""")

    col1, col2= st.columns(2)

    with col1:
        st.image('linkedin.png', width=50)
        st.markdown(f'<a href="{linkedin}" target="_blank">LinkedIn</a>', unsafe_allow_html=True)

    with col2:
        st.image('github.png', width=50)
        st.markdown(f'<a href="{github}" target="_blank">GitHub</a>', unsafe_allow_html=True)
   

# calling function
if __name__ == '__main__':
   run()