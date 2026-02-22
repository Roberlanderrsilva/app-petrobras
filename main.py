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
    },questoes = [
    {
        "enunciado": "Em uma unidade de processamento de petróleo, as bombas centrífugas são amplamente utilizadas. Para evitar o fenômeno da cavitação em uma bomba centrífuga, o operador deve garantir que:",
        "opcoes": ["A) O NPSH disponível seja menor que o NPSH requerido", "B) O NPSH disponível seja maior que o NPSH requerido", "C) A temperatura do fluido seja aumentada drasticamente", "D) A pressão na sucção seja reduzida ao mínimo", "E) A válvula de descarga esteja totalmente fechada"],
        "correta": "B) O NPSH disponível seja maior que o NPSH requerido",
        "explicacao": "Cavitação ocorre quando a pressão do líquido cai abaixo da pressão de vapor. Manter o NPSH disponível maior que o requerido evita a formação de bolhas de vapor."
    },
    {
        "enunciado": "No processo de refino, o equipamento utilizado para realizar a troca térmica entre dois fluidos sem que eles se misturem é o:",
        "opcoes": ["A) Torre de destilação", "B) Vaso separador", "C) Permutador de calor", "D) Compressor de pistão", "E) Ejetor de vácuo"],
        "correta": "C) Permutador de calor",
        "explicacao": "Permutadores de calor (como os de casco e tubo) são essenciais para o controle de temperatura no processamento de petróleo."
    },
    {
        "enunciado": "Sobre o armazenamento de combustíveis, a norma que estabelece os requisitos de segurança para o trabalho em Espaços Confinados, muito comum em limpezas de tanques, é a:",
        "opcoes": ["A) NR-10", "B) NR-13", "C) NR-20", "D) NR-33", "E) NR-35"],questoes = [
    {
        "enunciado": "Em uma unidade de processamento de petróleo, as bombas centrífugas são amplamente utilizadas. Para evitar o fenômeno da cavitação em uma bomba centrífuga, o operador deve garantir que:",
        "opcoes": ["A) O NPSH disponível seja menor que o NPSH requerido", "B) O NPSH disponível seja maior que o NPSH requerido", "C) A temperatura do fluido seja aumentada drasticamente", "D) A pressão na sucção seja reduzida ao mínimo", "E) A válvula de descarga esteja totalmente fechada"],
        "correta": "B) O NPSH disponível seja maior que o NPSH requerido",
        "explicacao": "Cavitação ocorre quando a pressão do líquido cai abaixo da pressão de vapor. Manter o NPSH disponível maior que o requerido evita a formação de bolhas de vapor."
    },
    {
        "enunciado": "No processo de refino, o equipamento utilizado para realizar a troca térmica entre dois fluidos sem que eles se misturem é o:",
        "opcoes": ["A) Torre de destilação", "B) Vaso separador", "C) Permutador de calor", "D) Compressor de pistão", "E) Ejetor de vácuo"],
        "correta": "C) Permutador de calor",
        "explicacao": "Permutadores de calor (como os de casco e tubo) são essenciais para o controle de temperatura no processamento de petróleo."
    },
    {
        "enunciado": "Sobre o armazenamento de combustíveis, a norma que estabelece os requisitos de segurança para o trabalho em Espaços Confinados, muito comum em limpezas de tanques, é a:",
        "opcoes": ["A) NR-10", "B) NR-13", "C) NR-20", "D) NR-33", "E) NR-35"],
        "correta": "D) NR-33",
        "explicacao": "A NR-33 define as medidas de prevenção e segurança para trabalhos em espaços que não foram projetados para ocupação humana contínua."
    },
    {
        "enunciado": "Em sistemas de tubulações industriais, a válvula que permite o fluxo em apenas uma direção, impedindo o retorno do fluido, é a válvula de:",
        "opcoes": ["A) Gaveta", "B) Globo", "C) Borboleta", "D) Esfera", "E) Retenção"],
        "correta": "E) Retenção",
        "explicacao": "Válvulas de retenção são dispositivos automáticos que impedem o fluxo reverso, protegendo bombas e equipamentos."
    },
    {
        "enunciado": "Na instrumentação industrial, o instrumento responsável por medir a diferença de pressão entre dois pontos em um processo é o:",
        "opcoes": ["A) Manômetro diferencial", "B) Termômetro bimetálico", "C) Rotâmetro", "D) Placa de orifício", "E) Densímetro"],
        "correta": "A) Manômetro diferencial",
        "explicacao": "O manômetro diferencial mede a queda de pressão (DP), sendo muito usado para medir vazão ou nível em vasos."
    },
    {
        "enunciado": "De acordo com a NR-20 (Segurança e Saúde no Trabalho com Inflamáveis e Combustíveis), os tanques que armazenam líquidos inflamáveis devem possuir sistemas de:",
        "opcoes": ["A) Iluminação interna constante", "B) Contenção de vazamentos (diques)", "C) Aquecimento por chama direta", "D) Ventilação para o interior do prédio", "E) Pressurização com oxigênio puro"],
        "correta": "B) Contenção de vazamentos (diques)",
        "explicacao": "A bacia de contenção (dique) é obrigatória para evitar que um vazamento se espalhe pelo meio ambiente ou pela unidade."
    },
    {
        "enunciado": "Qual componente de uma bomba centrífuga é responsável por ceder energia cinética ao fluido, transformando-a depois em energia de pressão?",
        "opcoes": ["A) Carcaça (Voluta)", "B) Impulsor (Rotor)", "C) Selo mecânico", "D) Gaxeta", "E) Eixo"],
        "correta": "B) Impulsor (Rotor)",
        "explicacao": "O impulsor é a peça giratória que 'empurra' o líquido, aumentando sua velocidade e energia."
    },
    {
        "enunciado": "Em uma torre de destilação fracionada de petróleo, os componentes mais leves (como GLP e Nafta) são retirados em qual parte da torre?",
        "opcoes": ["A) No fundo", "B) No topo", "C) No meio da zona de carga", "D) Abaixo do refervedor", "E) Na bacia de resíduos"],
        "correta": "B) No topo",
        "explicacao": "Na destilação, os gases e líquidos com menor ponto de ebulição (mais leves) sobem para o topo da torre."
    },
    {
        "enunciado": "A NR-13 trata da segurança de Caldeiras, Vasos de Pressão e Tubulações. Todo vaso de pressão deve ter fixada em seu corpo uma placa de identificação com a PMTA. PMTA significa:",
        "opcoes": ["A) Pressão Média de Trabalho Autorizada", "B) Pressão Máxima de Trabalho Admissível", "C) Ponto Mínimo de Teste de Ar", "D) Pressão Mensal de Teste de Água", "E) Potência Máxima de Tração Automática"],
        "correta": "B) Pressão Máxima de Trabalho Admissível",
        "explicacao": "A PMTA é o valor máximo de pressão que o vaso suporta com segurança, conforme o projeto de engenharia."
    },
    {
        "enunciado": "O equipamento que remove gotículas de líquido arrastadas por uma corrente de gás em um vaso separador é chamado de:",
        "opcoes": ["A) Quebra-jato", "B) Eliminador de névoa (Demister)", "C) Vertedouro", "D) Placa defletora", "E) Chicana"],
        "correta": "B) Eliminador de névoa (Demister)",
        "explicacao": "O Demister retém as microgotas de líquido para que o gás saia limpo pelo topo do separador."
    }
]

        "correta": "D) NR-33",
        "explicacao": "A NR-33 define as medidas de prevenção e segurança para trabalhos em espaços que não foram projetados para ocupação humana contínua."
    },
    {
        "enunciado": "Em sistemas de tubulações industriais, a válvula que permite o fluxo em apenas uma direção, impedindo o retorno do fluido, é a válvula de:",
        "opcoes": ["A) Gaveta", "B) Globo", "C) Borboleta", "D) Esfera", "E) Retenção"],
        "correta": "E) Retenção",
        "explicacao": "Válvulas de retenção são dispositivos automáticos que impedem o fluxo reverso, protegendo bombas e equipamentos."
    },
    {
        "enunciado": "Na instrumentação industrial, o instrumento responsável por medir a diferença de pressão entre dois pontos em um processo é o:",
        "opcoes": ["A) Manômetro diferencial", "B) Termômetro bimetálico", "C) Rotâmetro", "D) Placa de orifício", "E) Densímetro"],
        "correta": "A) Manômetro diferencial",
        "explicacao": "O manômetro diferencial mede a queda de pressão (DP), sendo muito usado para medir vazão ou nível em vasos."
    },
    {
        "enunciado": "De acordo com a NR-20 (Segurança e Saúde no Trabalho com Inflamáveis e Combustíveis), os tanques que armazenam líquidos inflamáveis devem possuir sistemas de:",
        "opcoes": ["A) Iluminação interna constante", "B) Contenção de vazamentos (diques)", "C) Aquecimento por chama direta", "D) Ventilação para o interior do prédio", "E) Pressurização com oxigênio puro"],
        "correta": "B) Contenção de vazamentos (diques)",
        "explicacao": "A bacia de contenção (dique) é obrigatória para evitar que um vazamento se espalhe pelo meio ambiente ou pela unidade."
    },
    {
        "enunciado": "Qual componente de uma bomba centrífuga é responsável por ceder energia cinética ao fluido, transformando-a depois em energia de pressão?",
        "opcoes": ["A) Carcaça (Voluta)", "B) Impulsor (Rotor)", "C) Selo mecânico", "D) Gaxeta", "E) Eixo"],
        "correta": "B) Impulsor (Rotor)",
        "explicacao": "O impulsor é a peça giratória que 'empurra' o líquido, aumentando sua velocidade e energia."
    },
    {
        "enunciado": "Em uma torre de destilação fracionada de petróleo, os componentes mais leves (como GLP e Nafta) são retirados em qual parte da torre?",
        "opcoes": ["A) No fundo", "B) No topo", "C) No meio da zona de carga", "D) Abaixo do refervedor", "E) Na bacia de resíduos"],
        "correta": "B) No topo",
        "explicacao": "Na destilação, os gases e líquidos com menor ponto de ebulição (mais leves) sobem para o topo da torre."
    },
    {
        "enunciado": "A NR-13 trata da segurança de Caldeiras, Vasos de Pressão e Tubulações. Todo vaso de pressão deve ter fixada em seu corpo uma placa de identificação com a PMTA. PMTA significa:",
        "opcoes": ["A) Pressão Média de Trabalho Autorizada", "B) Pressão Máxima de Trabalho Admissível", "C) Ponto Mínimo de Teste de Ar", "D) Pressão Mensal de Teste de Água", "E) Potência Máxima de Tração Automática"],
        "correta": "B) Pressão Máxima de Trabalho Admissível",
        "explicacao": "A PMTA é o valor máximo de pressão que o vaso suporta com segurança, conforme o projeto de engenharia."
    },
    {
        "enunciado": "O equipamento que remove gotículas de líquido arrastadas por uma corrente de gás em um vaso separador é chamado de:",
        "opcoes": ["A) Quebra-jato", "B) Eliminador de névoa (Demister)", "C) Vertedouro", "D) Placa defletora", "E) Chicana"],
        "correta": "B) Eliminador de névoa (Demister)",
        "explicacao": "O Demister retém as microgotas de líquido para que o gás saia limpo pelo topo do separador."
    }
],

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
