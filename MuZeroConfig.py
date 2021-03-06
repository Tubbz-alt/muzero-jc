import os

from abc import ABC, abstractmethod
from Network import NetworkTypes

class MuZeroConfig(ABC):

    @abstractmethod
    def __init__(self,
                 action_space_size: int,
                 max_moves: int,
                 discount: float,
                 dirichlet_alpha: float,
                 num_simulations: int,
                 batch_size: int,
                 td_steps: int,
                 num_actors:int,
                 lr_init: float,
                 lr_decay_steps: float,
                 visit_softmax_temperature_fn):
        ### Self-Play
        self.action_space_size = action_space_size 
        self.num_actors = num_actors 

        self.visit_softmax_temperature_fn = visit_softmax_temperature_fn
        self.max_moves = max_moves 
        self.num_simulations = num_simulations 
        self.discount = discount 

        # Root prior exploration noise.
        self.root_dirichlet_alpha = dirichlet_alpha
        self.root_exploration_fraction = 0.25

        # UCB formula
        self.pb_c_base = 19652 
        self.pb_c_init = 1.25

        ### Training
        self.training_steps = int(1e6) 
        self.checkpoint_interval = int(1e3) 
        self.window_size = int(1e6) 
        self.batch_size = batch_size 
        self.num_unroll_steps = 20 
        self.td_steps = td_steps 

        self.weight_decay = 1e-4 
        self.momentum = 0.9 

        # Exponential learning rate schedule
        self.lr_init = lr_init 
        self.lr_decay_rate = 0.1 
        self.lr_decay_steps = lr_decay_steps

        # Type of Network
        self.network_type = NetworkTypes.fully_connected

        # Size of the "normalized" vector for the rewards
        self.support_size = 10
        
        # Size of the observation (State of the Game)
        self.observation_shape = ()
        
        # Number of previous moves to feed into the network
        self.move_history = 0

        # Fully Connected Network
        self.encoding_size = 32
        self.fc_representation_layers = []  # Define the hidden layers in the representation network
        self.fc_dynamics_layers = [16]  # Define the hidden layers in the dynamics network
        self.fc_reward_layers = [16]  # Define the hidden layers in the reward network
        self.fc_value_layers = []  # Define the hidden layers in the value network
        self.fc_policy_layers = []  # Define the hidden layers in the policy network
        dir_path = os.path.dirname(os.path.realpath(__file__)) 
        self.path = os.path.join(dir_path, 'store')


    @abstractmethod
    def new_game(self):
        pass
