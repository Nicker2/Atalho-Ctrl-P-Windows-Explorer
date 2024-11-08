import pyautogui
import keyboard
import time
import pygetwindow as gw
import psutil

# Verificação de instalação do psutil
try:
    import psutil
except ImportError:
    print("psutil não está instalado. Instale com 'pip install psutil'.")
    exit(1)

def is_explorer_open_and_focused():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'explorer.exe':
            return True
    return False

def maximize_active_window():
    """Maximiza a janela ativa"""
    try:
        window = gw.getActiveWindow()
        if window is not None:
            print(f"Maximizando a janela: {window.title}")
            window.maximize()
        else:
            print("Nenhuma janela ativa encontrada.")
    except Exception as e:
        print(f"Erro ao maximizar a janela: {e}")

def wait_for_window(window_title, timeout=30):
    """Espera a janela com o título especificado aparecer, com um timeout"""
    start_time = time.time()
    while True:
        if window_title in [w.title for w in gw.getAllWindows() if w.visible]:
            print(f"Janela '{window_title}' encontrada.")
            return True

        if time.time() - start_time > timeout:
            print(f"Tempo limite de {timeout} segundos atingido. A janela '{window_title}' não foi encontrada. Não fará nada e aguardará outro Ctrl+P.")
            return False

        time.sleep(0.5)

def click_pixel_and_move():
    print("Maximizando a janela ativa...")
    maximize_active_window()

    # Aguarda 0.1 segundos para garantir que a janela seja maximizada
    time.sleep(0.1)

    print("Iniciando o processo de clique e movimentação do mouse...")

    # Clica no pixel 85x13
    pyautogui.click(x=85, y=13)
    print("Clique realizado em 85x13.")

    # Calcula o centro da tela
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width // 2, screen_height // 2
    pyautogui.moveTo(center_x, center_y)
    print(f"Cursor movido para o centro da tela: ({center_x}, {center_y}).")

    # Espera pela janela "Imprimir Imagens" com timeout
    if not wait_for_window("Imprimir Imagens"):
        return

    time.sleep(0.2)
    pyautogui.click(x=965, y=404)
    pyautogui.press('enter')
    print("Clique em 'Imprimir Imagens' e pressionamento de Enter realizado.")

    # Espera pela janela "Salvar Saída de Impressão como" com timeout
    if not wait_for_window("Salvar Saída de Impressão como"):
        return

    time.sleep(0.5)

    # Verifica o estado do Caps Lock
    caps_was_on = keyboard.is_pressed('caps lock')
    print(f"Caps Lock estava {'ativado' if caps_was_on else 'desativado'}.")

    if caps_was_on:
        keyboard.press_and_release('caps lock')
        print("Caps Lock desativado.")

    # Digita o nome do arquivo
    pyautogui.typewrite("BIOMETRIA - PACIENTE - FUNCIONARIO.pdf")
    print("Nome do arquivo digitado.")

    if caps_was_on:
        keyboard.press_and_release('caps lock')
        print("Caps Lock restaurado para o estado original.")

def main():
    print("Aguardando Ctrl+P. O programa maximizará a janela ativa, aguardará 0.1s e clicará no pixel 85x13.")
    
    # Adiciona a hotkey Ctrl+P
    keyboard.add_hotkey('ctrl+p', lambda: click_pixel_and_move() if is_explorer_open_and_focused() else print("Windows Explorer não está aberto ou não está em primeiro plano. Não fará nada."))

    keyboard.wait()  # Espera indefinidamente

if __name__ == "__main__":
    main()
