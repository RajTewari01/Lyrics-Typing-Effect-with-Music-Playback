from sys import stdout
import time
import itertools
from rich import print
from pygame import mixer

lyrics_list_5_words = [
    'This night is cold in',
    'the kingdom I can feel',
    'you fade away From the',
    'kitchen to the bathroom sink',
    'and Your steps keep me',
    'awake Don’t cut me down,',
    'throw me out, leave me',
    'here to waste I once',
    'was a man with dignity',
    'and grace Now I’m slippin’',
    'through the cracks of your',
    'cold embrace So please,',
    'please Could you find',
    'a way to let me',
    'down slowly? A little sympathy,',
    'I hope you can show',
    'me If you wanna go',
    'then I’ll be so lonely',
    'If you’re leavin’, baby, let',
    'me down slowly Let me',
    'down, down, let me down,',
    'down, let me down Let',
    'me down, down, let me',
    'down, down, let me down',
    'If you wanna go then',
    'I’ll be so lonely If',
    'you’re leavin’, baby, let me',
    'down slowly Cold skin,',
    'drag my feet on the',
    'tile As I’m walking down',
    'the corridor And I know',
    'we haven’t talked in a',
    'while So I’m lookin’ for',
    'an open door Don’t cut',
    'me down, throw me out,',
    'leave me here to waste',
    'I once was a man',
    'with dignity and grace',
    'Now I’m slippin’ through the',
    'cracks of your cold embrace',
    'So please, please Could you',
    'find a way to let',
    'me down slowly? A little',
    'sympathy, I hope you can',
    'show me If you wanna',
    'go then I’ll be so',
    'lonely If you’re leavin’, baby,',
    'let me down slowly Let',
    'me down, down, let me',
    'down, down, let me down',
    'Let me down, down, let',
    'me down, down, let me',
    'down If you wanna go',
    'then I’ll be so lonely',
    'If you’re leavin’, baby, let',
    'me down slowly And I',
    'can’t stop myself from fallin’',
    '(down) And I can’t stop',
    'myself from fallin’ (down) Could',
    'you find a way to',
    'let me down slowly? A',
    'little sympathy, I hope you',
    'can show me If you',
    'wanna go then I’ll be',
    'so lonely If you’re leavin’,',
    'baby, let me down slowly',
    'Let me down, down, let',
    'me down, down, let me',
    'down Let me down, down,',
    'let me down, down, let',
    'me down If you wanna',
    'go then I’ll be so',
    'lonely If you’re leavin’, baby,',
    'let me down slowly'
]



def word_by_word(lyrics,song,song_name):
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()
    print(f"[bold red]......{song_name.title()}.......[/bold red]",flush=False)
    time.sleep(3)
    stdout.flush()
    line_delay_values = [0.06, 0.04, 0.04, 0.06, 0.05, 0.06,0.04]
    colors=['red','blue','yellow','cyan']
    cycled_delays = itertools.cycle(line_delay_values)
    colo = itertools.cycle(colors)
    for i,j in zip(lyrics,colo):
        
        for k,l in zip(i,cycled_delays):
            print(f"[{j}]{k}[/{j}]",flush=False,end='',)
            time.sleep(l)
            stdout.flush()
        print()
        stdout.flush()
        time.sleep(0.8)
    mixer.music.stop()

        
       
word_by_word(lyrics_list_5_words,"D:/song/song.mp3",'let me down slowly')