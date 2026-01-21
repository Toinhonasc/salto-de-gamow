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
    
    # Seletor de Modo
    st.header("Modo de Experiência")
    mode = st.radio("Escolha sua jornada:", 
        ["📚 Regras do Jogo", "🎮 Desafio de Gamow (Jogo)", "🔬 Laboratório (Simulação)"]
    )

    st.markdown("---")
    if mode == "🔬 Laboratório (Simulação)":
        st.info("Modo livre para exploração das variáveis físicas sem pressão.")
    elif mode == "🎮 Desafio de Gamow (Jogo)":
        st.warning("Modo desafio com objetivos, níveis e gestão de energia.")

# Página: Regras (Tutorial)
if mode == "📚 Regras do Jogo":
    st.title("📜 Protocolo da Missão")
    st.markdown("### Bem-vindo à Trilha Quântica")
    st.write("Seu objetivo é guiar partículas instáveis para fora do núcleo atômico. Mas cuidado: a física quântica é traiçoeira.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### 1. A Barreira Dinâmica")
        st.write("O núcleo pulsa. A parede (barreira de potencial) fica mais grossa e mais fina. **Só tente escapar quando ela estiver fina!**")
    with col2:
        st.markdown("#### 2. Bateria Nuclear")
        st.write("Dar energia à partícula custa estabilidade. Se sua bateria acabar antes de completar os tunelamentos, o núcleo colapsa.")
    with col3:
        st.markdown("#### 3. Sintonia Fina")
        st.write("Não basta gastar energia. Você precisa sincronizar seu 'Boost' com a oscilação da barreira.")

    st.markdown("---")
    st.success("Tudo pronto? Selecione **'🎮 Desafio de Gamow'** no menu lateral para começar!")

# Página: Game V2
elif mode == "🎮 Desafio de Gamow (Jogo)":
    st.title("🎮 Trilha Quântica")
    components.html(open(os.path.join(os.path.dirname(__file__), 'game.html'), 'r', encoding='utf-8').read(), height=850, scrolling=False)

# Página: Simulação V1 (Original)
elif mode == "🔬 Laboratório (Simulação)":
    st.title("🔬 Laboratório de Tunelamento (Livre)")
    # ... (código existente da simulação)
    file_path = os.path.join(os.path.dirname(__file__), 'index.html')
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            components.html(f.read(), height=850, scrolling=False)
    except FileNotFoundError:
        st.error("Arquivo index.html não encontrado.")

    st.title("ℹ️ Sobre")
    st.write("""
    Este simulador foi criado para tornar visível o invisível. Através da interatividade, 
    buscamos construir uma intuição sobre fenômenos quânticos complexos.
    """)
    st.markdown("### Tecnologias Usadas")
    st.write("- **HTML5 Canvas**: Para renderização de alta performance.")
    st.write("- **JavaScript**: Para a física da simulação (Cálculo de função de onda e probabilidades).")
    st.write("- **Streamlit**: Para a estrutura da aplicação web e narrativa educacional.")
