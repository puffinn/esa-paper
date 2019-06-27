from __future__ import absolute_import
import _puffinnwrapper as puffinn
from ann_benchmarks.algorithms.base import BaseANN
import numpy

class Puffinn(BaseANN):
    def __init__(self, metric, space=10**6, hash_function="fht_crosspolytope", hash_source='pool', hash_args=None):
        self.metric = metric
        self.space = space
        self.filter_type = 'filter'
        self.eps = 1.0
        self.hash_function = hash_function
        self.hash_source = hash_source
        self.hash_args = hash_args

    def fit(self, X):
        if self.hash_args:
            self.index = puffinn.Index(self.metric, X.shape[1], self.space,\
                    hash_function=self.hash_function, hash_source=self.hash_source,\
                    hash_args=self.hash_args)
        else:
            self.index = puffinn.Index(self.metric, X.shape[1], self.space,\
                    hash_function=self.hash_function, hash_source=self.hash_source)
        for i, x in enumerate(X):
            self.index.insert(x.tolist())
        self.index.rebuild(10)

    def set_query_arguments(self, recall, filter_type = 'filter', eps=1.0):
        self.recall = recall
        self.eps = eps
        self.filter_type = filter_type
        self.index.set_sketch_eps(self.eps)

    def get_additional(self):
        dist_comps = self.index.get_distance_computations()
        self.index.reset_performance_metrics()
        return {"dist_comps" : dist_comps}

    def query(self, v, n):
        return self.index.search(v.tolist(), n, self.recall, self.filter_type)

    def __str__(self):
        return 'PUFFINN(space=%d, recall=%f, sketch_eps=%f, filter=%s, hf=%s, hashsource=%s)' % (self.space, self.recall, self.eps, self.filter_type, self.hash_function, self.hash_source)

