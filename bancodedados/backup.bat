REM Este script realiza backup de um banco de dados SQLite.
REM
REM Dependencias:
REM - SQLite3: O script depende do utilitario sqlite-tools-win-x64 (https://www.sqlite.org/download.html) Certifique-se de que esta instalado e acessivel no sistema.
REM
REM Use o comando 'setx' para criar ou modificar as variaveis de ambiente.
REM (O comando deve ser executado como administrador.)
REM   setx /m APP_DB_DSN "C:\.controleestoque\banco.db"
REM 
REM  APP_DB_DSN - Variavel do caminho do banco de dados(caminho absoluto). ex:  C:\.controleestoque\banco.db
REM  APP_BACKUP_FOLDER - Variavel do diretorio de saida do backup. ex: C:\.controleestoque\backup\
REM  APP_FOLDER - Variavel do diretorio de instalacao do aplicativo. ex: C:\Program Files (x86)\Controle de Estoque\
@echo off
set year=%date:~-4%
set month=%date:~4,1%
set day=%date:~0,2%

set hour=%time:~0,2%
set min=%time:~3,2%

REM realiza o paddind do mes
if %month% lss 10 set month=0%month%

REM Verifica se as variaveis de ambiente foram definidas

if "%APP_FOLDER%" equ "" (
    echo Error: Variavel nao definida.
    goto :eof
)

if "%APP_BACKUP_FOLDER%" equ "" (
    echo Error: Variavel nao definida.
    goto :eof
)

if "%APP_DB_DSN%" equ "" (
    echo Error: Variavel nao definida.
    goto :eof
)
REM Mudando para o diretorio do script
cd "%APP_FOLDER%bancodedados\"

REM Executa o comando SQLite para realizar o backup
sqlite3 %APP_DB_DSN% ".backup '%APP_BACKUP_FOLDER%banco_%year%%month%%day%_%hour%%min%bkp.db'"

REM Cria uma tarefa agendada no Windows para realizar o backup periodicamente
REM /tn: Nome da tarefa
REM /sc: Periodicidade de execução [HOURLY] por hora
REM /st e /et: Hora de início e término da tarefa
REM /tr: Especifica o programa ou comando a ser executado
REM /du: Duração da tarefa [HHHH:MM]
REM /mo: Especifica a frequência com que a tarefa é executada 
REM
REM Exemplo de agendamento:
REM schtasks /create /tn "backup_controle_estoque" /tr "'%APP_FOLDER%bancodedados\backup.bat'" /sc HOURLY /st 08:00 /mo 4"
REM 
REM Comando para testar a tarefa agendada:
REM schtasks /run /tn "backup_controle_estoque"

