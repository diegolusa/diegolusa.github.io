---
title: "Redes Neurais Artificiais"
tags:
 - Inteligência Artificial
 - Redes neurais artificiais
date: 2025-01-01 08:00:00
---



As Redes Neurais Artificiais (RNAs) são sistemas computacionais inspirados na estrutura e no funcionamento do cérebro humano. A ideia de simular o comportamento dos neurônios biológicos surgiu na década de 1940 com o trabalho seminal de *Warren McCulloch e Walter Pitts (1943)*[@mcculloch1943logical], que propuseram um modelo matemático simplificado do neurônio.

Em 1958, *Frank Rosenblatt* desenvolveu o Perceptron[@rosenblatt1958perceptron], um dos primeiros algoritmos de aprendizado supervisionado, que podia classificar padrões lineares. No entanto, a limitação do Perceptron em resolver problemas não linearmente separáveis, como o problema XOR, levou a um declínio no interesse por RNAs nos anos 1970.

A retomada aconteceu nos anos 1980 com a introdução do algoritmo de retropropagação do erro (**backpropagation**) por *Rumelhart, Hinton e Williams (1986)* [@rumelhart1986learning], permitindo o treinamento eficiente de redes multicamadas.

O verdadeiro boom ocorreu nas décadas de 2000 e 2010, com o aumento do poder computacional (GPUs), grandes conjuntos de dados e técnicas modernas como redes convolucionais (CNNs) e redes recorrentes (RNNs). Isso levou ao desenvolvimento do campo conhecido como *Deep Learning*.


## Analogias com a Neurociência

As Redes Neurais Artificiais (RNAs) foram inspiradas diretamente no funcionamento do cérebro humano. Embora simplificadas, essas redes compartilham características conceituais com os sistemas biológicos, o que pode ajudar na compreensão de seu funcionamento.

| Sistema Biológico     | Rede Neural Artificial                         |
| --------------------- | ---------------------------------------------- |
| Neurônio biológico    | Neurônio artificial (unidade de processamento) |
| Dendritos             | Entradas (atributos / *features*)              |
| Sinapses              | Pesos (w)                                      |
| Potencial de ação     | Ativação (saída do neurônio)                   |
| Axônio                | Saída do neurônio                              |
| Aprendizado sináptico | Ajuste de pesos (via retropropagação)          |

No cérebro, a força das conexões sinápticas muda com a experiência, um processo conhecido como plasticidade sináptica. De forma análoga, nas RNAs, os pesos das conexões são ajustados durante o treinamento para refletir padrões aprendidos a partir de dados.



## Posicionamento das RNAs na Inteligência Artificial

As Redes Neurais Artificiais (RNAs) fazem parte da grande área da Inteligência Artificial (IA), sendo um subconjunto do campo de **Aprendizado de Máquina (Machine Learning)**. Elas se destacam por sua capacidade de modelar funções altamente complexas por meio de estruturas compostas por múltiplas camadas de unidades computacionais interconectadas, conhecidas como neurônios artificiais.

A hierarquia pode ser descrita da seguinte forma:

- **Inteligência Artificial (IA)**: Campo mais amplo que busca criar sistemas capazes de simular a inteligência humana.
  - **Aprendizado de Máquina (Machine Learning)**: Subcampo da IA que utiliza algoritmos capazes de aprender a partir de dados, sem programação explícita para cada tarefa.
    - **Redes Neurais Artificiais (RNAs)**: Modelo computacional inspirado no cérebro humano, capaz de aprender padrões complexos por meio de exemplos.
      - **Deep Learning (Aprendizado Profundo)**: Subárea que utiliza RNAs com muitas camadas ocultas (redes profundas), com destaque para arquiteturas como CNNs (*redes convolucionais*), RNNs (*redes recorrentes*), LSTMs (*long short-term memory*) e Transformers.

Essa organização destaca que o Deep Learning é um refinamento das RNAs, que por sua vez são uma das ferramentas mais poderosas do Aprendizado de Máquina. O sucesso das RNAs modernas se deve, em grande parte, à sua capacidade de **extrair representações hierárquicas dos dados** e realizar tarefas de classificação, regressão e geração com alto desempenho.


!!! note "Importante"
    Embora Deep Learning seja quase sempre implementado com redes neurais, o termo se refere à profundidade do modelo, não exclusivamente à estrutura neural. Contudo, na prática, quase todas as aplicações de Deep Learning são baseadas em RNAs.


## Aplicações

Atualmente, as RNAs são amplamente utilizadas para diversas finalidades. Abaixo constam algumas delas:

- Reconhecimento de voz e assistentes virtuais (ex.: Siri, Alexa)
- Diagnóstico médico assistido por imagem
- Sistemas de recomendação (ex.: Netflix, Amazon)
- Veículos autônomos
- Previsão de séries temporais financeiras
- Geração de imagens, música e texto (ex.: modelos generativos)



## Funcionamento

As redes neurais artificiais (RNAs) funcionam como sistemas computacionais inspirados no funcionamento do cérebro humano, sendo compostas por unidades chamadas neurônios artificiais organizados em camadas. Essas redes são capazes de aprender padrões e realizar tarefas complexas, como reconhecimento de imagens, tradução automática e diagnóstico médico, a partir de exemplos.

As RNAs normalmente são compostas de três ou mais camadas, as quais têm atribuições especiais no processamento:

- **Camada de entrada**: recebe os dados de entrada (ex.: pixels de uma imagem).
- **Camadas ocultas**: processam os dados por meio de transformações não lineares.
- **Camada de saída**: gera o resultado (ex.: a classe da imagem).



!!! note "Importância das camadas"
    - O número de camadas e neurônios determina a capacidade de modelagem da rede.
    - Redes com múltiplas camadas (*deep networks*) são chamadas de redes profundas e são a base do *deep learning*.



Cada neurônio que compõe a rede realiza duas operações básicas:

- Soma ponderada dos sinais de entrada.
- Aplicação de uma função de ativação não linear, como *ReLU* ou *sigmoid*.


Quando um dado de entrada é fornecido à rede (por exemplo, os pixels de uma imagem), ele percorre a rede camada por camada. Cada neurônio recebe sinais das camadas anteriores, realiza uma soma ponderada dessas entradas (ou seja, cada entrada é multiplicada por um peso) e aplica uma função de ativação para gerar uma saída.

A saída de cada neurônio serve como entrada para os neurônios da camada seguinte, até que o resultado final seja obtido na camada de saída.

De forma simplificada, a ativação de um neurônio pode ser representada por:
$$
z = \sum_{i=1}^n w_i x_i + b \quad \text{e} \quad y = \phi(z)
$$

Onde:

- $x_i$: entrada
- $w_i$: peso
- $b$: viés
- $\phi$: função de ativação (ex.: ReLU, *sigmoid*, *tanh*)

O viés (bias) é um componente essencial que desempenha um papel crítico na capacidade da rede de aprender padrões complexos. Embora muitas vezes menos discutido do que os pesos, o viés é fundamental para garantir a flexibilidade e expressividade dos neurônios artificiais. Sem o viés, todas as saídas da função de ativação estariam fixadas na origem do espaço de entrada. Isso limitaria severamente a capacidade da rede de modelar funções complexas.


## Funções de ativação (5 mais usadas)

As funções de ativação introduzem **não linearidade**, permitindo que RNAs aprendam relações complexas. Na prática, costuma-se escolher ativações diferentes para **camadas ocultas** e para a **camada de saída**, dependendo do tipo de problema (classificação, regressão etc.).

![Gráficos de exemplo das ativações mais usadas](../../../img/ia/ativacoes_principais.svg)

As cinco funções mais comuns (e onde elas aparecem com frequência) são:

| Função         | Definição                                                      | Intervalo da saída   | Uso típico                                                                                                            |
| -------------- | -------------------------------------------------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Sigmoid**    | $\sigma(z)=\dfrac{1}{1+e^{-z}}$                                | $(0,1)$              | Saída em **classificação binária** (probabilidade); menos comum em camadas ocultas por saturação/gradientes pequenos. |
| **Tanh**       | $\tanh(z)$                                                     | $(-1,1)$             | Camadas ocultas em redes pequenas/antigas; útil quando se deseja saída centrada em 0.                                 |
| **ReLU**       | $\max(0,z)$                                                    | $[0,\infty)$         | Padrão em **camadas ocultas** em muitas arquiteturas (treino eficiente e simples).                                    |
| **Leaky ReLU** | $\max(\alpha z, z)$ (com $\alpha\approx 0{,}01$)               | $(-\infty,\infty)$   | Alternativa à ReLU para reduzir “neurônios mortos” (mantém pequeno gradiente para $z<0$).                             |
| **Softmax**    | $\text{softmax}(\mathbf{z})_k=\dfrac{e^{z_k}}{\sum_j e^{z_j}}$ | Soma das saídas $=1$ | Saída em **classificação multiclasse** (distribuição de probabilidades).                                              |

Em termos de comportamento, vale destacar que *sigmoid* e *tanh* **saturam** para valores grandes de $|z|$, o que tende a reduzir os gradientes; por isso, elas aparecem com mais frequência na **saída** (no caso da *sigmoid*) ou em redes específicas. Já a ReLU é simples e eficiente, mas pode levar a *neurônios mortos* quando muitos valores ficam negativos; a Leaky ReLU mitiga esse efeito ao manter uma pequena inclinação para $z<0$. Para a *softmax*, implementações reais costumam subtrair $\max(\mathbf{z})$ antes do exponencial para melhorar a estabilidade numérica.

!!! note "Vocabulário rápido"
    - **Saturação**: ocorre quando a função de ativação entra em uma região “quase plana”. Nessa região, pequenas variações em $z$ mudam muito pouco a saída $y=\phi(z)$, e o gradiente $\phi'(z)$ tende a ficar **próximo de 0**. Exemplo: na *sigmoid*, valores como $z\gg 0$ produzem saída próxima de 1; como a curva fica quase horizontal, o aprendizado pode ficar lento em camadas onde isso acontece com frequência.
    - **Neurônios mortos**: acontece principalmente com ReLU quando um neurônio passa a produzir **sempre 0** (isto é, $z<0$ para praticamente todas as entradas). Como a derivada da ReLU é 0 no lado negativo, o neurônio pode parar de atualizar seus pesos e “morrer” durante o treinamento.
    - **Hiperparâmetros**: são escolhas feitas **antes** (ou ao longo) do treinamento e que não são aprendidas diretamente a partir dos dados como os pesos e vieses. Exemplos comuns: taxa de aprendizado $\eta$, número de épocas, tamanho do *batch*, número de camadas/neurônios, escolha do otimizador (SGD/Adam) e parâmetros da própria ativação (por exemplo, $\alpha$ da Leaky ReLU).

!!! note "Escolha rápida (regra prática)"
    - Camadas ocultas: ReLU ou Leaky ReLU.
    - Saída binária: sigmoid.
    - Saída multiclasse: softmax.
    - Regressão: muitas vezes **sem** ativação na saída (identidade), dependendo da escala do alvo.


!!! note "Importância da função de ativação"
  A escolha de funções de ativação e do otimizador influencia significativamente o desempenho.


Após a **propagação direta** (*forward pass*), a rede compara o valor da saída obtida com o valor real (esperado), utilizando uma função de custo (ou função de perda), que mede o erro da previsão.

Exemplos de funções de custo:

- Erro quadrático médio (MSE)
- Entropia cruzada (Cross-Entropy)


Com o erro calculado, a rede precisa ajustá-lo. Isso é feito pela **retropropagação**, um processo que distribui o erro de volta através da rede (da saída para a entrada), aplicando a **regra da cadeia** para determinar quanto cada peso contribuiu para o erro total.

Através desse processo, são calculados os gradientes (derivadas parciais da função de custo em relação aos pesos). Usando os gradientes calculados, os pesos da rede são atualizados por meio de um algoritmo de otimização, como o *Gradiente Descendente* ou o *Adam*. O objetivo é minimizar o erro da rede ajustando os pesos iterativamente.


$$
w \leftarrow w - \eta \cdot \frac{\partial \mathcal{L}}{\partial w}
$$

Onde:

- $\eta$: taxa de aprendizado (learning rate)
- $\frac{\partial \mathcal{L}}{\partial w}$: gradiente da função de custo em relação ao peso


!!! note "Taxa de Aprendizado"

  A taxa de aprendizado (learning *rate*) é um hiperparâmetro fundamental no treinamento de redes neurais e outros algoritmos de aprendizado de máquina. Ela controla o tamanho dos passos que o algoritmo de otimização dá ao atualizar os pesos da rede durante o processo de aprendizado.

  Pode-se imaginar que o algoritmo está tentando descer uma montanha (ou minimizar uma função de erro). A taxa de aprendizado determina o quão grande será cada passo:
  - Se o passo for **muito pequeno**: o progresso será lento, e pode demorar muito para encontrar o mínimo.
  - Se o passo for **muito grande**: pode ultrapassar o mínimo e até divergir, oscilando sem convergir.

Esse ciclo (propagação → erro → retropropagação → ajuste de pesos) é repetido por várias **épocas** (iterações sobre o conjunto de dados), até que a rede atinja um bom desempenho, isto é, consiga realizar previsões com erro mínimo. Se fôssemos representar graficamente as etapas, teríamos a seguinte sequência:


```mermaid
graph LR
A[Entrada de dados] --> B[Camada de entrada]
B --> C[Camadas ocultas com funções de ativação]
C --> D[Camada de saída]
D --> E[Comparação com saída esperada]
E --> F[Função de custo]
F --> G[Retropropagação do erro]
G --> H[Ajuste dos pesos]
H --> B

```





## Tipos de Treinamento de Redes Neurais

O treinamento de uma Rede Neural Artificial (RNA) consiste no processo de ajustar seus pesos internos com base em um conjunto de dados. Existem diferentes tipos de treinamento, cada um adequado a um tipo específico de tarefa ou disponibilidade de dados. Os principais são:

### Aprendizado Supervisionado

A rede é treinada com exemplos rotulados, ou seja, entradas acompanhadas de suas respectivas saídas desejadas. O modelo aprende a mapear entradas para saídas minimizando o erro entre a previsão da rede e o valor real.

**Exemplos:**
- Classificação de imagens (ex.: gato ou cachorro)
- Previsão de preços (ex.: valor de imóveis)

### Aprendizado Não Supervisionado

A rede recebe apenas os dados de entrada, sem rótulos. O objetivo é descobrir padrões, agrupamentos ou estruturas nos dados.

**Exemplos:**
- Agrupamento (clustering)
- Redução de dimensionalidade
- Detecção de anomalias

### Aprendizado por Reforço

Neste tipo de treinamento, o agente (a rede) interage com um ambiente, realizando ações e recebendo recompensas ou penalidades. O objetivo é aprender uma política que maximize a recompensa acumulada.

**Exemplos:**
- Robôs aprendendo a andar
- Jogadores de xadrez artificiais (como AlphaZero)

### Aprendizado Semi-supervisionado

Combina elementos dos métodos supervisionado e não supervisionado. Uma pequena parte dos dados é rotulada, e a maior parte não. A rede aprende a partir da combinação desses dois conjuntos.

### Aprendizado Auto-supervisionado

Um tipo especial de aprendizado em que a própria estrutura dos dados fornece o rótulo. Muito usado em pré-treinamento de grandes modelos de linguagem.

**Exemplos:**
- Previsão de palavras ausentes em frases
- Previsão de frames futuros em vídeos

!!! tip "Escolha do tipo de treinamento"
    A escolha do tipo de treinamento depende da tarefa, da disponibilidade de dados rotulados e do objetivo do modelo.


## Principais Métricas em Redes Neurais

Durante o treinamento e a avaliação de redes neurais artificiais, é essencial utilizar métricas que permitam medir o desempenho do modelo. A escolha da métrica correta depende do tipo de problema:

- **Métricas de classificação** são usadas quando o objetivo é prever categorias ou classes. Avaliam o quanto as previsões do modelo se alinham com as classes reais.
- **Métricas de regressão** são usadas quando o objetivo é prever valores numéricos contínuos. Avaliam o quanto as previsões numéricas se aproximam dos valores reais.

A seguir, listamos as principais métricas utilizadas em cada tipo de tarefa:

### Métricas para Classificação

#### **Acurácia**  
  Proporção de previsões corretas sobre o total de exemplos.
$$
  \text{Acurácia} = \frac{\text{número de acertos}}{\text{total de exemplos}}
$$
#### **Precisão (Precision)**  
  Proporção de exemplos positivos preditos corretamente entre todos os exemplos preditos como positivos.

#### **Revocação (Recall ou Sensibilidade)**  
  Proporção de exemplos positivos corretamente identificados pelo modelo.

#### **F1-Score**  
  Média harmônica entre precisão e revocação. Equilibra as duas medidas, útil quando há desequilíbrio de classes.

#### **Matriz de Confusão**  

A matriz de confusão é uma tabela que resume o desempenho de um modelo de classificação, comparando os **valores reais** com os **valores preditos**.


```
                    PREDITO
                 Positivo  Negativo
REAL  Positivo |    VP    |   FN   |
      Negativo |    FP    |   VN   |
```
 
Neste exemplo, cada célula tem um significado:
 
| Sigla | Nome | Significado |
|-------|------|-------------|
| **VP** | Verdadeiro Positivo | O modelo disse **positivo** e estava **certo** |
| **VN** | Verdadeiro Negativo | O modelo disse **negativo** e estava **certo** |
| **FP** | Falso Positivo | O modelo disse **positivo** mas estava **errado** (Erro Tipo I) |
| **FN** | Falso Negativo | O modelo disse **negativo** mas estava **errado** (Erro Tipo II) |



Imagine um modelo de detecção de câncer que analisa 100 exames e apresenta o seguinte resultado:
 
```
                    PREDITO
                 Doente  Saudável
REAL  Doente  |   40   |   10   |   50 pacientes doentes
      Saudável|    5   |   45   |   50 pacientes saudáveis
```
 
A interpretação da matriz de confusão seria a seguinte:
- **40 VP** → doentes corretamente identificados
- **45 VN** → saudáveis corretamente identificados
- **10 FN** → doentes classificados como saudáveis *(perigoso!)*
- **5 FP** → saudáveis classificados como doentes


Com base nessa matriz, é possível calcular todas as outras métricas derivadas (precisão, revocação, F1-score, etc.). Vamos entender um pouco mais sobre cada uma delas.



1. **Acurácia**

> "De tudo que o modelo classificou, quanto ele acertou?"

$$\text{Acurácia} = \frac{VP + VN}{VP + VN + FP + FN}$$

No exemplo: (40+45)/100 = **85%**

É enganosa em dados desbalanceados (ex: 95% das amostras são da classe A).

---

2. **Precisão (Precision)**

> "De tudo que o modelo disse ser positivo, quanto realmente era?"

$$\text{Precisão} = \frac{VP}{VP + FP}$$

No exemplo: 40/(40+5) = **88,9%**

É útil quando **falsos positivos** são custosos (ex: spam filter — não quero bloquear e-mails legítimos).

---

3. **Recall (Sensibilidade)**

> "De todos os positivos reais, quantos o modelo encontrou?"

$$\text{Recall} = \frac{VP}{VP + FN}$$

No exemplo: 40/(40+10) = **80%**

É útil quando **falsos negativos** são custosos (ex: diagnóstico de câncer — não quero deixar doentes passarem).

---

4. **F1-Score**

> "Média harmônica entre Precisão e Recall."

$$\text{F1} = 2 \times \frac{\text{Precisão} \times \text{Recall}}{\text{Precisão} + \text{Recall}}$$

No exemplo: 2 × (0.889 × 0.80)/(0.889 + 0.80) = **84,2%**

É uma métrica que equilibra as duas outras. Ideal quando há **desbalanceamento de classes**.

---

5. **Especificidade**

> "De todos os negativos reais, quantos o modelo identificou corretamente?"

$$\text{Especificidade} = \frac{VN}{VN + FP}$$

No exemplo: 45/(45+5) = **90%**

---


##### Extensão para múltiplas classes

Em problemas com N classes (ex: classificar dígitos 0–9), a matriz vira **N×N**:

```
           Predito: 0   1   2
Real: 0  [  45    2   3  ]
Real: 1  [   1   48   1  ]
Real: 2  [   2    1  47  ]
```

A diagonal principal representa os **acertos**. Fora dela, os erros. As mesmas métricas são calculadas **por classe** (one-vs-rest) e depois agregadas com estratégias como *macro average* ou *weighted average*.


### Métricas para Regressão

- **Erro Quadrático Médio (MSE)**  
  Penaliza grandes erros de forma mais acentuada.

- **Raiz do Erro Quadrático Médio (RMSE)**  
  É a raiz quadrada do MSE, mantendo a unidade dos dados.

- **Erro Absoluto Médio (MAE)**  
  Média das diferenças absolutas entre valor previsto e real.

- **\( R^2 \) Score (Coeficiente de Determinação)**  
  Mede o quão bem a regressão explica a variabilidade dos dados. Varia de 0 (sem explicação) a 1 (explicação perfeita).

!!! note "Dica"
    Sempre escolha a métrica que reflete melhor o objetivo do modelo e o contexto do problema. Em problemas de desequilíbrio de classes, métricas como F1-Score ou AUC são mais indicadas que a simples acurácia.

