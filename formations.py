import tkinter as tk

def format_celular(entry):
    celular = entry.get()
    formatted_celular = ''.join(celular.split()).replace('.','').replace('-','')
    if not formatted_celular.isdigit():
        formatted_celular = ''.join(filter(str.isdigit, formatted_celular))
    if len(formatted_celular) > 11:
        formatted_celular = formatted_celular[:11]
    if len(formatted_celular) == 11:
        formatted_celular = f'({formatted_celular[:2]}) {formatted_celular[2:7]}-{formatted_celular[7:11]}'
    entry.delete(0, tk.END)
    entry.insert(0, formatted_celular)
    entry.bind("<FocusOut>", lambda event: formatted_celular)
    entry.bind("<FocusIn>", lambda event: formatted_celular)

def format_cpf(entry):
    cpf_text = entry.get()    
    formatted_cpf = ''.join(cpf_text.split()).replace('.', '').replace('-', '')    
    if not formatted_cpf.isdigit():
        formatted_cpf = ''.join(filter(str.isdigit, formatted_cpf))
    if len(formatted_cpf) > 11:        
        formatted_cpf = formatted_cpf[:11]    
    if len(formatted_cpf) == 11:       
        formatted_cpf = f'{formatted_cpf[:3]}.{formatted_cpf[3:6]}.{formatted_cpf[6:9]}-{formatted_cpf[9:12]}'    
    entry.delete(0, tk.END)
    entry.insert(0, formatted_cpf)
    entry.bind("<FocusOut>", lambda event: formatted_cpf)
    entry.bind("<FocusIn>", lambda event: formatted_cpf)

def format_nome(entry):
    nome_text = entry.get()
    formatted_nome = nome_text.title()
    entry.delete(0, tk.END)
    entry.insert(0, formatted_nome)
    entry.bind("<FocusOut>", lambda event: formatted_nome)
    entry.bind("<FocusIn>", lambda event: formatted_nome)

def format_email(entry):
    email_text = entry.get()  
    entry.delete(0, tk.END)
    entry.insert(0, email_text)
    entry.bind("<FocusOut>", lambda event: email_text)
    entry.bind("<FocusIn>", lambda event: email_text)


def placeholder_cpf(entry):
    if entry.get() == 'Digite apenas números':
        entry.delete(0, "end")    
    entry.insert(0, 'Digite apenas números')
    entry.bind("<FocusIn>", lambda event: entry.delete(0, "end"))        
    entry.bind("<KeyRelease>", lambda event: format_cpf(entry))
    

def placeholder_celular(entry):
    entry.insert(0, 'Digite apenas números')
    entry.bind("<FocusIn>", lambda event: entry.delete(0, "end"))        
    entry.bind("<KeyRelease>", lambda event: format_celular(entry))

def placeholder_nome(entry):
    entry.insert(0, 'Nome')
    entry.bind("<FocusIn>", lambda event: entry.delete(0, "end"))        
    entry.bind("<KeyRelease>", lambda event: format_nome(entry))

def placeholder_sobrenome(entry):
    entry.insert(0, 'Sobrenome ou apelido')
    entry.bind("<FocusIn>", lambda event: entry.delete(0, "end"))        
    entry.bind("<KeyRelease>", lambda event: format_nome(entry))

def placeholder_email(entry):
    entry.insert(0, 'Digite o e-mail')
    entry.bind("<FocusIn>", lambda event: entry.delete(0, "end"))        
    entry.bind("<KeyRelease>", lambda event: format_email(entry))
    



