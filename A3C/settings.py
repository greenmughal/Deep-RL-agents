
ENV = "Acrobot-v1"

DISPLAY = True
LOAD = False



FRAME_SKIP = 4

THREADS = 6
LIMIT_RUN_TIME = 360

EPSILON_START = 0.6
EPSILON_STOP = 0.01
EPSILON_STEPS = 1000
EPSILON_DECAY = (EPSILON_START - EPSILON_STOP) / EPSILON_STEPS

VALUE_REG = 0.05
ENTROPY_REG = 0.01

MAX_GRADIENT_NORM = 40
LEARNING_RATE = 5e-4

MAX_EPISODE_STEP = 2000
MAX_LEN_BUFFER = 64

DISCOUNT = 0.99
GENERALIZED_LAMBDA = 1

CONV = False
LAYERS_SIZE = [16, 16]

LSTM = True
LSTM_CELLS = 128

# Display Frequencies
DISP_EP_REWARD_FREQ = 50
PLOT_FREQ = 25000
RENDER_FREQ = 100

SAVE_FREQ = 10000
EP_ELONGATION = 50
