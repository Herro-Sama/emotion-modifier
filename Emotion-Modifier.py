import sys
import random
import pygame
from pygame.locals import *


# Just a small script that returns an emotion into the console.
# The emotions being used are .

emotions = ['Absorbed',
'Abhorrence',
'Acceptance',
'Admiration',
'Adoration',
'Adrift',
'Aching',
'Affection',
'Afraid',
'Agitated',
'Agony',
'Aggravated',
'Alarm',
'Alert',
'Alienated',
'Alive',
'Alone',
'Amazed',
'Amused',
'Anger',
'Angst',
'Animated',
'Animosity',
'Animus',
'Annoyed',
'Antagonistic',
'Anticipation',
'Antipathy',
'Antsy',
'Anxiety',
'Apathetic',
'Apologetic',
'Appalled',
'Appreciative',
'Apprehensive',
'Ardor',
'Arousal',
'Astonishment',
'Astounded',
'Attachment',
'Attraction',
'Aversion',
'Awe',
'Awkward',
'Baffled',
'Bashful',
'Befuddled',
'Bemused',
'Betrayed',
'Bewildered',
'Bitter',
'Blessed',
'Bliss',
'Blithe',
'Blue',
'Bold',
'Bonhomie',
'Boredom',
'Bothered',
'Bouncy',
'Brave',
'Breathless',
'Brooding',
'Bubbly',
'Buoyant',
'Burning',
'Calm',
'Captivated',
'Carefree',
'Caring',
'Cautious',
'Certain',
'Chagrin',
'Challenged',
'Chary',
'Cheerful',
'Choked',
'Choleric',
'Clueless',
'Cocky',
'Cold',
'Collected',
'Comfortable',
'Commiseration',
'Committed',
'Compassionate',
'Complacent',
'Complaisance',
'Composed',
'Compunction',
'Confused',
'Courage',
'Concerned',
'Confident',
'Conflicted',
'Consternation',
'Contemplative',
'Contempt',
'Contentment',
'Contrition',
'Cordial',
'Cowardly',
'Crafty',
'Cranky',
'Craving',
'Crestfallen',
'Cross',
'Cruel',
'Crummy',
'Crushed',
'Curious',
'Cynical',
'Defeated',
'Dejection',
'Delectation',
'Delighted',
'Delirious',
'Denial',
'Derisive',
'Desire',
'Desolation',
'Despair',
'Despondent',
'Detached',
'Determined',
'Detestation',
'Devastated',
'Devotion',
'Disappointed',
'Disbelief',
'Disdain',
'Disgruntled',
'Disgust',
'Disillusioned',
'Disinterested',
'Dismay',
'Distaste',
'Distracted',
'Distress',
'Disturbed',
'Doleful',
'Dopey',
'Doubtful',
'Down',
'Downcast',
'Drained',
'Dread',
'Dubious',
'Dumbfounded',
'Eager',
'Earnest',
'Ease',
'Ebullient',
'Ecstatic',
'Edgy',
'Elated',
'Embarrassment',
'Empathic',
'Empty',
'Enchantment',
'Energetic',
'Engrossed',
'Enjoyment',
'Enlightenment',
'Enmity',
'Entertainment',
'Enthralled',
'Enthusiasm',
'Envy',
'Euphoria',
'Exasperated',
'Excitement',
'Excluded',
'Exhausted',
'Exhilaration',
'Expectant',
'Exuberant',
'Fanatical',
'Fascinated',
'Fatigued',
'Feisty',
'Felicitous',
'Fervor',
'Flabbergasted',
'Floored',
'Fondness',
'Foolish',
'Foreboding',
'Fortunate',
'Frazzled',
'Free',
'Fretful',
'Frightened',
'Frustrated',
'Fulfilled',
'Furious',
'Genial',
'Giddy',
'Glad',
'Gleeful',
'Gloomy',
'Goofy',
'Gratified',
'Grateful',
'Greedy',
'Grief',
'Groggy',
'Grudging',
'Guarded',
'Guilt',
'Gung-ho',
'Gusto',
'Hankering',
'Happy',
'Harassed',
'Hatred',
'Heartache',
'Heartbroken',
'Helpless',
'Hesitant',
'Hollow',
'Homesick',
'Hopeful',
'Horrified',
'Hostile',
'Humiliated',
'Humored',
'Hurt',
'Hyper',
'Hysterical',
'Impatient',
'Incensed',
'Indifferent',
'Indignant',
'Infatuated',
'Inferior',
'Inspired',
'Intense',
'Interested',
'Intimacy',
'Intimidated',
'Intoxicated',
'Intrigued',
'Introspective',
'Invigorated',
'Irascible',
'Ire',
'Irritated',
'Isolated',
'Jaded',
'Jealous',
'Jittery',
'Jocular',
'Jocund',
'Jolly',
'Jovial',
'Joy',
'Jubilant',
'Jumpy',
'Keen',
'Lazy',
'Left out',
'Lethargic',
'Liberation',
'Lighthearted',
'Liking',
'Listless',
'Lively',
'Lonely',
'Longing',
'Lost',
'Love',
'Lucky',
'Lust',
'Mad',
'Meditative',
'Melancholic',
'Mellow',
'Merry',
'Miffed',
'Mirth',
'Mischievous',
'Miserable',
'Mollified',
'Mortified',
'Motivated',
'Mournful',
'Moved',
'Mystified',
'Nasty',
'Nauseous',
'Needy',
'Nervous',
'Neutral',
'Nonplussed',
'Nostalgic',
'Numb',
'Obsessed',
'Offended',
'Optimistic',
'Outrage',
'Overwhelmed',
'Pacified',
'Pain',
'Panic',
'Paranoid',
'Passion',
'Pathetic',
'Peaceful',
'Peevish',
'Pensive',
'Perky',
'Perplexed',
'Perturbed',
'Pessimistic',
'Petrified',
'Petty',
'Petulant',
'Phlegmatic',
'Pity',
'Playful',
'Pleasure',
'Positive',
'Possessive',
'Powerful',
'Powerless',
'Preoccupied',
'Protective',
'Proud',
'Psyched',
'Pumped',
'Puzzled',
'Quizzical',
'Rage',
'Rapture',
'Rattled',
'Reassured',
'Receptive',
'Reflective',
'Regret',
'Relaxed',
'Relief',
'Relish',
'Reluctance',
'Remorse',
'Repugnance',
'Resentment',
'Resignation',
'Restless',
'Revolted',
'Sad',
'Sanguine',
'Satisfied',
'Scandalized',
'Scorn',
'Secure',
'Self-Conscious',
'Selfish',
'Sensual',
'Sensitive',
'Serendipitous',
'Serene',
'Settled',
'Shaken',
'Shame',
'Sheepish',
'Shock',
'Shy',
'Sick',
'Silly',
'Sincere',
'Skeptical',
'Sluggish',
'Smug',
'Snappy',
'Solemn',
'Solicitous',
'Somber',
'Sore',
'Sorrow',
'Sorry',
'Sour',
'Speechless',
'Spiteful',
'Sprightly',
'Stirred',
'Stressed',
'Strong',
'Stung',
'Stunned',
'Stupefied',
'Submissive',
'Succor',
'Suffering',
'Suffocated',
'Sullen',
'Sunny',
'Superior',
'Sure',
'Surprised',
'Startled',
'Sympathy',
'Tenderness',
'Tense',
'Terror',
'Testy',
'Tetchy',
'Thankful',
'Thirst',
'Thoughtful',
'Thrill',
'Timid',
'Tired',
'Titillation',
'Tormented',
'Torn',
'Torture',
'Touched',
'Traumatized',
'Tranquil',
'Trepidation',
'Triumphant',
'Troubled',
'Trust',
'Twitchy',
'Upbeat',
'Upset',
'Uptight',
'Vehement',
'Vexation',
'Vigilant',
'Vindication',
'Vindictive',
'Warmth',
'Wary',
'Weak',
'Weary',
'Welcome',
'Woe',
'Wonder',
'Woozy',
'Worry',
'Wrath',
'Wretched',
'Yearning',
'Zeal',
'Zest']

result = random.randint(0, (len(emotions)-1))

pygame.init()

clock = pygame.time.Clock()

width = 800
height = 600

black = (0, 0, 0)
white = (255, 255, 255)

selecing = False

textFont = pygame.font.SysFont(None, 36)

textToDisplay = textFont.render(str(emotions[result]), True, black)

offset = len(emotions[result]) * 2

window = pygame.display.set_mode((width, height))

background = pygame.image.load('Background.gif')
handleUp = pygame.image.load('Handle.gif')
handleDown = pygame.image.load('HandleDown.gif')

pygame.display.set_caption("Emotional Roulette")

while True:
    keysPressed = pygame.key.get_pressed()

    window.fill(white)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    if keysPressed[K_SPACE]:
        selecing = True
        result = random.randint(0, (len(emotions)-1))
        textToDisplay = textFont.render(str(emotions[result]), True, black)
        offset = textToDisplay.get_rect().width
    if selecing:
        window.blit(handleDown, (0, 0))

    else:
        window.blit(handleUp, (0, 0))

    selecing = False
    window.blit(background, (0, 0))
    window.blit(textToDisplay, ((width - offset)/2, (height/2 - 18)))
    pygame.display.update()
    clock.tick(100)
