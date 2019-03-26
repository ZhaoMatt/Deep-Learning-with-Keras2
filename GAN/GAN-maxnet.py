import mxnet as mx
from mxnet.gluon import nn,data
import numpy as np

class GAN():
    def __init__(self):
        self.img_rows = 28
        self.img_cols = 28
        self.img_channels = 1
        self.img_shape=(self.img_rows, self.img_cols, self.img_channels)
        self.letent_dim = 10

        # build and compile desctiminator

        # build generator
        # fix discriminator
        # compile generator

    def build_discriminator(self):
        net = nn.Sequential()
        net.add()

    def build_generator(self):
        pass


