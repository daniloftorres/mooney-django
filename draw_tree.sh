#!/bin/bash

# Lista de arquivos/diretórios para ignorar
declare -a EXCLUDE_LIST=("postgres-data" "static" "docs" "mooney/mooney/static" "mooney/static","migrations/","migrations")

draw_tree() {
    local file="$1"
    local indent="$2"
    local basefile=$(basename "$file")

    # Checa se o arquivo/diretório está na lista de exclusões
    for exclude in "${EXCLUDE_LIST[@]}"; do
        if [[ "$file" == *"$exclude"* || "$basefile" == "$exclude" ]]; then
            return
        fi
    done

    # Verifica se é um diretório
    if [ -d "$file" ]; then
        echo "$indent├── $(basename "$file")/"
        for child in "$file"/*; do
            draw_tree "$child" "$indent│   "
        done
    else
        echo "$indent└── $(basename "$file")"
    fi
}

# Obtém o diretório atual
directory="$(pwd)"

# Imprime a estrutura da árvore
draw_tree "$directory" ""
