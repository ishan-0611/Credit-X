import streamlit as st
import pandas as pd

cards_data = [
    {"title": "Card 1", "content": "Content for card 1", "caption": "caption"},
    {"title": "Card 2", "content": "Content for card 2"},
    {"title": "Card 3", "content": "Content for card 3"},
    {"title": "Card 4", "content": "Content for card 4"},
    {"title": "Card 5", "content": "Content for card 5"},
    {"title": "Card 6", "content": "Content for card 6"},
]

cards_data2 = [
    {"title": "Visa", "content": "Primary Visa Card", "image": "https://raw.githubusercontent.com/ishan-0611/Python-projects/main/realistic-credit-card-design_23-2149126088.jpg.avif", "caption": "Visa Card ending in 1234"},
    {"title": "MasterCard", "content": "Backup MasterCard", "image": "https://raw.githubusercontent.com/ishan-0611/Python-projects/main/realistic-credit-card-design_23-2149126089.jpg.avif", "caption": "MasterCard ending in 5678"},
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


def upcoming_payments():
    payments = [
        {"Due Date": "2024-05-10", "Amount": 500, "Description": "Credit Card Bill"},
        {"Due Date": "2024-05-15", "Amount": 200, "Description": "Internet Bill"},
        {"Due Date": "2024-05-20", "Amount": 150, "Description": "Water Bill"}
    ]

    st.subheader("Upcoming Payments")
    df = pd.DataFrame(payments)
    st.table(df)


def financial_tips():
    tips = [
        "💡 **Tip 1:** Pay your credit card bills on time to avoid late fees.",
        "💡 **Tip 2:** Monitor your spending and create a budget.",
        "💡 **Tip 3:** Use reward points and cashback offers to save money.",
        "💡 **Tip 4:** Keep track of your credit score regularly."
    ]

    st.subheader("Financial Tips")
    for tip in tips:
        st.markdown(tip)


def home_page():
    financial_tips()

    st.markdown("---")
    st.subheader("Credit Card Options")
    for i in range(0, len(cards_data), 2):
        cols = st.columns(2)
        for col, card_data in zip(cols, cards_data2[i:i + 2]):
            with col:
                create_card(card_data['title'], card_data['content'], card_data['image'], card_data['caption'])

    st.markdown("---")
    upcoming_payments()
