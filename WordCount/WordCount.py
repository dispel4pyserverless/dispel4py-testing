from dispel4py.core import GenericPE
from dispel4py.base import IterativePE
from dispel4py.new.simple_process import process as simple_process
from dispel4py.new.multi_process import process as multi_process
from dispel4py.workflow_graph import WorkflowGraph
from easydict import EasyDict as edict
from client import d4pClient,Process
from dispel4py.new.dynamic_redis import process as dyn_process

class SplitLines(GenericPE):
    def __init__(self):
        GenericPE.__init__(self)
        self._add_input("input")
        self._add_output("output")
        
    def _process(self, inputs):
        import os 
        print("!!!SplitLines self.id %s, rankid %s, process.rank %s" % (self.id, os.getpid(), self.rank))	
        for line in inputs["input"].splitlines():
            self.write("output", line)

class SplitWords(IterativePE):

    def __init__(self):
        IterativePE.__init__(self)
        
    def _process(self, data):
        import os 
        print("!!!SplitWords self.id %s, rankid %s, process.rank %s" % (self.id, os.getpid(), self.rank))	
        for word in data.split(" "):
            self.write("output", (word,1))


class CountWords(GenericPE):
    def __init__(self):
        
        from collections import defaultdict
        GenericPE.__init__(self)
        self._add_input("input", grouping=[0])
        self._add_output("output")
        self.count=defaultdict(int)
        
    def _process(self, inputs):
        import os 
        print("!!!!CountWords self.id %s, rankid %s, process.rank %s" % (self.id, os.getpid(),self.rank))	
        word, count = inputs['input']
        self.count[word] += count
    
    def _postprocess(self):
        self.write('output', self.count)

split = SplitLines()
words = SplitWords()
count = CountWords()


graph = WorkflowGraph()
graph.connect(split, 'output', words, 'input')
graph.connect(words, 'output', count, 'input')


client = d4pClient()

#SIMPLE 
#simple_process(graph, {split: [ {'input' : "Hello Hello algo mas World World"}]})
#client.run(graph,input=[{'input' : "Hello Hello algo mas World World"}])

#MULTI 
#multi_process(graph, {split: [ {'input' : "Hello Hello algo mas World World"}]}, edict({'num':5, 'iter': 5,'simple': False}))
#client.run(graph,input=[{'input' : "Hello Hello algo mas World World"}],process=Process.MULTI,args=edict({'num':5, 'iter': 5,'simple': False}))

#REDIS 
#split.name = 'producer'
#dyn_process(graph,  {'producer': [ {'input' : "Hello Hello algo mas World World"}]}, edict({'num':5,'iter':10, 'simple':False, 'redis_ip':'localhost', 'redis_port':'6379'}))
#client.run(graph,input=[{'input' : "Hello Hello algo mas World World"}],process=Process.DYNAMIC,args= edict({'num':5,'iter':10, 'simple':False, 'redis_ip':'localhost', 'redis_port':'6379'}))
