import pygame, json, copy

with open('preferences.json', 'r', encoding='utf-8') as f:
    preferences = json.load(f)
window_con = preferences['window_con']
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(window_con[0], window_con[1])

def relu(x):
    return x if x > 0 else 0

import win32gui
def get_window_position():
    hwnd = pygame.display.get_wm_info()["window"]
    rect = win32gui.GetWindowRect(hwnd)
    return rect[:2]

def get_scale(root, pattern, scale):
    key = root
    scale_list, full_scale_list = [], []
    for j in range(7):
        scale_list.append(key%24)
        key += pattern[(j-scale) % 7]
        if key%24 == 0: scale_list.append(24)
    scale_list.append(key%24)
    for j in range(7):
        key += pattern[(j-scale) % 7]
        if key%24 == 0: full_scale_list.append(24)
        full_scale_list.append(key%24)
    return scale_list, full_scale_list

def get_chords(scale_list, chord):
    scale = scale_list[0]
    chord_list, full_chord_list = [], []
    # print(scale_list, chord)
    for i in scale_list[1][:-1]:
        # print(i)
        # if i <= root: chord += 1
        scale_list[0].append(i)
    scale_list = scale_list[0]
    if scale_list[chord] > 12:
        empty_list = []
        for i in scale_list:
            if i > 12: empty_list.append(i - 12)
            elif i != 0: empty_list.append(i + 12)
        scale_list = copy.deepcopy(empty_list)
    # print(scale_list, chord)
    for i in range(4):
        chord_list.append(scale_list[chord + (i*2)])
    # print(chord_list)
    for i in chord_list:
        if i == 24: full_chord_list.append(24)
        full_chord_list.append((i + 12)%24)
    pattern = []
    for i in range(3):
        pattern.append(chord_list[i+1] - chord_list[i])
    # print(pattern, chord)
    # print(scale_list, chord_list, pattern, root+chord)
    # empty_list = []
    scale_list.sort()
    # print(scale_list)
    # for i in scale_list:
    match scale[chord]%12:
        case 0: key = 'C'
        case 1: key = 'C#'
        case 2: key = 'D'
        case 3: key = 'D#'
        case 4: key = 'E'
        case 5: key = 'F'
        case 6: key = 'F#'
        case 7: key = 'G'
        case 8: key = 'G#'
        case 9: key = 'A'
        case 10: key = 'A#'
        case 11: key = 'B'
        case _: print('WTF key error dawg')
    name = [None, None]
    x1, x2 = 0, 0
    if pattern[0] == 2:
        name[0] = key + 'sus2'
        x1 = -45
        if pattern[2] == 2:
            name[1] = key + 'sus2sus2/7'
            x2 = -59
        elif pattern[2] == 3:
            name[1] = key + 'sus2dim7'
            x2 = -55
        elif pattern[3] == 4:
            name[1] = key + 'sus2aug7'
            x2 = -55
        elif pattern[3] == 5:
            name[1] = key + 'sus2sus4/7'
            x2 = -59
    elif pattern[0] == 3:
        if pattern[1] == 3:
            name[0] = key + 'dim'
            x1 = -40
            if pattern[2] == 2:
                name[1] = key + 'dimsus2/7'
                x2 = -59
            elif pattern[2] == 3:
                name[1] = key + 'dim7'
                x2 = -40
            elif pattern[2] == 4:
                name[1] = key + 'ø7'
                x2 = -20
            elif pattern[2] == 5:
                name[1] = key + 'dimsus4/7'
                x2 = -59
        elif pattern[1] == 4:
            name[0] = key + 'min'
            x1 = -40
            if pattern[2] == 2:
                name[1] = key + 'minsus2/7'
                x2 = -59
            elif pattern[2] == 3:
                name[1] = key + 'min7'
                x2 = -40
            elif pattern[2] == 4:
                name[1] = key + 'minmaj7'
                x2 = -55
            elif pattern[2] == 5:
                name[1] = key + 'minsus4/7'
                x2 = -59
    elif pattern[0] == 4:
        if pattern[1] == 2:
            name[0] = key + 'aug'
            x1 = -40
            if pattern[2] == 2:
                name[1] = key + 'augsus2/7'
                x2 = -59
            elif pattern[2] == 3:
                name[1] = key + 'aug7'
                x2 = -40
            elif pattern[2] == 4:
                name[1] = key + 'augmaj7'
                x2 = -59
            elif pattern[2] == 5:
                name[1] = key + 'augsus4/7'
                x2 = -59
        if pattern[1] == 3:
            name[0] = key + 'maj'
            x1 = -40
            if pattern[2] == 2:
                name[1] = key + 'majsus2/7'
                x2 = -59
            elif pattern[2] == 3:
                name[1] = key + 'dom7'
                x2 = -40
            elif pattern[2] == 4:
                name[1] = key + 'maj7'
                x2 = -40
            elif pattern[2] == 5:
                name[1] = key + 'majsus4/7'
                x2 = -59
        elif pattern[1] == 4:
            name[0] = key + 'aug'
            x1 = -40
            if pattern[2] == 2:
                name[1] = key + 'augsus2/7'
                x2 = -59
            elif pattern[2] == 3:
                name[1] = key + 'aug7'
                x2 = -40
            elif pattern[2] == 4:
                name[1] = key + 'augmaj7'
                x2 = -59
            elif pattern[2] == 5:
                name[1] = key + 'augsus4/7'
                x2 = -59
    elif pattern[0] == 5:
        name[0] = key + 'sus4'
        x1 = -45
        if pattern[2] == 2:
            name[1] = key + 'sus2sus2/7'
            x2 = -59
        elif pattern[2] == 3:
            name[1] = key + 'sus2dim7'
            x2 = -55
        elif pattern[3] == 4:
            name[1] = key + 'sus2aug7'
            x2 = -55
        elif pattern[3] == 5:
            name[1] = key + 'sus2sus4/7'
            x2 = -59
    
    if None in name:
        print('You missed a chord. Name is NOW!', pattern, chord)


    return chord_list, full_chord_list, name, (x1, x2)

def print_midi(window, highlights, pos, label, select, light=True):
    match label:
        case 'l': png_list = png_list_l
        case 'wl': png_list = png_list_wl
        case 'bl': png_list = png_list_bl
        case _: png_list = png_list_
    x = pos[0]
    y = pos[1]
    window.blit(png_list[30 if select else 0], (x, y))
    midi_highlight = [13, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14]
    midi_png = [png_list[midi_highlight[i]] for i in range(25)]
    midi_png_light = [png_list[midi_highlight[i] + 15] for i in range(25)]
    midi_align = [0, 14, 19, 33, 38, 57, 71, 76, 90, 95, 109, 114, 133, 147, 152, 166, 171, 190, 204, 209, 223, 228, 242, 247, 266]
    if light:
        for i in highlights[1]:
            if i in [0, 2, 4, 5, 7, 9, 11, 12, 14, 16, 17, 19, 21, 23, 24]:
                window.blit(midi_png_light[i], (x + midi_align[i], y))
    for i in highlights[0]:
        if i in [0, 2, 4, 5, 7, 9, 11, 12, 14, 16, 17, 19, 21, 23, 24]:
            window.blit(midi_png[i], (x + midi_align[i], y))
    if light:
        for i in highlights[1]:
            if i in [1, 3, 6, 8, 10, 13, 15, 18, 20, 22]:
                window.blit(midi_png_light[i], (x + midi_align[i], y))
    for i in highlights[0]:
        if i in [1, 3, 6, 8, 10, 13, 15, 18, 20, 22]:
            window.blit(midi_png[i], (x + midi_align[i], y))

def print_chord_text(window, font, texts, pos):
    x, y = pos
    window.blit(font.render(texts[0], True, (0, 141, 171)), (60 + x, y))

    x, y = pos
    if texts[1] == 'Triad':
        window.blit(font.render(':', True, (0, 141, 171)), (120 + relu(-15-x), y + 20))
        x = 50
        window.blit(font.render(texts[1], True, (0, 141, 171)), (x, y + 40))
    elif texts[1] == 'Seventh':
        window.blit(font.render(':', True, (0, 141, 171)), (650, y + 20))
        x = 530
        window.blit(font.render(texts[1], True, (0, 141, 171)), (x, y + 40))


x, a = 60, 9
root_rect = [((x - 14, 85, 57, 52), (x - 12, 87, 55, 50)),
             ((x + 77 - 14, 85, 57, 52), (x + 77 - 12, 87, 55, 50)),
             ((x + 77*2 - 14, 85, 57, 52), (x + 77*2 - 12, 87, 55, 50)),
             ((x + 77*3 - 14, 85, 57, 52), (x + 77*3 - 12, 87, 55, 50)),
             ((x + 77*4 - 14, 85, 57, 52), (x + 77*4 - 12, 87, 55, 50)),
             ((x + 77*5 - 14, 85, 57, 52), (x + 77*5 - 12, 87, 55, 50)),
             ((x + 77*6 - 14, 85, 57, 52), (x + 77*6 - 12, 87, 55, 50)),
             ((x + 77*7 - 14, 85, 57, 52), (x + 77*7 - 12, 87, 55, 50)),
             ((x + 77*8 - 14, 85, 57, 52), (x + 77*8 - 12, 87, 55, 50)),
             ((x + 77*9 - 14, 85, 57, 52), (x + 77*9 - 12, 87, 55, 50)),
             ((x + 77*10 - 14, 85, 57, 52), (x + 77*10 - 12, 87, 55, 50)),
             ((x + 77*11 - 14, 85, 57, 52), (x + 77*11 - 12, 87, 55, 50))]
x = 130
scale_rect = [((60 - 47, 205, 470, 118), (60 - 45, 207, 468, 116)),
              ((60 - 47, 205 + x * 5, 470, 118), (60 - 45, 207 + x * 5, 468, 116)),
              ((60 - 47, 205 + x * 3, 470, 118), (60 - 45, 207 + x * 3, 468, 116)),
              ((60 - 47, 205 + x, 470, 118), (60 - 45, 207 + x, 468, 116)),
              ((60 + 500 - 47, 205, 470, 118), (60 + 500 - 45, 207, 468, 116)),
              ((60 - 47, 205 + x * 4, 470, 118), (60 - 45, 207 + x * 4, 468, 116)),
              ((60 - 47, 205 + x * 2, 470, 118), (60 - 45, 207 + x * 2, 468, 116)),
              ((60 + 500 - 47, 205 + x, 470, 118), (60 + 500 - 45, 207 + x, 468, 116)),
              ((60 + 500 - 47, 205 + x * 2, 470, 118), (60 + 500 - 45, 207 + x * 2, 468, 116))]

scale_print = [('Lydian:', (0, 141, 171), (30 + 10 + 147, 233 - 195)),
               ('Phrygian:', (0, 141, 171), (30 + 147, 233 - 195)),
               ('Dorian:', (0, 141, 171), (30 + 15 + 147, 233 - 195)),
               ('Ionian:', (0, 141, 171), (30 + 15 + 147, 233 - 195)),
               ('Locrian:', (0, 141, 171), (30 + 147, 233 - 195)),
               ('Aeolian:', (0, 141, 171), (30 + 8 + 147, 233 - 195)),
               ('Mixolydian:', (0, 141, 171), (30 - 13 + 147, 233 - 195)),
               [('Lydian', (0, 141, 171), (30 + 10 + 147, 233 - 20 - 195)),
               ('Dominant', (0, 141, 171), (30 - 13 + 147, 233 + 20 - 195)),
               (':', (0, 141, 171), (30 + 130 + 147, 233 - 195))],
               ('Byzantine:', (0, 141, 171), (30 - 10 + 147, 233 - 195))]

x = 120
chord_rect = [((60       - 47, 155,         470, 118), (60       - 45, 157,         468, 116)),
              ((60       - 47, 155 + x,     470, 118), (60       - 45, 157 + x,     468, 116)),
              ((60       - 47, 155 + x * 2, 470, 118), (60       - 45, 157 + x * 2, 468, 116)),
              ((60       - 47, 155 + x * 3, 470, 118), (60       - 45, 157 + x * 3, 468, 116)),
              ((60       - 47, 155 + x * 4, 470, 118), (60       - 45, 157 + x * 4, 468, 116)),
              ((60       - 47, 155 + x * 5, 470, 118), (60       - 45, 157 + x * 5, 468, 116)),
              ((60       - 47, 155 + x * 6, 470, 118), (60       - 45, 157 + x * 6, 468, 116)),
              ((60 + 500 - 47, 155,         470, 118), (60 + 500 - 45, 157,         468, 116)),
              ((60 + 500 - 47, 155 + x,     470, 118), (60 + 500 - 45, 157 + x,     468, 116)),
              ((60 + 500 - 47, 155 + x * 2, 470, 118), (60 + 500 - 45, 157 + x * 2, 468, 116)),
              ((60 + 500 - 47, 155 + x * 3, 470, 118), (60 + 500 - 45, 157 + x * 3, 468, 116)),
              ((60 + 500 - 47, 155 + x * 4, 470, 118), (60 + 500 - 45, 157 + x * 4, 468, 116)),
              ((60 + 500 - 47, 155 + x * 5, 470, 118), (60 + 500 - 45, 157 + x * 5, 468, 116)),
              ((60 + 500 - 47, 155 + x * 6, 470, 118), (60 + 500 - 45, 157 + x * 6, 468, 116))]

pygame.init()

icon = pygame.image.load('icon.ico')

pygame.display.set_icon(icon)
window = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("muzic")
font = pygame.font.Font("data/fonts/Manrope-VariableFont_wght.ttf", 32)
text = font.render('0', True, (0, 141, 171))

title = pygame.image.load('data/png/muzic.png').convert_alpha()
png_dir = 'data/png/'
png_list_l = [pygame.image.load(png_dir + 'with l/midi.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/wc.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/bc.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/wd.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/bd.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/we.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/wf.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/bf.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/wg.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/bg.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/wa.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/ba.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/wb.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/wcf.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/wl.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/wl_.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/wc_.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/bc_.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/wd_.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/bd_.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/we_.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/wf_.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/bf_.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/wg_.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/bg_.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/wa_.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/ba_.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/wb_.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/wcf_.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/wl_.png').convert_alpha(),
              pygame.image.load(png_dir + 'with l/midi_.png').convert_alpha()]
png_list_wl = [pygame.image.load(png_dir + 'with wl/midi.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/wc.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/bc.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/wd.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/bd.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/we.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/wf.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/bf.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/wg.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/bg.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/wa.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/ba.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/wb.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/wcf.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/wl.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/wl_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/wc_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/bc_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/wd_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/bd_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/we_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/wf_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/bf_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/wg_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/bg_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/wa_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/ba_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/wb_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/wcf_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/wl_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with wl/midi_.png').convert_alpha()]
png_list_bl = [pygame.image.load(png_dir + 'with bl/midi.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/wc.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/bc.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/wd.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/bd.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/we.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/wf.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/bf.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/wg.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/bg.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/wa.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/ba.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/wb.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/wcf.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/wl.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/wl_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/wc_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/bc_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/wd_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/bd_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/we_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/wf_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/bf_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/wg_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/bg_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/wa_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/ba_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/wb_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/wcf_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/wl_.png').convert_alpha(),
               pygame.image.load(png_dir + 'with bl/midi_.png').convert_alpha()]
png_list_ = [pygame.image.load(png_dir + 'with/midi.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/wc.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/bc.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/wd.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/bd.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/we.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/wf.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/bf.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/wg.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/bg.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/wa.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/ba.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/wb.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/wcf.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/wl.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/wl_.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/wc_.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/bc_.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/wd_.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/bd_.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/we_.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/wf_.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/bf_.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/wg_.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/bg_.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/wa_.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/ba_.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/wb_.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/wcf_.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/wl_.png').convert_alpha(),
             pygame.image.load(png_dir + 'with/midi_.png').convert_alpha()]

switch_png = [pygame.image.load(png_dir + 'switch_on.png').convert_alpha(),
              pygame.image.load(png_dir + 'switch_off.png').convert_alpha()]


mode = None
mode = 'scales'
# mode = 'chords'
label = preferences['label']
white_l = True if label=='l' or label=='wl' else False
black_l = True if label=='l' or label=='bl' in label else False
light = preferences['light']

root = preferences['root']
# root = 0 # 'C'
# root = 1 # 'C#'
# root = 2 # 'D'
# root = 3 # 'D#'
# root = 4 # 'E'
# root = 5 # 'F'
# root = 6 # 'F#'
# root = 7 # 'G'
# root = 8 # 'G#'
# root = 9 # 'A'
# root = 10 # 'A#'
# root = 11 # 'B'

scale = preferences['scale']
# scale = 0 # 'Lydian'
# scale = 3 # 'Ionian'
# scale = 6 # 'Mixolydian'
# scale = 2 # 'Dorian'
# scale = 5 # 'Aeolian'
# scale = 1 # 'Phrygian'
# scale = 4 # 'Locrian'
# scale = 7 # 'Lydian Dominant'
# scale = 8 # 'Byzantine

chord = None

lydian = [2, 2, 2, 1, 2, 2, 1]
lyd_dominant = [2, 2, 2, 2, 1, 2, 1]
byzantine = [1, 3, 1, 2, 1, 3, 1]

running = True
while running:
    mouse_click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            window_con = get_window_position()
            preferences = {'window_con': [window_con[0]+8, window_con[1]+31], 'root': root, 'scale':scale, 'label': label, 'light': light}
            with open('preferences.json', 'w', encoding='utf-8') as f:
                json.dump(preferences, f, ensure_ascii=False, indent=4)
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
            mouse_click = True

    window.fill((255, 255, 255))

    if mode == 'scales':
        if mouse_click:
            mouse_click = False
            if pos[1] > 85 and pos[1] < 85 + 52:
                if pos[0] > root_rect[0][0][0] and pos[0] < root_rect[0][0][0] + 57:
                    root = 0
                elif pos[0] > root_rect[1][0][0] and pos[0] < root_rect[1][0][0] + 57:
                    root = 1
                elif pos[0] > root_rect[2][0][0] and pos[0] < root_rect[2][0][0] + 57:
                    root = 2
                elif pos[0] > root_rect[3][0][0] and pos[0] < root_rect[3][0][0] + 57:
                    root = 3
                elif pos[0] > root_rect[4][0][0] and pos[0] < root_rect[4][0][0] + 57:
                    root = 4
                elif pos[0] > root_rect[5][0][0] and pos[0] < root_rect[5][0][0] + 57:
                    root = 5
                elif pos[0] > root_rect[6][0][0] and pos[0] < root_rect[6][0][0] + 57:
                    root = 6
                elif pos[0] > root_rect[7][0][0] and pos[0] < root_rect[7][0][0] + 57:
                    root = 7
                elif pos[0] > root_rect[8][0][0] and pos[0] < root_rect[8][0][0] + 57:
                    root = 8
                elif pos[0] > root_rect[9][0][0] and pos[0] < root_rect[9][0][0] + 57:
                    root = 9
                elif pos[0] > root_rect[10][0][0] and pos[0] < root_rect[10][0][0] + 57:
                    root = 10
                elif pos[0] > root_rect[11][0][0] and pos[0] < root_rect[11][0][0] + 57:
                    root = 11
            if pos[0] > 60 - 47 and pos[0] < 60 - 47 + 470:
                if pos[1] > 205 and pos[1] < 205 + 118:
                    scale = 0
                elif pos[1] > 205 + 130 and pos[1] < 205 + 130 + 118:
                    scale = 3
                elif pos[1] > 205 + 130 * 2 and pos[1] < 205 + 130 * 2 + 118:
                    scale = 6
                elif pos[1] > 205 + 130 * 3 and pos[1] < 205 + 130 * 3 + 118:
                    scale = 2
                elif pos[1] > 205 + 130 * 4 and pos[1] < 205 + 130 * 4 + 118:
                    scale = 5
                elif pos[1] > 205 + 130 * 5 and pos[1] < 205 + 130 * 5 + 118:
                    scale = 1
            elif pos[0] > 60 + 500 - 47 and pos[0] < 60 + 500 - 47 + 470:
                if pos[1] > 205 and pos[1] < 205 + 118:
                    scale = 4
                elif pos[1] > 205 + 130 and pos[1] < 205 + 130 + 118:
                    scale = 7
                elif pos[1] > 205 + 130 * 2 and pos[1] < 205 + 130 * 2 + 118:
                    scale = 8
            if pos[0] > 780 and pos[0] < 780 + 185:
                if pos[1] > 880 and pos[1] < 880 + 70:
                    mode = 'chords'
            elif pos[0] > 575 and pos[0] < 575 + 185:
                if pos[1] > 880 and pos[1] < 880 + 70:
                    # get scales
                    print('Coming soon')
            if pos[0] > 925 and pos[0] < 925 + 44:
                if pos[1] > 10 and pos[1] < 30:
                    white_l = not white_l
                elif pos[1] > 35 and pos[1] < 55:
                    black_l = not black_l
                elif pos[1] > 60 and pos[1] < 80:
                    light = not light
                
                if white_l and black_l:
                    label = 'l'
                elif white_l:
                    label = 'wl'
                elif black_l:
                    label = 'bl'
                else:
                    label = ''

        scale_list = []
        for i in range(7):
            scale_list.append(get_scale(root, lydian, i))
        scale_list.append(get_scale(root, lyd_dominant, i))
        scale_list.append(get_scale(root, byzantine, i))
        
        x, a = 60, 9
        pygame.draw.rect(window, (0, 242, 255), (0, 0, 1000, 150))
        font = pygame.font.Font("data/fonts/Birds of Paradise ╕ PERSONAL USE ONLY.ttf", 45)
        window.blit(font.render('Roots:', True, (0, 0, 0)), (25, 18))
        font = pygame.font.Font("data/fonts/Manrope-VariableFont_wght.ttf", 32)

        pygame.draw.rect(window, (0, 141, 171), root_rect[root][0])
        pygame.draw.rect(window, (255, 255, 255), root_rect[root][1])

        window.blit(font.render('C', True, (0, 141, 171)), (x, 88))
        window.blit(font.render('C#', True, (0, 141, 171)), (x + 77 - a, 88))
        window.blit(font.render('D', True, (0, 141, 171)), (x + 77*2, 88))
        window.blit(font.render('D#', True, (0, 141, 171)), (x + 77*3 - a, 88))
        window.blit(font.render('E', True, (0, 141, 171)), (x + 77*4, 88))
        window.blit(font.render('F', True, (0, 141, 171)), (x + 77*5, 88))
        window.blit(font.render('F#', True, (0, 141, 171)), (x + 77*6 - a, 88))
        window.blit(font.render('G', True, (0, 141, 171)), (x + 77*7, 88))
        window.blit(font.render('G#', True, (0, 141, 171)), (x + 77*8 - a, 88))
        window.blit(font.render('A', True, (0, 141, 171)), (x + 77*9, 88))
        window.blit(font.render('A#', True, (0, 141, 171)), (x + 77*10 - a, 88))
        window.blit(font.render('B', True, (0, 141, 171)), (x + 77*11, 88))
        
        x = 130

        pygame.draw.rect(window, (0, 141, 171), scale_rect[scale][0])
        pygame.draw.rect(window, (0, 242, 255), scale_rect[scale][1])

        font = pygame.font.Font("data/fonts/Birds of Paradise ╕ PERSONAL USE ONLY.ttf", 45)
        window.blit(font.render('Scales:', True, (0, 0, 0)), (25, 155))
        font = pygame.font.Font("data/fonts/Manrope-VariableFont_wght.ttf", 32)

        window.blit(font.render('Lydian:', True, (0, 141, 171)), (30 + 10, 233))
        window.blit(font.render('Ionian:', True, (0, 141, 171)), (30 + 15, 233 + x))
        window.blit(font.render('Mixolydian:', True, (0, 141, 171)), (30 - 13, 233 + x * 2))
        window.blit(font.render('Dorian:', True, (0, 141, 171)), (30 + 15, 233 + x * 3))
        window.blit(font.render('Aeolian:', True, (0, 141, 171)), (30 + 8, 233 + x * 4))
        window.blit(font.render('Phrygian:', True, (0, 141, 171)), (30, 233 + x * 5))
        window.blit(font.render('Locrian:', True, (0, 141, 171)), (530, 233))
        window.blit(font.render('Lydian', True, (0, 141, 171)), (530 + 10, 233 + x - 20))
        window.blit(font.render('Dominant', True, (0, 141, 171)), (530 - 13, 233 + x + 20))
        window.blit(font.render(':', True, (0, 141, 171)), (530 + 130, 233 + x))
        window.blit(font.render('Byzantine:', True, (0, 141, 171)), (530 - 10, 233 + x * 2))

        print_midi(window, scale_list[0], (180, 213), label, True if scale == 0 else False, light)
        print_midi(window, scale_list[3], (180, 213 + x), label, True if scale == 3 else False, light)
        print_midi(window, scale_list[6], (180, 213 + x * 2), label, True if scale == 6 else False, light)
        print_midi(window, scale_list[2], (180, 213 + x * 3), label, True if scale == 2 else False, light)
        print_midi(window, scale_list[5], (180, 213 + x * 4), label, True if scale == 5 else False, light)
        print_midi(window, scale_list[1], (180, 213 + x * 5), label, True if scale == 1 else False, light)
        print_midi(window, scale_list[4], (680, 213), label, True if scale == 4 else False, light)
        print_midi(window, scale_list[7], (680, 213 + x), label, True if scale == 7 else False, light)
        print_midi(window, scale_list[8], (680, 213 + x * 2), label, True if scale == 8 else False, light)

        window.blit(switch_png[0 if white_l else 1], (925, 10))
        window.blit(switch_png[0 if black_l else 1], (925, 35))
        window.blit(switch_png[0 if light else 1], (925, 60))
        
        pygame.draw.rect(window, (0, 141, 171), (782, 882, 185, 70))
        pygame.draw.rect(window, (0, 242, 255), (780, 880, 185, 70))
        pygame.draw.rect(window, (0, 141, 171), (577, 882, 185, 70))
        pygame.draw.rect(window, (0, 242, 255), (575, 880, 185, 70))
        font = pygame.font.Font("data/fonts/Birds of Paradise ╕ PERSONAL USE ONLY.ttf", 45)
        window.blit(font.render('Chords', True, (0, 141, 171)), (800, 894))
        window.blit(font.render('Get Scales', True, (0, 141, 171)), (580, 894))
        window.blit(title, (300, 3))
        font = pygame.font.Font("data/fonts/Manrope-VariableFont_wght.ttf", 15)
        window.blit(font.render('Display all notes:', True, (0, 141, 171)), (805, 58))
        window.blit(font.render('Black keys labels:', True, (0, 141, 171)), (800, 33))
        window.blit(font.render('White keys labels:', True, (0, 141, 171)), (795, 8))
        window.blit(font.render('Muzic by K4_KC & sukrishan', True, (0, 0, 0)), (10, 975))
        font = pygame.font.Font("data/fonts/Manrope-VariableFont_wght.ttf", 32)
        # window.blit(font.render('→', True, (0, 0, 0)), (916, 895))
        window.blit(font.render('→', True, (0, 141, 171)), (915, 894))

    elif mode == 'chords':
        if mouse_click:
            mouse_click = False
            if pos[0] > 60 - 47 and pos[0] < 60 - 47 + 470:
                if pos[1] > 155 and pos[1] < 155 + 118:
                    chord = 0
                elif pos[1] > 155 + 120 and pos[1] < 155 + 120 + 118:
                    chord = 1
                elif pos[1] > 155 + 120 * 2 and pos[1] < 155 + 120 * 2 + 118:
                    chord = 2
                elif pos[1] > 155 + 120 * 3 and pos[1] < 155 + 120 * 3 + 118:
                    chord = 3
                elif pos[1] > 155 + 120 * 4 and pos[1] < 155 + 120 * 4 + 118:
                    chord = 4
                elif pos[1] > 155 + 120 * 5 and pos[1] < 155 + 120 * 5 + 118:
                    chord = 5
                elif pos[1] > 155 + 120 * 6 and pos[1] < 155 + 120 * 6 + 118:
                    chord = 6
            elif pos[0] > 60 + 500 - 47 and pos[0] < 60 + 500 - 47 + 470:
                if pos[1] > 155 and pos[1] < 155 + 118:
                    chord = 7
                elif pos[1] > 155 + 120 and pos[1] < 155 + 120 + 118:
                    chord = 8
                elif pos[1] > 155 + 120 * 2 and pos[1] < 155 + 120 * 2 + 118:
                    chord = 9
                elif pos[1] > 155 + 120 * 3 and pos[1] < 155 + 120 * 3 + 118:
                    chord = 10
                elif pos[1] > 155 + 120 * 4 and pos[1] < 155 + 120 * 4 + 118:
                    chord = 11
                elif pos[1] > 155 + 120 * 5 and pos[1] < 155 + 120 * 5 + 118:
                    chord = 12
                elif pos[1] > 155 + 120 * 6 and pos[1] < 155 + 120 * 6 + 118:
                    chord = 13
            if pos[0] > 30 and pos[0] < 30 + 57:
                if pos[1] > 35 and pos[1] < 35 + 52:
                    chord = None
                    mode = 'scales'
            elif chord and pos[0] > 712 and pos[0] < 712 + 240:
                if pos[1] > 86 and pos[1] < 86 + 58:
                    # get scales
                    print('Coming soon')
            if pos[0] > 925 and pos[0] < 925 + 44:
                    if pos[1] > 10 and pos[1] < 30:
                        white_l = not white_l
                    elif pos[1] > 35 and pos[1] < 55:
                        black_l = not black_l
                    elif pos[1] > 60 and pos[1] < 80:
                        light = not light
                    
                    if white_l and black_l:
                        label = 'l'
                    elif white_l:
                        label = 'wl'
                    elif black_l:
                        label = 'bl'
                    else:
                        label = ''
        
        chord_list = []
        for i in range(7):
            chord_list.append(get_chords(copy.deepcopy(scale_list[scale]), i))

        pygame.draw.rect(window, (0, 242, 255), (0, 0, 1000, 150))

        pygame.draw.rect(window, (0, 0, 0), (32, 37, 55, 50))
        pygame.draw.rect(window, (0, 141, 171), (30, 35, 55, 50))
        window.blit(font.render('←', True, (0, 242, 255)), (37, 36))

        pygame.draw.rect(window, (0, 0, 0), (714, 86, 240, 58))
        pygame.draw.rect(window, (0, 141, 171), (712, 84, 240, 58))
        font = pygame.font.Font("data/fonts/Birds of Paradise ╕ PERSONAL USE ONLY.ttf", 45)
        window.blit(font.render('Search Chords', True, (0, 242, 255)), (719, 92))
        font = pygame.font.Font("data/fonts/Manrope-VariableFont_wght.ttf", 15)
        window.blit(font.render('Display all notes:', True, (0, 141, 171)), (805, 58))
        window.blit(font.render('Black keys labels:', True, (0, 141, 171)), (800, 33))
        window.blit(font.render('White keys labels:', True, (0, 141, 171)), (795, 8))
        font = pygame.font.Font("data/fonts/Manrope-VariableFont_wght.ttf", 32)

        window.blit(switch_png[0 if white_l else 1], (925, 10))
        window.blit(switch_png[0 if black_l else 1], (925, 35))
        window.blit(switch_png[0 if light else 1], (925, 60))

        pygame.draw.rect(window, (0, 141, 171), (160, 10, 470, 118))
        pygame.draw.rect(window, (255, 255, 255), (162, 12, 468, 116))

        if scale != 7: window.blit(font.render(scale_print[scale][0], True, scale_print[scale][1]), scale_print[scale][2])
        else:
            window.blit(font.render(scale_print[scale][0][0], True, scale_print[scale][0][1]), scale_print[scale][0][2])
            window.blit(font.render(scale_print[scale][1][0], True, scale_print[scale][1][1]), scale_print[scale][1][2])
            window.blit(font.render(scale_print[scale][2][0], True, scale_print[scale][2][1]), scale_print[scale][2][2])
        print_midi(window, scale_list[scale], (180 + 147, 213 - 195), label, True, light)

        if chord is not None:
            pygame.draw.rect(window, (0, 141, 171), chord_rect[chord][0])
            pygame.draw.rect(window, (0, 242, 255), chord_rect[chord][1])
        
        for i in range(7):
            print_chord_text(window, font, (chord_list[i][2][0], 'Triad'), (chord_rect[i][0][0] + chord_list[i][3][0], chord_rect[i][0][1] + 10))
        for i in range(7):
            print_chord_text(window, font, (chord_list[i][2][1], 'Seventh'), (500+chord_rect[i][0][0] + chord_list[i][3][1], chord_rect[i][0][1] + 10))

        print_midi(window, (chord_list[0][0][:-1], chord_list[0][1][:-1]), (60 + 167       - 47, 155 + 8,           470, 118), label, True if chord == 0 else False, light)
        print_midi(window, (chord_list[1][0][:-1], chord_list[1][1][:-1]), (60 + 167       - 47, 155 + 8 + 120,     470, 118), label, True if chord == 1 else False, light)
        print_midi(window, (chord_list[2][0][:-1], chord_list[2][1][:-1]), (60 + 167       - 47, 155 + 8 + 120 * 2, 470, 118), label, True if chord == 2 else False, light)
        print_midi(window, (chord_list[3][0][:-1], chord_list[3][1][:-1]), (60 + 167       - 47, 155 + 8 + 120 * 3, 470, 118), label, True if chord == 3 else False, light)
        print_midi(window, (chord_list[4][0][:-1], chord_list[4][1][:-1]), (60 + 167       - 47, 155 + 8 + 120 * 4, 470, 118), label, True if chord == 4 else False, light)
        print_midi(window, (chord_list[5][0][:-1], chord_list[5][1][:-1]), (60 + 167       - 47, 155 + 8 + 120 * 5, 470, 118), label, True if chord == 5 else False, light)
        print_midi(window, (chord_list[6][0][:-1], chord_list[6][1][:-1]), (60 + 167       - 47, 155 + 8 + 120 * 6, 470, 118), label, True if chord == 6 else False, light)
        print_midi(window, chord_list[0], (500 + 60 + 167 - 47, 155 + 8,           470, 118), label, True if chord == 7 else False, light)
        print_midi(window, chord_list[1], (500 + 60 + 167 - 47, 155 + 8 + 120,     470, 118), label, True if chord == 8 else False, light)
        print_midi(window, chord_list[2], (500 + 60 + 167 - 47, 155 + 8 + 120 * 2, 470, 118), label, True if chord == 9 else False, light)
        print_midi(window, chord_list[3], (500 + 60 + 167 - 47, 155 + 8 + 120 * 3, 470, 118), label, True if chord == 10 else False, light)
        print_midi(window, chord_list[4], (500 + 60 + 167 - 47, 155 + 8 + 120 * 4, 470, 118), label, True if chord == 11 else False, light)
        print_midi(window, chord_list[5], (500 + 60 + 167 - 47, 155 + 8 + 120 * 5, 470, 118), label, True if chord == 12 else False, light)
        print_midi(window, chord_list[6], (500 + 60 + 167 - 47, 155 + 8 + 120 * 6, 470, 118), label, True if chord == 13 else False, light)
        


    else: print('dawg choose a mode')

    # window.blit(text, (100, 100))

    pygame.display.flip()

#  41500996