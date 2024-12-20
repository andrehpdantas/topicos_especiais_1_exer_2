# topicos_especiais_1_exer_2

## Exercício

Utilizando as ferramentas abordadas na aula de testes mobile para fazer automação de testes, escolha um aplicativo existente na loja de aplicativos e realize automação de 2 cenários de testes mobile de no mínimo 2 funcionalidades.

* Escolha a ferramenta que você tiver melhor afinidade para automação mobile
* Especifique 2 cenarios de testes para cada funcionalidade

Utilize documento base na pasta Automação para se guiar como fazer.
A entrega do código pode ser feita dentro do arquivo ou compartilhar uma pasta no drive.

## Resposta


### Ambiente 
- Sistema Operacional Windows 11
- Android Studio Android Studio Ladybug | 2024.2.1 Patch 2 | Build #AI-242.23339.11.2421.12550806
- Java 23.0.1 2024-10-15
- Python 3.13
- Smartfone Motorola Edge 4 5G


### Caso de Teste - CT01 Teste Capacidade de alteração de minutos

#### Pré-Condições
Aplicativo Pomodoro Timer aberto e na tela inicial.

#### Detalhamento
1. Usuário clica no menu sanduiche presente no canto superior direito, dando acesso as configurações do aplicativo
2. Usuário clica na widget POMODORO
3. Usuário seleciona a quantidade de minutos desejada para cada ciclo POMODORO.
4. Usuário clica no botão de confirmação.
5. Usuário clica no botão Voltar, presente no canto superior esquerdo da aplicação.
6. Usuário clica no botão MODO, presente logo abaixo do timer, até que a opção POMODORO apareça.

#### Pós-Condições
- A quantidade de minutos configurada pelo usuário deve aparecer no modo POMODORO. Por exemplo, se o usuário configurar 1 minuto, a string 
"POMODORO 1 MIN" deve ser mostrada.


### Caso de Teste - CT02 Teste Capacidade de alteração de pausas( Short Break e Long Break)

#### Pré-Condições
Aplicativo Pomodoro Timer aberto e na tela inicial.

#### Detalhamento
1. Usuário clica no menu sanduiche presente no canto superior direito, dando acesso as configurações do aplicativo
2. Usuário clica na widget BREAK
3. Usuário seleciona a quantidade de minutos desejada para cada ciclo BREAK.
4. Usuário clica no botão de confirmação.
5. Usuário clica no botão Voltar, presente no canto superior esquerdo da aplicação.
6. Usuário clica no botão MODO, presente logo abaixo do timer, até que a opção SHORT BREAK apareça.

#### Pós-Condições
- A quantidade de minutos configurada pelo usuário deve aparecer no modo SHORT BREAK. Por exemplo, se o usuário configurar 1 minuto, a string 
"SHORT BREAK 1 MIN" deve ser mostrada.


### Caso de Teste - CT03 Teste Inicio Ciclo Pomodoro( 1 minuto )

#### Pré-Condições
Aplicativo Pomodoro Timer aberto e na tela inicial.
#### Detalhamento
1. Usuário clica no menu sanduiche presente no canto superior direito, dando acesso as configurações do aplicativo
2. Usuário clica na widget POMODORO
3. Usuário seleciona a quantidade de minutos, no caso 1 minuto, desejada para cada ciclo POMODORO.
4. Usuário clica no botão de confirmação.
5. Usuário clica no botão Voltar, presente no canto superior esquerdo da aplicação.
6. Usuário clica no botão play do timer. 
7. Usuário aguarda a finalização da contagem do timer, que deve transitar automaticamente após alarme sonoro para a contagem do intervalo short break.
#### Pós-Condições
- O timer deve transitar do modo POMODORO para SHORT Break.

### Caso de Teste - CT04 Teste Interrupção Ciclo Pomodoro

#### Pré-Condições
Aplicativo Pomodoro Timer aberto e na tela inicial.
#### Detalhamento
1. Usuário clica no menu sanduiche presente no canto superior direito, dando acesso as configurações do aplicativo
2. Usuário clica na widget POMODORO
3. Usuário seleciona a quantidade de minutos, no caso 1 minuto, desejada para cada ciclo POMODORO.
4. Usuário clica no botão de confirmação.
5. Usuário clica no botão Voltar, presente no canto superior esquerdo da aplicação.
6. Usuário clica no botão play do timer. 
7. Usuário aguarda a finalização da timeout desejado, nesse teste 5 segundos, e clica no timer, pausando o ciclo pomodoro. 


#### Pós-Condições
- O timer deve pausar após o timeout desejado, no caso 5 segundos. A contagem deve ter sido decrementada de no mínimo 5 segundos. 


