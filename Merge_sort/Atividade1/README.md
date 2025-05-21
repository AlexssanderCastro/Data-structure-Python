<h1>Atividades sobre o alorítmo MergeSort</h1>
<hr>

<h2>Questão 1:</h2>
<br>
<p>Algoritmo de ordenaçao decrescente do Merge Sort presente no arquivo Questão1.py</p>
<br>
<hr>
<h2>Questão 2:</h2>
<p>Os códigos de ordenação e de checagem de ordenação estão no arquivo Questão2.py</p>

<h3>Teste 1: array de 10 elementos</h3> 

![image](https://github.com/user-attachments/assets/de8b6da7-4780-475e-9b90-b0390f937b24)

<p>Array foi ordenado</p>

![image](https://github.com/user-attachments/assets/34d4edc6-97d2-41d0-8468-c84cb0e75df5)
<br>
<h3>Teste 2: array de 100 elementos</h3> 

![image](https://github.com/user-attachments/assets/c117d41e-5098-4627-8442-1a2c785fad5e)
<p>Array foi ordenado</p>

![image](https://github.com/user-attachments/assets/8679b361-8d46-432f-9716-16610e68ca74)
<br>
<h3>Teste 3: array de 1000 elementos</h3> 

![image](https://github.com/user-attachments/assets/1c12974b-a5c7-4295-8d97-38a87465940f)
<p>Array foi ordenado</p>

![image](https://github.com/user-attachments/assets/3286948c-e3e4-41c5-ae44-4ef082befe01)






<hr>
<h2>Questão 3:os códigos estão no arquivo Questão3</h2>

<p>a)No caso de colocar -1 no meio deu erro no código porque provavelmente o index ficou negativo, já colocando +1 o merge_sort funcionou, mas as separações do array foram diferentes, mas não afetou o resultado</p>
<p>b)No caso do -1 não funciona, no +1 funciona</p>
<p>c)Sim a variação de -1 provoca falha, pois voce acaba ignorando certos elementos, e pode inclusive fazer ser criado um loop infinito em alguns casos</p>
<hr>


<h2>Questão 4:</h2>
<br>
Algoritmo de lista encadeada simples junto ao merge_sort que ordena essa lista presente no arquivo Questão4.py
<br>
<hr>
<h2>Questão 5:Códigos presentes no arquivo Questão5</h2>

<h3> :clipboard: Tabela de testes de comparação entre as versões do Merge Sort</h3>

| Tamanho do Vetor | Tempo Recursivo (s) | Tempo Iterativo (s) |
| ---------------- | ------------------- | ------------------- |
| 10               | 1.45                | 3.17                |
| 5.000            | 0.007               | 0.009               |
| 10.000           | 0.0122              | 0.0217              |
| 50.000           | 0.071               | 0.121               |
| 100.000          | 0.154               | 0.288               |
| 500.000          | 1.061               | 1.713               |
<br>
<h3>:bar_chart: Conclusão baseada nos testes:</h3> 
<p>A versão recursiva, além de ser mais simples de entender, possuiu um desempenho superior em todos os testes.</p>
<hr>
