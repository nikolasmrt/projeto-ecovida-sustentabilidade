# ♻ Eco-vida Sustentabilidade

Eco-vida Sustentabilidade é um sistema desktop interativo desenvolvido com Python e **PySide6**, com o objetivo de incentivar hábitos sustentáveis por meio de um registro diário de ações ecológicas.
A aplicação permite acompanhar seus impactos positivos no meio ambiente e receber recomendações personalizadas de melhorias.

---

## 📦 Funcionalidades

- ✅ Registro de hábitos sustentáveis (nome, categoria, unidade e quantidade)
- 📊 Geração de gráficos de hábitos por categoria **(agora com gráficos interativos e modernos via QtCharts)**
- 💡 Recomendações automáticas baseadas nos registros
- 🏆 Cálculo de pontuação sustentável do usuário
- 📄 Exportação de relatório PDF com gráficos e histórico de hábitos
- 🌐 Acesso integrado a dicas sustentáveis via Streamlit

---

## 🧰 Tecnologias Utilizadas

- `Python 3.13.3` (Compatível com `PySide6` a partir da versão 6.8)
- `PySide6` – Framework de UI para interfaces de desktop profissionais.
- `PySide6-Charts` – Módulo para gráficos interativos.
- `mysql-connector-python` – Para conexão com o banco de dados MySQL.
- `bcrypt` – Para criptografia de senhas.
- `fpdf` – Para geração de relatórios PDF.
- `matplotlib` – Ainda utilizado para geração de gráficos dentro do PDF (função `exportar_para_pdf` em `connection.py`).
- `Streamlit` – Interface web para dicas sustentáveis.

---

## 🔧 **Instalação e Uso**

### Pré-requisitos

1.  **Python 3.13.3** (versões como 3.11 ou 3.12 também são altamente recomendadas para compatibilidade mais ampla de pacotes binários como `PySide6-Charts`).
2.  **Acesso ao MySQL Server** com um banco de dados `ecovida` configurado e um usuário `root` com senha `1731`.

### Instalação das Dependências

Abra o Prompt de Comando (CMD) ou PowerShell **como administrador** (clique com o botão direito do mouse no ícone e selecione "Executar como administrador"). Navegue até a pasta do projeto:

```bash
cd "N:\Meus repositórios\projeto-ecovida-sustentabilidade"

pip install PySide6 PySide6-Charts mysql-connector-python bcrypt fpdf matplotlib