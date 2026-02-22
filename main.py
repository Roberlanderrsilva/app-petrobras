import streamlit as st
import random 

# --- CONFIGURAÇÃO E CABEÇALHO ---
st.set_page_config(page_title="Mentor Petrobras", layout="centered")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Petrobras_logo.svg/1200px-Petrobras_logo.svg.png", width=150)
st.title("⚓ Mentor Petrobras")
st.write("---")

# --- BANCO DE DADOS: BLOCO 01 (50 QUESTÕES) ---
if 'questoes_db' not in st.session_state:
    db_original = [    
        # Bloco de questões para o Aplicativo "Mentor" - Petrobras (Operador)
# ==========================================
# BLOCO DE TESTE: PADRÃO CESGRANRIO MASTER
# ==========================================
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
        }
            
  ]



  
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
         
