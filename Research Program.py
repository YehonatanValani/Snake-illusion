import pyglet
from pyglet.window import key
import random
import os

# Get the available screens (monitors)
screens = pyglet.canvas.get_display().get_screens()
# Assuming you have 2 monitors, you can choose one by index (0 or 1)
chosen_screen = screens[1]  # Change the index as needed

# Set the window to resizable
window = pyglet.window.Window(fullscreen=True, resizable=True, screen=chosen_screen)
window_width, window_height = window.get_size()

Answers = []
image_timer = None
answer_given = False
pause_time = 4.5  # Time in seconds to show each image
opening_image = 'openning_image.png' # must be located in your main library
pause_image_path = 'pause_image.png'  # must be located in your main library
pause_image_path_2 = 'pause_image2.png'  # must be located in your main library
folder_path = "C:\\#enter the path to the folder with the images to examine#"

# Get a list of all image files in the folder
image_files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]

# Filter only image files based on their extensions
image_extensions = ['.png', '.jpg', '.jpeg']
image_paths = [os.path.join(folder_path, file) for file in image_files if os.path.splitext(file)[1].lower() in image_extensions]

# Get the directory path of the first image
if image_paths:
    images_directory = os.path.dirname(image_paths[0])
    research_answers_path = os.path.join(images_directory, "#Enter name of the participant# - Research Answers.txt")


# Shuffle the image paths to ensure randomness
random.shuffle(image_paths)

# Initialize current_image to opening_image
if image_paths:
    current_image_path = opening_image
    print(f'Showing the opening image: {current_image_path}')
    current_image = pyglet.image.load(current_image_path)


def start_image_timer():
    global image_timer
    image_timer = pause_time


def show_random_image():
    global current_image, image_paths, current_image_path, prev_img

    if image_paths:
        prev_img = current_image_path
        current_image_path = image_paths.pop(0)  # Selects new random image
        current_image = pyglet.image.load(current_image_path)
        start_image_timer()
    else:
        # No more images left
        save_answers() # Saves answer to TXT file
        pyglet.app.exit()


@window.event
def on_key_press(symbol, modifiers):
    global current_image, answer_given, image_paths, current_image_path, image_timer, prev_img

    if symbol == key.SPACE and current_image_path == opening_image:
        # Show the next random image
        show_random_image()
    elif (symbol == key.I or symbol == key.O) and current_image_path == pause_image_path:
        answer = 'Inward' if symbol == key.I else 'Outward'
        print(f'{answer} rotation')
        current_answer = f'Showing the image: {os.path.basename(prev_img)} - answer is: {answer}'
        Answers.append(current_answer)
        show_random_image()
    elif (symbol == key.I or symbol == key.O) and current_image_path != opening_image:
        image_timer = None
        answer = 'Inward' if symbol == key.I else 'Outward'
        print(f'{answer} rotation')
        current_answer = f'Showing the image: {os.path.basename(current_image_path)} - answer is: {answer}'
        Answers.append(current_answer)
        show_pause_image_2()

    elif symbol == key.SPACE and current_image_path == pause_image_path_2:
        # Show the next random image
        show_random_image()
    else:
        return


@window.event
def on_draw():
    window.clear()
    if current_image is not None:
        # Calculate scaling factors to fit the image within the window while preserving aspect ratio
        image_ratio = current_image.width / current_image.height
        window_ratio = window_width / window_height
        if image_ratio > window_ratio:
            scale = window_width / current_image.width
            draw_width = window_width
            draw_height = current_image.height * scale
            draw_y = (window_height - draw_height) / 2
            current_image.blit(0, draw_y, width=draw_width, height=draw_height)
        else:
            scale = window_height / current_image.height
            draw_width = current_image.width * scale
            draw_height = window_height
            draw_x = (window_width - draw_width) / 2
            current_image.blit(draw_x, 0, width=draw_width, height=draw_height)


def show_pause_image():
    global current_image, current_image_path
    current_image_path = pause_image_path
    current_image = pyglet.image.load(current_image_path)


def show_pause_image_2():
    global current_image, current_image_path
    current_image_path = pause_image_path_2
    current_image = pyglet.image.load(current_image_path)


def save_answers():
    with open(research_answers_path, mode='w') as f:
        f.write('\n'.join(Answers))


def update(dt):
    global image_timer, current_image, prev_img, current_image_path

    if image_timer is not None:
        image_timer -= dt
        if image_timer <= 0:
            image_timer = None
            prev_img = current_image_path
            show_pause_image()


pyglet.clock.schedule_interval(update, 1 / 60.0)  # Update timer every frame
pyglet.app.run()
