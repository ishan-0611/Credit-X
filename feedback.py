import sqlite3
import streamlit as st


def submit_feedback(userID, name, ui_good, ui_rating, f_good, f_rating, best_f, overall_rating, add_comm):
    conn = sqlite3.connect('CreditX.db')

    try:
        conn.execute("Insert into FEEDBACK(userID, name, ui_good, ui_rating, f_good, f_rating, best_f, ov_rat, comm) values(?,?,?,?,?,?,?,?,?)", (userID, name, ui_good, ui_rating, f_good, f_rating, best_f, overall_rating, add_comm))
        conn.commit()
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()
    return True


def feedback_page(userID, name):
    st.subheader('Feedback Form :man-raising-hand:')

    with st.form("feedback_form"):
        ui_good = st.radio('**Did you like our User Interface ?** :sunglasses:', ['Yes', 'No'], index=None)
        ui_rating = st.slider('**Please Rate our UI**', 0, 5)

        f_good = st.radio('**Did you like our Functionality ?** :sunglasses:', ['Yes', 'No'], index=None)
        f_rating = st.slider('**Please Rate our Functionality**', 0, 5)

        best_f = st.radio('**Which feature did you like the most ?** :sunglasses:',
                          ['Credit Card Management', 'Payments Portal', 'Transactions History', 'User Profile'],
                          index=None)

        overall_rating = st.slider('**Overall Rating of the App**', 0, 10)
        add_comm = st.text_input('**Any Additional Comments...**')

        submitted = st.form_submit_button('Submit your feedback')

        if submitted:
            if submit_feedback(userID, name, ui_good, ui_rating, f_good, f_rating, best_f, overall_rating, add_comm):
                st.success('Feedback Submitted.')
            else:
                st.error('Feedback Not Submitted.')
