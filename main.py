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
questoes_simulado = [
        # ==============================================================================
        # ==============================================================================
# MATÉRIA: INSTRUMENTAÇÃO E CONTROLE DE PROCESSOS
# PADRÃO: CESGRANRIO (REALISMO TOTAL PETROBRAS)
# CONTEÚDO: MALHAS, SENSORES E VÁLVULAS
# STATUS: 100% ATUALIZADO ✅
# ==============================================================================

        {
            "enunciado": "Durante uma ronda operacional em uma unidade de destilação, o operador observa que uma válvula de controle de nível de um vaso separador está com 100% de abertura, mas o nível continua subindo acima do Set Point. Ao verificar o instrumento, nota-se que o sinal de saída do controlador (MV) é de 20 mA. Considerando que a válvula é do tipo 'Falha-Fechada' (Air-to-Open), qual a causa mais provável para o desvio?",
            "opcoes": [
                "A) O suprimento de ar de instrumentos da válvula foi interrompido.",
                "B) O posicionador da válvula está operando em malha aberta.",
                "C) Houve perda de sinal elétrico (0 mA) no transmissor de nível.",
                "D) A válvula está travada mecanicamente na posição aberta ou há obstrução na linha.",
                "E) O controlador foi colocado em modo manual por erro de lógica."
            ],
            "correta": "D) A válvula está travada mecanicamente na posição aberta ou há obstrução na linha.",
            "explicacao": "Se o sinal é 20mA (máximo) e a válvula é Air-to-Open, ela deveria estar totalmente aberta e dando vazão. Se o nível sobe mesmo com ela aberta, o problema é mecânico ou obstrução no fluxo."
        },
        
        {
            "enunciado": "Em sistemas de controle de processos químicos, a ação de controle Integral (I) é frequentemente utilizada em conjunto com a ação Proporcional (P). De acordo com a teoria de controle aplicada em refinarias, o principal objetivo técnico de inserir a ação Integral em uma malha de controle é:",
            "opcoes": [
                "A) Antecipar variações bruscas na variável de processo (PV).",
                "B) Eliminar o erro de regime permanente (Offset) entre a PV e o Set Point.",
                "C) Reduzir o tempo de resposta inicial da válvula de controle.",
                "D) Estabilizar a malha em caso de ruídos de alta frequência no sensor.",
                "E) Permitir que o controlador opere apenas com sinais pneumáticos."
            ],
            "correta": "B) Eliminar o erro de regime permanente (Offset) entre a PV e o Set Point.",
            "explicacao": "A Cesgranrio cobra muito esse conceito: a ação Proporcional gera um erro residual (offset). Somente a ação Integral consegue zerar esse erro ao longo do tempo."
        },
        {
            "enunciado": "Para a medição de temperatura em fornos de processo onde as temperaturas ultrapassam 1000°C, o sensor deve possuir alta robustez e ampla faixa de medição. Nestas condições, o instrumento mais adequado e comumente especificado nos projetos da Petrobras é o:",
            "opcoes": [
                "A) Termômetro bimetálico de haste rígida.",
                "B) Sensor de resistência PT-100 (RTD).",
                "C) Termopar tipo K (Cromel-Alumel).",
                "D) Termômetro de enchimento de mercúrio.",
                "E) Pressostato diferencial de temperatura."
            ],
            "correta": "C) Termopar tipo K (Cromel-Alumel).",
            "explicacao": "Enquanto o PT-100 é mais preciso para temperaturas baixas e médias, os termopares (especialmente o tipo K) são os preferidos para altas temperaturas de fornos devido à sua durabilidade e faixa de medição."
        },

    
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
        },
            
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
        },

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
        },
        # --- MATÉRIA 01: OPERAÇÕES UNITÁRIAS (BOMBAS, TROCADORES, DESTILAÇÃO) ---
        {
            "enunciado": "Em uma unidade de hidrotratamento, uma bomba centrífuga de grande porte apresenta sinais de instabilidade, com flutuações na pressão de descarga e ruído característico de 'pinhão sendo triturado'. O operador suspeita de cavitação no primeiro estágio da bomba. Considerando a termodinâmica do processo, qual ação operacional imediata poderia mitigar a cavitação sem interromper o fluxo?",
            "opcoes": ["A) Aumentar a temperatura do fluido na sucção para reduzir a viscosidade.", "B) Reduzir o nível do vaso de sucção para aumentar a velocidade do fluido.", "C) Promover o resfriamento do fluido de sucção ou aumentar a pressão estática no bocal de entrada.", "D) Fechar parcialmente a válvula de sucção para estabilizar o fluxo.", "E) Abrir totalmente a válvula de descarga para reduzir a contrapressão."],
            "correta": "C) Promover o resfriamento do fluido de sucção ou aumentar a pressão estática no bocal de entrada.",
            "explicacao": "Para evitar a cavitação, deve-se aumentar o NPSH disponível. Isso é feito aumentando a pressão na sucção ou diminuindo a pressão de vapor (resfriando o fluido)."
        },
        
        {
            "enunciado": "No projeto de trocadores de calor do tipo casco e tubos (shell and tube), as chicanas (baffles) desempenham papéis estruturais e térmicos. Sob o ponto de vista da eficiência da troca térmica, a função primordial das chicanas é:",
            "opcoes": ["A) Impedir a mistura entre o fluido do casco e o fluido dos tubos.", "B) Garantir que o escoamento no lado do casco seja puramente laminar.", "C) Induzir a turbulência e direcionar o fluido do casco para cruzar perpendicularmente o feixe de tubos.", "D) Atuar como isolante térmico para evitar perdas de calor para o ambiente externo.", "E) Facilitar o processo de drenagem e purga do trocador durante paradas de manutenção."],
            "correta": "C) Induzir a turbulência e direcionar o fluido do casco para cruzar perpendicularmente o feixe de tubos.",
            "explicacao": "As chicanas aumentam o coeficiente de transferência de calor ao promover turbulência e forçar o fluido a percorrer um caminho maior em contato com os tubos."
        },
        {
            "enunciado": "Durante a operação de uma coluna de destilação fracionada, ocorre o fenômeno de 'inundação' (flooding). Esse evento compromete severamente a eficiência da separação porque:",
            "opcoes": ["A) Aumenta excessivamente a temperatura no topo da torre.", "B) Ocorre o arraste excessivo de líquido pelo vapor ascendente, preenchendo o espaço entre os pratos.", "C) Aumenta a pureza do produto de fundo de forma descontrolada.", "D) Reduz a pressão diferencial ao longo da coluna.", "E) Impede a entrada de carga na seção de alimentação."],
            "correta": "B) Ocorre o arraste excessivo de líquido pelo vapor ascendente, preenchendo o espaço entre os pratos.",
            "explicacao": "A inundação ocorre quando a velocidade do vapor é tão alta que impede a descida do líquido, resultando em acúmulo de líquido nos pratos e perda de separação."
        },
        
        {
            "enunciado": "Bombas de deslocamento positivo, como as de pistão ou diafragma, são preferencialmente utilizadas em detrimento das centrífugas quando a aplicação exige:",
            "opcoes": ["A) Altíssimas vazões com baixas pressões de descarga.", "B) Manuseio de fluidos com baixíssima viscosidade, como GLP.", "C) Vazão constante independentemente de grandes variações na pressão de descarga (contrapressão).", "D) Baixo custo inicial de instalação e manutenção simplificada.", "E) Ausência total de válvulas de alívio no sistema de descarga."],
            "correta": "C) Vazão constante independentemente de grandes variações na pressão de descarga (contrapressão).",
            "explicacao": "Bombas de deslocamento positivo entregam um volume fixo por ciclo, sendo ideais para dosagem ou alta pressão com vazão constante."
        },
        {
            "enunciado": "Em sistemas de transferência de calor, o fenômeno de 'fouling' (incrustação) em permutadores resulta em um aumento progressivo da resistência térmica. Qual o impacto direto desse fenômeno na perda de carga (ΔP) do equipamento?",
            "opcoes": ["A) A perda de carga permanece inalterada.", "B) A perda de carga diminui devido ao polimento das superfícies.", "C) A perda de carga aumenta devido à redução da área de escoamento e aumento da rugosidade.", "D) O fouling impacta apenas a troca térmica, não afetando a mecânica do fluido.", "E) A perda de carga oscila apenas em fluidos gasosos."],
            "correta": "C) A perda de carga aumenta devido à redução da área de escoamento e aumento da rugosidade.",
            "explicacao": "As incrustações reduzem o diâmetro útil de passagem do fluido, aumentando a velocidade local e o atrito, o que eleva a perda de carga."
        },
        {
            "enunciado": "No processo de destilação atmosférica, a função do refluxo de topo é:",
            "opcoes": ["A) Fornecer calor adicional para a vaporização da carga.", "B) Controlar a temperatura no topo da torre e garantir a pureza da fração mais leve.", "C) Aumentar a pressão interna da coluna para facilitar a condensação.", "D) Lavar os pratos de fundo para remover resíduos pesados.", "E) Reduzir o tempo de residência do petróleo no refervedor."],
            "correta": "B) Controlar a temperatura no topo da torre e garantir a pureza da fração mais leve.",
            "explicacao": "O refluxo (líquido que retorna à torre) condensa os componentes menos voláteis que tentam sair pelo topo, purificando o produto de topo."
        },
        {
            "enunciado": "As válvulas de retenção (check valves) são componentes críticos em sistemas de bombeamento. Sua principal função em uma instalação industrial é:",
            "opcoes": ["A) Controlar a vazão de forma proporcional através de um sinal pneumático.", "B) Proteger a bomba contra a sobrepressão de descarga.", "C) Impedir o fluxo reverso que poderia causar a rotação inversa da bomba e danos ao selo mecânico.", "D) Isolar o equipamento para manutenção sem necessidade de drenagem.", "E) Reduzir a turbulência na sucção da bomba."],
            "correta": "C) Impedir o fluxo reverso que poderia causar a rotação inversa da bomba e danos ao selo mecânico.",
            "explicacao": "A válvula de retenção permite o fluxo em apenas um sentido, evitando que o fluido retorne quando a bomba é desligada."
        },
        {
            "enunciado": "O refervedor (reboiler) do tipo 'termossifão' utiliza qual princípio físico para promover a circulação do fluido entre o fundo da torre e o trocador?",
            "opcoes": ["A) Ação de uma bomba centrífuga dedicada.", "B) Diferença de densidade entre o líquido frio e a mistura líquido-vapor aquecida.", "C) Diferença de pressão pneumática injetada na base.", "D) Força centrífuga gerada por um rotor interno.", "E) Capilaridade das paredes dos tubos."],
            "correta": "B) Diferença de densidade entre o líquido frio e a mistura líquido-vapor aquecida.",
            "explicacao": "No termossifão, o fluido circula naturalmente porque a mistura aquecida (vaporizada) é menos densa e tende a subir, retornando à torre."
        },
        {
            "enunciado": "Um compressor centrífugo entra em regime de 'Surge' (pumping). Esse fenômeno é caracterizado por:",
            "opcoes": ["A) Uma operação extremamente silenciosa e eficiente.", "B) Oscilações violentas de pressão e vazão com possibilidade de fluxo reverso momentâneo.", "C) Aumento repentino na temperatura dos mancais apenas.", "D) Estabilização da rotação do motor elétrico.", "E) Redução total do consumo de energia."],
            "correta": "B) Oscilações violentas de pressão e vazão com possibilidade de fluxo reverso momentâneo.",
            "explicacao": "O surge ocorre quando a contrapressão é maior que a pressão gerada pelo compressor, causando instabilidade física grave na máquina."
        },
        {
            "enunciado": "Em trocadores de calor resfriados a ar (Air Coolers), o ajuste do ângulo das pás do ventilador (pitch) tem como objetivo:",
            "opcoes": ["A) Mudar o sentido do fluxo do fluido de processo.", "B) Controlar a vazão de ar e, consequentemente, a temperatura de saída do fluido processado.", "C) Reduzir o nível de ruído da unidade de refino.", "D) Evitar a corrosão externa dos tubos aletados.", "E) Aumentar a pressão interna dos tubos de processo."],
            "correta": "B) Controlar a vazão de ar e, consequentemente, a temperatura de saída do fluido processado.",
            "explicacao": "Alterar o ângulo das pás permite variar a quantidade de ar soprada sobre os tubos, ajustando a capacidade de resfriamento."
        },
        {
            "enunciado": "A eficiência de uma torre de refrigeração de água baseia-se primordialmente em qual fenômeno de transferência?",
            "opcoes": ["A) Condução térmica através das paredes metálicas.", "B) Radiação infravermelha para o espaço sideral.", "C) Evaporação parcial de uma fração da água em contato com o ar contra-corrente.", "D) Compressão adiabática do vapor d'água.", "E) Reação química exotérmica entre a água e o enchimento."],
            "correta": "C) Evaporação parcial de uma fração da água em contato com o ar contra-corrente.",
            "explicacao": "A água resfria porque cede calor latente para que uma pequena parte dela evapore ao entrar em contato com o ar."
        },
        {
            "enunciado": "Válvulas de controle do tipo 'Globo' são amplamente preferidas para serviços de:",
            "opcoes": ["A) Bloqueio estanque (on-off) sem perda de carga.", "B) Regulagem de vazão (throttling) devido à sua característica de controle linear ou igual porcentagem.", "C) Passagem de raspadores (pigs) em oleodutos.", "D) Operação com fluidos altamente corrosivos e abrasivos (lama).", "E) Serviços onde a queda de pressão deve ser absolutamente zero."],
            "correta": "B) Regulagem de vazão (throttling) devido à sua característica de controle linear ou igual porcentagem.",
            "explicacao": "Diferente da válvula gaveta, a válvula globo é projetada para trabalhar em posições intermediárias para ajustar o fluxo com precisão."
        },
        {
            "enunciado": "O fenômeno conhecido como 'Primado' (carry-over) em caldeiras a vapor consiste no arraste de gotículas de líquido junto com o vapor para a linha de saída. Uma das causas operacionais para o primado é:",
            "opcoes": ["A) Baixo nível de água no tubulão.", "B) Alta concentração de sólidos dissolvidos e excesso de produtos químicos na água (espumamento).", "C) Pressão de vapor muito acima da nominal.", "D) Uso de combustível com baixo poder calorífico.", "E) Excesso de purga de fundo."],
            "correta": "B) Alta concentração de sólidos dissolvidos e excesso de produtos químicos na água (espumamento).",
            "explicacao": "A contaminação da água causa bolhas estáveis (espuma), que são arrastadas pelo vapor, podendo causar danos em turbinas e trocadores."
        },
        {
            "enunciado": "Em uma bomba centrífuga, a função da voluta (ou carcaça em espiral) é:",
            "opcoes": ["A) Aumentar a velocidade do fluido que sai do rotor.", "B) Converter a energia cinética (velocidade) fornecida pelo rotor em energia de pressão.", "C) Filtrar as impurezas sólidas antes da descarga.", "D) Reduzir o peso total do equipamento para facilitar o suporte.", "E) Resfriar o selo mecânico através de dissipação natural."],
            "correta": "B) Converter a energia cinética (velocidade) fornecida pelo rotor em energia de pressão.",
            "explicacao": "A geometria da voluta, com área crescente, faz com que a velocidade diminua e a pressão aumente (Princípio de Bernoulli)."
        },
        {
            "enunciado": "O condensador de topo de uma torre de destilação tem a função de transformar o vapor de topo em líquido. Parte desse líquido retorna à torre (refluxo) e a outra parte segue como produto. Se o refluxo for interrompido, o que acontece com o perfil de pureza no topo?",
            "opcoes": ["A) A pureza aumenta drasticamente.", "B) A pureza diminui, pois vapores mais pesados não serão condensados e sairão com o produto.", "C) O perfil de pureza não se altera.", "D) A torre entra em vácuo instantaneamente.", "E) O produto de fundo torna-se mais leve."],
            "correta": "B) A pureza diminui, pois vapores mais pesados não serão condensados e sairão com o produto.",
            "explicacao": "Sem refluxo, não há 'lavagem' do vapor ascendente, permitindo que frações pesadas contaminem o produto leve de topo."
        },
        {
            "enunciado": "Ejetores a vácuo, comuns em colunas de destilação a vácuo, operam baseados em qual princípio?",
            "opcoes": ["A) Compressão mecânica por pistões de alta frequência.", "B) Efeito Venturi, utilizando um fluido motriz (geralmente vapor) em alta velocidade.", "C) Resfriamento criogênico dos gases residuais.", "D) Atração eletrostática de moléculas de hidrocarbonetos.", "E) Reação de combustão interna controlada."],
            "correta": "B) Efeito Venturi, utilizando um fluido motriz (geralmente vapor) em alta velocidade.",
            "explicacao": "O vapor motriz passa por um bocal convergente-divergente, criando uma zona de baixa pressão que succiona os gases da torre."
        },
        {
            "enunciado": "Em permutadores de calor do tipo placa, qual a principal vantagem em relação aos de casco e tubos para aplicações com fluidos limpos?",
            "opcoes": ["A) Suportam pressões e temperaturas muito mais elevadas.", "B) Ocupam maior área de instalação (pegada industrial).", "C) Elevado coeficiente de transferência de calor e facilidade de ampliação da área de troca.", "D) São imunes a qualquer tipo de corrosão química.", "E) Não exigem gaxetas ou juntas de vedação."],
            "correta": "C) Elevado coeficiente de transferência de calor e facilidade de ampliação da área de troca.",
            "explicacao": "Trocadores de placa são muito compactos e eficientes, permitindo adicionar mais placas para aumentar a capacidade térmica."
        },
        {
            "enunciado": "Qual o componente de uma caldeira aquatubular responsável por separar o vapor saturado da água líquida antes do superaquecimento?",
            "opcoes": ["A) Fornalha.", "B) Tubulão de vapor (Steam Drum).", "C) Economizador.", "D) Soprador de fuligem.", "E) Pré-aquecedor de ar."],
            "correta": "B) Tubulão de vapor (Steam Drum).",
            "explicacao": "No tubulão superior, a água pesada fica embaixo e o vapor sobe para ser coletado, evitando arraste de líquido."
        },
        {
            "enunciado": "A vedação entre o eixo rotativo e a carcaça de uma bomba centrífuga para evitar vazamentos de fluidos perigosos é feita preferencialmente por:",
            "opcoes": ["A) Gaxetas de amianto.", "B) Selos mecânicos.", "C) Juntas de cortiça.", "D) Buchas de bronze.", "E) Anéis de borracha simples."],
            "correta": "B) Selos mecânicos.",
            "explicacao": "Selos mecânicos oferecem vedação superior, menor atrito e menos vazamentos que as antigas gaxetas, sendo padrão na indústria do petróleo."
        },
        {
            "enunciado": "Em uma torre de destilação, a região situada acima do prato de alimentação é denominada:",
            "opcoes": ["A) Seção de esgotamento (stripping section).", "B) Seção de retificação (rectifying section).", "C) Zona de flash.", "D) Bacia de acumulação.", "E) Plenum de descarga."],
            "correta": "B) Seção de retificação (rectifying section).",
            "explicacao": "A seção de retificação é onde ocorre o enriquecimento do vapor nos componentes mais voláteis."
        },
            
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
         
