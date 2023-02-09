## Simple Execution
### Application
#### COMMAND: ```simple_process(graph, {split: [ {'input' : "Hello Hello algo mas World World"}]})```
#### OUTPUT:
```
Inputs: {'SplitLines0': [{'input': 'Hello Hello algo mas World World'}]}
SimplePE: Processed 1 iteration.
Outputs: {'CountWords2': {'output': [defaultdict(<class 'int'>, {'Hello': 2, 'algo': 1, 'mas': 1, 'World': 2})]}}
```

### Serverless
#### COMMAND: ```client.run(graph,input=[{'input' : "Hello Hello algo mas World World"}],args=edict({'iter':5}))```
#### OUTPUT:
```
Executing workflow with simple process
Inputs: {'SplitLines0': [{'input': 'Hello Hello algo mas World World'}]}
SimplePE: Processed 1 iteration.
Outputs: {'CountWords2': {'output': [defaultdict(<class 'int'>, {'Hello': 2, 'algo': 1, 'mas': 1, 'World': 2})]}}
```
## Multi Execution
### Application
#### COMMAND: ```multi_process(graph, {split: [ {'input' : "Hello Hello algo mas World World"}]}, edict({'num':5, 'iter': 5,'simple': False}))```
#### OUTPUT:
```
Processes: {'SplitLines0': range(0, 1), 'SplitWords1': range(1, 3), 'CountWords2': range(3, 5)}
SplitLines0 (rank 0): Processed 1 iteration.
SplitWords1 (rank 1): Processed 1 iteration.
CountWords2 (rank 3): Processed 4 iterations.
SplitWords1 (rank 2): Processed 0 iterations.
CountWords2 (rank 4): Processed 2 iterations.
```
### Serverless 
#### COMMAND: ```client.run(graph,input=[{'input' : "Hello Hello algo mas World World"}],process=Process.MULTI,args=edict({'num':5, 'iter': 5,'simple': False}))```
#### OUTPUT:
```
Executing workflow with multi process
Processes: {'SplitLines0': range(0, 1), 'SplitWords1': range(1, 3), 'CountWords2': range(3, 5)}
SplitLines0 (rank 0): Processed 1 iteration.
SplitWords1 (rank 1): Processed 1 iteration.
SplitWords1 (rank 2): Processed 0 iterations.
CountWords2 (rank 3): Processed 2 iterations.
CountWords2 (rank 4): Processed 4 iterations.
```

#### Redis
### Application 
#### COMMAND: ```dyn_process(graph,  {split: [ {'input' : "Hello Hello algo mas World World"}]}, edict({'num':5,'iter':10, 'simple':False, 'redis_ip':'localhost', 'redis_port':'6379'}))```
OUTPUT:

### Serverless
COMMAND:
OUTPUT:


-- Note how to specify iterations in simple process 
