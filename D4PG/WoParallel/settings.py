
ENV = "BipedalWalker-v2"

LOAD = False
DISPLAY = True
GUI = True

NB_ATOMS = 51
MIN_VALUE = -100
MAX_VALUE = 500

N_STEP_RETURN = 3
DISCOUNT = 0.99
DISCOUNT_N = DISCOUNT ** N_STEP_RETURN

# Memory settings
MEMORY_SIZE = 1000000
BATCH_SIZE = 64

# Learning rates
ACTOR_LEARNING_RATE = 5
CRITIC_LEARNING_RATE = 5


# Maximal number of steps during one episode
TRAINING_EPS = 1000000
MAX_EPISODE_STEPS = 500

# Rate to update target network toward primary network
TRAINING_FREQ = 1
UPDATE_TARGET_RATE = 0.05

NOISE_SCALE = 0.3
NOISE_DECAY = 0.99995


# Display Frequencies
EP_REWARD_FREQ = 50
PLOT_FREQ = 5000
RENDER_FREQ = 50
GIF_FREQ = 1000
SAVE_FREQ = 10000

MAX_NB_GIF = 50
GIF_PATH = 'results/gif/'
