REM Este script realiza backup de um banco de dados SQLite.
REM
REM Dependências:
REM - SQLite3: O script depende do utilitário sqlite-tools-win-x64 (https://www.sqlite.org/download.html) Certifique-se de que está instalado e acessível no sistema.
REM
REM Este script recebe dois parâmetros: 
REM   %1 - O primeiro parâmetro é o nome do arquivo de entrada(caminho absoluto). ex:  C:\.controleestoque\banco.db
REM   %2 - O segundo parâmetro é o diretório de saída. ex: C:\.controleestoque\
@echo off
set year=%date:~-4%
set month=%date:~4,1%
set day=%date:~0,2%

set hour=%time:~0,2%
set min=%time:~3,2%

REM realiza o paddind do mes
if %month% lss 10 set month=0%month%

REM Verifica se ambos os parâmetros foram fornecidos

if "%~1" equ "" (
    echo Error: Missing the first parameter.
    goto :eof
)

if "%~2" equ "" (
    echo Error: Missing the second parameter.
    goto :eof
)

REM Executa o comando SQLite para realizar o backup
sqlite3 %1 ".backup '%2%banco_year%%month%%day%_%hour%%min%bkp.db'"

REM Cria uma tarefa agendada no Windows para realizar o backup periodicamente
REM /tn: Nome da tarefa
REM /sc: Periodicidade de execução [HOURLY] por hora
REM /st e /et: Hora de início e término da tarefa
REM /tr: Especifica o programa ou comando a ser executado
REM
REM Exemplo de agendamento:
REM schtasks /create /tn "backup_controle_estoque" /tr backup.bat %1 %2 /sc HOURLY /st 18:00 /et 08:00

