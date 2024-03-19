import subprocess
import sys

def install_requirements(file='requirements.txt'):
    try:
        # Instala los paquetes utilizando pip y el archivo de requerimientos
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', file])
        print(f'Todos los requerimientos de {file} han sido instalados exitosamente.')
    except subprocess.CalledProcessError as e:
        print(f'Error al instalar los requerimientos de {file}. Detalles del error: {e}')

if __name__ == '__main__':
    install_requirements()
