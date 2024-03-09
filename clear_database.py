from django.apps import apps
from django.db import connection
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mooney.base")
django.setup()


def clear_database():
    print("Limpando o banco de dados...")
    with connection.cursor() as cursor:
        cursor.execute("BEGIN;")
        for model in apps.get_models():
            table_name = model._meta.db_table
            print(f"Removendo tabela {table_name}...")
            cursor.execute(f"DROP TABLE IF EXISTS \"{table_name}\" CASCADE;")
        cursor.execute("COMMIT;")


if __name__ == "__main__":
    confirm = input(
        "Isso irá DESTRUIR todos os dados. Deseja continuar? (y/n): ")
    if confirm.lower() == 'y':
        clear_database()
        print("Banco de dados limpo.")
    else:
        print("Operação cancelada.")
