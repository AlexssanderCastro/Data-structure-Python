# :book:Estrutura de Dados 2


<strong>Aluno: Alexssander José de Oliveira de Castro</strong>



---

<p align="center">
  <strong>Comparação entre Bubble Sort Tradicional e Bubble Sort Otimizado</strong>
</p>


---
<h2 align="center">
  <strong>Códigos</strong>
</h2>



<strong>BubbleSort Tradicional:</strong>

![image](https://github.com/user-attachments/assets/0106adfc-db11-4e59-9a7a-8b9501e30afd)

<strong>BubbleSort Otimizado:</strong>

![image](https://github.com/user-attachments/assets/0d234ef2-69d2-428a-b1ed-3a82c3d60dcc)


---
<h2 align="center">
  <strong>Testes</strong>
</h2>

---

<strong>Teste 1️⃣: lista = [11, 4, 30, 22, 7, 26]</strong>


<p align="center">
  <strong>BubbleSort Tradicional</strong>
</p>

![image](https://github.com/user-attachments/assets/a06fccd0-4364-4caf-8411-be7da244181d)

<p align="center">
  <strong>BubbleSort Otimizado</strong>
</p>

![image](https://github.com/user-attachments/assets/37fa587b-ddfe-4a4b-abad-f295317291d5)

<br>
<br>
<br>

---

<strong>Teste 2️⃣: lista = [22, 35, 15, 14, 1, 29, 72]</strong>


<p align="center">
  <strong>BubbleSort Tradicional</strong>
</p>

![image](https://github.com/user-attachments/assets/125f0892-6bb3-4047-931f-4e152246cc81)


<p align="center">
  <strong>BubbleSort Otimizado</strong>
</p>

![image](https://github.com/user-attachments/assets/088e0873-6497-4b77-90b6-925599f5ee76)

<br>
<br>
<br>

---

<strong>Teste 3️⃣: lista = [1, 5, 23, 44, 42, 41, 57]</strong>


<p align="center">
  <strong>BubbleSort Tradicional</strong>
</p>

![image](https://github.com/user-attachments/assets/3102f0f8-3a6b-47cc-93ef-bf380248d8da)


<p align="center">
  <strong>BubbleSort Otimizado</strong>
</p>

![image](https://github.com/user-attachments/assets/7f928c51-15e6-4cfb-8914-ccdff12ca164)


---

<h2 align="center">
  <strong>Comparação de tempo e iterações</strong>
</h2>

<div align="center">

| Teste | Algoritmo              | Iterações | Tempo de Execução (s) |
|:-----:|:----------------------:|:---------:|:---------------------:|
| 1     | Bubble Sort            | 5         | 0.001192              |
| 1     | Bubble Sort Otimizado  | 4         | 0.001002              |
| 2     | Bubble Sort            | 6         | 0.002149              |
| 2     | Bubble Sort Otimizado  | 5         | 0.002481              |
| 3     | Bubble Sort            | 6         | 0.001016              |
| 3     | Bubble Sort Otimizado  | 3         | 0.001053              |


</div>

---


<h2 align="center">🎯Análise conclusiva dos resultados</h2>


<p align="justify">
Embora o Bubble Sort Otimizado reduza o número de iterações ao detectar quando a lista já está ordenada, em alguns casos ele pode apresentar um tempo de execução maior. Isso ocorre porque a versão otimizada adiciona uma verificação extra a cada iteração para determinar se houve trocas, o que gera uma pequena sobrecarga computacional. Em listas pequenas, essa verificação pode anular os ganhos da otimização, tornando o tempo de execução similar ou até ligeiramente maior do que o Bubble Sort tradicional. Além disso, variações no processamento do sistema podem influenciar os tempos medidos. No entanto, para listas grandes ou quase ordenadas, a versão otimizada geralmente se destaca, reduzindo significativamente as iterações e melhorando o desempenho geral.
</p>
