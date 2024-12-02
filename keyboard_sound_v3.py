import pygame
from pynput import keyboard

# Initialize Pygame mixer
pygame.mixer.init()

# Load sounds
press_sound = pygame.mixer.Sound("./01_mech_keyboard_sound/enter.wav")
release_sound = pygame.mixer.Sound("./01_mech_keyboard_sound/enter-up.wav")

# Flag to track if Ctrl key is being pressed
ctrl_pressed = False
# Dictionary to track if a key is already pressed (to avoid continuous sound)
key_pressed = {}

def on_press(key):
    global ctrl_pressed
    # Check if Ctrl is pressed
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        ctrl_pressed = True
    
    # Avoid playing sound continuously for the same key press
    if hasattr(key, 'char') and key.char and key.char not in key_pressed:
        key_pressed[key.char] = True
        press_sound.play()
    elif hasattr(key, 'name') and key.name not in key_pressed:
        key_pressed[key.name] = True
        press_sound.play()

def on_release(key):
    global ctrl_pressed
    release_sound.play()
    
    # Exit when Ctrl + Esc is pressed
    if key == keyboard.Key.esc and ctrl_pressed:
        print("Ctrl + Esc pressed. Exiting...")
        return False  # Exit the listener
    
    # Reset the Ctrl key press state when released
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        ctrl_pressed = False
    
    # Reset key press state when the key is released
    if hasattr(key, 'char') and key.char:
        if key.char in key_pressed:
            del key_pressed[key.char]
    elif hasattr(key, 'name'):
        if key.name in key_pressed:
            del key_pressed[key.name]

# Set up the listener for keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Press Ctrl + Esc to exit.")
    listener.join()
