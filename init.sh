#!/bin/bash

VENV_DIR="venv"
EXEC_CMD="fastapi run api.py "

echo "EJECUCIÓN INICIAL 'SI=S, NO=n'"
read SiNo

SiNo=$(echo "$SiNo" | tr '[:upper:]' '[:lower:]')

# Verificar si el entorno virtual ya existe
if [ ! -d "$VENV_DIR" ]; then
    echo "Creando entorno virtual..."
    python3 -m venv "$VENV_DIR"
fi

# Activar el entorno virtual
source "$VENV_DIR/bin/activate"

if [ "$SiNo" = "s" ]; then
    echo "Instalando dependencias..."
    pip install -r requirements.txt
    exit 0
else
    echo "Iniciando Servicio WHISPER API"
    echo "**** iniciado TMUX ****"

    tmux new-session -d -s $session
    tmux new-window -t $session:$term0 -n 'API-WHISPER'
    tmux send-keys -t $session:$term0 'sh app/'$sh1
    tmux send-keys -t $session:$term0 Enter
    $EXEC_CMD
    tmux send-keys -t $session:$term0 Enter
fi
