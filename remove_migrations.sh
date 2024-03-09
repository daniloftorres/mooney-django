#!/bin/bash

#chmod +x remove_migrations.sh
#./remove_migrations.sh

echo "Procurando e removendo arquivos de migração..."

# Encontra e remove arquivos de migração Python, exceto __init__.py
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

echo "Arquivos de migração removidos."
