<h2 align='center'>Automação - Obtenção de cotações online e atualização de cálculos em banco de dados
(Automation - Webscraping for prices and update DB)
</h2>


### Descrição

<p></p>
Script em Python que, criando uma nova janela do navegador, acessa sites definidos e coleta cotações de moedas atualizadas. Em seguida atualiza informações de bancos e dados e prepara dados para exibição ou envio.

<p>Python script that creates a new browser window to access and collect predefined currencies prices. Updates then a DB and handle the data to be displayed or mailed.</p>
<br>

### Funcionalidades do projeto

* Esse script pode trabalhar em segundo plano. O Usuário não precisa aguardar sua finalização.
* Acessa sites definidos pelo usuário, coletando cotações específicadas pelo usuário
* Atualiza banco de dados e processa os dados
* Exporta banco de dados
<br>

* This script can work in background. User doesn't require to wait for it to finish.
* Access predefined websites collecting latest prices
* Updates DB and process the data
* Exports DB
<br>


### Tecnologias utilizadas

* Webdriver
* Selenium
<br>


### Rodando o projeto

* Selenium recomenda o uso dos navegadores Chrome ou Firefox para melhor desempenho
* Inicialmente é necessário instalar manualmente o webdriver do navegador utilizado. Buscar no google chromedriver/firefoxdriver/etc
* O script coleta a cotação dos sites utilizando o caminho XPATH do elemento HTML no site e o nome do Atributo que contém a cotação. Se o usuário for utilizar o google como a fonte das cotações, não será necessário atualizar os caminhos. Se for utilizar outros sites, será necessário obter o novo caminho XPATH e atualizar o nome do Atributo que contém o preço.
* Para obter um caminho XPATH de um elemento HTML use a ferramenta inspecionar do navegador, selecione na aba de inspeção o elemento HTML que contém a cotação, botão direito, copiar, caminho XPATH. Assim que selecionar o elemento na aba inspecionar, o nome do Atributo que contém a cotação poderá ser visto.
* Normalize pontos e vírgulas nos valores conforme necessário para evitar conflitos
<br>

* Selenium recomends Chrome or Firefox to better results
* First it's necessary to manually install the browser webdriver. Google chromedriver/firefoxdriver/etc
* The script collects the prices through the HTML element's XPATH and Attribute containing the price. If the user is gonna use the prices given by google there's no need to update the code. If other site are required it will be necessary to obtain the new XPATH and Attribute name.
* To obtaing a new HTML element's XPATH use the browser Inspect tool on the HTML element, right click it on the inspect window, copy, XPATH. The Attribute name can be seen when selecting the element.
* Normalize the dots and commas on values to avoid conflicts.
