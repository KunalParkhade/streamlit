import streamlit as st

st.header('st.button')

if st.button('Say hello', type="primary", icon=":material/radio_button_checked:", width="stretch"):
    st.write('Why hello there')
else:
    st.write('Goodbye')

if st.button('Say hello', type="primary", icon=":material/radio_button_checked:"):
    st.write('Why hello there')
else:
    st.write('Goodbye')


left, middle, right = st.columns(3)
if left.button("Plain button", width="stretch"):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="☺️", width="stretch"):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", width="stretch"):
    right.button("You clicked the material button.")