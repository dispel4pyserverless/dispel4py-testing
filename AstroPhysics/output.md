
## Simple
### Application 
#### COMMAND: 
```
simple_process(graph, {read: [{"input" : "coordinates.txt"}]})
```
#### OUTPUT:
```
Inputs: {'read': [{'input': 'resources/coordinates.txt'}]}
Reading file resources/coordinates.txt
reading VOTable RA=0.77345, DEC=-1.9143
reading VOTable RA=0.83487, DEC=29.7972
reading VOTable RA=0.84108, DEC=30.7821
reading VOTable RA=0.99487, DEC=20.7524
reading VOTable RA=1.97625, DEC=20.4123
reading VOTable RA=2.22791, DEC=23.8174
reading VOTable RA=2.77662, DEC=2.6780
reading VOTable RA=3.03766, DEC=12.0455
reading VOTable RA=3.15941, DEC=5.5053
reading VOTable RA=3.25308, DEC=39.2458
reading VOTable RA=3.63283, DEC=-0.7362
reading VOTable RA=3.99000, DEC=14.0752
reading VOTable RA=4.06195, DEC=10.3320
reading VOTable RA=4.72170, DEC=10.5941
reading VOTable RA=5.27725, DEC=26.5133
reading VOTable RA=5.39700, DEC=1.1655
reading VOTable RA=5.83791, DEC=1.8465
reading VOTable RA=5.97291, DEC=28.3333
reading VOTable RA=6.06754, DEC=14.2368
reading VOTable RA=6.24525, DEC=43.6625
...
```
### Serverless
#### COMMAND: 
```
client.run(graph,input=[{"input" : "resources/coordinates.txt"}],resources=True)
```
#### OUTPUT:
```
Executing workflow with simple process
Inputs: {'read0': [{'input': 'resources/coordinates.txt'}]}
Reading file resources/coordinates.txt
reading VOTable RA=0.77345, DEC=-1.9143
reading VOTable RA=0.83487, DEC=29.7972
reading VOTable RA=0.84108, DEC=30.7821
reading VOTable RA=0.99487, DEC=20.7524
reading VOTable RA=1.97625, DEC=20.4123
reading VOTable RA=2.22791, DEC=23.8174
reading VOTable RA=2.77662, DEC=2.6780
reading VOTable RA=3.03766, DEC=12.0455
reading VOTable RA=3.15941, DEC=5.5053
reading VOTable RA=3.25308, DEC=39.2458
reading VOTable RA=3.63283, DEC=-0.7362
reading VOTable RA=3.99000, DEC=14.0752
reading VOTable RA=4.06195, DEC=10.3320
reading VOTable RA=4.72170, DEC=10.5941
reading VOTable RA=5.27725, DEC=26.5133
reading VOTable RA=5.39700, DEC=1.1655
reading VOTable RA=5.83791, DEC=1.8465
...
```
## Multi
### Application 
#### COMMAND: 
```
multi_process(graph, {read:[{"input" : "resources/coordinates.txt"}]}, edict({'num':5, 'iter': 5,'simple': False}))
```
#### OUTPUT:
```
Processes: {'read0': range(0, 1), 'GetVOTable1': range(1, 2), 'FilterColumns2': range(2, 3), 'InternalExtinction3': range(3, 4)}
Reading file resources/coordinates.txt
reading VOTable RA=0.77345, DEC=-1.9143
read0 (rank 0): Processed 1 iteration.
reading VOTable RA=0.83487, DEC=29.7972
reading VOTable RA=0.84108, DEC=30.7821
reading VOTable RA=0.99487, DEC=20.7524
reading VOTable RA=1.97625, DEC=20.4123
WARNING: W22: None:15:0: W22: The DEFINITIONS element is deprecated in VOTable 1.1.  Ignoring [astropy.io.votable.tree]
W22: None:15:0: W22: The DEFINITIONS element is deprecated in VOTable 1.1.  Ignoring
reading VOTable RA=2.22791, DEC=23.8174
WARNING: W50: None:64:4: W50: Invalid unit string '"h:m:s"' [astropy.io.votable.tree]
W50: None:64:4: W50: Invalid unit string '"h:m:s"'
WARNING: W50: None:67:4: W50: Invalid unit string '"d:m:s"' [astropy.io.votable.tree]
W50: None:67:4: W50: Invalid unit string '"d:m:s"'
WARNING: W50: None:76:4: W50: Invalid unit string '[0.1arcmin]' [astropy.io.votable.tree]
W50: None:76:4: W50: Invalid unit string '[0.1arcmin]'
extracted column: MType = SBbc
extracted column: logR25 = 0.35
WARNING: W22: None:15:0: W22: The DEFINITIONS element is deprecated in VOTable 1.1.  Ignoring [astropy.io.votable.tree]
W22: None:15:0: W22: The DEFINITIONS element is deprecated in VOTable 1.1.  Ignoring
extracted column: MType = SBc
extracted column: logR25 = 0.15
extracted column: MType = Sc
extracted column: logR25 = 0.22
extracted column: MType = Sbc
extracted column: logR25 = 0.61
extracted column: MType = SO-a
extracted column: logR25 = 0.37
reading VOTable RA=2.77662, DEC=2.6780
extracted column: MType = Sb
...
```
### Serverless
#### COMMAND:
```
client.run(graph,input=[{"input" : "resources/coordinates.txt"}],process=Process.MULTI,args=edict({'num':5, 'iter': 5,'simple': False}),resources=True)
```
#### OUTPUT:
```
Executing workflow with multi process
Processes: {'read0': range(0, 1), 'GetVOTable1': range(1, 2), 'FilterColumns2': range(2, 3), 'InternalExtinction3': range(3, 4)}
Reading file resources/coordinates.txt
read0 (rank 0): Processed 1 iteration.
reading VOTable RA=0.77345, DEC=-1.9143
reading VOTable RA=0.83487, DEC=29.7972
reading VOTable RA=0.84108, DEC=30.7821
reading VOTable RA=0.99487, DEC=20.7524
reading VOTable RA=1.97625, DEC=20.4123
WARNING: W22: None:15:0: W22: The DEFINITIONS element is deprecated in VOTable 1.1.  Ignoring [astropy.io.votable.tree]
reading VOTable RA=2.22791, DEC=23.8174
reading VOTable RA=2.77662, DEC=2.6780
reading VOTable RA=3.03766, DEC=12.0455
WARNING: W50: None:64:4: W50: Invalid unit string '"h:m:s"' [astropy.io.votable.tree]
WARNING: W50: None:67:4: W50: Invalid unit string '"d:m:s"' [astropy.io.votable.tree]
WARNING: W50: None:76:4: W50: Invalid unit string '[0.1arcmin]' [astropy.io.votable.tree]
extracted column: MType = SBbc
extracted column: logR25 = 0.35
WARNING: W22: None:15:0: W22: The DEFINITIONS element is deprecated in VOTable 1.1.  Ignoring [astropy.io.votable.tree]
extracted column: MType = SBc
extracted column: logR25 = 0.15
extracted column: MType = Sc
extracted column: logR25 = 0.22
extracted column: MType = Sbc
extracted column: logR25 = 0.61
extracted column: MType = SO-a
extracted column: logR25 = 0.37
extracted column: MType = Sb
extracted column: logR25 = 0.36
extracted column: MType = Sbc
extracted column: logR25 = 0.17
reading VOTable RA=3.15941, DEC=5.5053
...
```

## Redis 
### Application 
#### COMMAND: 
```
read.name = 'producer'
dyn_process(graph, {'producer': [{"input" : "resources/coordinates.txt"} ]}, edict({'num':5,'iter':10, 'simple':False, 'redis_ip':'localhost', 'redis_port':'6379'}))
```
#### OUTPUT:
```
Starting 5 workers communicating
process:0 for instance:None redis connection created.
process:1 for instance:None redis connection created.
Reading file resources/coordinates.txt
process:2 for instance:None redis connection created.
reading VOTable RA=0.77345, DEC=-1.9143
process:3 for instance:None redis connection created.
process:4 for instance:None redis connection created.
reading VOTable RA=0.83487, DEC=29.7972
reading VOTable RA=0.84108, DEC=30.7821
reading VOTable RA=0.99487, DEC=20.7524
reading VOTable RA=1.97625, DEC=20.4123
reading VOTable RA=2.22791, DEC=23.8174
reading VOTable RA=2.77662, DEC=2.6780
reading VOTable RA=3.03766, DEC=12.0455
reading VOTable RA=3.15941, DEC=5.5053
reading VOTable RA=3.25308, DEC=39.2458
reading VOTable RA=3.63283, DEC=-0.7362
reading VOTable RA=3.99000, DEC=14.0752
reading VOTable RA=4.06195, DEC=10.3320
reading VOTable RA=4.72170, DEC=10.5941
reading VOTable RA=5.27725, DEC=26.5133
reading VOTable RA=5.39700, DEC=1.1655
...
```
### Serverless
#### COMMAND:
```
client.run(graph,input=[{"input" : "resources/coordinates.txt"} ], args=edict({'num':5,'simple':False,'redis_ip':'localhost','redis_port':'6379'}),process=Process.DYNAMIC,resources=True)
```
#### OUTPUT:
```
Executing workflow with dynamic process
Starting 5 workers communicating
process:0 for instance:None redis connection created.
process:1 for instance:None redis connection created.
process:2 for instance:None redis connection created.
Reading file resources/coordinates.txt
process:3 for instance:None redis connection created.
process:4 for instance:None redis connection created.
reading VOTable RA=0.83487, DEC=29.7972
reading VOTable RA=0.84108, DEC=30.7821
reading VOTable RA=0.77345, DEC=-1.9143
reading VOTable RA=0.99487, DEC=20.7524
reading VOTable RA=1.97625, DEC=20.4123
reading VOTable RA=2.22791, DEC=23.8174
reading VOTable RA=2.77662, DEC=2.6780
reading VOTable RA=3.03766, DEC=12.0455
reading VOTable RA=3.15941, DEC=5.5053
reading VOTable RA=3.25308, DEC=39.2458
reading VOTable RA=3.63283, DEC=-0.7362
reading VOTable RA=3.99000, DEC=14.0752
reading VOTable RA=4.06195, DEC=10.3320
reading VOTable RA=4.72170, DEC=10.5941
reading VOTable RA=5.27725, DEC=26.5133
reading VOTable RA=5.39700, DEC=1.1655
reading VOTable RA=5.83791, DEC=1.8465
reading VOTable RA=5.97291, DEC=28.3333
...
```
