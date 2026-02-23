yoimport streamlit as st
import random 

# --- SISTEMA DE CORES E CONTRASTE (COLE AQUI) ---
if 'tema' not in st.session_state:
    st.session_state.tema = "Fundo Escuro"

st.sidebar.title("Configurações do Mentor")
st.session_state.tema = st.sidebar.radio("Escolha o contraste:", ["Fundo Escuro", "Fundo Claro"])

if st.session_state.tema == "Fundo Escuro":
    cor_fundo_box = "#121212"  # Preto
    cor_texto_quest = "#FACC15" # Amarelo (Alto Contraste)
else:
    cor_fundo_box = "#F0F2F6"  # Cinza claro
    cor_texto_quest = "#1E3A8A" # Azul Escuro
# -----------------------------------------------


# --- CONFIGURAÇÃO E CABEÇALHO ---
st.set_page_config(page_title="Mentor Petrobras", layout="centered")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Petrobras_logo.svg/1200px-Petrobras_logo.svg.png", width=150)
st.title("⚓ Mentor Petrobras")
st.write("---")

# --- BANCO DE DADOS: BLOCO 01 (50 QUESTÕES) ---
if 'questoes_db' not in st.session_state:
    db_original = [    
     # ==============================================================================
# BLOCO: INSTRUMENTAÇÃO (QUESTÕES 04 A 10) - PADRÃO CESGRANRIO
# ==============================================================================
        {
            "enunciado": "Em uma unidade de destilação atmosférica, o operador nota que a temperatura no topo da torre está acima do valor de Set Point, comprometendo a especificação da Nafta. Para corrigir esse desvio e garantir o fracionamento adequado, a ação operacional imediata deve ser:",
            "opcoes": [
                "A) Reduzir a carga de petróleo da unidade.",
                "B) Aumentar a vazão de refluxo de topo da coluna.",
                "C) Diminuir a pressão de vapor do refervedor.",
                "D) Aumentar a temperatura de saída do forno.",
                "E) Abrir totalmente a retirada de Diesel de fundo."
            ],
            "correta": "B) Aumentar a vazão de refluxo de topo da coluna.",
            "explicacao": "O refluxo é a variável manipulada para controlar a temperatura de topo. Aumentando o refluxo, retira-se calor, baixando a temperatura e melhorando a qualidade da Nafta."
        },
        {
            "enunciado": "A NR-13 estabelece requisitos mínimos para a gestão da integridade estrutural de caldeiras e vasos de pressão. De acordo com essa norma, um vaso de pressão que opera com fluido inflamável e volume superior a 1m³ deve obrigatoriamente possuir:",
        "opcoes": [
                "A) Pintura externa na cor vermelha de segurança.",
                "B) Placa de identificação indelével e prontuário atualizado.",
                "C) Sensor de temperatura digital em todos os drenos.",
                "D) Sistema de resfriamento por nitrogênio líquido.",
                "E) Operador dedicado 24h sem intervalos."
            ],
            "correta": "B) Placa de identificação indelével e prontuário atualizado.",
            "explicacao": "A NR-13 exige que todo vaso de pressão tenha placa de identificação visível e documentação técnica (prontuário) disponível para fiscalização e segurança."
        },
        {
            "enunciado": "Sensores de pressão do tipo 'Célula de Carga' ou 'Piezoelétricos' são comuns em processos industriais. No entanto, para indicação local de pressão em campo, sem necessidade de energia elétrica, o elemento sensor mecânico mais utilizado em manômetros na Petrobras é o:",
            "opcoes": [
                "A) Tubo de Venturi.",
                "B) Tubo de Bourdon.",
                "C) Sensor Capacitivo.",
                "D) Termistor NTC.",
                "E) Placa de Orifício."
            ],
            "correta": "B) Tubo de Bourdon.",
            "explicacao": "O tubo de Bourdon converte a pressão interna em movimento mecânico do ponteiro, sendo o padrão para manômetros locais pela sua robustez e simplicidade."
        },
        
        {
            "enunciado": "Em uma malha de controle de vazão que utiliza uma placa de orifício como elemento primário, o transmissor de pressão diferencial (DP) indica um valor de 25% da escala de pressão. De acordo com a relação quadrática entre vazão e pressão diferencial, qual o valor percentual da vazão correspondente?",
            "opcoes": [
                "A) 12,5%",
                "B) 25,0%",
                "C) 50,0%",
                "D) 62,5%",
                "E) 100,0%"
            ],
            "correta": "C) 50,0%",
            "explicacao": "Na medição por placa de orifício, a vazão é proporcional à raiz quadrada da pressão diferencial. Raiz de 0,25 (25%) é igual a 0,50 (50%)."
        },
        
        {
            "enunciado": "Durante a calibração de um transmissor de pressão com range de 0 a 10 kgf/cm², o técnico observa que o instrumento apresenta uma leitura de 4,2 mA quando a pressão aplicada é zero. Esse tipo de erro, que desloca toda a curva de calibração paralelamente, é conhecido como:",
            "opcoes": [
                "A) Erro de Angularidade (Span).",
                "B) Erro de Zero (Histerese).",
                "C) Erro de Zero (Offset).",
                "D) Erro de Linearidade.",
                "E) Erro de Repetibilidade."
            ],
            "correta": "C) Erro de Zero (Offset).",
            "explicacao": "O erro de zero ocorre quando o sinal de saída inicial não corresponde ao valor mínimo da escala (4 mA), mas mantém a mesma inclinação da curva."
        },
        {
            "enunciado": "Válvulas de controle do tipo 'Globo' são amplamente utilizadas em refinarias devido à sua capacidade de regulagem. Em uma situação de emergência por falha de ar comprimido, uma válvula 'Falha-Aberta' (Air-to-Close) irá:",
            "opcoes": [
                "A) Permanecer na última posição em que estava.",
                "B) Deslocar-se totalmente para a posição de fechamento.",
                "C) Abrir-se totalmente, permitindo a passagem total do fluido.",
                "D) Reduzir a vazão para 50% por segurança.",
                "E) Travar mecanicamente no meio do curso."
            ],
            "correta": "C) Abrir-se totalmente, permitindo a passagem total do fluido.",
            "explicacao": "Válvulas Air-to-Close (Ar para fechar) possuem molas que as empurram para a posição aberta caso o suprimento de ar falhe."
        },
        
        {
            "enunciado": "Para medir a temperatura de um mancal de uma bomba centrífuga de grande porte, utiliza-se um sensor do tipo PT-100. Sobre este instrumento, é correto afirmar que ele opera baseado na:",
            "opcoes": [
                "A) Geração de uma milivoltagem proporcional ao calor.",
                "B) Variação da resistência elétrica de um fio de platina com a temperatura.",
                "C) Dilatação de um gás inerte dentro de um bulbo metálico.",
                "D) Mudança na cor de um cristal líquido sensível.",
                "E) Emissão de radiação infravermelha pelo metal."
            ],
            "correta": "B) Variação da resistência elétrica de um fio de platina com a temperatura.",
            "explicacao": "O PT-100 é uma termorresistência (RTD) feita de platina que possui exatamente 100 Ohms quando está a 0°C."
        },
        {
            "enunciado": "Em um sistema de controle digital, o protocolo de comunicação HART é muito utilizado. Sua principal característica técnica é permitir a:",
            "opcoes": [
                "A) Substituição total dos fios de cobre por fibra óptica.",
                "B) Transmissão de sinais apenas em corrente alternada de alta potência.",
                "C) Sobreposição de um sinal digital de comunicação sobre o sinal analógico 4-20 mA.",
                "D) Eliminação completa da necessidade de calibração periódica.",
                "E) Medição de vazão mássica em tubulações de pequeno diâmetro."
            ],
            "correta": "C) Sobreposição de um sinal digital de comunicação sobre o sinal analógico 4-20 mA.",
            "explicacao": "O HART permite configurar e diagnosticar instrumentos inteligentes sem interromper o sinal analógico de controle."
        },
        {
            "enunciado": "Um pressostato é um instrumento de segurança e intertravamento. Quando a pressão do processo atinge um valor crítico predefinido (setpoint do pressostato), ele atua diretamente sobre:",
            "opcoes": [
                "A) Um potenciômetro de ajuste fino.",
                "B) Um contato elétrico seco (abre ou fecha um circuito).",
                "C) Uma válvula manual do tipo gaveta.",
                "D) O display digital do operador no painel.",
                "E) A velocidade de rotação do motor elétrico."
            ],
            "correta": "B) Um contato elétrico seco (abre ou fecha um circuito).",
            "explicacao": "Diferente do transmissor, o pressostato é uma chave on/off que aciona alarmes ou desliga equipamentos em caso de sobrepressão."
        },
        {
            "enunciado": "O posicionador de uma válvula de controle tem como função principal garantir que a posição da haste da válvula corresponda exatamente ao sinal enviado pelo controlador. O uso do posicionador é altamente recomendado quando:",
            "opcoes": [
                "A) O fluido do processo é água limpa em baixa pressão.",
                "B) Há necessidade de minimizar os efeitos de atrito na gaxeta e histerese.",
                "C) A válvula é de ação manual e não possui atuador.",
                "D) O processo é muito lento e não exige precisão.",
                "E) O sinal de controle é exclusivamente digital via Wi-Fi."
            ],
            "correta": "B) Há necessidade de minimizar os efeitos de atrito na gaxeta e histerese.",
            "explicacao": "O posicionador corrige desvios causados pelo atrito da haste, garantindo que a válvula abra exatamente o que o controlador pediu."
        }
            
            
  ],
    random.shuffle(db_original) 
    st.session_state.questoes_db = db_original

questoes = st.session_state.questoes_db

# --- LÓGICA DO APP (REVISADA) ---
if 'indice' not in st.session_state:
    st.session_state.indice = 0
    st.session_state.mostrar_explica = False

if st.session_state.indice < len(questoes):
    q = questoes[st.session_state.indice]
        st.subheader(f"Questão {st.session_state.indice + 1} de {len(questoes)}")
    
    # --- BOX COM ALTO CONTRASTE (NOVO) ---
    st.markdown(f"""
        <div style="
            background-color: {cor_fundo_box}; 
            padding: 20px; 
            border-radius: 12px; 
            border: 3px solid #3b82f6; 
            margin-bottom: 20px;">
            <p style="
                color: {cor_texto_quest}; 
                font-size: 20px; 
                font-weight: bold; 
                line-height: 1.6;
                margin: 0;">
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
        st.markdown(f"**Explicação:** {q['explicacao']}")
        if st.button("Próxima Questão ➡️"):
            st.session_state.indice += 1
            st.session_state.mostrar_explica = False
            st.rerun()
else:
    st.balloons()
    st.success("🎉 Você concluiu o Bloco de 50 questões!")
    if st.button("Recomeçar e Embaralhar"):
        del st.session_state.questoes_db 
        st.session_state.indice = 0
        st.session_state.mostrar_explica = False
        st.rerun()
         
