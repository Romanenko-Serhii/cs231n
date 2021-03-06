import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  num_classes = W.shape[1]
  num_train = X.shape[0]
  loss = 0.0
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  for i in range(num_train):
      scores = X[i].dot(W)
      exp_scores = np.exp(scores)
      exp_scores_norm = exp_scores/ np.sum(exp_scores)
      loss += -np.log(exp_scores_norm[y[i]])
      dscores = exp_scores_norm.copy()
      dscores[y[i]] -= 1
      for j in range(num_classes):
        dW[:,j] += X[i,:]*(dscores[j])
        dW[:,y[i]] -= X[i,:]*(dscores[j])
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################
  loss /= num_train
  dW /= num_train
  loss += reg * np.sum(W * W)
  dW += reg * W
  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  num_classes = W.shape[1]
  num_train = X.shape[0]
  index = np.arange(num_train)
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  scores = X.dot(W)
  exp_scores = np.exp(scores)
  exp_scores_sum = np.sum(exp_scores, axis=1)
  exp_scores_sum = np.expand_dims(exp_scores_sum, axis = 1)
  exp_scores_norm = exp_scores / exp_scores_sum
  loss = np.sum(-np.log(exp_scores_norm[index,y])) / num_train
  loss += reg * np.sum(W * W)

  dscores = exp_scores_norm.copy()
  dscores[index,y] -= 1
  dW = X.T.dot(dscores/num_train)
  dW += reg * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW
