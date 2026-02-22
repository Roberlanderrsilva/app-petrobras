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
                 # --- MATÉRIA 02: SEGURANÇA INDUSTRIAL E NORMAS REGULAMENTADORAS (NRs) ---
        {
            "enunciado": "A NR-13 estabelece que toda caldeira deve possuir um 'Prontuário' atualizado. Em caso de perda desse documento, qual deve ser a ação imediata do proprietário para conformidade legal?",
            "opcoes": ["A) Operar a caldeira apenas em carga mínima.", "B) Reconstituir o prontuário através de inspeção técnica e recálculo da PMTA por profissional habilitado.", "C) Solicitar uma cópia simples ao fabricante via e-mail.", "D) Substituir a caldeira por uma nova imediatamente.", "E) Ignorar a ausência do documento desde que a válvula de segurança funcione."],
            "correta": "B) Reconstituir o prontuário através de inspeção técnica e recálculo da PMTA por profissional habilitado.",
            "explicacao": "A falta do prontuário é infração grave. A reconstituição técnica é obrigatória para garantir a integridade e segurança operacional."
        },
        {
            "enunciado": "De acordo com a NR-33 (Espaços Confinados), o 'Vigia' possui funções específicas. Qual das alternativas abaixo descreve uma proibição para o Vigia durante a entrada dos trabalhadores?",
            "opcoes": ["A) Manter contato contínuo com os trabalhadores autorizados.", "B) Operar os dispositivos de emergência e salvamento.", "C) Realizar outras tarefas que possam comprometer seu dever principal de monitoramento.", "D) Ordenar o abandono do espaço em caso de risco detectado.", "E) Acionar o plano de resgate quando necessário."],
            "correta": "C) Realizar outras tarefas que possam comprometer seu dever principal de monitoramento.",
            "explicacao": "O vigia deve ter foco exclusivo na segurança dos trabalhadores no interior do espaço, não podendo realizar tarefas paralelas."
        },
        
        {
            "enunciado": "A NR-20 classifica as instalações em Classes (I, II e III) de acordo com a atividade e a capacidade de armazenamento. Uma refinaria de petróleo, devido à complexidade e volume de inflamáveis, é tipicamente classificada como:",
            "opcoes": ["A) Instalação de Classe I.", "B) Instalação de Classe II.", "C) Instalação de Classe III.", "D) Instalação de Risco Moderado.", "E) Área de Preservação Industrial."],
            "correta": "C) Instalação de Classe III.",
            "explicacao": "Refinarias e unidades de processamento de gás são instalações de Classe III por lidarem com grandes volumes de inflamáveis e processos complexos."
        },
        {
            "enunciado": "No contexto da NR-10 (Segurança em Eletricidade), o estado de 'Desenergização' de um circuito só é reconhecido legalmente após o cumprimento de uma sequência de procedimentos. O primeiro passo dessa sequência é:",
            "opcoes": ["A) Instalação de aterramento temporário.", "B) Seccionamento da fonte de energia.", "C) Proteção dos elementos energizados adjacentes.", "D) Impedimento de reenergização (travamento).", "E) Constatação da ausência de tensão."],
            "correta": "B) Seccionamento da fonte de energia.",
            "explicacao": "A desenergização começa obrigatoriamente pelo seccionamento físico do circuito, seguido pelo travamento e teste de ausência de tensão."
        },
        
        {
            "enunciado": "A NR-35 estabelece que o sistema de proteção contra quedas (SPQ) é obrigatório sempre que houver risco de queda. Qual o fator de queda ideal para minimizar o impacto no corpo do trabalhador em caso de retenção?",
            "opcoes": ["A) Fator de queda igual a 2.", "B) Fator de queda maior que 2.", "C) Fator de queda menor que 1.", "D) Fator de queda infinito.", "E) O fator de queda não influencia a força de impacto."],
            "correta": "C) Fator de queda menor que 1.",
            "explicacao": "Quanto menor o fator de queda (distância da queda dividida pelo comprimento do talabarte), menor será a força de impacto transmitida ao trabalhador."
        },
        {
            "enunciado": "Durante uma ronda, um operador detecta um incêndio em um transformador de óleo que ainda está conectado à rede elétrica. Qual o extintor de incêndio MAIS indicado para esta situação específica?",
            "opcoes": ["A) Extintor de Água (H2O).", "B) Extintor de Espuma Mecânica.", "C) Extintor de Dióxido de Carbono (CO2) ou Pó Químico (PQS).", "D) Extintor de Água Pressurizada com aditivo.", "E) Abafamento com mantas de algodão."],
            "correta": "C) Extintor de Dióxido de Carbono (CO2) ou Pó Químico (PQS).",
            "explicacao": "Para equipamentos elétricos energizados (Classe C), devem-se usar agentes não condutores, como CO2 ou PQS."
        },
        {
            "enunciado": "Em segurança química, o diamante de Hommel (NFPA 704) é utilizado para identificação rápida de riscos. O que representa a cor VERMELHA neste diagrama?",
            "opcoes": ["A) Risco à Saúde.", "B) Reatividade Química.", "C) Inflamabilidade.", "D) Riscos Específicos (Oxidante, Radioativo).", "E) Nível de Corrosividade."],
            "correta": "C) Inflamabilidade.",
            "explicacao": "Vermelho indica o perigo de fogo; Azul (Saúde); Amarelo (Reatividade) e Branco (Riscos Específicos)."
        },
        [attachment_0](attachment)
        {
            "enunciado": "Segundo a NR-13, as válvulas de segurança de um vaso de pressão devem ser testadas periodicamente. O nome técnico da pressão na qual a válvula de segurança é ajustada para abrir é:",
            "opcoes": ["A) Pressão de Teste Hidrostático.", "B) Pressão de Ajuste ou Set Point.", "C) Pressão de Ruptura do Casco.", "D) Pressão Atmosférica Local.", "E) Pressão Média de Operação."],
            "correta": "B) Pressão de Ajuste ou Set Point.",
            "explicacao": "O set point é a pressão exata calibrada para que a válvula abra e proteja o vaso contra sobrepressão."
        },
        {
            "enunciado": "A Permissão de Trabalho (PT) é um documento essencial para atividades de risco. Qual a validade padrão de uma PT, conforme as boas práticas de gestão de segurança na indústria do petróleo?",
            "opcoes": ["A) Válida por todo o ano civil.", "B) Válida apenas para a duração do turno de trabalho, podendo ser revalidada.", "C) Válida por tempo indeterminado até o fim da obra.", "D) Válida apenas para o horário comercial (08:00 às 17:00).", "E) Válida por uma semana, independente das condições do local."],
            "correta": "B) Válida apenas para a duração do turno de trabalho, podendo ser revalidada.",
            "explicacao": "A PT deve ser limitada ao turno para garantir que as condições de segurança sejam reavaliadas na troca de equipe."
        },
        {
            "enunciado": "O conceito de 'Lote de Inflamáveis' na NR-20 é fundamental para o distanciamento de tanques. Para fins desta norma, o que define um líquido combustível?",
            "opcoes": ["A) Qualquer líquido que tenha cheiro forte.", "B) Líquido com ponto de fulgor > 60 °C e <= 93 °C.", "C) Líquido que entra em ebulição a 100 °C.", "D) Líquido com ponto de fulgor abaixo de 0 °C.", "E) Somente derivados de petróleo bruto."],
            "correta": "B) Líquido com ponto de fulgor > 60 °C e <= 93 °C.",
            "explicacao": "A NR-20 separa inflamáveis (PF <= 60°C) de combustíveis (PF entre 60°C e 93°C)."
        },
        {
            "enunciado": "Na análise de acidentes, a pirâmide de Bird sugere que para cada acidente grave, ocorrem centenas de 'quase-acidentes'. Qual a importância técnica de relatar um quase-acidente na refinaria?",
            "opcoes": ["A) Gerar punições para a equipe envolvida.", "B) Prevenir a ocorrência de acidentes reais através da correção de desvios.", "C) Aumentar a burocracia do setor de RH.", "D) Cumprir apenas uma meta estética de segurança.", "E) Reduzir o salário dos supervisores."],
            "correta": "B) Prevenir a ocorrência de acidentes reais através da correção de desvios.",
            "explicacao": "O relato do 'quase-acidente' permite identificar falhas no sistema antes que alguém se machuque."
        },
        {
            "enunciado": "O monitoramento de gases em espaços confinados deve ser contínuo. Se o alarme de oxigênio (O2) disparar indicando concentração abaixo de 19,5%, qual deve ser a ação imediata?",
            "opcoes": ["A) Continuar o trabalho e aumentar a ventilação.", "B) Colocar uma máscara simples de poeira e prosseguir.", "C) Abandonar o local imediatamente, pois a atmosfera é considerada IPVS ou deficiente de O2.", "D) Ignorar o alarme, pois o corpo humano suporta até 15% de O2.", "E) Esperar o supervisor chegar para avaliar."],
            "correta": "C) Abandonar o local imediatamente, pois a atmosfera é considerada IPVS ou deficiente de O2.",
            "explicacao": "Abaixo de 19,5% de O2, o risco de asfixia é real e imediato. O abandono é obrigatório."
        },
        {
            "enunciado": "A NR-12 trata da segurança em máquinas. O dispositivo que impede o funcionamento da máquina caso a proteção móvel seja aberta é chamado de:",
            "opcoes": ["A) Botão de liga/desliga comum.", "B) Dispositivo de intertravamento (chave de segurança).", "C) Pedal de acionamento simples.", "D) Cabo de alimentação reforçado.", "E) Sensor de temperatura de carcaça."],
            "correta": "B) Dispositivo de intertravamento (chave de segurança).",
            "explicacao": "O intertravamento interrompe o comando de partida ou o movimento da máquina se a proteção for violada."
        },
        {
            "enunciado": "O EPC (Equipamento de Proteção Coletiva) tem prioridade sobre o EPI (Equipamento de Proteção Individual) porque:",
            "opcoes": ["A) O EPC é mais barato.", "B) O EPC elimina ou reduz o risco na fonte, protegendo todos os trabalhadores simultaneamente.", "C) O EPI é opcional na indústria do petróleo.", "D) O EPC não precisa de manutenção.", "E) O uso do EPI causa desconforto térmico."],
            "correta": "B) O EPC elimina ou reduz o risco na fonte, protegendo todos os trabalhadores simultaneamente.",
            "explicacao": "A hierarquia de controle de riscos sempre prioriza medidas coletivas antes das individuais."
        },
        {
            "enunciado": "Qual o agente extintor recomendado para fogos em cozinhas industriais (Classe K), envolvendo óleos e gorduras vegetais/animais?",
            "opcoes": ["A) Água pressurizada.", "B) Pó Químico Seco comum (BC).", "C) Solução de Acetato de Potássio (Agente Saponificante).", "D) Dióxido de Carbono (CO2).", "E) Extintor de espuma de alta expansão."],
            "correta": "C) Solução de Acetato de Potássio (Agente Saponificante).",
            "explicacao": "O agente classe K saponifica a gordura, criando uma camada que abafa o fogo e evita a reignição."
        },
        {
            "enunciado": "Em trabalhos de soldagem em áreas classificadas, o teste de explosividade (LEL) deve indicar qual valor para que a Permissão de Trabalho de 'fogo' seja liberada?",
            "opcoes": ["A) 50% do LEL.", "B) 20% do LEL.", "C) 0% de LEL (presença zero de gases inflamáveis).", "D) 100% de LEL.", "E) Qualquer valor abaixo do limite superior."],
            "correta": "C) 0% de LEL (presença zero de gases inflamáveis).",
            "explicacao": "Para trabalhos com chama aberta em áreas com risco de explosão, a atmosfera deve estar completamente livre de inflamáveis (0% LEL)."
        },
        {
            "enunciado": "A NR-10 define 'Zona de Risco' como o entorno de parte condutora energizada, não segregada. O acesso a esta zona é restrito apenas a:",
            "opcoes": ["A) Qualquer funcionário da limpeza.", "B) Trabalhadores autorizados e com treinamentos específicos.", "C) Visitantes acompanhados.", "D) Engenheiros civis sem treinamento elétrico.", "E) Operadores de produção sem curso de SEP."],
            "correta": "B) Trabalhadores autorizados e com treinamentos específicos.",
            "explicacao": "Apenas profissionais qualificados e autorizados podem intervir em zonas de risco elétrico."
        },
        {
            "enunciado": "O que caracteriza uma atmosfera 'IPVS' (Imediatamente Perigosa à Vida ou à Saúde)?",
            "opcoes": ["A) Uma atmosfera com cheiro de óleo diesel.", "B) Uma atmosfera que apresenta risco imediato de morte ou efeitos debilitantes graves à saúde.", "C) Um local com temperatura acima de 30°C.", "D) Uma sala com ruído acima de 80 dB.", "E) Qualquer ambiente externo com chuva."],
            "correta": "B) Uma atmosfera que apresenta risco imediato de morte ou efeitos debilitantes graves à saúde.",
            "explicacao": "IPVS exige medidas extremas de proteção, como o uso de ar mandado ou máscara autônoma."
        },
        {
            "enunciado": "Sobre o uso de cinturão de segurança tipo paraquedista em trabalhos acima de 2 metros, o ponto de ancoragem deve suportar uma carga mínima determinada por norma ou cálculo. Este sistema visa evitar:",
            "opcoes": ["A) O cansaço físico do trabalhador.", "B) O impacto contra o nível inferior e o efeito pêndulo.", "C) O uso de óculos de proteção.", "D) A necessidade de supervisão.", "E) A transpiração excessiva."],
            "correta": "B) O impacto contra o nível inferior e o efeito pêndulo.",
            "explicacao": "O sistema de retenção de queda deve ser planejado para parar o trabalhador antes que ele atinja o solo ou estruturas."
        },
        {
            "enunciado": "A sigla CAT (Comunicação de Acidente de Trabalho) deve ser emitida pela empresa mesmo em casos de acidentes sem afastamento. Qual o prazo legal para emissão da CAT em caso de morte?",
            "opcoes": ["A) Até o final do mês.", "B) Em até 24 horas.", "C) Imediatamente.", "D) Em até 7 dias úteis.", "E) Não é necessário emitir CAT em caso de morte."],
            "correta": "C) Imediatamente.",
            "explicacao": "Acidentes fatais exigem comunicação imediata às autoridades competentes."
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
         
