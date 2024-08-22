from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title("Calculadora")

#Caixa de entrada para digitação dos números.
textoentrada = StringVar()
calculoOperacoes = ""
caixa_de_entrada = Entry(janela, font="Arial 20 bold",
                        textvariable=textoentrada,
                         background="#BBB",
                         border=5,
                         foreground="black"
                           ). grid(row=1, padx=10, columnspan=5, pady=15)

#Função que ao clicar nos números, eles vão para a caixa de entrada.
def enviarnumeros(char):
    global calculoOperacoes
    calculoOperacoes += str(char)
    textoentrada.set(calculoOperacoes)
    
#Botão 7.
botao7 = Button(janela, text="7",
                border=5,
                foreground="black",
                background="#BBB",
                font="Arial 20 bold",
                command=lambda:enviarnumeros("7")).grid(row=2,column=0,sticky="NSEW")

#Botão 8.
botao8 = Button(janela, text="8",
                border=5,
                foreground="black",
                background="#BBB",
                font="Arial 20 bold",
                command=lambda:enviarnumeros("8")).grid(row=2,column=1,sticky="NSEW")

#Botão 9.
botao9 = Button(janela, text="9",
                border=5,
                foreground="black",
                background="#BBB",
                font="Arial 20 bold",
                command=lambda:enviarnumeros("9")).grid(row=2,column=2,sticky="NSEW")    

#Função para deletar um número por vez.
def deletar_numero():
    global calculoOperacoes
    texto = calculoOperacoes[:-1] #Pega todo o texto do entry e apaga apenas o ultimo digito.
    calculoOperacoes = texto
    textoentrada.set(calculoOperacoes)

#Botão de deletar número.
botao_deletar = Button(janela, text="DEL",
                border=5,
                foreground="white",
                background="#DB701F",
                font="Arial 20 bold",
                command=deletar_numero).grid(row=2,column=3,sticky="NSEW")

#Função que limpa toda a caixa de entrada.
def limpar():
    global calculoOperacoes
    calculoOperacoes = ""
    textoentrada.set(calculoOperacoes)

#Botão de limpar a caixa de entrada.
botao_limpar_tudo = Button(janela, text="AC",
                border=5,
                foreground="white",
                background="#DB701F",
                font="Arial 20 bold",
                command=limpar).grid(row=2,column=4,sticky="NSEW")

#Botão 4.
botao4 = Button(janela, text="4",
                border=5,
                foreground="black",
                background="#BBB",
                font="Arial 20 bold",
                command=lambda:enviarnumeros("4")).grid(row=3,column=0,sticky="NSEW") 

#Botão 5.
botao5 = Button(janela, text="5",
                border=5,
                foreground="black",
                background="#BBB",
                font="Arial 20 bold",
                command=lambda:enviarnumeros("5")).grid(row=3,column=1,sticky="NSEW")  

#Botão 6.
botao6 = Button(janela, text="6",
                border=5,
                foreground="black",
                background="#BBB",
                font="Arial 20 bold",
                command=lambda:enviarnumeros("6")).grid(row=3,column=2,sticky="NSEW") 

#Botão de Multiplicação.
botao_multiplicacao = Button(janela, text="*",
                border=5,
                foreground="black",
                background="#BBB",
                font="Arial 20 bold",
                command=lambda:enviarnumeros("*")).grid(row=3,column=3,sticky="NSEW")

#Botão de Divisão.
botao_divisao = Button(janela, text="/",
                border=5,
                foreground="black",
                background="#BBB",
                font="Arial 20 bold",
                command=lambda:enviarnumeros("/")).grid(row=3,column=4,sticky="NSEW")  

#Botão 1.
botao1 = Button(janela, text="1",
                border=5,
                foreground="black",
                background="#BBB",
                font="Arial 20 bold",
                command=lambda:enviarnumeros("1")).grid(row=4,column=0,sticky="NSEW") 

#Botão 2.
botao2 = Button(janela, text="2",
                border=5,
                foreground="black",
                background="#BBB",
                font="Arial 20 bold",
                command=lambda:enviarnumeros("2")).grid(row=4,column=1,sticky="NSEW")

#Botão 3.
botao3 = Button(janela, text="3",
                border=5,
                foreground="black",
                background="#BBB",
                font="Arial 20 bold",
                command=lambda:enviarnumeros("3")).grid(row=4,column=2,sticky="NSEW")  

#Botão de Adição.
botao_adicao = Button(janela, text="+",
                border=5,
                foreground="black",
                background="#BBB",
                font="Arial 20 bold",
                command=lambda:enviarnumeros("+")).grid(row=4,column=3,sticky="NSEW")  

#Botão de Subtração.
botao_subtracao = Button(janela, text="-",
                border=5,
                foreground="black",
                background="#BBB",
                font="Arial 20 bold",
                command=lambda:enviarnumeros("-")).grid(row=4,column=4,sticky="NSEW")  

#Botão 0.
botao0 = Button(janela, text="0",
                border=5,
                foreground="black",
                background="#BBB",
                font="Arial 20 bold",
                command=lambda:enviarnumeros("0")).grid(row=5,column=0,sticky="NSEW") 
   
#Botão de ponto.
botao_ponto = Button(janela, text=".",
                border=5,
                foreground="black",
                background="#BBB",
                font="Arial 20 bold",
                command=lambda:enviarnumeros(".")).grid(row=5,column=1,sticky="NSEW")   

#Função para realizar as contas.
def funcaoigual():
    try: #try para tentar fazer todo o cálculo ao clicar em igual
     global calculoOperacoes
     resultadocalculo = str(eval(calculoOperacoes)) #eval avalia se é um cálculo válido e efetua o calculo
     textoentrada.set(resultadocalculo)
     calculoOperacoes = resultadocalculo
    except ZeroDivisionError: #Se tentar dividir um número por 0, vai abrir uma caixa de mensagem dizendo que não é possível dividir por zero.
        messagebox.showinfo("Divisão por 0", "Não é possível dividir por 0!")
        calculoOperacoes = ""
        textoentrada.set(calculoOperacoes)
    
#Botão de igual.
botao_igual = Button(janela, text="=",
                border=5,
                foreground="black",
                background="#BBB",
                font="Arial 20 bold",
                command=funcaoigual).grid(row=5,column=2, columnspan=3 ,sticky="NSEW")  

janela.mainloop()