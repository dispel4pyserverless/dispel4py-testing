## Simple
### Application 
#### COMMAND: 
```
simple_process(graph, {producer: 5})
```
#### OUTPUT:
```
Inputs: {'NumberProducer0': 5}
IsPrime1: before checking data - 38 - is prime or not“
IsPrime1: before checking data - 567 - is prime or not“
IsPrime1: before checking data - 445 - is prime or not“
IsPrime1: before checking data - 594 - is prime or not“
IsPrime1: before checking data - 764 - is prime or not“
SimplePE: Processed 1 iteration.
Outputs: {}
```
### Serverless
#### COMMAND: 
```
client.run(graph,input=5)
```
#### OUTPUT:
```
Executing workflow with simple process
Inputs: {'NumberProducer0': 5}
IsPrime1: before checking data - 421 - is prime or not“
IsPrime1: before checking data - 14 - is prime or not“
IsPrime1: before checking data - 845 - is prime or not“
IsPrime1: before checking data - 558 - is prime or not“
IsPrime1: before checking data - 82 - is prime or not“
PrintPrime2: the num 421 is prime
SimplePE: Processed 1 iteration.
Outputs: {}
```
## Multi
### Application 
#### COMMAND: 
```
client.run(graph,input=5,process=Process.MULTI,args=edict({'num':5, 'iter':5,'simple': False}))
```
#### OUTPUT:
```
Processes: {'NumberProducer0': range(0, 1), 'IsPrime1': range(1, 3), 'PrintPrime2': range(3, 5)}
IsPrime1 (rank 1): before checking data - 878 - is prime or not“
NumberProducer0 (rank 0): Processed 5 iterations.
IsPrime1 (rank 1): before checking data - 674 - is prime or not“
IsPrime1 (rank 1): before checking data - 811 - is prime or not“
IsPrime1 (rank 2): before checking data - 898 - is prime or not“
IsPrime1 (rank 2): before checking data - 7 - is prime or not“
IsPrime1 (rank 2): Processed 2 iterations.
PrintPrime2 (rank 3): the num 811 is prime
PrintPrime2 (rank 4): the num 7 is prime
PrintPrime2 (rank 3): Processed 1 iteration.
IsPrime1 (rank 1): Processed 3 iterations.
PrintPrime2 (rank 4): Processed 1 iteration.
```

### Serverless
#### COMMAND:
```
client.run(graph,input=5,process=Process.MULTI,args=edict({'num':5, 'iter': 5,'simple': False}))
```
#### OUTPUT:
```
Processes: {'NumberProducer0': range(0, 1), 'IsPrime1': range(1, 3), 'PrintPrime2': range(3, 5)}
NumberProducer0 (rank 0): Processed 5 iterations.
IsPrime1 (rank 1): before checking data - 594 - is prime or not“
IsPrime1 (rank 1): before checking data - 529 - is prime or not“
IsPrime1 (rank 1): before checking data - 439 - is prime or not“
IsPrime1 (rank 1): Processed 3 iterations.
IsPrime1 (rank 2): before checking data - 718 - is prime or not“
IsPrime1 (rank 2): before checking data - 146 - is prime or not“
IsPrime1 (rank 2): Processed 2 iterations.
PrintPrime2 (rank 3): the num 439 is prime
PrintPrime2 (rank 3): Processed 1 iteration.
PrintPrime2 (rank 4): Processed 0 iterations.
```

## Redis 
### Application 
#### COMMAND: 
```
producer.name='producer'
dyn_process(graph,{'producer': 5}, edict({'num':5,'iter':5, 'simple':False, 'redis_ip':'localhost', 'redis_port':'6379'}))
```
#### OUTPUT:
```
Starting 5 workers communicating
process:1 for instance:None redis connection created.
process:0 for instance:None redis connection created.
process:2 for instance:None redis connection created.
process:3 for instance:None redis connection created.
before checking data - 599 - is prime or not“
before checking data - 600 - is prime or not“
before checking data - 797 - is prime or not“
before checking data - 556 - is prime or not“
process:4 for instance:None redis connection created.
before checking data - 918 - is prime or not“
the num 797 is prime
the num 599 is prime
TERMINATED: stateless process:4 ends now
TERMINATED: stateless process:0 ends now
TERMINATED: stateless process:3 ends now
TERMINATED: stateless process:1 ends now
TERMINATED: stateless process:2 ends now
ELAPSED TIME(minus 10 second(s) for AUTO_TERMINATE): 0.10175657272338867
Begin to clean redis stream keys...
```
### Serverless
#### COMMAND:
```
client.run(graph,input=5,process=Process.DYNAMIC,args= edict({'num':5,'iter':5, 'simple':False, 'redis_ip':'localhost', 'redis_port':'6379'}))
```
#### OUTPUT:
```
Executing workflow with dynamic process
Starting 5 workers communicating
process:0 for instance:None redis connection created.
process:1 for instance:None redis connection created.
process:2 for instance:None redis connection created.
before checking data - 562 - is prime or not“
before checking data - 589 - is prime or not“
before checking data - 685 - is prime or not“
before checking data - 83 - is prime or not“
the num 83 is prime
before checking data - 884 - is prime or not“
process:4 for instance:None redis connection created.
process:3 for instance:None redis connection created.
TERMINATED: stateless process:3 ends now
TERMINATED: stateless process:0 ends now
TERMINATED: stateless process:4 ends now
TERMINATED: stateless process:1 ends now
TERMINATED: stateless process:2 ends now
ELAPSED TIME(minus 10 second(s) for AUTO_TERMINATE): 0.10506653785705566
```
