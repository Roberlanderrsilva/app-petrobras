import streamlit as st

st.set_page_config(page_title="Mentor Petrobras", layout="centered")

st.title("⚓ Mentor Petrobras")
st.subheader("Simulado Inteligente")

# Banco de Dados de Perguntas (Podemos poner miles aquí)
questoes = [
    {
        "pergunta": "De acordo com a NR-10, qual o foco principal?",
        "opcoes": ["Estética", "Segurança e Saúde", "Economia", "Iluminação"],
        "correta": "Segurança e Saúde"
    },
    {
        "pergunta": "Qual equipamento é usado para elevar a pressão de um fluido líquido?",
        "opcoes": ["Compressor", "Válvula", "Bomba Centrifuga", "Permutador"],
        "correta": "Bomba Centrifuga"
    },
    {
        "pergunta": "Na estabilidade de navios (Lastro), o que é o Metacentro?",
        "opcoes": ["O fundo do navio", "Um ponto de referência para estabilidade", "O peso da carga", "A âncora"],
        "correta": "Um ponto de referência para estabilidade"
    }
]

# Sistema de navegação simples usando o índice da pergunta
if 'indice' not in st.session_state:
    st.session_state.indice = 0

q = questoes[st.session_state.indice]

st.write(f"### Questão {st.session_state.indice + 1}")
st.write(f"**{q['pergunta']}**")

resposta = st.radio("Escolha a opção:", q['opcoes'], key=f"q_{st.session_state.indice}")

if st.button("Confirmar Resposta"):
    if resposta == q['correta']:
        st.success("✅ Correto!")
    else:
        st.error(f"❌ Errado! A resposta era: {q['correta']}")

# Botão para ir para a próxima
if st.button("Próxima Questão ➡️"):
    if st.session_state.indice < len(questoes) - 1:
        st.session_state.indice += 1
        st.rerun()
    else:
        st.write("🎉 Você terminou o simulado de teste!")
        if st.button("Recomeçar"):
            st.session_state.indice = 0
            st.rerun()
            
