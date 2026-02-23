import streamlit as st
import random

# 1. CONFIGURAÇÃO (Sempre a primeira coisa)
st.set_page_config(page_title="Mentor Petrobras", layout="centered")

# 2. SISTEMA DE CORES
if 'tema' not in st.session_state:
    st.session_state.tema = "Fundo Escuro"

st.sidebar.title("Configurações do Mentor")
st.session_state.tema = st.sidebar.radio("Escolha o contraste:", ["Fundo Escuro", "Fundo Claro"])

if st.session_state.tema == "Fundo Escuro":
    cor_fundo_box = "#121212"
    cor_texto_quest = "#FACC15"
else:
    cor_fundo_box = "#F0F2F6"
    cor_texto_quest = "#1E3A8A"

# 3. CABEÇALHO
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Petrobras_logo.svg/1200px-Petrobras_logo.svg.png", width=150)
st.title("⚓ Mentor Petrobras")
st.write("---")

# 4. BANCO DE DADOS (Coloquei 2 de exemplo, você completa com as suas)
if 'questoes_db' not in st.session_state:
    db_original = [
        {
            "enunciado": "Qual o principal processo de separação física em uma refinaria?",
            "opcoes": ["Craqueamento", "Destilação", "Hidrotratamento", "Alquilação"],
            "correta": "Destilação",
            "explicacao": "A destilação separa os componentes do petróleo por calor e pontos de ebulição."
        },
        {
            "enunciado": "O que o Hidrotratamento (HDT) remove do combustível?",
            "opcoes": ["Água", "Sal", "Enxofre", "Areia"],
            "correta": "Enxofre",
            "explicacao": "O HDT é usado para remover contaminantes como enxofre e nitrogênio."
        }
    ]
    random.shuffle(db_original)
    st.session_state.questoes_db = db_original

questoes = st.session_state.questoes_db

# 5. LÓGICA DO APP
if 'indice' not in st.session_state:
    st.session_state.indice = 0
    st.session_state.mostrar_explica = False

if st.session_state.indice < len(questoes):
    q = questoes[st.session_state.indice]
    st.subheader(f"Questão {st.session_state.indice + 1} de {len(questoes)}")
    
    st.markdown(f"""
        <div style="background-color: {cor_fundo_box}; padding: 20px; border-radius: 12px; border: 3px solid #3b82f6; margin-bottom: 20px;">
            <p style="color: {cor_texto_quest}; font-size: 20px; font-weight: bold; line-height: 1.6; margin: 0;">
                {q['enunciado']}
            </p>
        </div>
        """, unsafe_allow_html=True)

    resposta = st.radio("Escolha a alternativa:", q['opcoes'], key=f"rad_{st.session_state.indice}")

    if st.button("Confirmar Resposta"):
        if resposta == q['correta']:
            st.success("✅ CORRETO!")
        else:
            st.error(f"❌ INCORRETO! A resposta certa era: {q['correta']}")
        st.session_state.mostrar_explica = True

    if st.session_state.mostrar_explica:
        st.info(f"**Explicação:** {q['explicacao']}")
        if st.button("Próxima Questão ➡️"):
            st.session_state.indice += 1
            st.session_state.mostrar_explica = False
            st.rerun()
else:
    st.balloons()
    st.success("🎉 Você concluiu o bloco!")
    if st.button("Recomeçar"):
        del st.session_state.questoes_db
        st.session_state.indice = 0
        st.session_state.mostrar_explica = False
        st.rerun()
        
