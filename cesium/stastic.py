# coding:utf-8
import numpy


class BaseAnalysis(object):
    def __init__(self, samples):
        if isinstance(samples, basestring):
            self.samples = samples.split(",|、| ")
        self.samples = samples
        self.narray = numpy.array(self.samples)

    def mean(self):
        """获取期望"""
        return numpy.mean(self.samples)

    def variance(self):
        """获取方差"""
        return numpy.var(self.samples)

    def std(self):
        """获取标准差"""
        return numpy.std(self.samples)

    def t_range(self):
        pass

    def t_range_rate(self):
        pass

    def t_confidence_area(self, rate):
        pass

    def t_confidence_left(self):
        pass

    def t_confidence_right(self):
        pass

cesium = BaseAnalysis
