import streamlit as st
 
st.title('Departments')
 
# Create tabs
tab_titles = ['HR Support', 'IT Support', 'Transportation Support']
tabs = st.tabs(tab_titles)
 
import streamlit as st

# ---- Session state initialization ----
if 'HR_tickets' not in st.session_state:
    st.session_state['HR_tickets'] = []

if 'IT_tickets' not in st.session_state:
    st.session_state['IT_tickets'] = []

if 'Transport_tickets' not in st.session_state:
    st.session_state['Transport_tickets'] = []


# Add content to each tab...
with tabs[0]:
    st.header('HR Support tickets')
    for i, ticket in enumerate(st.session_state['HR_tickets'], start=1):
        st.write(f"{i} : {ticket}")

with tabs[1]:
    st.header('IT Support tickets')
    for i, ticket in enumerate(st.session_state['IT_tickets'], start=1):
        st.write(f"{i} : {ticket}")

with tabs[2]:
    st.header('Transportation Support tickets')
    for i, ticket in enumerate(st.session_state['Transport_tickets'], start=1):
        st.write(f"{i} : {ticket}")
    
 