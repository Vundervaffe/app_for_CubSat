import streamlit as st
from PIL import Image

arduino = Image.open("pictures\Arduino_Uno.jpg")
milky_way = Image.open("pictures\milky_way.jpg")
earth_from_stratosphere = Image.open("pictures\earth_from_stratosphere.jpg")
habble = Image.open("pictures\habble.jpg")

st.markdown("<h1>CubeSat LearnHub</h1>", unsafe_allow_html = True)
st.sidebar.markdown("# этот раздел о нашем проекте")

st.header("что такое CubeSat LearnHub?")
st.write('''<p>CubeSat LearnHub - учебно-методический комплекс (УМК) 
            по проектированию и разработке учебного макета спутника 
            Барс-3 типа CubeSat. Он обеспечивает удобный доступ к учебным 
            материалам, информации о проекте, примерам проектов студентов и 
            контактной информации.</p>''', unsafe_allow_html = True)


tab1, tab2, tab3 = st.tabs(["Что такое CubeSat", "Основные характеристики CubeSat", "применение CubeSat"])
with tab1:
   st.header("Что такое CubeSat")
   st.write('''<p>Кубсат (CubeSat) - это стандартный тип миниатюрного искусственного
    спутника, который широко используется в космических миссиях. Название "Кубсат" 
    происходит от его формы - это куб со стороной, обычно, 10 см. Кубсаты созданы для 
    сокращения размера, веса и стоимости космических миссий и предоставления доступа к 
    космическому пространству для различных организаций, включая университеты, 
    исследовательские лаборатории и стартапы.</p>''', unsafe_allow_html = True)
   st.image(milky_way)

with tab2:
   st.header("Основные характеристики CubeSat")
   st.write('''<ul>
                <li>Размер: Кубсаты имеют стандартный размер, обычно <em>10 см × 10 см × 10 см</em>,
                хотя существуют и другие варианты размеров, такие как <b>1U</b> (<em>10 см × 10 см × 10
                см</em>), <b>2U</b> (<em>10 см × 10 см × 20 см</em>) и т. д. Они могут быть объединены в стопки 
                для создания больших структур.</li>
                <li>Масса: Кубсаты обладают малой массой, что делает их легкими и доступными 
                для запуска совместно с другими космическими грузами.</li>
                <li>Сборка: Кубсаты обычно легко собираются из стандартных компонентов, что 
                снижает затраты на разработку и изготовление.</li>
                <li>Задачи: Кубсаты могут выполнять разнообразные задачи, включая съемку Земли, 
                исследование атмосферы, изучение космической погоды, коммуникацию и технологические 
                испытания.</li>
                <li>Классификация: В зависимости от размера и массы Кубсаты классифицируют на разные
                типы: <b>1U</b>, <b>2U</b>, <b>3U</b> и так далее. Например, <b>1U</b> Кубсат имеет размер <em>10 см × 10 см × 10 см</em>
                и массу около 1 кг.</li>
                <li>Контроль: В большинстве случаев Кубсаты оборудуются средствами для маневрирования
                 и контроля, которые позволяют управлять их полетом.</li>
                </ul>''', unsafe_allow_html = True)
   st.image(earth_from_stratosphere)

with tab3:
   st.header("применение CubeSat")
   st.write('''<p>Кубсаты стали популярными инструментами для проведения космических исследований
   и миссий, так как они предоставляют доступ к космосу для небольших исследовательских команд 
   и стартапов, которые ранее не могли позволить себе разработку и запуск собственных спутников. 
   Кубсаты активно используются в образовательных исследовательских программных инициативах, которые 
   способствуют привлечению новых специалистов в космическую индустрию.</p>''', unsafe_allow_html = True)
   st.image(habble)