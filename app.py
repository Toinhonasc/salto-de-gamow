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
    st.title("🎓 Como Jogar (Tutorial)")
    st.markdown("### Objetivo: Escapar do Núcleo")
    
    st.info("Sua missão é fazer a partícula (bolinha vermelha) atravessar a parede (azul).")

    st.markdown("### 🎮 Controles")
    st.markdown("1.  **Botão Vermelho Gigante**: No jogo, haverá um botão grande escrito **'INJETAR ENERGIA'**. Ou use a tecla **ESPAÇO** do teclado.")
    st.markdown("2.  **Segurar o Botão**: Aumenta a energia da partícula.")
    st.markdown("3.  **Soltar o Botão**: Economiza bateria.")

    st.markdown("### ⚠️ A Estratégia")
    col1, col2 = st.columns(2)
    with col1:
        st.error("❌ **NÃO SEGURE O TEMPO TODO!**")
        st.write("Isso acaba com sua bateria instantaneamente e você perde.")
    with col2:
        st.success("✅ **TENHA PACIÊNCIA**")
        st.write("Espere a 'parede' ficar fina (pulsando). Só injete energia nesse momento exato.")

    st.markdown("---")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjEx.../giphy.gif", caption="Exemplo: Espere a barreira diminuir!") # Placeholder visualization if real one existed
    st.write("Pronto? Vá para a aba **'🎮 Desafio de Gamow'** e clique no botão **Começar Missão**.")

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
