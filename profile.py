import streamlit as st
import sqlite3
import plotly.graph_objs as go


def get_user_details(UserID):
    conn = sqlite3.connect('CreditX.db')
    c = conn.cursor()
    c.execute('Select UserID, Name, Password from USER where UserID = ?;', (UserID,))
    user_details = c.fetchone()
    conn.close()
    return user_details


def update_user_details(UserID, Name, Password):
    conn = sqlite3.connect('CreditX.db')
    c = conn.cursor()
    c.execute('Update USER set Name = ?, Password = ? where UserID = ?;', (Name, Password, UserID))
    conn.commit()
    conn.close()


def get_credit_card_stats(UserID):
    conn = sqlite3.connect('CreditX.db')
    c = conn.cursor()
    c.execute('Select COUNT(*), SUM(Balance) from CARDS where UserID = ?', (UserID,))
    stats = c.fetchone()
    conn.close()
    return stats if stats else (0, 0)


def profile_page(userID, name):
    st.subheader('Your Profile :sunglasses:')

    details_tab, update_tab = st.tabs(['**View Details**', '**Update Details**'])
    with details_tab:
        user_details = get_user_details(userID)
        if user_details:
            masked_password = '*' * len(user_details[2])
            st.markdown(f'**User ID** : {user_details[0]}')
            st.markdown(f'**User Name** : {user_details[1]}')

            card_stats = get_credit_card_stats(userID)
            st.markdown(f'**Number of Credit Cards** : {card_stats[0]}')
            st.markdown(f'**Total Balance across all Credit Cards** : {card_stats[1]}')

            fig = go.Figure(go.Indicator(
                mode='number+gauge',
                value=card_stats[1],
                gauge={'axis': {'range': [0, 50000]}},
                title={'text': "Total Balance"},
                domain={'x': [0, 1], 'y': [0, 1]}
            ))
            st.plotly_chart(fig, use_container_width=True)

        else:
            st.info('No User Details Found.')

    with update_tab:
        user_details = get_user_details(userID)
        if user_details:
            with st.form('update_form'):
                new_name = st.text_input('**Enter Name**', value=user_details[1])
                new_password = st.text_input('**Enter Password**', value=user_details[2], type='password')
                submitted = st.form_submit_button('Update Details')

                if submitted:
                    update_user_details(userID, new_name, new_password)
                    st.success('Details Updated Successfully.')
                    st.rerun()

        else:
            st.info('No User Details Found.')
