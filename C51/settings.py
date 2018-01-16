
ENV = "LunarLander-v2"

LOAD = False
DISPLAY = True
GUI = True

CONV = False

DISCOUNT = 0.99
NB_ATOMS = 51
MIN_VALUE = -100
MAX_VALUE = 100

LEARNING_RATE = 7.5e-4


FRAME_SKIP = 0
BUFFER_SIZE = 100000
BATCH_SIZE = 64

# Number of episodes of game environment to train with
TRAINING_STEPS = 100000
PRE_TRAIN_STEPS = 1

# Maximal number of steps during one episode
MAX_EPISODE_STEPS = 200
TRAINING_FREQ = 4

# Rate to update target network toward primary network
UPDATE_TARGET_RATE = 0.1


EPSILON_START = 0.8
EPSILON_STOP = 0.01
EPSILON_STEPS = 5000
EPSILON_DECAY = (EPSILON_START - EPSILON_STOP) / EPSILON_STEPS

# Display Frequencies
EP_REWARD_FREQ = 10
PLOT_FREQ = 25
RENDER_FREQ = 50
GIF_FREQ = 75
SAVE_FREQ = 0

MAX_NB_GIF = 5
GIF_PATH = 'results/gif/'
EP_ELONGATION = 0
