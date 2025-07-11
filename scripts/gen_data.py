#!/usr/bin/python3
# coding=utf-8
#
# Copyright (C) 2023-2024. Huawei Technologies Co., Ltd. All rights reserved.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# ===============================================================================

import numpy as np


def gen_golden_data_simple():
    input_x = np.random.uniform(1, 100, [8, 2048]).astype(np.float16)
    input_y = np.random.uniform(1, 100, [8, 2048]).astype(np.float16)
    golden = (input_x + input_y).astype(np.float16)

    input_x.tofile("/root/MyProject/addKernelDemo/clion_out/input/input_x.bin")
    input_y.tofile("/root/MyProject/addKernelDemo/clion_out/input/input_y.bin")
    golden.tofile("/root/MyProject/addKernelDemo/clion_out/output/golden.bin")


if __name__ == "__main__":
    gen_golden_data_simple()
