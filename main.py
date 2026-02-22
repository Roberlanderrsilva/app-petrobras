import streamlit as st
import random 

# --- CONFIGURAÇÃO E CABEÇALHO ---
st.set_page_config(page_title="Mentor Petrobras", layout="centered")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Petrobras_logo.svg/1200px-Petrobras_logo.svg.png", width=150)
st.title("⚓ Mentor Petrobras")
st.write("---")

# --- BANCO DE DADOS: BLOCO 01 (50 QUESTÕES) ---
if 'questoes_db' not in st.session_state:
    db_original = [            # --- MATÉRIA 03: PROCESSOS DE REFINO E PETROQUÍMICA ---
        {
            "enunciado": "O processo de Craqueamento Catalítico Fluido (FCC) é uma das unidades mais rentáveis de uma refinaria. Qual a principal transformação química que ocorre nesse processo e qual o seu objetivo comercial?",
            "opcoes": ["A) Unir moléculas leves para formar polímeros de alta densidade.", "B) Quebrar moléculas pesadas de hidrocarbonetos em frações mais leves e valiosas, como gasolina e GLP.", "C) Remover nitrogênio e enxofre através da reação com hidrogênio gasoso.", "D) Transformar óleo diesel em óleo lubrificante de alta viscosidade.", "E) Separar mecanicamente a água salgada do petróleo bruto."],
            "correta": "B) Quebrar moléculas pesadas de hidrocarbonetos em frações mais leves e valiosas, como gasolina e GLP.",
            "explicacao": "O FCC 'quebra' (craqueia) cadeias longas em cadeias menores, aumentando a produção de combustíveis nobres a partir de resíduos pesados."
        },
        {
            "enunciado": "Nas unidades de Hidrotratamento (HDT), o petróleo ou seus derivados reagem com hidrogênio sob alta pressão e temperatura em presença de catalisador. O principal objetivo ambiental e operacional deste processo é:",
            "opcoes": ["A) Aumentar o teor de aromáticos na gasolina.", "B) Reduzir o teor de enxofre e contaminantes metálicos, diminuindo a emissão de SOx.", "C) Transformar todo o óleo em gás natural sintético.", "D) Resfriar a carga para armazenamento em tanques de baixa pressão.", "E) Aumentar a densidade do produto final para exportação."],
            "correta": "B) Reduzir o teor de enxofre e contaminantes metálicos, diminuindo a emissão de SOx.",
            "explicacao": "O HDT remove enxofre (dessulfurização), o que é vital para atender normas ambientais e proteger catalisadores de unidades subsequentes."
        },
        {
            "enunciado": "A Reforma Catalítica é um processo projetado para reorganizar as moléculas de nafta. O principal ganho de qualidade para a corrente de gasolina gerada nesse processo é o aumento da:",
            "opcoes": ["A) Volatilidade.", "B) Octanagem.", "C) Viscosidade.", "D) Corrosividade.", "E) Ponto de fulgor."],
            "correta": "B) Octanagem.",
            "explicacao": "A reforma transforma hidrocarbonetos lineares em aromáticos e ramificados, que possuem maior resistência à detonação (maior octanagem)."
        },
        {
            "enunciado": "No processamento primário de petróleo, a 'Dessalgação' ocorre antes da carga entrar na torre de destilação. Por que a presença de sais como o Cloreto de Magnésio (MgCl2) é extremamente perigosa para as torres de destilação?",
            "opcoes": ["A) Porque os sais entopem os queimadores dos fornos.", "B) Porque em altas temperaturas esses sais sofrem hidrólise, liberando Ácido Clorídrico (HCl), que causa corrosão severa no topo da torre.", "C) Porque os sais tornam o petróleo inflamável demais.", "D) Porque o sal impede a evaporação da nafta leve.", "E) Porque o sal reage com o aço inox tornando-o mais frágil."],
            "correta": "B) Porque em altas temperaturas esses sais sofrem hidrólise, liberando Ácido Clorídrico (HCl), que causa corrosão severa no topo da torre.",
            "explicacao": "O HCl gerado ataca o metal dos pratos e condensadores de topo, exigindo a remoção quase total dos sais na dessalgadora."
        },
        {
            "enunciado": "O Coqueamento Retardado é um processo térmico severo. O produto sólido gerado nesse processo, que possui alto teor de carbono e é utilizado na indústria siderúrgica e de alumínio, é o:",
            "opcoes": ["A) Resíduo de vácuo.", "B) Coque de petróleo.", "C) Asfalto líquido.", "D) Betume.", "E) Parafina macrocristalina."],
            "correta": "B) Coque de petróleo.",
            "explicacao": "O coque é o produto sólido resultante da 'queima' térmica controlada dos resíduos mais pesados do refino."
        },
        {
            "enunciado": "Em uma unidade de Recuperação de Enxofre (URE), utiliza-se frequentemente o Processo Claus. Qual o principal reagente gasoso que é convertido em enxofre elementar líquido nesse processo?",
            "opcoes": ["A) Metano (CH4).", "B) Gás Sulfídrico (H2S).", "C) Dióxido de Carbono (CO2).", "D) Monóxido de Carbono (CO).", "E) Amônia (NH3)."],
            "correta": "B) Gás Sulfídrico (H2S).",
            "explicacao": "A URE transforma o H2S tóxico (vindo do HDT e outras unidades) em enxofre puro, que é um subproduto comercializável."
        },
        {
            "enunciado": "A destilação a vácuo é aplicada aos resíduos da destilação atmosférica (RAT). O uso de vácuo (pressões abaixo da atmosférica) tem como objetivo técnico:",
            "opcoes": ["A) Aumentar a velocidade de vaporização dos gases leves.", "B) Reduzir a temperatura de ebulição dos hidrocarbonetos pesados, evitando o craqueamento térmico indesejado e a formação de coque nos tubos do forno.", "C) Impedir que o oxigênio entre na torre e cause explosões.", "D) Separar o enxofre do óleo diesel sem uso de catalisadores.", "E) Aumentar a pressão interna para economizar vapor."],
            "correta": "B) Reduzir a temperatura de ebulição dos hidrocarbonetos pesados, evitando o craqueamento térmico indesejado e a formação de coque nos tubos do forno.",
            "explicacao": "Ao baixar a pressão, as substâncias fervem em temperaturas menores, permitindo separar frações pesadas sem 'queimar' o óleo."
        },
        {
            "enunciado": "O Gás Liquefeito de Petróleo (GLP) é composto majoritariamente por quais hidrocarbonetos?",
            "opcoes": ["A) Metano e Etano.", "B) Propano e Butano.", "C) Pentano e Hexano.", "D) Benzeno e Tolueno.", "E) Octano e Decano."],
            "correta": "B) Propano e Butano.",
            "explicacao": "O GLP (gás de cozinha) é a mistura de C3 (propano) e C4 (butano), que podem ser liquefeitos sob pressões moderadas."
        },
        {
            "enunciado": "Na indústria petroquímica, o 'Vapor Cracking' (Etileno) utiliza como carga principal a Nafta ou o Etano. O principal objetivo deste processo é a produção de olefinas leves, como:",
            "opcoes": ["A) Querosene e Diesel.", "B) Etileno e Propileno.", "C) Óleos Lubrificantes.", "D) Resíduo Asfáltico.", "E) Gasolina de Aviação."],
            "correta": "B) Etileno e Propileno.",
            "explicacao": "O etileno e o propileno são as matérias-primas básicas para a produção de quase todos os plásticos (polietileno, polipropileno)."
        },
        {
            "enunciado": "O processo de Desasfaltação a Propano visa extrair óleos nobres de resíduos pesados. O propano atua nesse processo como:",
            "opcoes": ["A) Catalisador sólido.", "B) Solvente seletivo.", "C) Combustível para o forno.", "D) Agente de resfriamento criogênico.", "E) Inibidor de corrosão."],
            "correta": "B) Solvente seletivo.",
            "explicacao": "O propano líquido dissolve o óleo mas não dissolve o asfalto, permitindo a separação por diferença de solubilidade."
        },
        {
            "enunciado": "Em uma torre de destilação, a 'Zona de Flash' localiza-se:",
            "opcoes": ["A) No topo da torre, junto aos condensadores.", "B) No fundo da torre, abaixo do refervedor.", "C) Na seção de entrada da carga, onde ocorre a vaporização parcial instantânea.", "D) Dentro dos acumuladores de refluxo.", "E) No sistema de purga de gases incondensáveis."],
            "correta": "C) Na seção de entrada da carga, onde ocorre a vaporização parcial instantânea.",
            "explicacao": "A carga chega aquecida e, ao entrar na torre (menor pressão), parte dela 'pisca' (vaporiza instantaneamente) na zona de flash."
        },
        {
            "enunciado": "O Hidrocraqueamento Catalítico (HCC) diferencia-se do FCC principalmente por:",
            "opcoes": ["A) Não utilizar catalisadores.", "B) Operar na presença de hidrogênio e em pressões muito mais elevadas, produzindo derivados saturados e de alta pureza.", "C) Produzir apenas resíduos asfálticos.", "D) Ser um processo puramente mecânico de centrifugação.", "E) Ocorrer apenas em temperatura ambiente."],
            "correta": "B) Operar na presença de hidrogênio e em pressões muito mais elevadas, produzindo derivados saturados e de alta pureza.",
            "explicacao": "O HCC combina craqueamento com hidrogenação, resultando em produtos de altíssima qualidade ambiental."
        },
        {
            "enunciado": "Qual a finalidade da unidade de Alquilação nas refinarias modernas?",
            "opcoes": ["A) Produzir GLP a partir de asfalto.", "B) Produzir um componente de gasolina de altíssima octanagem (alquilado) a partir de isobutano e olefinas leves.", "C) Queimar gases residuais para gerar energia elétrica.", "D) Tratar a água de descarte da dessalgadora.", "E) Separar o óleo lubrificante da parafina."],
            "correta": "B) Produzir um componente de gasolina de altíssima octanagem (alquilado) a partir de isobutano e olefinas leves.",
            "explicacao": "A alquilação usa catalisadores ácidos para criar moléculas ramificadas ideais para gasolinas premium."
        },
        {
            "enunciado": "O 'Ponto de Fulgor' de um derivado de petróleo é definido como a temperatura mínima na qual:",
            "opcoes": ["A) O líquido entra em ebulição constante.", "B) O combustível queima continuamente sem necessidade de chama externa.", "C) O vapor do combustível forma uma mistura inflamável com o ar, capaz de sofrer uma inflamação momentânea (lampejo) diante de uma fonte de ignição.", "D) O óleo torna-se sólido devido ao frio.", "E) A viscosidade do fluido chega a zero."],
            "correta": "C) O vapor do combustível forma uma mistura inflamável com o ar, capaz de sofrer uma inflamação momentânea (lampejo) diante de uma fonte de ignição.",
            "explicacao": "É uma medida crítica de segurança para transporte e armazenamento de combustíveis."
        },
        {
            "enunciado": "A 'Corrente de Reciclo' em processos químicos industriais serve primordialmente para:",
            "opcoes": ["A) Aumentar o desperdício de energia térmica.", "B) Reintroduzir reagentes não convertidos no reator, aumentando a conversão global do processo.", "C) Descartar impurezas sólidas do sistema.", "D) Reduzir a pressão operacional do reator.", "E) Limpar as tubulações durante a operação normal."],
            "correta": "B) Reintroduzir reagentes não convertidos no reator, aumentando a conversão global do processo.",
            "explicacao": "O reciclo garante que a matéria-prima seja aproveitada ao máximo antes de sair do sistema."
        },
        {
            "enunciado": "Em uma unidade de Destilação Atmosférica, o que é o 'RAT'?",
            "opcoes": ["A) Refino Altamente Tecnológico.", "B) Resíduo Atmosférico (fração pesada que não vaporizou na torre atmosférica).", "C) Reagente de Ativação Térmica.", "D) Regulador de Alta Temperatura.", "E) Retorno de Água Tratada."],
            "correta": "B) Resíduo Atmosférico (fração pesada que não vaporizou na torre atmosférica).",
            "explicacao": "O RAT é a carga da unidade de vácuo ou do coqueamento."
        },
        {
            "enunciado": "O catalisador utilizado no processo de FCC circula continuamente entre dois vasos principais. Quais são eles?",
            "opcoes": ["A) Forno e Permutador.", "B) Reator e Regenerador.", "C) Torre de Destilação e Condensador.", "D) Dessalgadora e Separador API.", "E) Filtro e Bomba."],
            "correta": "B) Reator e Regenerador.",
            "explicacao": "No reator ocorre a quebra do óleo; no regenerador o coque depositado no catalisador é queimado para reativá-lo."
        },
        {
            "enunciado": "O 'Ponto de Fluidez' (Pour Point) é uma especificação importante para óleos combustíveis e lubrificantes porque indica:",
            "opcoes": ["A) A temperatura na qual o óleo pega fogo.", "B) A menor temperatura na qual o óleo ainda consegue escoar por gravidade.", "C) A cor exata do produto final.", "D) O teor de enxofre presente na amostra.", "E) A pressão de vapor do produto a 20°C."],
            "correta": "B) A menor temperatura na qual o óleo ainda consegue escoar por gravidade.",
            "explicacao": "Se a temperatura baixar do ponto de fluidez, o óleo 'congela' (para de escoar), entupindo tubulações."
        },
        {
            "enunciado": "A unidade de Isomerização visa transformar parafinas lineares (como n-pentano) em parafinas ramificadas (como isopentano). O objetivo é:",
            "opcoes": ["A) Diminuir o volume da gasolina.", "B) Aumentar o índice de octano da gasolina sem adicionar chumbo ou aromáticos.", "C) Remover o nitrogênio da carga.", "D) Transformar gás em líquido.", "E) Produzir óleo diesel a partir de nafta."],
            "correta": "B) Aumentar o índice de octano da gasolina sem adicionar chumbo ou aromáticos.",
            "explicacao": "Moléculas ramificadas queimam melhor no motor, aumentando a octanagem."
        },
        {
            "enunciado": "O que define uma 'Área Classificada' em uma refinaria de petróleo?",
            "opcoes": ["A) Uma área onde o acesso é permitido apenas a diretores.", "B) Um local onde existe ou pode existir uma atmosfera explosiva devido à presença de gases, vapores ou poeiras inflamáveis.", "C) Uma zona de preservação ambiental com florestas nativas.", "D) Uma área de escritório com ar-condicionado.", "E) Um local onde não há nenhum risco elétrico."],
            "correta": "B) Um local onde existe ou pode existir uma atmosfera explosiva devido à presença de gases, vapores ou poeiras inflamáveis.",
            "explicacao": "Áreas classificadas exigem equipamentos elétricos especiais (Ex) para evitar centelhas que causem explosão."
        }
            
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
         
