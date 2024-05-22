import time

import streamlit as st
import sqlite3
from datetime import datetime


def get_credit_cards(userID):
    conn = sqlite3.connect('CreditX.db')
    c = conn.cursor()
    c.execute('Select CardID, Name, CardNo, Bank, Balance FROM CARDS WHERE UserID = ?', (userID,))
    cards = c.fetchall()
    conn.close()
    return cards


def update_balance(CardID, new_balance):
    conn = sqlite3.connect('CreditX.db')
    c = conn.cursor()
    c.execute('Update CARDS set Balance = ? where CardID = ?', (new_balance, CardID))
    conn.commit()
    conn.close()


def create_payment(UserID, Name, PaymentAmt, Recipient, CardNo, Date):
    conn = sqlite3.connect('CreditX.db')
    c = conn.cursor()
    c.execute('Insert into PAYMENTS(UserID, Name, PaymentAmt, Recipient, CardNo, Date) values'
              '(?,?,?,?,?,?);', (UserID, Name, PaymentAmt, Recipient, CardNo, Date))
    conn.commit()
    conn.close()


def process_payment(sender_id, recipient_card_no, payment_amt):
    conn = sqlite3.connect('CreditX.db')
    c = conn.cursor()

    c.execute('Select CardID, Balance from CARDS where UserID = ? and Balance >= ?;', (sender_id, payment_amt))
    sender_card = c.fetchone()

    if not sender_card:
        conn.close()
        return False, 'Insufficient Funds'

    sender_card_id, sender_balance = sender_card

    c.execute('Select CardId, Balance from Cards where CardNo = ?;', (recipient_card_no,))
    recipient_card = c.fetchone()

    if not recipient_card:
        conn.close()
        return False, 'Recipient Card Not Found'

    recipient_card_id, recipient_balance = recipient_card

    new_sender_balance = sender_balance - payment_amt
    new_recipient_balance = recipient_balance + payment_amt

    c.execute('Update CARDS Set Balance = ? where CardID = ?;', (new_sender_balance, sender_card_id))
    c.execute('Update CARDS Set Balance = ? where CardID = ?;', (new_recipient_balance, recipient_card_id))
    conn.commit()

    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute('Select Name, CardNo from CARDS where CardID = ?', (sender_card_id,))
    sender_name, sender_card_no = c.fetchone()
    create_payment(sender_id, sender_name, payment_amt, recipient_card_no, sender_card_no, date)
    conn.close()
    return True, 'Payment Successful'


def payments_page(userID, Name):
    st.subheader('Payment Portal :moneybag:')

    with st.form('payment_form'):
        recipient_card_no = st.text_input('**Recipient Card Number**')
        payment_amt = st.number_input('**Payment Amount**', min_value=0)
        submitted = st.form_submit_button('Make Payment')

        if submitted:
            success, message = process_payment(userID, recipient_card_no, payment_amt)
            if success:
                st.success(message)
                time.sleep(0.5)
                st.balloons()
            else:
                st.error(message)
