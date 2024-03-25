import matplotlib.pyplot as plt
import numpy as np
import os
import colorsys


def snakeillusiongeneretor(pattern, num_of_patterns, background, colors, shift_angel,flipped_colors, pattern2,g1_color,g2_color): # g1_color & g2_color are here in order to name the images

    sizes = pattern * num_of_patterns
    sizes2 = pattern2 * num_of_patterns
    # inner_r = np.array([1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1])  # changed form 0.1 intervalls 10 total
    inner_r = np.array(np.linspace(1, 0.03, num=9))
    inner_r = inner_r * 2
    dis = 2
    # create outer pie chart
    fig, ax = plt.subplots(figsize=(19.20, 10.80))

    x = 2
    # right circle
    startangle = 90
    for rad in range(len(inner_r)):
        startangle = startangle + shift_angel

        ax.pie(sizes, colors=colors, radius=inner_r[rad], center=(x, 0), startangle=startangle)

    ax.pie([1], colors=[background], radius=inner_r[8], center=(x, 0))
    # left (flipped) circle
    for rad in range(len(inner_r)):
        startangle = startangle + shift_angel
        ax.pie(sizes2, colors=flipped_colors, radius=inner_r[rad], center=(-x, 0), startangle=startangle)
    ax.pie([1], colors=[background], radius=inner_r[8], center=(-x, 0))
    ax.autoscale()
    fig.patch.set_facecolor(background)

    # set limits of the x and y axes to crop the image
    a = 2.5
    plt.xlim([-a, a])
    plt.ylim([-a, a])


    # display the chart
    plt.show(center=(0, 0))
    folder_path = f'C:\\' # change the output folder to save the images accordingly
    fig_name = f'gray, {pattern}.png' # set the image name
    fig.savefig(os.path.join(folder_path, fig_name))




gray_width = 1  # the width of an original segment

shift_angel = -12.5  # how each pie chart is rotated
num_of_patterns = 24 # numer of patterns in a single snake cycle

g1_color = (0.7,0.7,0.7) # 0 - 1 (black - white)
g2_color = (0.7,0.7,0.7) # 0 - 1 (black - white)

colors = ['black', g1_color, 'white', g2_color] * 10
flipped_colors = ['black', g2_color, 'white', g1_color] * 10
background = (0.5,0.5,0.5)

g2_list = [1]
g1_list = [3.5, 3.4, 3.25, 3, 2.5, 2, 1.9, 1.8, 1.75, 0.5, 0.4, 0.25, 0.1]


for g1 in g1_list: # selecting all possible combinations
    for g2 in g2_list:
        pattern2 = [1, g1, 1, g2]
        pattern1 = [1, g2, 1, g1]

        snakeillusiongeneretor(pattern1, num_of_patterns, background, colors, shift_angel,flipped_colors,pattern2,g1_color,g2_color) # sending all the relevant parameters in order to create a snake illusion
