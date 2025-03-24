# :book:Estrutura de Dados 2


<strong>Aluno: Alexssander José de Oliveira de Castro</strong>



---

<p align="center">
  <strong>Comparação entre Selection Sort Tradicional e Selection Sort Otimizado</strong>
</p>


---
<h2 align="center">
  <strong>Códigos</strong>
</h2>



<strong>SelectionSort Tradicional:</strong>

![image](https://github.com/user-attachments/assets/b5322394-3140-4b43-bd77-75b955638605)


<strong>SelectionSort Otimizado:</strong>

![image](https://github.com/user-attachments/assets/aeb18a86-ea1e-47ec-b3ea-1bf27d097fa1)



---
<h2 align="center">
  <strong>Testes</strong>
</h2>

---

<strong>Teste 1️⃣: lista = [11, 4, 30, 22, 7, 26]</strong>


<p align="center">
  <strong>SelectionSort Tradicional</strong>
</p>

![image](https://github.com/user-attachments/assets/4182b44a-8e83-43cf-923f-855af1a1ba7e)


<p align="center">
  <strong>SelectionSort Otimizado</strong>
</p>

![image](https://github.com/user-attachments/assets/c8ea84dd-9d5d-4563-8e81-377677136208)


<br>
<br>
<br>

---

<strong>Teste 2️⃣: lista = [22, 35, 15, 14, 1, 29, 72]</strong>


<p align="center">
  <strong>SelectionSort Tradicional</strong>
</p>

![image](https://github.com/user-attachments/assets/ff2c4ee9-5441-479c-8ffe-bc88e11e9fa1)


<p align="center">
  <strong>SelectionSort Otimizado</strong>
</p>

![image](https://github.com/user-attachments/assets/6b943a75-a8a1-4661-ac58-80c6098dac9e)


<br>
<br>
<br>

---

<strong>Teste 3️⃣: lista = [1, 5, 23, 44, 42, 41, 57]</strong>


<p align="center">
  <strong>SelectionSort Tradicional</strong>
</p>

![image](https://github.com/user-attachments/assets/89a39e02-7440-4676-804e-1bc591ce4721)


<p align="center">
  <strong>SelectionSort Otimizado</strong>
</p>


![image](https://github.com/user-attachments/assets/b072ddf3-33f5-4fe4-96bb-e7cfde4ef926)


---

<h2 align="center">
  <strong>Comparação de tempo e iterações</strong>
</h2>

<div align="center">

| Teste | Algoritmo                 | Iterações | Tempo de Execução (s) |
|:-----:|:-------------------------:|:---------:|:---------------------:|
| 1     | Selection Sort            | 5         | 0.001192              |
| 1     | Selection Sort Otimizado  | 4         | 0.001002              |
| 2     | Selection Sort            | 6         | 0.002149              |
| 2     | Selection Sort Otimizado  | 5         | 0.002481              |
| 3     | Selection Sort            | 6         | 0.001016              |
| 3     | Selection Sort Otimizado  | 3         | 0.001053              |


</div>

---


<h2 align="center">🎯Análise conclusiva dos resultados</h2>


<p align="justify">
Embora o Bubble Sort Otimizado reduza o número de iterações ao detectar quando a lista já está ordenada, em alguns casos ele pode apresentar um tempo de execução maior. Isso ocorre porque a versão otimizada adiciona uma verificação extra a cada iteração para determinar se houve trocas, o que gera uma pequena sobrecarga computacional. Em listas pequenas, essa verificação pode anular os ganhos da otimização, tornando o tempo de execução similar ou até ligeiramente maior do que o Bubble Sort tradicional. Além disso, variações no processamento do sistema podem influenciar os tempos medidos. No entanto, para listas grandes ou quase ordenadas, a versão otimizada geralmente se destaca, reduzindo significativamente as iterações e melhorando o desempenho geral.
</p>
