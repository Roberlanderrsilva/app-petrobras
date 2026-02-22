import streamlit as st

# Configuração da página (Isso ajuda no design limpo)
st.set_page_config(page_title="Mentor Petrobras", layout="centered")

# Título Principal
st.title("⚓ Mentor Petrobras")
st.subheader("Preparatório: Operador de Produção e Lastro")

# Barra Lateral para navegação
with st.sidebar:
    st.header("Configurações")
    cargo = st.selectbox(
        "Escolha seu cargo:",
        ("Operador de Produção", "Operador de Lastro")
    )
    st.write("---")
    st.write("Modo: Estudo Ativo")

# Área de Conteúdo
st.info(f"Estudando para: **{cargo}**")

# Simulação de Questão (Foco em Elétrica/Segurança - Sua área!)
st.markdown("### Questão de Conhecimentos Específicos")
st.write("**De acordo com a NR-10, qual é o foco principal da norma em instalações elétricas?**")

# Alternativas com botões de rádio
alternativas = [
    "A) Apenas a estética da fiação",
    "B) Garantir a segurança e saúde dos trabalhadores",
    "C) Aumentar o desperdício de energia",
    "D) Evitar apenas o uso de ferramentas manuais"
]

resposta = st.radio("Selecione a opção correta:", alternativas)

# Botão de Confirmação
if st.button("Confirmar Resposta"):
    if "B)" in resposta:
        st.success("✅ Resposta Correta! Você dominou esse conceito de NR-10.")
        st.balloons()
    else:
        st.error("❌ Resposta Incorreta. Revise os conceitos fundamentais da NR-10.")

# Rodapé simples
st.markdown("---")
st.caption("Desenvolvido por Roberlande | Foco: Operador Petrobras")
