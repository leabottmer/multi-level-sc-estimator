#############
# Libraries #
#############

import scipy.io
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import ray
import time
import itertools
import cvxpy as cp
import random
from scipy.linalg import block_diag

#########################################
# Helper functions for estimating error #
#########################################

# Error between observed and estimated value
def e(X, Y, weights):
    Y= Y.ravel()
    return (Y-X.T @ weights.value)
# Mean error between observed and estimated value 
def e_mean(X, Y, weights):
    Y= Y.ravel()
    return np.mean(Y-X.T @ weights.value)
# Mean squared error between observed and estimated value 
def mse(X, Y, weights):
    Y= Y.ravel()
    return np.mean((Y-X.T @ weights.value)**2)

#############################
# Helper Functions for mlSC #
#############################

# Loss function
def loss_fn(control_vals, target, weights):
    """
    Standard squared error loss.
    control_vals: (num_controls, T)
    target: (T,)
    weights: cvxpy variable of shape (num_controls,)
    """
    pred = control_vals.T @ weights  # shape (T,)
    return cp.sum_squares(target - pred)

# Constrained objective function
def obj_func_constr(weights, control_vals, target, lambd, Q, var_y_est):
    """
    Full SC objective with vectorized penalty.
    lambd: nonnegative scalar (cvxpy Parameter or float)
    Q: precomputed penalty matrix
    """
    return loss_fn(control_vals, target, weights) + lambd *var_y_est* cp.quad_form(weights, Q)

# Build matrix for penalty term
def build_penalty_matrix(v_sc_list):
    """
    Precompute block-diagonal penalty matrix Q for all states.

    v_sc_list: list of arrays, each array is v_s for an aggregate unit s, where v_s are the population weights for units within aggregate unit s
    Returns: Q (numpy array)
    """
    blocks = []
    for v in v_sc_list:
        v = v.reshape(-1, 1)  # column vector
        ones = np.ones((1, len(v)))
        M_s = np.eye(len(v)) - v @ ones
        Q_s = M_s.T @ M_s
        blocks.append(Q_s)
    return block_diag(*blocks)
