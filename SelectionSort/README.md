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

![image](https://github.com/user-attachments/assets/aeb18a86-ea1e-47ec-b3ea-1bf27d097fa1)


<strong>SelectionSort Otimizado:</strong>





---
<h2 align="center">
  <strong>Testes</strong>
</h2>

---

<strong>Teste 1️⃣: lista = [11, 4, 30, 22, 7, 26]</strong>


<p align="center">
  <strong>SelectionSort Tradicional</strong>
</p>

![image](https://github.com/user-attachments/assets/c8ea84dd-9d5d-4563-8e81-377677136208)


<p align="center">
  <strong>SelectionSort Otimizado</strong>
</p>

![image](https://github.com/user-attachments/assets/2a9659a3-6fd1-438d-81b0-06c5ef03540b)



<br>
<br>
<br>

---

<strong>Teste 2️⃣: lista = [22, 35, 15, 14, 1, 29, 72]</strong>


<p align="center">
  <strong>SelectionSort Tradicional</strong>
</p>

![image](https://github.com/user-attachments/assets/6b943a75-a8a1-4661-ac58-80c6098dac9e)


<p align="center">
  <strong>SelectionSort Otimizado</strong>
</p>

![image](https://github.com/user-attachments/assets/0cd62029-0e84-4a84-8467-bdc71b7f74d2)



<br>
<br>
<br>

---

<strong>Teste 3️⃣: lista = [1, 5, 23, 44, 42, 41, 57]</strong>


<p align="center">
  <strong>SelectionSort Tradicional</strong>
</p>

![image](https://github.com/user-attachments/assets/b072ddf3-33f5-4fe4-96bb-e7cfde4ef926)

<p align="center">
  <strong>SelectionSort Otimizado</strong>
</p>

![image](https://github.com/user-attachments/assets/115ae727-2594-4aac-af85-6c25ffc968cf)




---

<h2 align="center">
  <strong>Comparação de tempo e iterações</strong>
</h2>

<div align="center">

| Teste | Algoritmo                 | Iterações | Tempo de Execução (s) |
|:-----:|:-------------------------:|:---------:|:---------------------:|
| 1     | Selection Sort            | 6         | 0.001005              |
| 1     | Selection Sort Otimizado  | 4         | 0.001002              |
| 2     | Selection Sort            | 7         | 0.002163              |
| 2     | Selection Sort Otimizado  | 7         |                       |
| 3     | Selection Sort            | 7         | 0.002088              |
| 3     | Selection Sort Otimizado  | 7         |                       |


</div>

---


<h2 align="center">🎯Análise conclusiva dos resultados</h2>


<p align="justify">
Embora o Bubble Sort Otimizado reduza o número de iterações ao detectar quando a lista já está ordenada, em alguns casos ele pode apresentar um tempo de execução maior. Isso ocorre porque a versão otimizada adiciona uma verificação extra a cada iteração para determinar se houve trocas, o que gera uma pequena sobrecarga computacional. Em listas pequenas, essa verificação pode anular os ganhos da otimização, tornando o tempo de execução similar ou até ligeiramente maior do que o Bubble Sort tradicional. Além disso, variações no processamento do sistema podem influenciar os tempos medidos. No entanto, para listas grandes ou quase ordenadas, a versão otimizada geralmente se destaca, reduzindo significativamente as iterações e melhorando o desempenho geral.
</p>
