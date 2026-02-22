import streamlit as st

st.set_page_config(page_title="Mentor Petrobras", layout="centered")

# --- CABEÇALHO VISUAL ---
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Petrobras_logo.svg/1200px-Petrobras_logo.svg.png", width=150)

st.title("⚓ Mentor Petrobras")
st.markdown("""
    <h3 style='color: #008542;'>Simulado Especialista: Operador de Produção</h3>
    <p><i>Prepare-se com foco na banca Cesgranrio</i></p>
    """, unsafe_allow_html=True)

st.write("---")

# BANCO DE DADOS (10 QUESTÕES)
questoes = [
    {
        "enunciado": "Em uma unidade de processamento de petróleo, as bombas centrífugas são amplamente utilizadas. Para evitar o fenômeno da cavitação em uma bomba centrífuga, o operador deve garantir que:",
        "opcoes": ["A) O NPSH disponível seja menor que o NPSH requerido", "B) O NPSH disponível seja maior que o NPSH requerido", "C) A temperatura do fluido seja aumentada drasticamente", "D) A pressão na sucção seja reduzida ao mínimo", "E) A válvula de descarga esteja totalmente fechada"],
        "correta": "B) O NPSH disponível seja mayor que o NPSH requerido",
        "explicacao": "Cavitação ocorre quando a pressão do líquido cai abaixo da pressão de vapor. Manter o NPSH disponível maior que o requerido evita a formação de bolhas de vapor."
    },
    {
        "enunciado": "No processo de refino, o equipamento utilizado para realizar a troca térmica entre dois fluidos sem que eles se misturem é o:",
        "opcoes": ["A) Torre de destilação", "B) Vaso separador", "C) Permutador de calor", "D) Compressor de pistão", "E) Ejetor de vácuo"],
        "correta": "C) Permutador de calor",
        "explicacao": "Permutadores de calor são essenciais para o controle de temperatura no processamento de petróleo."
    },
    {
        "enunciado": "Sobre o armazenamento de combustíveis, a norma que estabelece os requisitos de segurança para o trabalho em Espaços Confinados, muito comum em limpezas de tanques, é a:",
        "opcoes": ["A) NR-10", "B) NR-13", "C) NR-20", "D) NR-33", "E) NR-35"],
        "correta": "D) NR-33",
        "explicacao": "A NR-33 define as medidas de prevenção e segurança para trabalhos em espaços confinados."
    },
    {
        "enunciado": "Em sistemas de tubulações industriais, a válvula que permite o fluxo em apenas uma direção, impedindo o retorno do fluido, é a válvula de:",
        "opcoes": ["A) Gaveta", "B) Globo", "C) Borboleta", "D) Esfera", "E) Retenção"],
        "correta": "E) Retenção",
        "explicacao": "Válvulas de retenção impedem o fluxo reverso, protegendo bombas e equipamentos."
    },
    {
        "enunciado": "Na instrumentação industrial, o instrumento responsável por medir a diferença de pressão entre dois pontos em um processo é o:",
        "opcoes": ["A) Manômetro diferencial", "B) Termômetro bimetálico", "C) Rotâmetro", "D) Placa de orifício", "E) Densímetro"],
        "correta": "A) Manômetro diferencial",
        "explicacao": "O manômetro diferencial mede a queda de pressão (DP)."
    },
    {
        "enunciado": "De acordo com a NR-20, os tanques que armazenam líquidos inflamáveis devem possuir sistemas de:",
        "opcoes": ["A) Iluminação interna constante", "B) Contenção de vazamentos (diques)", "C) Aquecimento por chama direta", "D) Ventilação para o interior do prédio", "E) Pressurização com oxigênio puro"],
        "correta": "B) Contenção de vazamentos (diques)",
        "explicacao": "A bacia de contenção (dique) evita que vazamentos se espalhem."
    },
    {
        "enunciado": "Qual componente de uma bomba centrífuga é responsável por ceder energia cinética ao fluido, transformando-a depois em energia de pressão?",
        "opcoes": ["A) Carcaça (Voluta)", "B) Impulsor (Rotor)", "C) Selo mecânico", "D) Gaxeta", "E) Eixo"],
        "correta": "B) Impulsor (Rotor)",
        "explicacao": "O impulsor é a peça giratória que 'empurra' o líquido."
    },
    {
        "enunciado": "Em uma torre de destilação fracionada de petróleo, os componentes mais leves (como GLP e Nafta) são retirados em qual parte da torre?",
        "opcoes": ["A) No fundo", "B) No topo", "C) No meio da zona de carga", "D) Abaixo do refervedor", "E) Na bacia de resíduos"],
        "correta": "B) No topo",
        "explicacao": "Gases e líquidos mais leves sobem para o topo da torre."
    },
    {
        "enunciado": "A NR-13 trata de Caldeiras e Vasos de Pressão. PMTA significa:",
        "opcoes": ["A) Pressão Média de Trabalho Autorizada", "B) Pressão Máxima de Trabalho Admissível", "C) Ponto Mínimo de Teste de Ar", "D) Pressão Mensal de Teste de Água", "E) Potência Máxima de Tração Automática"],
        "correta": "B) Pressão Máxima de Trabalho Admissível",
        "explicacao": "A PMTA é o valor máximo de pressão que o vaso suporta com segurança."
    },
    {
        "enunciado": "O equipamento que remove gotículas de líquido arrastadas por uma corrente de gás em um vaso separador é o:",
        "opcoes": ["A) Quebra-jato", "B) Eliminador de névoa (Demister)", "C) Vertedouro", "D) Placa defletora", "E) Chicana"],
        "correta": "B) Eliminador de névoa (Demister)",
        "explicacao": "O Demister retém microgotas de líquido para o gás sair limpo."
    }
]

# --- LÓGICA DE NAVEGAÇÃO CORRIGIDA ---
if st.session_state.indice < len(questoes):
    q = questoes[st.session_state.indice]
    st.subheader(f"Questão {st.session_state.indice + 1} de {len(questoes)}")
    st.info(q["enunciado"])

    resposta = st.radio("Escolha a alternativa:", q['opcoes'], key=f"rad_{st.session_state.indice}")

    if st.button("Confirmar Resposta"):
        if resposta == q['correta']:
            st.success("✅ CORRETO!")
        else:
            st.error(f"❌ INCORRETO! A resposta certa era: {q['correta']}")
        st.session_state.mostrar_explica = True

    if st.session_state.mostrar_explica:
        st.markdown(f"**Explicação:** {q['explicacao']}")
        
        if st.button("Próxima Questão ➡️"):
            if st.session_state.indice < len(questoes) - 1:
                st.session_state.indice += 1
                st.session_state.mostrar_explica = False
                st.rerun()
            else:
                # Se for a última, avançamos o índice para mostrar a tela final
                st.session_state.indice += 1
                st.rerun()

else:
    # --- TELA FINAL ---
    st.balloons()
    st.success("🎉 Parabéns! Você completou este bloco de questões.")
    if st.button("Recomeçar Simulado"):
        st.session_state.indice = 0
        st.session_state.mostrar_explica = False
        st.rerun()
        
