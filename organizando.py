import os

def criandoDiretorios(caminho, diretorio):
    try:
        os.makedirs(f"{caminho}\\{diretorio}")
    except Exception as e:
        print(e)

    return 0

def verificaDir():
    caminho = "C:\\Users\\gsp37\\OneDrive\\Área de Trabalho\\teste"
    for root, _, files in os.walk(caminho):
        for file in files:
            filename, file_extension = os.path.splitext(f'{root}\\{file}')
            print(f'{root}\\{file}')
            folderName = file_extension.replace(".", "").capitalize()
            criandoDiretorios(caminho, folderName)

            file_path = f'{root}\\{file}'
            new_file_path = f"{caminho}\\{folderName}\\{file}"
            os.rename(file_path, new_file_path)

verificaDir()