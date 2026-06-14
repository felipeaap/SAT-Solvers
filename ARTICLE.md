# **A Evolução dos Algoritmos para o Problema da Satisfatibilidade Booleana (SAT)**

## **Introdução**

O Problema da Satisfatibilidade Booleana (SAT – *Boolean Satisfiability Problem*) consiste em determinar se existe uma atribuição de valores verdade às variáveis de uma fórmula booleana capaz de torná-la verdadeira. Formalmente, dado um conjunto de variáveis booleanas e uma expressão lógica composta por operadores como conjunção, disjunção e negação, o objetivo é verificar se existe ao menos uma combinação de valores que satisfaça toda a fórmula.

O SAT foi o primeiro problema a ser demonstrado como NP-Completo por Stephen Cook em 1971, tornando-se um dos problemas centrais da Teoria da Complexidade Computacional. Além de sua importância teórica, possui inúmeras aplicações práticas em áreas como verificação formal de hardware e software, inteligência artificial, planejamento automático, bioinformática e otimização combinatória.

Ao longo das últimas décadas, diversos algoritmos foram desenvolvidos para resolver instâncias SAT de forma cada vez mais eficiente. A evolução desses métodos pode ser compreendida como uma sequência de tentativas para reduzir o espaço de busca necessário para encontrar uma solução ou provar sua inexistência. Esta trajetória inicia-se com a busca exaustiva, passa pelos algoritmos de Davis-Putnam e DPLL e culmina nos modernos resolvedores baseados em Conflict-Driven Clause Learning (CDCL).

---

# **1\. Busca Exaustiva (Brute Force)**

A busca exaustiva representa a abordagem mais simples e intuitiva para resolver o problema SAT. O método consiste em enumerar todas as possíveis atribuições de valores verdade para as variáveis da fórmula e verificar, uma a uma, se a expressão é satisfeita.

Considerando uma fórmula composta por n variáveis booleanas, existem exatamente 2ⁿ atribuições possíveis. O algoritmo avalia cada combinação até encontrar uma solução ou concluir que nenhuma delas satisfaz a fórmula.

Considere a fórmula:

F \= (A ∨ B) ∧ (¬A ∨ C)

Nesse caso, existem oito possíveis atribuições para as variáveis A, B e C. O algoritmo verifica cada uma delas individualmente até determinar se a fórmula é satisfatível.

A principal vantagem dessa abordagem é sua simplicidade conceitual. O método é completo e garante encontrar uma solução sempre que ela existir. Entretanto, seu custo computacional cresce exponencialmente com o número de variáveis, apresentando complexidade temporal O(2ⁿ).

Essa explosão combinatória torna a busca exaustiva impraticável para instâncias moderadas ou grandes. Por exemplo, uma fórmula com apenas 30 variáveis já possui mais de um bilhão de atribuições possíveis.

A limitação observada nesse método motivou o desenvolvimento de técnicas capazes de evitar a exploração explícita de todo o espaço de busca. O primeiro avanço significativo nessa direção foi o algoritmo de Davis-Putnam.

---

# **2\. Algoritmo de Davis-Putnam**

Proposto por Martin Davis e Hilary Putnam em 1960, o algoritmo de Davis-Putnam (DP) representou uma mudança importante de paradigma. Em vez de testar atribuições diretamente, o método procura simplificar a fórmula por meio de transformações lógicas que preservam sua satisfatibilidade.

A principal técnica utilizada é a resolução. Considere a fórmula:

(A ∨ B) ∧ (¬A ∨ C)

Como a variável A aparece em polaridades opostas, é possível aplicar a regra de resolução e gerar a cláusula:

(B ∨ C)

Após essa operação, as cláusulas originais podem ser removidas e a variável A é eliminada da fórmula.

O algoritmo repete esse processo sucessivamente até que uma das seguintes situações ocorra:

* obtenção de uma cláusula vazia, indicando insatisfatibilidade;  
* eliminação completa das variáveis;  
* redução da fórmula ao conjunto vazio de cláusulas, indicando satisfatibilidade.

O método representou um avanço importante em relação à busca exaustiva, pois substituiu a enumeração explícita de atribuições por manipulações simbólicas da fórmula.

Entretanto, surgiu uma nova limitação. A aplicação repetida da resolução pode gerar um número extremamente elevado de cláusulas intermediárias. Em muitas instâncias, o crescimento dessas cláusulas ocorre de forma explosiva, consumindo grandes quantidades de memória.

Assim, embora o algoritmo evitasse a explosão de atribuições observada na busca exaustiva, ele introduzia um novo problema: a explosão de cláusulas.

Essa limitação levou ao desenvolvimento de uma nova abordagem, baseada em busca controlada e retrocesso, conhecida como DPLL.

---

# **3\. Algoritmo Davis-Putnam-Logemann-Loveland (DPLL)**

O algoritmo Davis-Putnam-Logemann-Loveland (DPLL), introduzido em 1962 por Martin Davis, George Logemann e Donald Loveland, representa uma evolução direta do método Davis-Putnam.

A principal mudança consiste na substituição da eliminação sistemática de variáveis por uma estratégia de busca baseada em decisões e retrocesso (*backtracking*). Em vez de gerar novas cláusulas por resolução, o algoritmo atribui valores às variáveis e simplifica a fórmula progressivamente.

Quando uma decisão leva a uma contradição, o algoritmo retorna ao último ponto de escolha e tenta a alternativa oposta.

Além do mecanismo de busca, o DPLL introduz duas técnicas fundamentais de simplificação.

### **Propagação Unitária**

Sempre que uma cláusula contém apenas um literal, esse literal deve necessariamente ser verdadeiro.

Considere:

(A) ∧ (¬A ∨ B)

A cláusula unitária (A) força a atribuição A \= verdadeiro. Após a simplificação, obtém-se:

(B)

o que implica imediatamente B \= verdadeiro.

### **Eliminação de Literais Puros**

Um literal é considerado puro quando aparece apenas em uma polaridade ao longo de toda a fórmula.

Por exemplo:

(A ∨ B) ∧ (A ∨ C)

Como A aparece apenas de forma positiva, atribuir A \= verdadeiro satisfaz todas as cláusulas que o contêm, permitindo sua remoção imediata.

O funcionamento geral do DPLL pode ser resumido em quatro etapas:

1. Aplicar propagação unitária;  
2. Aplicar eliminação de literais puros;  
3. Escolher uma variável para decisão;  
4. Retroceder em caso de conflito.

Embora o DPLL mantenha complexidade exponencial no pior caso, sua eficiência prática é significativamente superior à dos métodos anteriores. Ao evitar a explosão de cláusulas do Davis-Putnam e reduzir drasticamente o espaço efetivamente explorado, tornou-se a base conceitual dos resolvedores SAT modernos.

Ainda assim, um problema permanecia: o algoritmo não aprendia com seus erros. Quando um conflito ocorria, o DPLL simplesmente retornava à decisão anterior, podendo repetir raciocínios semelhantes diversas vezes. Essa limitação motivou o surgimento dos resolvedores CDCL.

---

# **4\. Conflict-Driven Clause Learning (CDCL)**

Os algoritmos Conflict-Driven Clause Learning (CDCL) surgiram como uma extensão do DPLL com o objetivo de tornar a busca mais inteligente.

A principal ideia consiste em analisar os conflitos encontrados durante a execução e extrair conhecimento útil a partir deles. Em vez de apenas retroceder, o algoritmo aprende novas cláusulas capazes de impedir que o mesmo erro seja repetido futuramente.

Considere a fórmula:

(A ∨ B)  
∧ (¬A ∨ C)  
∧ (¬B ∨ C)  
∧ (¬C)

Suponha que o algoritmo decida inicialmente:

A \= verdadeiro

A propagação unitária implica:

C \= verdadeiro

Entretanto, a cláusula (¬C) exige simultaneamente:

C \= falso

resultando em um conflito.

Enquanto o DPLL apenas retornaria à decisão anterior, o CDCL analisa as causas da contradição e gera uma cláusula aprendida que impede a repetição da mesma combinação de decisões.

Para realizar essa análise, o algoritmo mantém uma estrutura chamada grafo de implicação, que registra as dependências entre decisões e propagações.

Outra inovação importante é o retrocesso não cronológico (*backjumping*). Em vez de retornar passo a passo pelos níveis da árvore de busca, o algoritmo identifica diretamente a decisão responsável pelo conflito e retorna imediatamente a ela.

Os resolvedores CDCL modernos também utilizam reinicializações periódicas (*restarts*), reiniciando a busca sem descartar as cláusulas aprendidas. Dessa forma, novas regiões do espaço de busca podem ser exploradas sem perder o conhecimento acumulado.

Essas técnicas transformaram profundamente a resolução de SAT. Enquanto os métodos anteriores exploravam o espaço de busca de forma relativamente passiva, o CDCL aprende continuamente com os conflitos encontrados, reduzindo progressivamente a quantidade de trabalho necessária.

A implementação deste algoritmo necessita de um banco de dados crescente das resoluções, para que possam ser consultadas com cada vez maior velocidade, no projeto desenvolvido o CDCL não foi devidamente desenvolvido com todas as otimizações necessárias, tampouco com a criação e manutenção de um banco de dados.

Atualmente, resolvedores como MiniSAT, Glucose, Lingeling, CaDiCaL e Kissat utilizam variantes dessa arquitetura. Embora o problema SAT permaneça exponencial no pior caso, os avanços proporcionados pelo CDCL permitem resolver instâncias industriais contendo milhões de variáveis e cláusulas, algo impensável para os algoritmos clássicos.

---

# **Conclusão**

A evolução dos algoritmos SAT pode ser entendida como uma sucessão de estratégias destinadas a reduzir diferentes formas de explosão combinatória.

A busca exaustiva sofre com a explosão do número de atribuições possíveis. O algoritmo de Davis-Putnam reduz esse problema por meio da resolução, mas passa a enfrentar a explosão de cláusulas intermediárias. O DPLL substitui a eliminação sistemática por busca com retrocesso e técnicas de simplificação, reduzindo significativamente o espaço explorado. Por fim, o CDCL introduz aprendizado de cláusulas, análise de conflitos e retrocesso não cronológico, permitindo que o resolvedor acumule conhecimento durante a execução.

Essa trajetória demonstra como os resolvedores SAT evoluíram de métodos puramente exploratórios para sistemas capazes de aprender com a própria busca, constituindo a base dos solucionadores utilizados atualmente em aplicações industriais e científicas de grande escala.
