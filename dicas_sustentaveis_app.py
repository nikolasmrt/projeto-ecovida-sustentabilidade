import streamlit as st

st.set_page_config(
    page_title="Dicas Sustentáveis • Eco-vida",
    page_icon="♻️", 
    layout="wide" 
)


with st.sidebar:
    st.image("https://placehold.co/100x100/2D6A4F/ffffff?text=ECOVIDA", use_column_width=True) 
    st.header("🌿 Eco-vida: Seu Guia Sustentável")
    st.write(
        "Bem-vindo(a) ao seu portal de hábitos conscientes! "
        "Aqui, você encontra inspiração e dicas práticas para transformar seu dia a dia em uma jornada mais verde. "
        "Pequenas ações geram grandes impactos! 🌍"
    )
    st.markdown("---")
    st.subheader("📚 Seções Rápidas")
    st.markdown("- [Por que Sustentabilidade?](#por-que-a-sustentabilidade-importa)")
    st.markdown("- [Dicas Essenciais](#dicas-sustentaveis-do-eco-vida)")
    st.markdown("---")
    st.info("💡 **Dica Profissional:** Integre o monitoramento de hábitos sustentáveis em sua rotina com aplicativos como o Eco-vida para visualizar seu impacto!")

# Título Principal 
st.title("✨ Dicas Sustentáveis do Eco-vida: Um Futuro Mais Verde!")
st.markdown("---")
st.markdown(
    "Bem-vindo(a) ao seu guia interativo de hábitos conscientes. "
    "Explore como pequenas mudanças podem gerar um **grande impacto** para um planeta mais saudável e um estilo de vida mais **futurista e responsável**."
)
st.markdown("---")

# Seção "Por que a Sustentabilidade Importa?"
st.header("🤔 Por que a Sustentabilidade Importa?")
st.write(
    "A sustentabilidade não é apenas uma palavra da moda, é um pilar fundamental para o futuro do nosso planeta e das próximas gerações. "
    "Adotar práticas sustentáveis é investir em um mundo com recursos, saúde e qualidade de vida para todos. "
    "É sobre equilibrar as necessidades atuais sem comprometer a capacidade das futuras gerações de atender às suas próprias necessidades."
)

st.subheader("Benefícios de um Estilo de Vida Sustentável:")
col1_why, col2_why, col3_why = st.columns(3)
with col1_why:
    st.markdown("#### 🌎 Proteção Ambiental")
    st.markdown("Reduz a poluição, conserva recursos naturais e protege a biodiversidade.")
with col2_why:
    st.markdown("#### 💰 Economia Inteligente")
    st.markdown("Diminui custos com energia, água e resíduos, promovendo eficiência e novas tecnologias.")
with col3_why:
    st.markdown("#### 💖 Saúde e Bem-Estar")
    st.markdown("Promove ambientes mais limpos e saudáveis, impactando diretamente a qualidade de vida.")

st.markdown("---")

# Dicas Sustentáveis Essenciais (Agora em Colunas com Expanders)
st.header("🚀 Dicas Sustentáveis do Eco-vida")
st.markdown(
    "Explore nossas categorias de dicas e descubra como você pode contribuir para um futuro mais sustentável hoje!"
)

tabs = st.tabs(["💧 Água", "⚡ Energia", "🚗 Transporte", "🗑️ Resíduos"])

with tabs[0]:
    st.subheader("💧 Economizando Água: Cada Gota Conta!")
    col_water1, col_water2 = st.columns(2)
    with col_water1:
        st.markdown("**Banhos Conscientes:**")
        with st.expander("Ver detalhes"):
            st.write("- Tome banhos mais curtos (menos de 5 minutos).")
            st.write("- Feche a torneira enquanto se ensaboa.")
            st.write("- Use um balde para coletar a água fria inicial do chuveiro para reuso.")

        st.markdown("**Torneiras e Vazamentos:**")
        with st.expander("Ver detalhes"):
            st.write("- Feche a torneira enquanto escova os dentes ou lava a louça.")
            st.write("- Conserte vazamentos imediatamente: um pequeno gotejamento pode desperdiçar milhares de litros por ano.")

    with col_water2:
        st.markdown("**Reaproveitamento e Eficiência:**")
        with st.expander("Ver detalhes"):
            st.write("- Reaproveite a água da chuva para regar plantas ou lavar áreas externas.")
            st.write("- Lave roupas com carga completa na máquina e use o ciclo econômico, se disponível.")
            st.write("- Prefira sistemas de descarga com caixa acoplada e duplo fluxo.")

        st.markdown("**Jardinagem Inteligente:**")
        with st.expander("Ver detalhes"):
            st.write("- Regue as plantas no início da manhã ou final da tarde para reduzir a evaporação.")
            st.write("- Utilize sistemas de irrigação por gotejamento, que são mais eficientes.")

with tabs[1]:
    st.subheader("⚡ Economizando Energia: Iluminando o Futuro!")
    col_energy1, col_energy2 = st.columns(2)
    with col_energy1:
        st.markdown("**Eletrodomésticos:**")
        with st.expander("Ver detalhes"):
            st.write("- Desligue aparelhos da tomada quando não estiverem em uso (evite o 'stand-by').")
            st.write("- Limpe a parte traseira da geladeira e verifique a vedação da porta para maior eficiência.")
            st.write("- Use a máquina de lavar e secar com carga total e prefira secar roupas ao sol.")

        st.markdown("**Iluminação:**")
        with st.expander("Ver detalhes"):
            st.write("- Prefira lâmpadas de LED, que consomem até 80% menos energia e duram mais.")
            st.write("- Aproveite a luz natural sempre que possível, abrindo cortinas e persianas.")

    with col_energy2:
        st.markdown("**Climatização:**")
        with st.expander("Ver detalhes"):
            st.write("- Use ventilador em vez de ar-condicionado quando possível. Se usar ar-condicionado, mantenha-o em temperaturas amenas (23°C).")
            st.write("- Mantenha filtros de ar-condicionado limpos para otimizar o funcionamento.")

        st.markdown("**Consciência e Programação:**")
        with st.expander("Ver detalhes"):
            st.write("- Programe aparelhos para o modo de economia de energia ou use temporizadores.")
            st.write("- Considere a instalação de painéis solares para geração própria de energia.")

with tabs[2]:
    st.subheader("🚗 Mobilidade Sustentável: Movendo-se com Responsabilidade!")
    col_transport1, col_transport2 = st.columns(2)
    with col_transport1:
        st.markdown("**Alternativas Inteligentes:**")
        with st.expander("Ver detalhes"):
            st.write("- Prefira caminhar ou pedalar para distâncias curtas. É saudável e ecológico!")
            st.write("- Use transporte público (ônibus, metrô, trem) sempre que possível.")

        st.markdown("**Compartilhamento e Manutenção:**")
        with st.expander("Ver detalhes"):
            st.write("- Organize caronas com colegas e vizinhos para ir ao trabalho ou escola.")
            st.write("- Faça manutenções regulares no carro para reduzir o consumo de combustível e as emissões.")

    with col_transport2:
        st.markdown("**Tecnologia e Planejamento:**")
        with st.expander("Ver detalhes"):
            st.write("- Se possível, opte por veículos elétricos ou híbridos, que emitem menos poluentes.")
            st.write("- Planeje suas rotas para otimizar viagens e evitar o trânsito.")
            st.write("- Use aplicativos de mobilidade compartilhada (bicicletas, patinetes elétricos).")

        st.markdown("**Viagens Conscientes:**")
        with st.expander("Ver detalhes"):
            st.write("- Para viagens longas, considere trens ou ônibus em vez de aviões, quando viável.")
            st.write("- Ao alugar um carro, opte por modelos mais eficientes em termos de combustível.")

with tabs[3]:
    st.subheader("🗑️ Reduzindo e Reciclando Resíduos: Menos Lixo, Mais Vida!")
    col_waste1, col_waste2 = st.columns(2)
    with col_waste1:
        st.markdown("**Reduzir é o Primeiro Passo:**")
        with st.expander("Ver detalhes"):
            st.write("- Evite produtos com excesso de embalagem ou embalagens desnecessárias.")
            st.write("- Prefira comprar a granel sempre que possível para reduzir o desperdício de embalagens.")
            st.write("- Leve sacolas reutilizáveis ao fazer compras e recuse sacolas plásticas descartáveis.")

        st.markdown("**Reutilizar para Inovar:**")
        with st.expander("Ver detalhes"):
            st.write("- Reutilize potes, garrafas e outros materiais sempre que possível em casa.")
            st.write("- Doe roupas, livros e eletrônicos em bom estado em vez de jogá-los fora.")

    with col_waste2:
        st.markdown("**Reciclar Corretamente:**")
        with st.expander("Ver detalhes"):
            st.write("- Separe lixo reciclável (plástico, papel, vidro, metal) do orgânico.")
            st.write("- Participe de iniciativas locais de coleta seletiva e informe-se sobre os pontos de coleta.")
            st.write("- Lave embalagens antes de reciclar para evitar contaminação.")

        st.markdown("**Compostagem:**")
        with st.expander("Ver detalhes"):
            st.write("- Considere a compostagem de resíduos orgânicos (restos de alimentos, folhas) para criar adubo natural.")
            st.write("- A compostagem reduz a quantidade de lixo enviado para aterros e enriquece o solo.")

# Rodapé
st.markdown("---")
st.markdown("🌱 _Continue registrando seus hábitos no sistema Eco-vida para acompanhar seu impacto sustentável e ver sua pontuação crescer!_")
st.markdown("<p style='text-align: center; color: gray;'>© 2025 Eco-vida Sustentabilidade. Todos os direitos reservados.</p>", unsafe_allow_html=True)

