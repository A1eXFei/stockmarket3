# -*- coding: UTF-8 -*-
import os


def export(dir, filename, data):

    if data.shape[0] > 0:
        if not os.path.exists(dir):
            os.makedirs(dir)
        data.to_csv(dir + os.sep + filename, index=False)
