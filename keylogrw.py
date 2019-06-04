from pynput import keyboard

def on_press(key):
    print("Pressed key : ", format(key))

def on_release(key):
    print("Released key : ", format(key))
with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()
)
