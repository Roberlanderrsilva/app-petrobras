import streamlit as st

st.set_page_config(page_title="Simulado Petrobras - Cesgranrio", layout="centered")

# Estilo para botões grandes e limpos
st.markdown("""
    <style>
    div.stButton > button:first-child { width: 100%; height: 3em; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚓ Mentor Petrobras")
st.write("---")

# Banco de Dados padrão Cesgranrio (ABCDE)
questoes = [
    {
        "enunciado": "Em uma instalação industrial, a norma que estabelece os requisitos e condições mínimas objetivando a implementação de medidas de controle e sistemas preventivos, de forma a garantir a segurança e a saúde dos trabalhadores que, direta ou indiretamente, interajam em instalações elétricas e serviços com eletricidade é a:",
        "opcoes": [
            "A) NR-10",
            "B) NR-12",
            "C) NR-13",
            "D) NR-33",
            "E) NR-35"
        ],
        "correta": "A) NR-10",
        "explicacao": "A NR-10 é a norma específica para segurança em instalações e serviços em eletricidade."
    },
    {
        "enunciado": "No que se refere ao transporte de fluidos, o equipamento dinâmico que tem por finalidade transformar energia mecânica em energia de pressão, cedendo esta última ao fluido líquido, é denominado:",
        "opcoes": [
            "A) Compressor alternativo",
            "B) Compressor centrífugo",
            "C) Bomba centrífuga",
            "D) Ejetor",
            "E) Turbina a vapor"
        ],
        "correta": "C) Bomba centrífuga",
        "explicacao": "Bombas são para líquidos; compressores são para gases e vapores."
    }
]

# Inicialização do estado
if 'indice' not in st.session_state:
    st.session_state.indice = 0
    st.session_state.mostrar_explica = False

q = questoes[st.session_state.indice]

# Layout da Questão
st.subheader(f"Questão {st.session_state.indice + 1}")
st.info(q["enunciado"])

resposta = st.radio("Escolha a alternativa correta:", q['opcoes'], key=f"rad_{st.session_state.indice}")

col1, col2 = st.columns(2)

with col1:
    if st.button("Confirmar"):
        if resposta == q['correta']:
            st.success("✅ CORRETO!")
        else:
            st.error(f"❌ INCORRETO!")
        st.session_state.mostrar_explica = True

with col2:
    if st.button("Próxima ➡️"):
        if st.session_state.indice < len(questoes) - 1:
            st.session_state.indice += 1
            st.session_state.mostrar_explica = False
            st.rerun()
        else:
            st.warning("Fim do simulado de teste!")

if st.session_state.mostrar_explica:
    st.help(f"**Explicação:** {q['explicacao']}")
