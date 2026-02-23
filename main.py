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
            "enunciado": "Na destilação atmosférica do petróleo, qual fração é retirada no topo da torre por possuir o menor ponto de ebulição?",
            "opcoes": ["Diesel", "Querosene", "Gás Liquefeito (GLP) e Nafta leve", "Resíduo Atmosférico"],
            "correta": "Gás Liquefeito (GLP) e Nafta leve",
            "explicacao": "Os componentes mais leves têm menores temperaturas de ebulição e sobem até o topo da torre de destilação."
        },
        {
            "enunciado": "Qual o objetivo principal do processo de Craqueamento Catalítico Fluido (FCC) em uma refinaria?",
            "opcoes": ["Remover sal do petróleo bruto", "Transformar frações pesadas em frações leves de maior valor, como a gasolina", "Apenas resfriar os produtos finais", "Misturar água ao óleo"],
            "correta": "Transformar frações pesadas em frações leves de maior valor, como a gasolina",
            "explicacao": "O craqueamento 'quebra' moléculas grandes e pesadas em moléculas menores e mais valiosas, aumentando a produção de gasolina e GLP."
        },
        {
            "enunciado": "O processo de Hidrotratamento (HDT) é fundamental para atender normas ambientais porque:",
            "opcoes": ["Aumenta o volume do petróleo", "Remove enxofre e nitrogênio dos combustíveis", "Transforma óleo em gás naturalmente", "Reduz o custo da energia elétrica na refinaria"],
            "correta": "Remove enxofre e nitrogênio dos combustíveis",
            "explicacao": "O HDT utiliza hidrogênio para reagir com impurezas (como enxofre), reduzindo a emissão de poluentes na queima do combustível."
        },
        {
            "enunciado": "Na unidade de Destilação a Vácuo, por que se reduz a pressão para destilar o resíduo atmosférico?",
            "opcoes": ["Para economizar energia elétrica", "Permitir a vaporização de frações pesadas sem decomposição térmica (coqueificação)", "Para aumentar a densidade do óleo", "Para remover a água restante"],
            "correta": "Permitir a vaporização de frações pesadas sem decomposição térmica (coqueificação)",
            "explicacao": "Ao reduzir a pressão, o ponto de ebulição cai, permitindo separar o óleo sem precisar de temperaturas tão altas que degradariam o produto."
        },
        {
            "enunciado": "O processo de Reforma Catalítica tem como objetivo principal:",
            "opcoes": ["Produzir querosene de aviação", "Aumentar a octanagem da nafta para produzir gasolina de alta qualidade", "Separar areia do petróleo", "Gerar resíduo asfáltico"],
            "correta": "Aumentar a octanagem da nafta para produzir gasolina de alta qualidade",
            "explicacao": "A reforma reorganiza as moléculas para que a gasolina resista melhor à compressão no motor sem detonar prematuramente."
        },
        {
            "enunciado": "Qual o subproduto sólido gerado na Unidade de Coqueamento Retardado (UCR)?",
            "opcoes": ["Enxofre líquido", "Coque de Petróleo", "Piche", "Sal gema"],
            "correta": "Coque de Petróleo",
            "explicacao": "O coque é um material sólido rico em carbono, usado como combustível industrial ou na fabricação de eletrodos."
        },
        {
            "enunciado": "A dessalgação do petróleo bruto ocorre antes da destilação para evitar:",
            "opcoes": ["O excesso de gasolina no topo", "Corrosão nos equipamentos e deposição de sais nos trocadores", "Que o petróleo fique muito ralo", "A mudança da cor do óleo"],
            "correta": "Corrosão nos equipamentos e deposição de sais nos trocadores",
            "explicacao": "O sal e a água causam corrosão severa e entupimentos por incrustação nas torres e trocadores de calor."
        },
        {
            "enunciado": "No Craqueamento Catalítico (FCC), o que acontece com o catalisador após a reação?",
            "opcoes": ["Ele é descartado", "Fica impregnado de coque e precisa ser regenerado por combustão", "Ele vira gasolina", "Ele dissolve no óleo"],
            "correta": "Fica impregnado de coque e precisa ser regenerado por combustão",
            "explicacao": "O catalisador é circulante; ele reage, 'suja' de coque, é limpo pelo fogo no regenerador e volta quente para o processo."
        },
        {
            "enunciado": "A Alquilação Catalítica é um processo que:",
            "opcoes": ["Diminui a octanagem da gasolina", "Produz componentes de alta octanagem a partir de gases leves", "Serve apenas para limpar o diesel", "É usado para fabricar asfalto"],
            "correta": "Produz componentes de alta octanagem a partir de gases leves",
            "explicacao": "É o inverso do craqueamento: ela 'junta' moléculas pequenas de gás para formar um líquido nobre para a gasolina."
        },
        {
            "enunciado": "A 'Nafta' produzida na destilação é a principal matéria-prima para qual indústria?",
            "opcoes": ["Alimentícia", "Petroquímica (plásticos, borrachas, fertilizantes)", "Construção civil pesada", "Têxtil de algodão"],
            "correta": "Petroquímica (plásticos, borrachas, fertilizantes)",
            "explicacao": "A nafta é enviada para centrais petroquímicas onde é transformada em produtos básicos para fazer plásticos e químicos."
        }
        ]
    
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
        
