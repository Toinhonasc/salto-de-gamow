import streamlit as st
import streamlit.components.v1 as components
import os

# Configuração da Página
st.set_page_config(
    page_title="O Salto de Gamow - Simulador",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização Customizada
st.markdown("""
<style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1 {
        color: #e33f46;
    }
    .stAlert {
        background-color: #1a1c24;
        color: #e8eaee;
        border: 1px solid #2a2d36;
    }
</style>
""", unsafe_allow_html=True)

# Barra Lateral - Navegação e Contexto
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/George_Gamow.jpg/220px-George_Gamow.jpg", caption="George Gamow")
    st.title("O Salto de Gamow")
    st.markdown("---")
    st.write("Um playground interativo para explorar o **Tunelamento Quântico** e o **Decaimento Alfa**.")
    
    st.header("Tópicos")
    page = st.radio("Navegar por:", ["Simulador Interativo", "Fundamentos Teóricos", "Sobre o Projeto"])

    st.markdown("---")
    st.caption("Desenvolvido para ensino de Física Moderna.")

# Página: Simulador
if page == "Simulador Interativo":
    st.title("⚛️ Laboratório de Tunelamento")
    st.markdown("""
    Experimente controlar uma partícula alfa presa no núcleo atômico. 
    Ajuste a **Energia (E)** e a **Barreira ($V_0$)** para ver a mágica da Mecânica Quântica acontecer.
    """)

    # Carregar o arquivo HTML local
    # Lendo o arquivo index.html que está no mesmo diretório
    file_path = os.path.join(os.path.dirname(__file__), 'index.html')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        # Ajustar altura do iframe para caber o simulador sem scroll duplo
        components.html(html_content, height=850, scrolling=False)
        
    except FileNotFoundError:
        st.error("Erro: O arquivo 'index.html' não foi encontrado no diretório.")

    st.info("💡 **Dica:** No modo 'Arcade', tente escapar o mais rápido possível ajustando os parâmetros estrategicamente!")

# Página: Teoria
elif page == "Fundamentos Teóricos":
    st.title("📚 Fundamentos do Decaimento Alfa")
    
    st.markdown("### O Que é o Salto de Gamow?")
    st.write("""
    Em 1928, **George Gamow** resolveu um mistério que a física clássica não conseguia explicar: 
    *Como uma partícula alfa escapa de um núcleo atômico se ela não tem energia suficiente para pular a barreira de potencial?*
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Visão Clássica ❌")
        st.write("Imagine uma bola em um buraco fundo. Se você não chutá-la forte o suficiente (Energia < Altura da Borda), ela **nunca** sairá. Ela bate e volta para sempre.")
        
    with col2:
        st.markdown("#### Visão Quântica ✅")
        st.write("Na mecânica quântica, a partícula se comporta como uma **onda**. Mesmo que a barreira seja alta, existe uma pequena probabilidade da onda 'vazar' para o outro lado.")

    st.markdown("---")
    
    st.markdown("### A Fórmula da Probabilidade")
    st.latex(r'''
    T \approx e^{-2k_2 a}
    ''')
    st.write("Onde:")
    st.markdown("- **$T$**: Probabilidade de transmissão (escapar).")
    st.markdown("- **$a$**: Largura da barreira (o quão 'gorda' é a parede).")
    st.markdown("- **$k_2$**: Depende da diferença entre a altura da barreira ($V_0$) e a energia da partícula ($E$).")
    
    st.success("""
    **Conclusão Impactante:** Uma pequena mudança na energia ou na largura da barreira causa uma mudança **exponencial** na probabilidade de escape. 
    Isso explica por que alguns elementos radioativos demoram bilhões de anos para decair, enquanto outros duram frações de segundo!
    """)

# Página: Sobre
elif page == "Sobre o Projeto":
    st.title("ℹ️ Sobre")
    st.write("""
    Este simulador foi criado para tornar visível o invisível. Através da interatividade, 
    buscamos construir uma intuição sobre fenômenos quânticos complexos.
    """)
    st.markdown("### Tecnologias Usadas")
    st.write("- **HTML5 Canvas**: Para renderização de alta performance.")
    st.write("- **JavaScript**: Para a física da simulação (Cálculo de função de onda e probabilidades).")
    st.write("- **Streamlit**: Para a estrutura da aplicação web e narrativa educacional.")
