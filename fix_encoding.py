import codecs
import os

readme_path = "README.md"
backup_path = "README_backup.md"

if not os.path.exists(readme_path):
    print(f"Erro: O arquivo {readme_path} não foi encontrado.")
else:
    try:
        # Tenta ler o arquivo com a codificação atual (pode ser a que está bugando)
        with open(readme_path, 'r', encoding='utf-8') as f: # Mantemos utf-8 aqui, mas pode ser ajustado se suspeitarmos de outra encoding fonte
            content = f.read()

        # Faz um backup do arquivo original (apenas por segurança)
        if os.path.exists(backup_path):
             os.remove(backup_path)
        os.rename(readme_path, backup_path)

        # Escreve o conteúdo de volta no arquivo README.md, garantindo a codificação UTF-8
        with codecs.open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Arquivo {readme_path} re-salvo com codificação UTF-8. Backup criado em {backup_path}.")

    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo {readme_path}: {e}")