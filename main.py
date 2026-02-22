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
        {"enunciado": "Para evitar a cavitação em bombas centrífugas, o operador deve garantir que:", "opcoes": ["A) NPSH disponível < NPSH requerido", "B) NPSH disponível > NPSH requerido", "C) Pressão de sucção seja zero", "D) Fluido esteja fervendo", "E) Válvula de sucção fechada"], "correta": "B) NPSH disponível > NPSH requerido", "explicacao": "O NPSH disponível deve ser sempre maior que o requerido para evitar vaporização do fluido."},
        {"enunciado": "Qual norma regulamentadora trata de Segurança em Instalações e Serviços em Eletricidade?", "opcoes": ["A) NR-10", "B) NR-12", "C) NR-13", "D) NR-20", "E) NR-35"], "correta": "A) NR-10", "explicacao": "A NR-10 é a norma técnica para riscos elétricos."},
        {"enunciado": "O equipamento que realiza a troca térmica entre dois fluidos sem contato direto é:", "opcoes": ["A) Torre de resfriamento", "B) Vaso de pressão", "C) Permutador de calor", "D) Caldeira", "E) Forno"], "correta": "C) Permutador de calor", "explicacao": "Permutadores transferem calor através de paredes metálicas (tubos)."},
        {"enunciado": "A principal função de um 'Demister' (Eliminador de Névoa) é:", "opcoes": ["A) Aquecer o gás", "B) Remover gotículas de líquido do fluxo de gás", "C) Filtrar areia", "D) Medir a pressão", "E) Condensar o vapor"], "correta": "B) Remover gotículas de líquido do fluxo de gás", "explicacao": "O demister retém o líquido arrastado pelo gás por impacto em uma malha."},
        {"enunciado": "Sobre o GLP (Gás Liquefeito de Petróleo), é correto afirmar que:", "opcoes": ["A) É mais leve que o ar", "B) É composto principalmente por metano", "C) É mais pesado que o ar e tende a se acumular em locais baixos", "D) Não é inflamável", "E) Não possui odor natural ou artificial"], "correta": "C) É mais pesado que o ar e tende a se acumular em locais baixos", "explicacao": "O GLP é mais denso que o ar, o que exige ventilação ao nível do solo."},
        {"enunciado": "O instrumento utilizado para medir a vazão baseado na diferença de pressão em um estreitamento é:", "opcoes": ["A) Termopar", "B) Placa de orifício", "C) Manômetro de Bourdon", "D) Rotâmetro", "E) Radar"], "correta": "B) Placa de orifício", "explicacao": "A placa de orifício gera um diferencial de pressão proporcional à vazão."},
        {"enunciado": "A válvula que permite o fluxo em apenas um sentido é a:", "opcoes": ["A) Globo", "B) Gaveta", "C) Retenção", "D) Borboleta", "E) Esfera"], "correta": "C) Retenção", "explicacao": "Válvulas de retenção impedem o retorno do fluido."},
        {"enunciado": "Qual o principal risco do H2S (Gás Sulfídrico)?", "opcoes": ["A) Apenas inflamabilidade", "B) Toxicidade aguda e corrosividade", "C) É um gás inerte", "D) Causa apenas tontura leve", "E) É benéfico à saúde"], "correta": "B) Toxicidade aguda e corrosividade", "explicacao": "O H2S é extremamente tóxico e 'mata' o olfato em altas concentrações."},
        {"enunciado": "Em segurança do trabalho, a sigla EPC significa:", "opcoes": ["A) Equipamento de Proteção Individual", "B) Equipamento de Proteção Coletiva", "C) Exame de Pressão Clínica", "D) Empresa de Petróleo e Combustível", "E) Elemento de Proteção de Carga"], "correta": "B) Equipamento de Proteção Coletiva", "explicacao": "EPCs protegem todos no ambiente, como corrimãos e exaustores."},
        {"enunciado": "O ponto de fulgor é a temperatura mínima na qual um combustível:", "opcoes": ["A) Queima continuamente", "B) Libera vapores que formam mistura inflamável momentânea", "C) Entra em ignição espontânea", "D) Se torna sólido", "E) Evapora totalmente"], "correta": "B) Libera vapores que formam mistura inflamável momentânea", "explicacao": "No ponto de fulgor, há um 'flash' momentâneo."},
        {"enunciado": "Na NR-13, a sigla PMTA significa:", "opcoes": ["A) Pressão Média de Trabalho Autorizada", "B) Pressão Máxima de Trabalho Admissível", "C) Potência Máxima", "D) Ponto de Manutenção", "E) Pressão Mínima"], "correta": "B) Pressão Máxima de Trabalho Admissível", "explicacao": "A PMTA é o limite de pressão de segurança para vasos e caldeiras."},
        {"enunciado": "O equipamento que remove calor usando ar ambiente é o:", "opcoes": ["A) Refervedor", "B) Permutador casco e tubos", "C) Air Cooler", "D) Caldeira", "E) Forno"], "correta": "C) Air Cooler", "explicacao": "Air coolers usam ventiladores para trocar calor com a atmosfera."},
        {"enunciado": "A cor de identificação de tubulações de incêndio (NR-26) é:", "opcoes": ["A) Amarelo", "B) Verde", "C) Azul", "D) Vermelho", "E) Branco"], "correta": "D) Vermelho", "explicacao": "Vermelho é usado para equipamentos de proteção e combate a incêndio."},
        {"enunciado": "Qual o objetivo do sistema de 'Flare' (Tocha)?", "opcoes": ["A) Iluminação", "B) Queimar gases residuais com segurança", "C) Gerar vapor", "D) Aquecer óleo", "E) Filtrar o ar"], "correta": "B) Queimar gases residuais com segurança", "explicacao": "O flare alivia pressão queimando gases que não podem ser liberados puro."},
        {"enunciado": "Segundo a NR-35, trabalho em altura é acima de:", "opcoes": ["A) 1,00 m", "B) 1,50 m", "C) 2,00 m", "D) 3,00 m", "E) 5,00 m"], "correta": "C) 2,00 m", "explicacao": "A norma define trabalho em altura a partir de 2 metros de queda livre."},
        {"enunciado": "O 'Golpe de Aríete' é causado por:", "opcoes": ["A) Baixa temperatura", "B) Fechamento brusco de válvulas", "C) Excesso de gás", "D) Falta de óleo", "E) Corrosão"], "correta": "B) Fechamento brusco de válvulas", "explicacao": "A interrupção súbita do fluxo cria uma onda de choque na tubulação."},
        {"enunciado": "A Árvore de Natal Molhada (ANM) serve para:", "opcoes": ["A) Gerar energia", "B) Controle do fluxo do poço submarino", "C) Bombear lama", "D) Separar gás", "E) Armazenar diesel"], "correta": "B) Controle do fluxo do poço submarino", "explicacao": "A ANM controla a produção e segurança no fundo do mar."},
        {"enunciado": "O 'Quebra-jato' em um vaso serve para:", "opcoes": ["A) Filtrar o óleo", "B) Reduzir turbulência na entrada", "C) Aquecer a água", "D) Medir nível", "E) Coletar amostras"], "correta": "B) Reduzir turbulência na entrada", "explicacao": "Dissipa a energia do fluido para facilitar a separação das fases."},
        {"enunciado": "Classe de incêndio que envolve metais combustíveis (ex: sódio):", "opcoes": ["A) Classe A", "B) Classe B", "C) Classe C", "D) Classe D", "E) Classe K"], "correta": "D) Classe D", "explicacao": "Metais pirofóricos exigem agentes extintores especiais de pó classe D."},
        {"enunciado": "O 'Rotâmetro' mede qual grandeza?", "opcoes": ["A) Pressão", "B) Temperatura", "C) Vazão instantânea", "D) Nível", "E) Densidade"], "correta": "C) Vazão instantânea", "explicacao": "É um medidor de área variável que indica o fluxo visualmente."},
        {"enunciado": "Função do 'Refervedor' (Reboiler) na torre:", "opcoes": ["A) Resfriar topo", "B) Vaporizar o fundo da torre", "C) Limpar diesel", "D) Bombear óleo", "E) Filtrar gás"], "correta": "B) Vaporizar o fundo da torre", "explicacao": "Fornece o calor necessário para manter a destilação."},
        {"enunciado": "Válvula com menor perda de carga quando aberta:", "opcoes": ["A) Globo", "B) Agulha", "C) Esfera ou Gaveta", "D) Borboleta", "E) Diafragma"], "correta": "C) Esfera ou Gaveta", "explicacao": "Oferecem passagem plena ao fluido, minimizando resistência."},
        {"enunciado": "O que é 'NPSH Requerido'?", "opcoes": ["A) Pressão da instalação", "B) Pressão mínima exigida pela bomba", "C) Nível do tanque", "D) Velocidade", "E) Temperatura"], "correta": "B) Pressão mínima exigida pela bomba", "explicacao": "É a pressão que a bomba precisa na sucção para não cavitar."},
        {"enunciado": "Bomba de deslocamento positivo (ex: pistão) caracteriza-se por:", "opcoes": ["A) Não gerar pressão", "B) Vazão constante independente da pressão", "C) Só para água", "D) Igual a centrífuga", "E) Sem válvulas"], "correta": "B) Vazão constante independente da pressão", "explicacao": "Elas deslocam um volume fixo a cada ciclo de movimento."},
        {"enunciado": "A sigla FISPQ (FDS) refere-se a:", "opcoes": ["A) Inspeção de prédios", "B) Segurança de Produtos Químicos", "C) Salários", "D) Solda", "E) Saúde"], "correta": "B) Segurança de Produtos Químicos", "explicacao": "Documento com riscos, manuseio e primeiros socorros químicos."},
        {"enunciado": "O compressor 'Alternativo' assemelha-se a:", "opcoes": ["A) Ventilador", "B) Motor de pistão", "C) Turbina", "D) Moinho", "E) Mangueira"], "correta": "B) Motor de pistão", "explicacao": "Usa o movimento de vai-e-vem do pistão para comprimir o gás."},
        {"enunciado": "Componente que protege contra sólidos na linha:", "opcoes": ["A) Vaso", "B) Filtro ou Strainer", "C) Permutador", "D) PSV", "E) Tanque"], "correta": "B) Filtro ou Strainer", "explicacao": "Retém detritos para proteger bombas e válvulas a jusante."},
        {"enunciado": "NR-33 exige monitorar a atmosfera com:", "opcoes": ["A) Termômetro", "B) Detector de gases multigas", "C) Lanterna", "D) Rádio", "E) Anemômetro"], "correta": "B) Detector de gases multigas", "explicacao": "Obrigatório medir O2, inflamáveis e gases tóxicos antes de entrar."},
        {"enunciado": "A 'Bacia de Contenção' serve para:", "opcoes": ["A) Beber água", "B) Conter vazamentos e evitar poluição", "C) Fundação", "D) Resfriar", "E) Guardar ferramentas"], "correta": "B) Conter vazamentos e evitar poluição", "explicacao": "Retém o volume do tanque em caso de vazamento."},
        {"enunciado": "Separação por solubilidade em solvente é:", "opcoes": ["A) Destilação", "B) Absorção ou Extração", "C) Filtração", "D) Decantação", "E) Centrifugação"], "correta": "B) Absorção ou Extração", "explicacao": "O solvente captura seletivamente um componente da mistura."},
        {"enunciado": "EPI para proteção auditiva:", "opcoes": ["A) Capacete", "B) Protetor auricular", "C) Óculos", "D) Luva", "E) Máscara"], "correta": "B) Protetor auricular", "explicacao": "Essencial em ambientes com ruído acima do limite."},
        {"enunciado": "Função do selo mecânico em bombas:", "opcoes": ["A) Lubrificar", "B) Vedação do fluido para o ambiente", "C) Resfriar", "D) Aumentar vazão", "E) Filtrar"], "correta": "B) Vedação do fluido para o ambiente", "explicacao": "Impede que o fluido escape pelo eixo da bomba."},
        {"enunciado": "Fração retirada na base da torre de destilação:", "opcoes": ["A) Nafta", "B) Querosene", "C) Resíduo atmosférico", "D) GLP", "E) Diesel"], "correta": "C) Resíduo atmosférico", "explicacao": "Os componentes mais pesados ficam no fundo da torre."},
        {"enunciado": "Termopar mede temperatura através de:", "opcoes": ["A) Mercúrio", "B) Diferença de potencial elétrico", "C) Laser", "D) Pressão", "E) Som"], "correta": "B) Diferença de potencial elétrico", "explicacao": "Usa a junta de dois metais (efeito Seebeck)."},
        {"enunciado": "Acumulador hidráulico serve para:", "opcoes": ["A) Resfriar", "B) Armazenar energia (fluido pressurizado)", "C) Filtrar ar", "D) Medir", "E) Aquecer"], "correta": "B) Armazenar energia (fluido pressurizado)", "explicacao": "Garante pressão em caso de falha da bomba principal."},
        {"enunciado": "Quem emite PT para trabalho em altura?", "opcoes": ["A) Trabalhador", "B) Porteiro", "C) Supervisor autorizado", "D) Médico", "E) Sindicato"], "correta": "C) Supervisor autorizado", "explicacao": "Documento assinado por quem avaliou os riscos do local."},
        {"enunciado": "Bomba centrífuga com sucção fechada gera:", "opcoes": ["A) Rendimento", "B) Superaquecimento e danos", "C) Pressão infinita", "D) Economia", "E) Vácuo puro"], "correta": "B) Superaquecimento e danos", "explicacao": "Sem fluxo para resfriar, a bomba pode travar."},
        {"enunciado": "Chicanas (Baffles) no trocador servem para:", "opcoes": ["A) Vedar", "B) Direcionar fluxo e suporte mecânico", "C) Bombear", "D) Filtrar", "E) Aquecer"], "correta": "B) Direcionar fluxo e suporte mecânico", "explicacao": "Melhoram a troca térmica e evitam vibração dos tubos."},
        {"enunciado": "Agente proibido para fogo elétrico energizado:", "opcoes": ["A) CO2", "B) Pó Químico", "C) Água", "D) Halon", "E) Pó ABC"], "correta": "C) Água", "explicacao": "Água conduz eletricidade e causa choque fatal."},
        {"enunciado": "Máquina que aumenta pressão reduzindo volume do gás:", "opcoes": ["A) Soprador", "B) Compressor", "C) Exaustor", "D) Condensador", "E) Válvula"], "correta": "B) Compressor", "explicacao": "Fundamental para movimentar gases em alta pressão."},
        {"enunciado": "Válvula de esfera é do tipo:", "opcoes": ["A) Gaveta", "B) Globo", "C) Quarto de volta", "D) Agulha", "E) Diafragma"], "correta": "C) Quarto de volta", "explicacao": "Gira 90 graus para abrir ou fechar totalmente."},
        {"enunciado": "Função da PSV em vasos de pressão:", "opcoes": ["A) Controle", "B) Proteção contra sobrepressão", "C) Nível", "D) Drenagem", "E) Limpeza"], "correta": "B) Proteção contra sobrepressão", "explicacao": "Abre automaticamente para evitar a explosão do vaso."},
        {"enunciado": "Objetivo da Permissão de Trabalho (PT):", "opcoes": ["A) Férias", "B) Garantia de análise de riscos e segurança", "C) Ponto", "D) Salário", "E) Materiais"], "correta": "B) Garantia de análise de riscos e segurança", "explicacao": "Documento vital para qualquer serviço de risco na área."},
        {"enunciado": "Manômetro no verde indica:", "opcoes": ["A) Vazio", "B) Pressurizado e pronto para uso", "C) Descarte", "D) Tóxico", "E) Água"], "correta": "B) Pressurizado e pronto para uso", "explicacao": "Indica que a pressão interna do extintor está correta."},
        {"enunciado": "Torre de resfriamento esfria a água por:", "opcoes": ["A) Gelo", "B) Evaporação parcial", "C) Nitrogênio", "D) Sombras", "E) Vácuo"], "correta": "B) Evaporação parcial", "explicacao": "A troca térmica ocorre com o ar ambiente através da evaporação."},
        {"enunciado": "Norma para Máquinas e Equipamentos:", "opcoes": ["A) NR-10", "B) NR-12", "C) NR-13", "D) NR-20", "E) NR-35"], "correta": "B) NR-12", "explicacao": "Regula proteções físicas e operação segura de máquinas."},
        {"enunciado": "Manômetro local serve para:", "opcoes": ["A) Mandar sinal", "B) Leitura visual no campo", "C) Ligar alarmes", "D) Filtrar óleo", "E) Esfriar linha"], "correta": "B) Leitura visual no campo", "explicacao": "Indica a pressão apenas para quem está perto do equipamento."},
        {"enunciado": "Craqueamento Catalítico (FCC) serve para:", "opcoes": ["A) Limpar areia", "B) Quebrar moléculas pesadas em leves (Gasolina/GLP)", "C) Congelar diesel", "D) Adicionar água", "E) Pintar tanques"], "correta": "B) Quebrar moléculas pesadas em leves (Gasolina/GLP)", "explicacao": "Transforma frações pesadas em produtos de alto valor comercial."},
        {"enunciado": "O que caracteriza Espaço Confinado (NR-33)?", "opcoes": ["A) Sala ampla", "B) Local sem ventilação e sem ocupação contínua", "C) Pátio aberto", "D) Escritório", "E) Oficina"], "correta": "B) Local sem ventilação e sem ocupação contínua", "explicacao": "Locais com entrada/saída limitada e risco atmosférico."},
        {"enunciado": "Barômetro mede:", "opcoes": ["A) Pressão interna", "B) Pressão atmosférica", "C) Temperatura", "D) Vazão", "E) Vácuo"], "correta": "B) Pressão atmosférica", "explicacao": "Mede a pressão do ar ambiente."}
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
         
