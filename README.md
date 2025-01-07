# <img src="https://raw.githubusercontent.com/dimasbetioli/concrete-ia-app/refs/heads/main/mult.png" width="40" /> IA Aplicada à Previsão da Resistência de Concretos <img src="https://raw.githubusercontent.com/dimasbetioli/concrete-ia-app/refs/heads/main/mult.png" width="40" />

Este projeto utiliza Inteligência Artificial para prever a resistência do concreto aos 28 dias com base em uma variedade de variáveis de entrada, como características do cimento, água, materiais adicionais, e outros fatores que influenciam o processo de concretagem.

## Funcionalidades

O aplicativo permite que o usuário insira dados de forma manual ou faça upload de um arquivo Excel contendo os dados necessários para a previsão. A seguir, as principais funcionalidades:

1. **Inserção Manual de Dados:**
   - O usuário escolhe entre diferentes configurações de variáveis (como CT_Cimento, CT_Agua, resistências reais em diferentes dias, e aditivos).
   - A previsão da resistência do concreto aos 28 dias é calculada com base no modelo pré-treinado.

2. **Carregar Arquivo Excel:**
   - O usuário pode carregar um arquivo Excel contendo os dados, que são processados e as previsões de resistência são aplicadas a cada linha do arquivo.
   - Um arquivo Excel de saída é gerado com as previsões, pronto para ser baixado.

## Tecnologias

- **Streamlit**: Framework utilizado para criar a interface do usuário.
- **Scikit-learn**: Biblioteca usada para carregar e aplicar os modelos de predição de IA.
- **Pandas**: Usado para manipulação de dados.
- **Openpyxl**: Para leitura e escrita de arquivos Excel.

## Como Rodar o Projeto

### Requisitos

- Python 3.8 ou superior
- Bibliotecas: `streamlit`, `numpy`, `pandas`, `joblib`, `openpyxl`

### Passos

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu_usuario/nome_do_repositorio.git
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute o aplicativo Streamlit:
    ```bash
    streamlit run app.py
    ```

4. Acesse o aplicativo em seu navegador: [http://localhost:8501](http://localhost:8501)

## Estrutura do Código

O código principal está dividido em três partes:

1. **Entrada de Dados**:
   - O usuário pode escolher entre inserir dados manualmente ou carregar um arquivo Excel.
   
2. **Previsão**:
   - Com base nos dados inseridos, o modelo adequado é carregado e a previsão da resistência do concreto é calculada e exibida.
   
3. **Saída**:
   - A previsão pode ser visualizada diretamente na interface do Streamlit ou, no caso do upload de um arquivo Excel, o arquivo atualizado é gerado para download.

## Modelos Utilizados

O projeto utiliza vários modelos treinados com base nas configurações de entrada. Cada modelo foi salvo em um arquivo `.pkl` (por exemplo, `modelo1.pkl`, `modelo2.pkl`, etc.) e é carregado conforme a escolha do usuário.

## Contribuição

Se você gostaria de contribuir para este projeto, por favor, siga estas etapas:

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nome-da-feature`)
3. Commit suas alterações (`git commit -am 'Adiciona uma nova feature'`)
4. Push para a branch (`git push origin feature/nome-da-feature`)
5. Abra um Pull Request

## Licença

Distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
