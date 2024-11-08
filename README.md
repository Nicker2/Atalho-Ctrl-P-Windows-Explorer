# **Windows Explorer Print Helper**

Este script facilita o processo de impressão para PDF diretamente do **Windows Explorer**, especialmente útil para o **Hospital dos Olhos de Caraguatatuba** na criação de relatórios de biometria. Ele adiciona um atalho `Ctrl+P` que maximiza a janela ativa, clica em áreas específicas da tela e automatiza a impressão de dois arquivos de imagem para uma folha A4 como PDF, usando o **Microsoft Print to PDF**.

## **Descrição**

Este script realiza as seguintes ações:

1. **Verificação da Janela Ativa**: Quando o atalho `Ctrl+P` é pressionado, o script verifica se o **Windows Explorer** está aberto e ativo.
2. **Maximização da Janela**: Se o Explorer estiver ativo, o script maximiza a janela ativa para garantir que o processo de impressão seja feito corretamente.
3. **Clique e Movimentação**: O script clica em uma área específica da tela (pixel `85x13`) e move o cursor para o centro da tela, preparando o processo de impressão.
4. **Automação da Impressão**: O script aguarda a janela de impressão e preenche automaticamente o nome do arquivo para salvar o PDF, como `BIOMETRIA - PACIENTE - FUNCIONARIO.pdf`.

Esse processo é ideal para quem precisa criar rapidamente relatórios de exames de biometria, principalmente para hospitais ou clínicas de oftalmologia.

## **Requisitos**

- **Python 3.x** ou superior.
- As seguintes bibliotecas Python:
  - `pyautogui`
  - `keyboard`
  - `pygetwindow`
  - `psutil`

Você pode instalar as bibliotecas necessárias com o seguinte comando:

```bash
pip install pyautogui keyboard pygetwindow psutil
```

## **Arquivos e Scripts Necessários**

O processo envolve vários arquivos e scripts interconectados. Abaixo estão os detalhes sobre cada um:

### **1. `executar_iniciar_ctrlp.BAT`**

Este arquivo **BAT** é responsável por iniciar o processo do script Python. Ele chama o script `iniciar_ctrlp.py`, que, por sua vez, executa outro script invisível que roda o processo de impressão no Windows Explorer. 

- **Caminho de instalação**: ajuste conforme necessário para o seu ambiente de instalação, substituindo `D:\Meus Documentos\Documentos\Nova pasta\` pelo diretório correto.

### **2. `iniciar_ctrlp.py`**

Este script Python chama o script invisível `executar_invisivel_ctrlp.py` para rodar o script principal de automação sem abrir uma janela visível. Ele verifica se o Python e o script estão presentes e então executa o processo invisível.

- **Caminho de instalação**: ajuste o caminho para o local correto do Python e do script a ser executado.

### **3. `executar_invisivel_ctrlp.py`**

Este script é responsável por verificar a existência do Python e do script principal `CTRLP.PY`, além de garantir que o script seja executado de forma invisível (sem mostrar uma janela de terminal) e que o processo seja reiniciado caso ocorra algum erro.

- **Caminho de instalação**: ajuste o caminho para o local correto do Python e do script a ser executado.

### **4. `CTRLP.PY`**

Este é o script principal de automação, responsável por realizar a captura de tela, clicar em áreas específicas e gerenciar a impressão do conteúdo no Windows Explorer. 

- **Caminho de instalação**: ajuste o caminho para o diretório correto onde o script `CTRLP.PY` se encontra.

### **5. `DEBUG_EXECUTAR_CTRLP.BAT`**

Este arquivo **BAT** serve para depurar o script principal, exibindo no console o que está acontecendo enquanto o script Python é executado. Ele pode ser útil durante o processo de desenvolvimento ou se você encontrar algum erro na execução do script.

- **Caminho de instalação**: ajuste conforme o local onde você deseja colocar o arquivo de depuração.

## **Instruções para Uso**

### **1. Criando o Atalho de Impressão**

Para o script funcionar corretamente, você precisa adicionar o atalho de **impressão** à **barra de ferramentas de acesso rápido** do **Windows Explorer**. Isso permitirá que o script utilize o **Microsoft Print to PDF** diretamente do Explorer.

### **2. Seleção de Arquivos de Imagem**

O script está configurado para funcionar quando você selecionar **dois arquivos de imagem** na janela do **Windows Explorer**. Ao pressionar `Ctrl+P`, o script realizará a impressão dessas imagens no formato PDF, com o nome de arquivo preenchido automaticamente.

### **3. Execução do Script**

1. **Execute o script** `executar_iniciar_ctrlp.BAT` para iniciar o processo de automação.
2. Quando você pressionar **Ctrl+P** no **Windows Explorer**, o script verificará se o Explorer está ativo e maximizará a janela.
3. O script clicará nas áreas específicas da tela, aguardará a janela de impressão e preencherá automaticamente o nome do arquivo.
4. **A impressão para PDF** será realizada automaticamente, gerando o relatório com o nome formatado como `BIOMETRIA - PACIENTE - FUNCIONARIO.pdf`.

## **Licença**

Este projeto está licenciado sob a **MIT License**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## **Autor**

Desenvolvido por **Nicolas Bonza Cavalari Borges**.

## **Contribuições**

Se você encontrar algum problema ou quiser sugerir melhorias, fique à vontade para abrir uma **issue** ou enviar um **pull request**.

---
