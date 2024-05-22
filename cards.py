import pandas as pd
import streamlit as st
import sqlite3


cards_data2 = [
    {"title": "Amex", "content": "American Express", "image": "https://raw.githubusercontent.com/ishan-0611/Python-projects/main/black-credit-card_1017-6276.jpg.avif", "caption": "Amex Card ending in 9101"},
    {"title": "Discover", "content": "Travel Discover Card", "image": "https://raw.githubusercontent.com/ishan-0611/Python-projects/main/realistic-credit-card-template_23-2149137814.jpg.avif", "caption": "Discover Card ending in 1121"},
]


def create_card(title, content, image, caption):
    st.markdown(
        f"""
        <div style="width: 300px; margin-bottom: 20px; border: 1px solid #ddd; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s;">
            <img src="{image}" alt="{title}" style="width:100%">
            <div style="padding: 16px;">
                <h4 style="margin: 0;"><b>{title}</b></h4>
                <p>{content}</p>
            </div>
            <div style="text-align:center; padding: 10px; background-color: #f1f1f1;">
                {caption}
            </div>
        </div>
        <style>
            .card:hover {{
                box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
            }}
        </style>
        """,
        unsafe_allow_html=True
    )


def get_credit_cards(userID):
    conn = sqlite3.connect('CreditX.db')
    c = conn.cursor()
    c.execute('Select CardID, Name, CardNo, Bank, Balance FROM CARDS WHERE UserID = ?', (userID,))
    cards = c.fetchall()
    conn.close()
    return cards


def add_credit_card(userID, Name, CardNo, Bank, Balance):
    conn = sqlite3.connect('CreditX.db')
    c = conn.cursor()
    c.execute('Insert into CARDS(UserID, Name, CardNo, Bank, Balance) values(?,?,?,?,?);',(userID, Name, CardNo, Bank, Balance))
    conn.commit()
    conn.close()


def update_balance(CardID, new_balance):
    conn = sqlite3.connect('CreditX.db')
    c = conn.cursor()
    c.execute('Update CARDS set Balance = ? where CardID = ?', (new_balance, CardID))
    conn.commit()
    conn.close()


def cards_page(userID, name):
    st.subheader('Manage your Credit Cards :credit_card:')

    balance_tab, view_cards, add_cards = st.tabs(['**Balance**', '**View Credit Cards**', '**Add Credit Cards**'])
    with add_cards:
        st.subheader('**Enter your details**')
        with st.form('add_card'):
            card_no = st.text_input('**Enter Card Number**')
            bank = st.text_input('**Enter Bank Name**')
            balance = st.text_input('**Enter Balance**')
            submitted = st.form_submit_button('Add Credit Card')

            if submitted:
                add_credit_card(userID, name, card_no, bank, balance)
                st.success('Credit Card Added.')

    with view_cards:
        st.subheader('Your Credit Cards')
        cards = get_credit_cards(userID)
        if cards:
            card_df = pd.DataFrame(cards, columns=['CardID', 'Name', 'CardNo', 'Bank', 'Balance'])
            st.dataframe(card_df.drop(columns=['CardID']))
        else:
            st.info('No Credit Cards Found. Please Add a Credit Card.')

        st.markdown("---")
        st.subheader("Credit Card Options")
        for i in range(0, len(cards_data2), 2):
            cols = st.columns(2)
            for col, card_data in zip(cols, cards_data2[i:i + 2]):
                with col:
                    create_card(card_data['title'], card_data['content'], card_data['image'], card_data['caption'])

    with balance_tab:
        st.subheader('Balance Overview')
        cards = get_credit_cards(userID)
        if cards:
            for card in cards:
                card_id, name, cardno, bank, balance = card
                st.write(f"**{name}** - **{cardno}** **({bank})**")
                new_bal = st.number_input(f'Update Balance for {cardno}', min_value=0, value=balance, key=f'balance_{card_id}')
                if st.button(f'Update Balance', key=f'update_{card_id}'):
                    update_balance(card_id, new_bal)
                    st.success(f'Balance Updated for card {card_no}')
                    st.rerun()
        else:
            st.info('No Credit Cards Found. Please Add a Credit Card.')
