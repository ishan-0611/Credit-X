import pandas as pd
import streamlit as st
import sqlite3


def get_user_transactions(UserID):
    conn = sqlite3.connect('CreditX.db')
    c = conn.cursor()

    query = '''
    Select PaymentID, PaymentAmt, Recipient, CardNo, Date
    FROM PAYMENTS
    WHERE UserID = ?
    ORDER BY Date DESC;
    '''
    transactions = pd.read_sql(query, conn, params=(UserID,))
    conn.close()
    return transactions


def history_page(userID, name):
    st.subheader('Your Transaction History')

    transactions = get_user_transactions(userID)

    if not transactions.empty:
        st.markdown(f'UserID : **{userID}** , Name : **{name}**')
        st.dataframe(transactions)
    else:
        st.info('No Transaction History Found.')
