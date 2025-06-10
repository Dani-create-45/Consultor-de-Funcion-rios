import tkinter as tk
from tkinter import messagebox

# Dados dos funcionários
funcionarios = {
    1: {'CPF': '728.495.634-21', 'Nome': 'Carlos Mendes', 'Email': 'carlos.mendes@example.com', 'Cargo': 'Desenvolvedor', 'Projetos': ['Sistema de Vendas', 'App Mobile']},
    2: {'CPF': '581.930.472-38', 'Nome': 'Maria Oliveira', 'Email': 'maria.oliveira@empresa.com', 'Cargo': 'Analista de Dados', 'Projetos': ['Análise de Mercado', 'Relatórios BI']},
    3: {'CPF': '346.102.759-47', 'Nome': 'Carlos Oliveira', 'Email': 'carlos.oliveira@empresa.com', 'Cargo': 'Gerente de Projetos', 'Projetos': ['Implementação ERP', 'Infraestrutura']},
    4: {'CPF': '970.283.614-52', 'Nome': 'Ana Soarez', 'Email': 'ana.soarez@empresa.com', 'Cargo': 'Desenvolvedor', 'Projetos': ['Site Institucional', 'E-commerce']},
    5: {'CPF': '999.888.777-66', 'Nome': 'Pedro Lima', 'Email': 'pedro.lima@empresa.com', 'Cargo': 'Suporte Técnico', 'Projetos': ['Manutenção de Sistemas', 'Help Desk']},
    6: {'CPF': '204.587.913-68', 'Nome': 'Lucas Ferreira', 'Email': 'lucas.ferreira@empresa.com', 'Cargo': 'Analista de Segurança', 'Projetos': ['Segurança da Informação', 'Auditoria']},
    7: {'CPF': '389.471.256-73', 'Nome': 'Mariana Silva', 'Email': 'mariana.silva@empresa.com', 'Cargo': 'Desenvolvedor', 'Projetos': ['Aplicativo Financeiro', 'Plataforma Web']},
    8: {'CPF': '914.286.370-84', 'Nome': 'Emerson Nogueira', 'Email': 'emerson.nogueira@empresa.com', 'Cargo': 'Designer', 'Projetos': ['UI/UX do App', 'Identidade Visual']},
    9: {'CPF': '702.134.598-29', 'Nome': 'Beatriz Costa', 'Email': 'beatriz.costa@empresa.com', 'Cargo': 'Analista de Marketing', 'Projetos': ['Campanha Publicitária', 'SEO']},
    10: {'CPF': '518.726.903-57', 'Nome': 'Carlos Souza', 'Email': 'carlos.souza@empresa.com', 'Cargo': 'Administrador de Redes', 'Projetos': ['Infraestrutura de Rede', 'Segurança de Rede']}
}

# Funções de busca
def buscar_por_cpf(cpf):
    for f in funcionarios.values():
        if f['CPF'] == cpf:
            return f
    return None

def buscar_por_nome(nome):
    return [f for f in funcionarios.values() if f['Nome'].lower().startswith(nome.lower())]

def buscar_por_cargo(cargo):
    return [f for f in funcionarios.values() if f['Cargo'].lower() == cargo.lower()]

# Exibir funcionário formatado
def formatar_funcionario(f):
    return f"""
CPF: {f['CPF']}
Nome: {f['Nome']}
E-mail: {f['Email']}
Cargo: {f['Cargo']}
Projetos: {', '.join(f['Projetos'])}
"""

# Lógica de busca acionada pelos botões
def executar_busca(tipo):
    entrada_valor = campo_entrada.get().strip()
    if not entrada_valor:
        messagebox.showwarning("Campo vazio", "Digite algo para buscar.")
        return

    if tipo == "cpf":
        resultado = buscar_por_cpf(entrada_valor)
        texto = formatar_funcionario(resultado) if resultado else "Funcionário não encontrado."

    elif tipo == "nome":
        resultados = buscar_por_nome(entrada_valor)
        if resultados:
            texto = ""
            for f in resultados:
                texto += formatar_funcionario(f) + "\n" + "-"*30 + "\n"
        else:
            texto = "Nenhum funcionário encontrado com esse nome."

    elif tipo == "cargo":
        resultados = buscar_por_cargo(entrada_valor)
        if resultados:
            texto = ""
            for f in resultados:
                texto += formatar_funcionario(f) + "\n" + "-"*30 + "\n"
        else:
            texto = "Nenhum funcionário encontrado com esse cargo."

    campo_resultado.config(state="normal")
    campo_resultado.delete(1.0, tk.END)
    campo_resultado.insert(tk.END, texto)
    campo_resultado.config(state="disabled")

# Interface gráfica com tkinter
janela = tk.Tk()
janela.title("Consulta de Funcionários")
janela.geometry("700x500")

# Campo de entrada
tk.Label(janela, text="Digite CPF, Nome ou Cargo:").grid(row=0, column=0, padx=10, pady=5)
campo_entrada = tk.Entry(janela, width=50)
campo_entrada.grid(row=0, column=1, padx=10, pady=5)

# Botões
tk.Button(janela, text="Buscar por CPF", width=20, command=lambda: executar_busca("cpf")).grid(row=1, column=0, pady=5)
tk.Button(janela, text="Buscar por Nome", width=20, command=lambda: executar_busca("nome")).grid(row=1, column=1, pady=5)
tk.Button(janela, text="Buscar por Cargo", width=20, command=lambda: executar_busca("cargo")).grid(row=2, column=0, columnspan=2, pady=5)

# Área de resultados
campo_resultado = tk.Text(janela, height=20, width=80, state="disabled", wrap="word", font=("Courier", 10))
campo_resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

janela.mainloop()