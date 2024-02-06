import sys
from cx_Freeze import setup, Executable

additional_folders = ['bancodedados', 'clientes', 'compra', 'estoque', 'financeiro', 'fornecedor', 'imagens', 'impressora', 'styles', 'trocas', 'vendas', 'functions']

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "excludes": [],
    "zip_include_packages": ["tkinter", "pyautogui", "dotenv", "unicode"],
    "include_files": additional_folders,
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="Controle de Estoque",
    version="1.9",
    description="My GUI application!",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)