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

# 4. BANCO DE DADOS (BLOCO 01 - REFINO)
if 'questoes_db' not in st.session_state:
    db_original = [
        {
            questoes_petrobras_avancadas = [
    # --- BLOCO: OPERADOR DE PRODUÇÃO (ENUNCIADOS LONGOS) ---
    {
        "id": 1,
        "area": "Produção",
        "pergunta": "Durante o processamento primário de petróleo em uma Unidade de Manutenção e Segurança (UMS), o fluido multifásico proveniente dos poços atinge o vaso separador de primeiro estágio. Devido à alta pressão e velocidade de entrada, o fluido tende a gerar turbulência e arraste de gotículas de óleo para a corrente de gás. Para mitigar esse arraste mecânico e garantir que o gás saia pelo topo com o menor teor de líquido possível, utiliza-se um componente interno constituído por uma malha metálica ou de polímero. Esse componente é o:",
        "opcoes": ["A) Defletor de entrada (Inlet Diverter)", "B) Quebra-ondas (Wave Breaker)", "C) Extrator de névoa (Demister Pad)", "D) Placa de orifício de fundo"],
        "resposta": "C"
    },
    {
        "id": 2,
        "area": "Produção",
        "pergunta": "Um operador de produção identifica, durante sua ronda, que uma bomba centrífuga de transferência de água de descarte apresenta um ruído característico de 'bombeamento de pedras', acompanhado de forte vibração e queda na pressão de descarga. Ao verificar o NPSH disponível, constata-se que este é inferior ao NPSH requerido pelo fabricante. Esse cenário técnico descreve o fenômeno destrutivo que causa pites de erosão no impulsor, conhecido como:",
        "opcoes": ["A) Golpe de Aríete", "B) Cavitação", "C) Surto de Pressão (Surge)", "D) Flotação centrípeta"],
        "resposta": "B"
    },
    {
        "id": 3,
        "area": "Produção",
        "pergunta": "Em ambientes de exploração 'offshore', a presença de H2S (Gás Sulfídrico) em correntes de processo é monitorada rigorosamente. Em um cenário de vazamento acidental em uma área baixa da planta (conveses inferiores), o operador deve saber que este gás, além de ser altamente tóxico e letal em baixas concentrações, possui uma característica física fundamental que dita seu comportamento de dispersão. Essa característica é:",
        "opcoes": ["A) Ser mais leve que o ar, tendendo a se acumular em tetos.", "B) Ser inodoro em qualquer concentração, impossibilitando a detecção humana.", "C) Ser mais denso (pesado) que o ar, tendendo a se acumular em canaletas e pontos baixos.", "D) Ser altamente reativo com o nitrogênio atmosférico, gerando chamas verdes."],
        "resposta": "C"
    },
    {
        "id": 4,
        "area": "Produção",
        "pergunta": "Considere um sistema de segurança instrumentado de uma plataforma (SIS). Quando uma variável de processo, como o nível de um vaso separador, atinge o limite de 'Muito Alto' (LSHH), o sistema deve agir para isolar a entrada de fluidos e proteger a integridade da planta. A válvula automática, projetada para fechamento rápido e estanqueidade total, acionada pelo sistema de intertravamento de emergência, é denominada:",
        "opcoes": ["A) Válvula de Controle de Fluxo (FCV)", "B) Válvula de Parada de Emergência (ESDV)", "C) Válvula de Alívio de Pressão (PSV)", "D) Válvula Globo de bloqueio manual"],
        "resposta": "B"
    },
]

questoes_petrobras_avancadas = [
    # --- BLOCO: OPERADOR DE PRODUÇÃO (ENUNCIADOS LONGOS) ---
    {
        "id": 1,
        "area": "Produção",
        "pergunta": "Durante o processamento primário de petróleo em uma Unidade de Manutenção e Segurança (UMS), o fluido multifásico proveniente dos poços atinge o vaso separador de primeiro estágio. Devido à alta pressão e velocidade de entrada, o fluido tende a gerar turbulência e arraste de gotículas de óleo para a corrente de gás. Para mitigar esse arraste mecânico e garantir que o gás saia pelo topo com o menor teor de líquido possível, utiliza-se um componente interno constituído por uma malha metálica ou de polímero. Esse componente é o:",
        "opcoes": ["A) Defletor de entrada (Inlet Diverter)", "B) Quebra-ondas (Wave Breaker)", "C) Extrator de névoa (Demister Pad)", "D) Placa de orifício de fundo"],
        "resposta": "C"
    },
    {
        "id": 2,
        "area": "Produção",
        "pergunta": "Um operador de produção identifica, durante sua ronda, que uma bomba centrífuga de transferência de água de descarte apresenta um ruído característico de 'bombeamento de pedras', acompanhado de forte vibração e queda na pressão de descarga. Ao verificar o NPSH disponível, constata-se que este é inferior ao NPSH requerido pelo fabricante. Esse cenário técnico descreve o fenômeno destrutivo que causa pites de erosão no impulsor, conhecido como:",
        "opcoes": ["A) Golpe de Aríete", "B) Cavitação", "C) Surto de Pressão (Surge)", "D) Flotação centrípeta"],
        "resposta": "B"
    },
    {
        "id": 3,
        "area": "Produção",
        "pergunta": "Em ambientes de exploração 'offshore', a presença de H2S (Gás Sulfídrico) em correntes de processo é monitorada rigorosamente. Em um cenário de vazamento acidental em uma área baixa da planta (conveses inferiores), o operador deve saber que este gás, além de ser altamente tóxico e letal em baixas concentrações, possui uma característica física fundamental que dita seu comportamento de dispersão. Essa característica é:",
        "opcoes": ["A) Ser mais leve que o ar, tendendo a se acumular em tetos.", "B) Ser inodoro em qualquer concentração, impossibilitando a detecção humana.", "C) Ser mais denso (pesado) que o ar, tendendo a se acumular em canaletas e pontos baixos.", "D) Ser altamente reativo com o nitrogênio atmosférico, gerando chamas verdes."],
        "resposta": "C"
    },
    {
        "id": 4,
        "area": "Produção",
        "pergunta": "Considere um sistema de segurança instrumentado de uma plataforma (SIS). Quando uma variável de processo, como o nível de um vaso separador, atinge o limite de 'Muito Alto' (LSHH), o sistema deve agir para isolar a entrada de fluidos e proteger a integridade da planta. A válvula automática, projetada para fechamento rápido e estanqueidade total, acionada pelo sistema de intertravamento de emergência, é denominada:",
        "opcoes": ["A) Válvula de Controle de Fluxo (FCV)", "B) Válvula de Parada de Emergência (ESDV)", "C) Válvula de Alívio de Pressão (PSV)", "D) Válvula Globo de bloqueio manual"],
        "resposta": "B"
    },
]

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
        },
        {
            "enunciado": "Qual é a principal função de uma bomba centrífuga em uma instalação industrial?",
            "opcoes": ["Aumentar a temperatura de um gás", "Transferir energia cinética a um fluido para transformá-la em energia de pressão", "Medir a vazão de sólidos", "Resfriar o óleo lubrificante"],
            "correta": "Transferir energia cinética a um fluido para transformá-la em energia de pressão",
            "explicacao": "A bomba centrífuga utiliza um rotor para acelerar o líquido, e a carcaça (voluta) converte essa velocidade em pressão."
        },
        {
            "enunciado": "O fenômeno da cavitação em bombas centrífugas ocorre quando:",
            "opcoes": ["A pressão do líquido cai abaixo da sua pressão de vapor, formando bolhas que implodem", "O motor elétrico gira rápido demais", "O fluido está muito quente", "Há excesso de lubrificante nos mancais"],
            "correta": "A pressão do líquido cai abaixo da sua pressão de vapor, formando bolhas que implodem",
            "explicacao": "A cavitação causa ruído, vibração e pode destruir o rotor da bomba devido ao impacto das implosões das bolhas de vapor."
        },
        {
            "enunciado": "Para evitar a cavitação, é necessário garantir que o valor de ________ seja superior ao requerido pela bomba.",
            "opcoes": ["Vazão", "NPSH disponível", "Temperatura externa", "Tensão elétrica"],
            "correta": "NPSH disponível",
            "explicacao": "O NPSH (Net Positive Suction Head) disponível deve ser sempre maior que o requerido pelo fabricante para evitar a formação de bolhas no bocal de sucção."
        },
        {
            "enunciado": "Qual tipo de compressor é mais indicado para grandes vazões e pressões moderadas em refinarias?",
            "opcoes": ["Compressor de Pistão", "Compressor Centrífugo", "Compressor de Palhetas", "Compressor de Diafragma"],
            "correta": "Compressor Centrífugo",
            "explicacao": "Os compressores centrífugos (dinâmicos) são ideais para processos contínuos que exigem grandes volumes de gás, como no craqueamento catalítico."
        },
        {
            "enunciado": "A função primordial do selo mecânico em uma bomba é:",
            "opcoes": ["Aumentar a vazão", "Evitar o vazamento de fluido entre o eixo rotativo e a carcaça da bomba", "Alinhar o motor", "Reduzir o consumo de energia"],
            "correta": "Evitar o vazamento de fluido entre o eixo rotativo e a carcaça da bomba",
            "explicacao": "O selo mecânico substitui as antigas gaxetas, oferecendo uma vedação muito mais eficiente e segura para produtos perigosos."
        },
        {
            "enunciado": "O 'Surge' (Surto) em compressores centrífugos é um fenômeno perigoso que consiste em:",
            "opcoes": ["Um aumento repentino na temperatura do ar", "A inversão cíclica do fluxo de gás, podendo causar danos mecânicos graves", "O travamento total do eixo", "Vazamento de óleo pelo selo"],
            "correta": "A inversão cíclica do fluxo de gás, podendo causar danos mecânicos graves",
            "explicacao": "O surge ocorre quando a vazão cai abaixo de um limite crítico e a pressão de descarga empurra o gás de volta para dentro do compressor."
        },
        {
            "enunciado": "Bombas de deslocamento positivo (como as de engrenagem) são preferíveis às centrífugas quando:",
            "opcoes": ["O fluido tem baixíssima viscosidade", "O fluido é muito viscoso (como óleo pesado) ou exige dosagem precisa", "A vazão é extremamente alta", "Não há necessidade de pressão"],
            "correta": "O fluido é muito viscoso (como óleo pesado) ou exige dosagem precisa",
            "explicacao": "Bombas de deslocamento positivo movem um volume fixo a cada rotação, sendo eficientes com fluidos grossos onde a centrífuga falharia."
        },
        {
            "enunciado": "O que acontece se uma bomba centrífuga operar com a válvula de descarga totalmente fechada por muito tempo (Shut-off)?",
            "opcoes": ["A bomba gasta menos energia", "O fluido aquece rapidamente devido ao atrito, podendo danificar vedações e partes internas", "A pressão cai para zero", "O motor para automaticamente"],
            "correta": "O fluido aquece rapidamente devido ao atrito, podendo danificar vedações e partes internas",
            "explicacao": "Sem fluxo para levar o calor embora, a energia do motor é convertida em calor no líquido parado dentro da carcaça."
        },
        {
            "enunciado": "Em um compressor de pistão (alternativo), a função das válvulas de sucção e descarga é:",
            "opcoes": ["Controlar a velocidade do motor", "Garantir o fluxo unidirecional do gás durante os ciclos de compressão", "Misturar óleo ao gás", "Resfriar o cilindro"],
            "correta": "Garantir o fluxo unidirecional do gás durante os ciclos de compressão",
            "explicacao": "As válvulas abrem e fecham por diferença de pressão, permitindo que o gás entre no cilindro e saia apenas para a linha de descarga."
        },
        {
            "enunciado": "Qual componente é responsável por transmitir o movimento do motor para o eixo da bomba?",
            "opcoes": ["Rotor", "Acoplamento", "Voluta", "Mancal"],
            "correta": "Acoplamento",
            "explicacao": "O acoplamento une o eixo do motor ao eixo da bomba, permitindo a transmissão de torque e absorvendo pequenas vibrações ou desalinhamentos."
        },        
        {
            "enunciado": "De acordo com a NR-13, qual é o documento obrigatório que deve conter o histórico de todas as inspeções de segurança de uma caldeira ou vaso de pressão?",
            "opcoes": ["Prontuário da Caldeira", "Livro de Registro de Segurança", "Certificado de Garantia", "Manual do Fabricante"],
            "correta": "Livro de Registro de Segurança",
            "explicacao": "O Livro de Registro de Segurança é onde o PH (Profissional Habilitado) anota todas as ocorrências e inspeções, sendo vital para a rastreabilidade da segurança."
        },
        {
            "enunciado": "A NR-20 classifica as instalações que trabalham com inflamáveis e combustíveis em três classes (I, II e III). Uma refinaria de petróleo enquadra-se geralmente em qual classe?",
            "opcoes": ["Classe I", "Classe II", "Classe III", "Classe IV"],
            "correta": "Classe III",
            "explicacao": "As refinarias são instalações de alta complexidade e grande volume de inflamáveis, sendo classificadas como Classe III pela NR-20."
        },
        {
            "enunciado": "O que deve ser feito imediatamente se for detectado que uma caldeira está a operar sem os seus dispositivos de segurança (como a válvula de segurança)?",
            "opcoes": ["Continuar a operação com cuidado", "Solicitar manutenção para a próxima semana", "Interromper a operação imediatamente (Parada de Emergência)", "Aumentar a pressão para testar"],
            "correta": "Interromper a operação imediatamente (Parada de Emergência)",
            "explicacao": "Operar sem dispositivos de segurança é considerado um Risco Grave e Iminente (RGI), exigindo a paragem imediata do equipamento."
        },
        {
            "enunciado": "Segundo a NR-20, o Prontuário da Instalação deve conter o 'Plano de Resposta a Emergências'. Qual o objetivo deste plano?",
            "opcoes": ["Controlar o stock de óleo", "Definir ações para minimizar impactos de acidentes e proteger os trabalhadores", "Calcular o lucro da empresa", "Organizar as férias dos funcionários"],
            "correta": "Definir ações para minimizar impactos de acidentes e proteger os trabalhadores",
            "explicacao": "O Plano de Resposta a Emergências detalha como agir em caso de fugas, incêndios ou explosões para salvar vidas e o ambiente."
        },
        {
            "enunciado": "Na NR-13, os vasos de pressão são classificados em categorias. Quais as principais variáveis usadas para definir estas categorias?",
            "opcoes": ["Cor e Peso", "Pressão e Temperatura", "Classe de fluido e o produto P.V (Pressão x Volume)", "Apenas o tipo de aço utilizado"],
            "correta": "Classe de fluido e o produto P.V (Pressão x Volume)",
            "explicacao": "A categoria do vaso (de 1 a 5) depende do quão perigoso é o fluido e da energia armazenada (pressão multiplicada pelo volume)."
        },
        {
            "enunciado": "O Exame de Estanqueidade em tubulações que transportam inflamáveis deve ser realizado:",
            "opcoes": ["Apenas quando há uma fuga visível", "Periodicamente, conforme o plano de inspeção da instalação", "Uma vez a cada 20 anos", "Nunca, tubulações não precisam de exame"],
            "correta": "Periodicamente, conforme o plano de inspeção da instalação",
            "explicacao": "A estanqueidade garante que não existem micro-fugas que possam causar explosões ou contaminação ambiental."
        },
        {
            "enunciado": "A sigla 'TH' na NR-13 refere-se a um teste fundamental após reparações importantes. O que significa?",
            "opcoes": ["Teste de Humidade", "Teste Hidrostático", "Teste de Hidrogénio", "Temperatura Homogénea"],
            "correta": "Teste Hidrostático",
            "explicacao": "O Teste Hidrostático usa água sob pressão para verificar a resistência estrutural e a ausência de fugas em equipamentos sob pressão."
        },
        {
            "enunciado": "Qual o equipamento de proteção coletiva (EPC) mais comum em áreas de transferência de inflamáveis para evitar a ignição por eletricidade estática?",
            "opcoes": ["Extintor de pó", "Ligação à terra (Aterramento)", "Sirene de alarme", "Cones de sinalização"],
            "correta": "Ligação à terra (Aterramento)",
            "explicacao": "O aterramento drena a eletricidade estática acumulada, impedindo que faíscas iniciem um incêndio durante a carga ou descarga de inflamáveis."
        },
        {
            "enunciado": "A inspeção de segurança inicial de um vaso de pressão deve ser feita:",
            "opcoes": ["Após 1 ano de uso", "Somente se o vaso apresentar defeito", "Antes do vaso ser colocado em operação", "Quando o PH tiver tempo livre"],
            "correta": "Antes do vaso ser colocado em operação",
            "explicacao": "Nenhum vaso de pressão pode começar a trabalhar sem a inspeção inicial que garanta que foi instalado corretamente e está seguro."
        },
        {
            "enunciado": "Em caso de 'Risco Grave e Iminente' detectado durante uma inspeção, o PH (Profissional Habilitado) tem o dever de:",
            "opcoes": ["Anotar e esperar o relatório mensal", "Ignorar se a produção estiver alta", "Determinar a paragem do equipamento e comunicar a gerência", "Tentar consertar sozinho com o equipamento ligado"],
            "correta": "Determinar a paragem do equipamento e comunicar a gerência",
            "explicacao": "A segurança das pessoas vem sempre primeiro; o PH deve paralisar qualquer operação que coloque vidas em risco direto."
        },        {
            "enunciado": "Na instrumentação industrial, o que significa a sigla 'PT' gravada num fluxograma de processo?",
            "opcoes": ["Painel Totalizador", "Transmissor de Pressão (Pressure Transmitter)", "Ponto de Temperatura", "Purga de Tubagem"],
            "correta": "Transmissor de Pressão (Pressure Transmitter)",
            "explicacao": "A sigla PT indica um instrumento que mede a pressão num ponto e envia o sinal para uma sala de controlo ou indicador."
        },
        {
            "enunciado": "Qual é a função de uma 'Válvula de Controlo' num sistema de malha fechada?",
            "opcoes": ["Apenas abrir ou fechar totalmente o fluxo", "Atuar como o elemento final de controlo para ajustar a vazão conforme o sinal do controlador", "Medir a temperatura do fluido", "Proteger o sistema contra explosões"],
            "correta": "Atuar como o elemento final de controlo para ajustar a vazão conforme o sinal do controlador",
            "explicacao": "A válvula de controlo modula a abertura (ex: 30%, 50%) para manter uma variável como nível ou pressão no valor desejado (setpoint)."
        },
        {
            "enunciado": "O que acontece numa válvula de controlo do tipo 'Falha Aberta' (FO - Fail Open) se houver perda do suprimento de ar comprimido?",
            "opcoes": ["A válvula trava na última posição", "A válvula fecha-se totalmente por segurança", "A válvula abre-se totalmente por ação de uma mola", "A válvula explode"],
            "correta": "A válvula abre-se totalmente por ação de uma mola",
            "explicacao": "Válvulas FO são projetadas para que, em caso de falha de energia ou ar, a mola force a abertura total (comum em sistemas de resfriamento)."
        },
        {
            "enunciado": "O instrumento utilizado para medir a diferença de pressão entre dois pontos, muito comum na medição de nível e vazão, é o:",
            "opcoes": ["Termómetro", "Transmissor de Pressão Diferencial (DPT)", "Voltímetro", "Densímetro"],
            "correta": "Transmissor de Pressão Diferencial (DPT)",
            "explicacao": "O DPT mede a diferença entre dois pontos; na vazão, mede a queda de pressão numa placa de orifício para calcular o fluxo."
        },
        {
            "enunciado": "Numa malha de controlo, o que representa o 'Setpoint' (SP)?",
            "opcoes": ["O valor real que o sensor está a ler agora", "O valor desejado que o operador define para uma variável (ex: manter a 50°C)", "O erro entre a leitura e a realidade", "A velocidade de rotação da bomba"],
            "correta": "O valor desejado que o operador define para uma variável (ex: manter a 50°C)",
            "explicacao": "O Setpoint é o alvo. O controlador trabalha para que a Variável de Processo (PV) fique igual ao Setpoint (SP)."
        },
        {
            "enunciado": "A sigla 'TIC' num diagrama de instrumentação refere-se a um:",
            "opcoes": ["Transmissor Indicador de Corrente", "Controlador Indicador de Temperatura", "Tubo de Inspeção de Caldeira", "Teste de Interrupção de Circuito"],
            "correta": "Controlador Indicador de Temperatura",
            "explicacao": "O TIC (Temperature Indicator Controller) lê a temperatura e decide se deve abrir ou fechar uma válvula para controlá-la."
        },
        {
            "enunciado": "Qual destes sensores é o mais indicado para medir temperaturas elevadas em fornos de refinaria?",
            "opcoes": ["Termómetro de mercúrio", "Termopar", "Bóia de nível", "Manómetro"],
            "correta": "Termopar",
            "explicacao": "Os termopares são sensores robustos feitos de dois metais diferentes que geram uma milivoltagem proporcional ao calor, ideais para altas temperaturas."
        },
        {
            "enunciado": "O 'PLC' (ou CLP em português) é um equipamento fundamental na automação. O que significa a sigla?",
            "opcoes": ["Controlador Lógico Programável", "Circuito de Ligação Permanente", "Compressor de Leve Carga", "Painel de Leitura Central"],
            "correta": "Controlador Lógico Programável",
            "explicacao": "O PLC é o 'cérebro' eletrónico que executa a lógica de controlo de máquinas e processos industriais."
        },
        {
            "enunciado": "O que é uma 'Placa de Orifício'?",
            "opcoes": ["Um dispositivo de segurança contra incêndios", "Um elemento primário para medição de vazão por diferencial de pressão", "Uma peça para tapar buracos em tanques", "Um tipo de filtro de óleo"],
            "correta": "Um elemento primário para medição de vazão por diferencial de pressão",
            "explicacao": "É um disco com um furo no meio colocado na tubagem. A restrição gera uma diferença de pressão que permite calcular a vazão."
        },
        {
            "enunciado": "O sinal de transmissão padrão analógico mais utilizado na instrumentação industrial é:",
            "opcoes": ["0 a 100 Volts", "4 a 20 mA (miliamperes)", "10 a 50 Amperes", "0 a 5 Volts"],
            "correta": "4 a 20 mA (miliamperes)",
            "explicacao": "O padrão 4-20mA é o mais usado porque permite detetar cabos rompidos (se o sinal for 0mA, há erro) e é resistente a ruídos elétricos."
        },        
        {
            "enunciado": "O petróleo é composto predominantemente por quais elementos químicos?",
            "opcoes": ["Oxigênio e Nitrogênio", "Carbono e Hidrogênio", "Enxofre e Ferro", "Hélio e Argônio"],
            "correta": "Carbono e Hidrogênio",
            "explicacao": "O petróleo é uma mistura complexa de hidrocarbonetos, moléculas formadas essencialmente por átomos de carbono e hidrogênio."
        },
        {
            "enunciado": "Na química orgânica, como são classificados os hidrocarbonetos que possuem apenas ligações simples entre os átomos de carbono?",
            "opcoes": ["Alcenos", "Alcinos", "Alcanos", "Aromáticos"],
            "correta": "Alcanos",
            "explicacao": "Alcanos são hidrocarbonetos saturados (apenas ligações simples), como o metano, etano e propano."
        },
        {
            "enunciado": "O índice que mede a resistência da gasolina à detonação prematura (batida de pino) no motor é chamado de:",
            "opcoes": ["Ponto de Fulgor", "Viscosidade", "Octanagem", "Número de Cetano"],
            "correta": "Octanagem",
            "explicacao": "Quanto maior a octanagem, maior a capacidade da gasolina de ser comprimida sem explodir antes da centelha da vela."
        },
        {
            "enunciado": "Em uma escala de pH, uma solução com valor 2 é considerada:",
            "opcoes": ["Fortemente Básica", "Neutra", "Fortemente Ácida", "Levemente Alcalina"],
            "correta": "Fortemente Ácida",
            "explicacao": "A escala de pH vai de 0 a 14. Valores abaixo de 7 são ácidos (quanto menor, mais ácido) e acima de 7 são básicos."
        },
        {
            "enunciado": "Qual é a principal diferença entre um fenômeno físico e um fenômeno químico?",
            "opcoes": ["O físico muda a cor, o químico não", "O físico não altera a natureza da matéria; o químico transforma substâncias em novas substâncias", "O químico é sempre mais rápido que o físico", "Não existe diferença prática"],
            "correta": "O físico não altera a natureza da matéria; o químico transforma substâncias em novas substâncias",
            "explicacao": "A destilação é um fenômeno físico (mudança de estado). A combustão é um fenômeno químico (transformação de combustível em CO2 e água)."
        },
        {
            "enunciado": "O processo de separação de misturas que utiliza a diferença de densidade para separar água e óleo em um decantador é a:",
            "opcoes": ["Filtração", "Decantação", "Sublimação", "Cristalização"],
            "correta": "Decantação",
            "explicacao": "Na decantação, o líquido mais denso (água) deposita-se no fundo, enquanto o menos denso (óleo) flutua."
        },
        {
            "enunciado": "O que representa a 'Massa Molar' de uma substância?",
            "opcoes": ["O volume ocupado por um gás", "A massa em gramas presente em um mol de moléculas daquela substância", "A temperatura de ebulição", "A pressão exercida no recipiente"],
            "correta": "A massa em gramas presente em um mol de moléculas daquela substância",
            "explicacao": "A massa molar (g/mol) é fundamental para cálculos estequiométricos em reações químicas industriais."
        },
        {
            "enunciado": "Qual hidrocarboneto aromático é um dos solventes mais comuns e base para muitos produtos petroquímicos, mas exige rigoroso controle por ser tóxico?",
            "opcoes": ["Metano", "Benzeno", "Etanol", "Acetileno"],
            "correta": "Benzeno",
            "explicacao": "O benzeno é um anel aromático fundamental na petroquímica, mas é carcinogênico e possui limites rígidos de exposição na NR-15."
        },
        {
            "enunciado": "Em uma reação de combustão completa de um hidrocarboneto, os produtos finais são sempre:",
            "opcoes": ["Monóxido de Carbono e Fuligem", "Dióxido de Carbono (CO2) e Água (H2O)", "Apenas Hidrogênio líquido", "Enxofre e Nitrogênio"],
            "correta": "Dióxido de Carbono (CO2) e Água (H2O)",
            "explicacao": "A combustão completa consome todo o combustível na presença de oxigênio suficiente, gerando CO2 e vapor de água."
        },
        {
            "enunciado": "O que caracteriza uma reação química Exotérmica?",
            "opcoes": ["A absorção de calor do ambiente", "A liberação de calor para o ambiente", "A mudança de cor para o azul", "A formação de gelo"],
            "correta": "A liberação de calor para o ambiente",
            "explicacao": "Reações exotérmicas, como a queima de combustíveis em fornos, liberam energia térmica para o meio externo."
        },        
        {
            "enunciado": "Qual é a principal função de um lubrificante em máquinas rotativas como bombas e compressores?",
            "opcoes": ["Aumentar o ruído", "Reduzir o atrito e o desgaste entre as superfícies em movimento", "Aumentar a temperatura de operação", "Solidificar as peças"],
            "correta": "Reduzir o atrito e o desgaste entre as superfícies em movimento",
            "explicacao": "O lubrificante cria uma película que separa as superfícies metálicas, diminuindo o atrito, o calor e o desgaste."
        },
        {
            "enunciado": "O componente mecânico destinado a suportar um eixo e permitir sua rotação com o mínimo de atrito é o:",
            "opcoes": ["Mancal", "Parafuso", "Chaveta", "Flange"],
            "correta": "Mancal",
            "explicacao": "Os mancais (de deslizamento ou de rolamento) são os suportes que guiam e apoiam os eixos rotativos."
        },
        {
            "enunciado": "A 'Viscosidade' de um óleo lubrificante é definida como:",
            "opcoes": ["A cor do óleo", "A resistência do fluido ao escoamento", "O ponto em que o óleo congela", "A quantidade de água no óleo"],
            "correta": "A resistência do fluido ao escoamento",
            "explicacao": "Óleos mais grossos têm alta viscosidade; óleos mais finos têm baixa viscosidade. É a propriedade mais importante de um lubrificante."
        },
        {
            "enunciado": "Qual ferramenta é utilizada para medir com precisão de centésimos de milímetro o diâmetro de um eixo ou a espessura de uma peça?",
            "opcoes": ["Trena", "Micrômetro", "Martelo", "Chave de fenda"],
            "correta": "Micrômetro",
            "explicacao": "O micrômetro é um instrumento de medição linear de alta precisão, essencial para ajustes mecânicos finos."
        },
        {
            "enunciado": "O desalinhamento entre o eixo do motor e o eixo da bomba pode causar:",
            "opcoes": ["Aumento da eficiência", "Vibração excessiva e desgaste prematuro de rolamentos e selos", "Resfriamento do motor", "Economia de energia"],
            "correta": "Vibração excessiva e desgaste prematuro de rolamentos e selos",
            "explicacao": "Eixos desalinhados forçam os componentes, gerando vibração que destrói vedações e rolamentos rapidamente."
        },
        {
            "enunciado": "A Manutenção Preditiva baseia-se em:",
            "opcoes": ["Consertar apenas quando quebra", "Trocar peças por tempo de uso", "Monitorar o estado do equipamento (ex: análise de vibração) para intervir apenas quando necessário", "Pintar a máquina toda semana"],
            "correta": "Monitorar o estado do equipamento (ex: análise de vibração) para intervir apenas quando necessário",
            "explicacao": "A preditiva 'prevê' a falha através de dados técnicos, como termografia."
        },        
        {
            "enunciado": "De acordo com a Lei de Ohm, qual é a relação entre Tensão (V), Corrente (I) e Resistência (R)?",
            "opcoes": ["V = R / I", "V = I * R", "I = V * R", "R = V * I"],
            "correta": "V = I * R",
            "explicacao": "A tensão é igual ao produto da corrente pela resistência. É a fórmula fundamental da eletricidade."
        },
        {
            "enunciado": "Qual é a unidade de medida da Potência Elétrica no Sistema Internacional?",
            "opcoes": ["Volt (V)", "Ampere (A)", "Watt (W)", "Ohm (Ω)"],
            "correta": "Watt (W)",
            "explicacao": "O Watt mede a taxa de conversão de energia elétrica em trabalho ou calor por unidade de tempo."
        },
        {
            "enunciado": "O motor elétrico mais utilizado na indústria petroquímica para acionar bombas e compressores, devido à sua robustez e baixo custo, é o:",
            "opcoes": ["Motor de Corrente Contínua", "Motor de Indução Trifásico (Gaiola de Esquilo)", "Motor a Vapor", "Motor Monofásico de Íman Permanente"],
            "correta": "Motor de Indução Trifásico (Gaiola de Esquilo)",
            "explicacao": "Este motor é extremamente robusto, não possui escovas (o que reduz faíscas em áreas inflamáveis) e exige pouca manutenção."
        },
        {
            "enunciado": "A função de um transformador numa subestação industrial é:",
            "opcoes": ["Transformar Corrente Alternada em Contínua", "Alterar os níveis de tensão (aumentar ou diminuir) mantendo a frequência", "Armazenar energia para emergências", "Medir o consumo de reativos"],
            "correta": "Alterar os níveis de tensão (aumentar ou diminuir) mantendo a frequência",
            "explicacao": "Os transformadores permitem baixar a alta tensão da rede para níveis seguros de utilização nos motores das unidades (ex: 440V ou 380V)."
        },
        {
            "enunciado": "O dispositivo de proteção que interrompe o circuito automaticamente quando deteta uma sobrecarga ou curto-circuito é o:",
            "opcoes": ["Resistor", "Disjuntor", "Capacitor", "Voltímetro"],
            "correta": "Disjuntor",
            "explicacao": "O disjuntor protege os cabos e equipamentos contra danos causados por correntes excessivas."
        },
        {
            "enunciado": "Em eletricidade, o que caracteriza um 'Curto-circuito'?",
            "opcoes": ["Um circuito com resistência infinita", "A união direta de dois pontos de um circuito com resistência quase nula, gerando uma corrente altíssima", "O desligamento propositado de uma lâmpada", "A falta de tensão numa tomada"],
            "correta": "A união direta de dois pontos de um circuito com resistência quase nula, gerando uma corrente altíssima",
            "explicacao": "No curto-circuito, a corrente sobe bruscamente, podendo causar incêndios e danos graves se a proteção (disjuntor) não atuar."
        },
        {
            "enunciado": "O instrumento utilizado para medir a tensão elétrica (voltagem) entre dois pontos de um painel é o:",
            "opcoes": ["Amperímetro", "Voltímetro", "Ohmímetro", "Wattímetro"],
            "correta": "Voltímetro",
            "explicacao": "O voltímetro deve ser ligado em paralelo com o componente ou pontos que se deseja medir a diferença de potencial."
        },
        {
            "enunciado": "Qual é a principal diferença entre Corrente Alternada (CA) e Corrente Contínua (CC)?",
            "opcoes": ["A CA muda de sentido periodicamente, enquanto a CC flui num único sentido", "A CC é usada em motores grandes e a CA em pilhas", "A CA não dá choque e a CC sim", "Não há diferença, são apenas nomes diferentes"],
            "correta": "A CA muda de sentido periodicamente, enquanto a CC flui num único sentido",
            "explicacao": "A CA é a corrente das redes elétricas e motores industriais; a CC é comum em baterias e circuitos eletrónicos."
        },
        {
            "enunciado": "O 'Multímetro' é uma ferramenta versátil porque permite medir:",
            "opcoes": ["Apenas a temperatura", "Várias grandezas como Tensão, Corrente e Resistência num único aparelho", "Apenas o nível de ruído", "A pressão de pneus"],
            "correta": "Várias grandezas como Tensão, Corrente e Resist",
        },    
        
            
        
        
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
        if 'questoes_db' in st.session_state:
            del st.session_state.questoes_db
        st.session_state.indice = 0
        st.session_state.mostrar_explica = False
        st.rerun()
    
