import tkinter as tk

def format_cpf(entry):
    # Obtém o texto atual no Entry
    cpf_text = entry.get()

    # Remove espaços em branco, pontos e traços do CPF atual
    formatted_cpf = ''.join(cpf_text.split()).replace('.', '').replace('-', '')

        # Verifica se a string contém apenas números
    if not formatted_cpf.isdigit():
        formatted_cpf = ''.join(filter(str.isdigit, formatted_cpf))

    if len(formatted_cpf) > 11:
        # Limita o CPF a 11 dígitos
        formatted_cpf = formatted_cpf[:11]

    # Verifica se o CPF já está no formato correto
    if len(formatted_cpf) == 11:
        # Formata o CPF com pontos e traços
        formatted_cpf = f'{formatted_cpf[:3]}.{formatted_cpf[3:6]}.{formatted_cpf[6:9]}-{formatted_cpf[9:12]}'

    # Define o texto formatado no Entry
    entry.delete(0, tk.END)
    entry.insert(0, formatted_cpf)
