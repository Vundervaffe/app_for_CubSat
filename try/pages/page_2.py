import streamlit as st
from PIL import Image

arduino = Image.open("pictures\Arduino_Uno.png")


tab1, tab2, tab3 = st.tabs(["Концепция и проектирование", "Компоненты и системы", "Тестирование и запуск"])

with tab1:
    st.header("Концепция и проектирование")

with tab2:
    st.header("Компоненты и системы") 
    st.write('''Большинство проектов будет реализовано на плате Arduino Uno.''' )
    st.image(arduino)

    col1, col2 = st.columns(2)

    with col1:
        st.write('''<div>Микроконтроллер</div>
                    <div>Рабочее напряжение</div>
                    <div>Входное напряжение (рекомендуемое)</div>
                    <div>Входное напряжение (предельное)</div>
                    <div>Цифровые Входы/Выходы</div>
                    <div>Аналоговые входы</div>
                    <div>Постоянный ток через вход/выход</div>
                    <div>Постоянный ток для вывода</div>
                    <div>Флеш-память</div>
                    <div></div>
                    <div>ОЗУ</div>
                    <div>EEPROM(ATmega328)</div>
                    <div>Тактовая частота</div>''', unsafe_allow_html = True)
    with col2:
        st.write('''<div>ATmega328</div>
                    <div>5 В</div>
                    <div>7-12 В</div>
                    <div>6-20 В</div>
                    <div>14 (6 из которых могут быть ШИМ)</div>
                    <div>6</div>
                    <div>40 мА</div>
                    <div>3.3 В 50 мА</div>
                    <div>32 Кб (ATmega328), 0.5 Кб для загрузчика</div>
                    <div>2 Кб (ATmega328)</div>
                    <div>1 Кб (ATmega328)</div>
                    <div>16 МГц</div>''', unsafe_allow_html = True)
    
    st.write('''<div>Для программирования платы нужно использовть Arduino IDE</div>''' )
with tab3:
    st.header("Тестирование и запуск")