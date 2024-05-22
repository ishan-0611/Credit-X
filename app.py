import streamlit as st
from auth import create_user, authenticate_user
from style import info_string

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'userID' not in st.session_state:
    st.session_state.userID = ""
if 'name' not in st.session_state:
    st.session_state.name = ""
if 'password' not in st.session_state:
    st.session_state.password = ""
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'


def login():
    with st.form('login_form'):
        st.markdown('**Enter Login Credentials**')
        userID = st.text_input('Enter UserID')
        name = st.text_input('Enter Name')
        password = st.text_input('Enter Password', type='password')
        submitted = st.form_submit_button('Login')

        if submitted:
            if authenticate_user(userID, name, password):
                st.session_state.authenticated = True
                st.session_state.userID = userID
                st.session_state.name = name
                st.session_state.password = password
                st.rerun()
            else:
                st.error('Invalid Credentials. Please Sign Up.')


def signup():
    with st.form('signup_form'):
        st.markdown('**Enter Sign Up Credentials**')
        userID = st.text_input('Enter UserID')
        name = st.text_input('Enter Name')
        password = st.text_input('Enter Password', type='password')
        submitted = st.form_submit_button('Sign Up')

        if submitted:
            if create_user(userID, name, password):
                st.success('SignUp successful. You can now Login.')
            else:
                st.error('Some of the Credentials already exist.')


if not st.session_state.authenticated:
    st.header(':heavy_dollar_sign: :bank: Credit-X :bank: :heavy_dollar_sign:', divider='grey')

    login_tab, signup_tab = st.tabs(['**Login**', '**Sign Up**'])

    with login_tab:
        login()

    with signup_tab:
        signup()

else:
    st.subheader(':heavy_dollar_sign: :bank: Credit-X :bank: :heavy_dollar_sign:', divider='grey')
    st.sidebar.header(f'Welcome, {st.session_state.name}')
    if 'about' not in st.session_state:
        st.session_state.about = False
    with st.sidebar:
        ab = st.sidebar.button('About')
        if ab:
            st.session_state.about = not st.session_state.about

        if st.session_state.about:
            st.info(info_string)

    b0 = st.sidebar.button('Home')
    b1 = st.sidebar.button('Manage Credit Cards')
    b2 = st.sidebar.button('Payment Portal')
    b3 = st.sidebar.button('Transaction History')
    b4 = st.sidebar.button('User Profile')
    b5 = st.sidebar.button('Feedback Form')

    with st.sidebar:
        logout = st.button('Log Out')
        if logout:
            st.session_state.authenticated = False
            st.rerun()

    st.sidebar.markdown('Developer : **Ishan** **Chaturvedi**')
    st.sidebar.link_button(label='Github', url='https://github.com/ishan-0611')

    # Navigation Logic
    if b0:
        st.session_state.current_page = 'home'
    elif b1:
        st.session_state.current_page = 'cards'
    elif b2:
        st.session_state.current_page = 'payments'
    elif b3:
        st.session_state.current_page = 'history'
    elif b4:
        st.session_state.current_page = 'profile'
    elif b5:
        st.session_state.current_page = 'feedback'

    current_page = st.session_state.current_page

    if current_page == 'home':
        from home import home_page
        home_page()

    elif current_page == 'cards':
        from cards import cards_page
        cards_page(st.session_state.userID, st.session_state.name)

    elif current_page == 'payments':
        from payments import payments_page
        payments_page(st.session_state.userID, st.session_state.name)

    elif current_page == 'history':
        from history import history_page
        history_page(st.session_state.userID, st.session_state.name)

    elif current_page == 'profile':
        from profile import profile_page
        profile_page(st.session_state.userID, st.session_state.name)

    elif current_page == 'feedback':
        from feedback import feedback_page
        feedback_page(st.session_state.userID, st.session_state.name)
