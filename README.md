# Máquina de Turing Não Determinística (MTND)

Algoritmo que simule uma Máquina de Turing Não Determinista. A entrada consiste da especificação de uma MTND e de um conjunto de palavras. A saída consiste em uma lista indicando ‘S’ caso a MTND reconheça a palavra em questão e ‘N’ caso contrário.

## O que é?

Este código se refere a uma implementação de uma Máquina de Turing Não-Determinística (MTND) em Python. A MTND é um modelo computacional teórico que pode ser utilizado para resolver uma grande variedade de problemas, incluindo aqueles que não são solucionáveis por uma Máquina de Turing Determinística (MTD). A MTND é importante porque é uma das principais bases teóricas para a computação moderna, e muitos algoritmos e estruturas de dados são baseados em sua teoria. Além disso, a MTND é usada em muitas aplicações práticas, como análise de linguagem natural, criptografia, inteligência artificial e reconhecimento de padrões.

## Projeto do Algoritmo
### Estruturação do Algoritmo

O algoritmo foi pensado para seguir os seguintes passos:

1. Ler a GLC e transformá-la em um conjunto de regras de produção.
2. Ler a palavra a ser verificada.
3. Inicializar a MTND com o estado inicial e a palavra na fita.
4. Enquanto houver transições possíveis na MTND, gerar todas as possíveis configurações da fita e da pilha, seguindo as regras de produção da GLC.
5. Se a palavra for gerada por uma dessas configurações, a MTND aceita a palavra. Caso contrário, a MTND rejeita a palavra.

### Estruturas de Dados

1. Dicionário: é utilizado para armazenar as transições da MTND em uma forma que possa ser facilmente acessada. Cada chave do dicionário representa uma dupla formada por um estado da MTND e um símbolo da entrada, e o valor correspondente é uma lista contendo todas as transições possíveis a partir dessa dupla.

2. Lista: é utilizada para armazenar as transições geradas a partir de uma determinada configuração da MTND. Essa lista é atualizada a cada iteração do algoritmo e serve como entrada para a próxima iteração.

3. Pilha: é utilizada para armazenar as configurações da MTND que ainda não foram processadas pelo algoritmo. A cada iteração do algoritmo, uma nova configuração é retirada da pilha e suas transições são geradas e adicionadas à lista de transições.

4. Vetor: é utilizado para representar a fita da MTND. Cada posição do vetor corresponde a uma célula da fita e armazena um símbolo da fita.

### Como é gerenciado o não determinismo?

O não determinismo em uma MTND é gerado através da possibilidade de ter múltiplas transições possíveis para um mesmo estado e símbolo lido na fita. Quando isso ocorre, a MTND pode escolher qualquer uma das transições possíveis. No código, isso é percorrida com uma pilha de transições.

## Metodologia

A estratégia utilizada pelo algoritmo para testar as possíveis transições é a de retroceder em caso de rejeição, ou seja, se uma transição leva a um estado de rejeição, a máquina volta à última transição válida e tenta outra opção de transição. Se todas as transições possíveis a partir de uma dada configuração da máquina forem rejeitadas, a máquina também volta à última transição válida e tenta outra opção.

A metodologia do software é baseada na estruturação do código de forma modular, com funções e métodos específicos para cada tarefa da máquina de Turing, como a leitura das transições, a validação das transições e a escrita na fita. Além disso, o código foi desenvolvido com o uso de boas práticas de programação, tais como a utilização de nomes de variáveis e funções claros e autoexplicativos, comentários e documentação, bem como o uso de estruturas de dados apropriadas, como dicionários e listas.

Os testes foram realizados de acordo casos específicos conhecidos ao executar o programa. O versionamento foi controlado de acordo seu envio a plataforma Git.

## Resultados e Conclusões

## Resultados

De maneira a executar testes empíricos, utilizando a biblioteca Numpy aliada a Sci-KitLearn, foi possível tratar um vetor de palavras gerados em relação a um segundo vetor de tempo de execução do código. Essa comparação foi plotada e com a linearização possível ver um tempo estimado de execução do código para as palavras que podem ser aceitas pela MTND.
O código abaixo mostra as alterações incluídas no código apresentado no repositório para ser possível imprimir o gráfico e acesso à regressão.

```
test_words = ['ab']                              #Geração de i palavras
for i in range (0, 100):
    test_words.append( 'a' + test_words0[i] + 'b')


language.test_words = test_words                 #Colocação na MTND

tempos = []                                       

for word in language.test_words:                 #Execução de i palavras
    ini = time.time()*1000
    language.process_word(word, language.initial_state)
    fin = time.time()*1000
    tempos.append(fin - ini)

plt.xlabel('Tamanho da Palvara')        #Impressao do gráfico com regressão linear
plt.ylabel('Tempo de Execução (ms)')
x = np.array(list(zip(range(0,101))))
y = np.array(tempos)
plt.scatter(x, tempos)
lr = LinearRegression()
lr.fit(x,y)
plt.plot(x, lr.predict(x), color='red')
plt.show()
```
Apresentado então o gráfico que ilustra o tempo de execução à medida que o tamanho da palavra máquina cresce, apresente uma regressão linear.

![image](https://user-images.githubusercontent.com/50549048/224910752-c88dbf89-d26c-446d-b1e1-f05736a8efd7.png)

## Conclusão

A implementação apresentada é um exemplo de como uma máquina de Turing não determinística pode ser implementada em Python. Através dessa implementação, é possível entender melhor o funcionamento de uma MTND e como ela pode ser usada para resolver problemas em diversas áreas.

O tempo de execução do código foi satisfatório, o crescimento do tempo de execução seguiu o esperado para a MT analisada. 

A implementação pode ser expandida para incluir outras funcionalidades, como a leitura de entrada de arquivos ou a geração de saída em diferentes formatos.
