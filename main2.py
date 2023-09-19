co1 = "#f5f5f5"
# Criar a janela principal
root = tk.Tk()
root.title("Empresa Filial")
root.configure(background=co1)
root.geometry("700x600")
root.resizable(True, True)
root.maxsize(width=900, height=900)
root.minsize(width=600, height=600)

# Validando entrada salario
def validar_entrada_salario(event):
    texto = event.widget.get()
    
    # Remove todos os caracteres não numéricos, vírgulas e pontos
    novo_texto = re.sub(r'[^0-9]', '', texto)
    
    # Insere vírgulas e pontos para formatar o número
    if len(novo_texto) >= 3:
        novo_texto = novo_texto[:-2] + '.' + novo_texto[-2:]
    if len(novo_texto) >= 7:
        novo_texto = novo_texto[:-6] + '.' + novo_texto[-6:]
    if len(novo_texto) >= 11:
        novo_texto = novo_texto[:-8] + ',' + novo_texto[-8:]
    
    event.widget.delete(0, tk.END)
    event.widget.insert(0, novo_texto)

# Validando entrada data
def validar_data(event):
    texto = event.widget.get()
    novo_texto = re.sub(r'[^0-9]', '', texto)  # Remove todos os caracteres não numéricos
    if len(novo_texto) > 8:
        novo_texto = novo_texto[:8]

    if len(novo_texto) >= 2:
        novo_texto = novo_texto[:2] + '/' + novo_texto[2:]
    if len(novo_texto) >= 5:
        novo_texto = novo_texto[:5] + '/' + novo_texto[5:]

    event.widget.delete(0, tk.END)
    event.widget.insert(0, novo_texto)
    
    try:
        data = datetime.strptime(novo_texto, '%d/%m/%Y')
        ano_atual = datetime.now().year
        if data.year <= ano_atual:
            resultado.config(text="Data válida")
            data_valida = True  # Define como verdadeiro se a data for válida
        else:
            data_valida = False  # Define como falso se a data for um ano futuro
    except ValueError:
        data_valida = False  # Define como falso se a data for inválida
    
# Validador para remover, números e caracteres especiais
def validar_entrada(event):
    texto = event.widget.get()
    novo_texto = re.sub(r'[^a-zA-Z\s]', '', texto)
    event.widget.delete(0, tk.END)
    event.widget.insert(0, novo_texto)

# Criar rótulos e campos de entrada Nome
nome_label = tk.Label(root, text="Nome:", font="Helvetica 12")
nome_label.place(relx=0.02, rely=0.04)
nome_entry = tk.Entry(root, font="Helvetica 12", width=25)
nome_entry.place(relx=0.02, rely=0.09)
nome_entry.bind('<KeyRelease>', validar_entrada)

# Criar rótulos e campos de entrada Funcoes
funcoes_label = tk.Label(root, text="Funcoes:",font="Helvetica 12")
funcoes_label.place(relx=0.02, rely=0.17)
funcoes_entry = tk.Entry(root, font="Helvetica 12", width=25)
funcoes_entry.place(relx=0.02, rely=0.22)
funcoes_entry.bind('<KeyRelease>', validar_entrada)

# Criar rótulos e campos de entrada Demanda
demanda_label = tk.Label(root, text="Demanda:",font="Helvetica 12")
demanda_label.place(relx=0.42, rely=0.04)
demanda_entry = tk.Entry(root,font="Helvetica 12", width=25)
demanda_entry.place(relx=0.42, rely=0.09)
demanda_entry.bind('<KeyRelease>', validar_entrada)

# Criar rótulos e campos de entrada Servicos
servico_label = tk.Label(root, text="Servico:", font="Helvetica 12")
servico_label.place(relx=0.42, rely=0.18)
servico_entry = tk.Entry(root, font="Helvetica 12", width=25)
servico_entry.place(relx=0.42, rely=0.23)
servico_entry.bind('<KeyRelease>', validar_entrada)

# Criar rótulos e campos de entrada Cidade
cidade_label = tk.Label(root, text="Cidade:", font="Helvetica 12")
cidade_label.place(relx=0.02, rely=0.30)
cidade_entry = tk.Entry(root, font="Helvetica 12", width=25)
cidade_entry.place(relx=0.02, rely=0.35)
cidade_entry.bind('<KeyRelease>', validar_entrada)

# Criar rótulos e campos de entrada Salario
salario_label = tk.Label(root, text="Salario:", font="Helvetica 12")
salario_label.place(relx=0.42, rely=0.30)
salario_entry = tk.Entry(root, font="Helvetica 12", width=25)
salario_entry.place(relx=0.42, rely=0.35)
salario_entry.bind('<KeyRelease>', validar_entrada_salario)

# Criar rótulos e campos de entrada Data Contratação
data_contrata_label = tk.Label(root, text="Data Contratação:", font="Helvetica 12")
data_contrata_label.place(relx=0.02, rely=0.41)
data_contrata_entry = tk.Entry(root, font="Helvetica 12", width=25)
data_contrata_entry.place(relx=0.02, rely=0.45)
data_contrata_entry.bind('<KeyRelease>', validar_data)

# Botão Limpar
def clear():
    nome_entry.delete(0, 'end')
    funcoes_entry.delete(0, 'end')
    demanda_entry.delete(0, 'end')
    servico_entry.delete(0, 'end')
    cidade_entry.delete(0, 'end')
    salario_entry.delete(0, 'end')
    data_contrata_entry.delete(0, 'end')

# Botão para inserir dados
inserir_button = tk.Button(root, width=10, text="Inserir Dados", activebackground='gray', font="Helvetica 11",command=inserir_dados)
inserir_button.place(relx=0.03, rely=0.93)

# Configurar a função clear como comando para o botão "Inserir Dados"
inserir_button.config(command=lambda: [inserir_dados(), clear()])

# Botão para sair
sair_button = tk.Button(root, width=10, text="Sair", activebackground='gray', font="Helvetica 11", command=sair)
sair_button.place(relx=0.19, rely=0.93)

# Criar o Treeview
tree = ttk.Treeview(root, columns=('Nome', 'Funcoes', 'Demanda', 'Servico', 'Cidade', 'Salario', 'data_contrata'), show='headings')
tree.heading('Nome', text='Nome')
tree.heading('Funcoes', text='Funcoes')
tree.heading('Demanda', text='Demanda')
tree.heading('Servico', text='Servico')
tree.heading('Cidade', text='Cidade')
tree.heading('Salario', text='Salario')
tree.heading('data_contrata', text='Data contratação')

# Configurar a largura das colunas
tree.column('Nome', width=90)
tree.column('Funcoes', width=90)
tree.column('Demanda', width=90)
tree.column('Servico', width=90)
tree.column('Cidade', width=90)
tree.column('Salario', width=90)
tree.column('data_contrata', width=100)


# Colocar o Treeview na interface
tree.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.4)

root.mainloop()
# Insert para inclusão na tabela do DB
# if __name__ == "__main__":
#     filial = Filial()
#     filial.insert("ppaola", "Suporte", "Atendimentos", "Procurar falhas", "Petrolandia")
