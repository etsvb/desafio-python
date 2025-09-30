# desafio-python

01) Realize a refatoração do código abaixo, alterando a estrutura de `def case` para o uso o
`IF/ELIF`. Outras alterações no código poderão ser realizadas também:

```
print ("ESCOLHA A CERVEJA PELO NUMERO")
print ("1-ANTARTICA R$6.00;2-SKOL R$6.50;3-BRAHMA R$8.20;4-SOL
R$8.25;")
cerveja = input ("5-NORTENHA R$16.80;6-PROIBIDA R$4.80;7-DEVASSA
R$5.90;8-HEINEKEN R$9.00")
q = float(input("Quantas ???"))
def case_1():
 valor_cerveja = 6 * q
 nome = "Antartida"
def case_2():
 valor_cerveja = 6.5 * q
 nome = "Skol"
def case_3():
 valor_cerveja = 8.2 * q
 nome = "Brahma"
def case_4():
 valor_cerveja = 8.25 * q
 nome = "Sol"
def case_5():
 valor_cerveja = 16.8 * q
 nome = "Nortenha"
def case_6():
 valor_cerveja = 4.8 * q
 nome = "Proibida"
def case_7():
 valor_cerveja = 5.9 * q
 nome = "Devassa"
def case_8():
 valor_cerveja = 9 * q
 nome = "Heineken"
def case_default():
 print "Valor invalido"
print (nome,"custa",valor_cerveja,"Reais, por",q,"cerveja(s)")
```

A **refatoração** é uma forma disciplinada de reestruturar o **código** quando pequenas
mudanças são feitas nele para melhorar o design, performance ou funcionamento
do mesmo. Um aspecto importante de uma refatoração é que ela melhora a
estrutura sem mudar o comportamento de funcionamento; uma refatoração não
adiciona nem remove funcionalidade.
