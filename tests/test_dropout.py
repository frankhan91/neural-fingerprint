import numpy as np
import numpy.random as npr
from deepmolecule.build_vanilla_net import dropout

def test_no_dropout_has_no_effect():
    weights = npr.randn(1000)
    dropout_weights = dropout(weights, 0)
    assert np.allclose(weights, dropout_weights)

def test_dropout_has_effect():
    weights = npr.randn(1000)
    dropout_weights = dropout(weights, 0.5)
    assert not np.allclose(weights, dropout_weights)

def test_dropout_everything():
    weights = npr.randn(100)
    dropout_weights = dropout(weights, 0.99999)
    assert np.allclose(dropout_weights, np.zeros(len(weights)))
