## Elastic Cluster Unassgined Recovery

When you've performed or suffered a full cluster restart, it's probably many shards
were set as unassigned because of **CLUSTER_RECOVERED**. This can be fixed with primary
shard relocation, but this task can be turned tedious if you have a lot of shards
to reallocate.

In my case, I had 400+ shards to reallocate, so I've created this Command Line Interface
program in order to help in this task.

## How it works

It's quite simply, you need to provide your ElasticSearch endpoint and that's all!.

The program will query the _cluster allocation REST in order to achieve the unassignment 
problems and it will try to solve it initilizing the primary shard to the first node which
haves a copy on it. 

**IT WILL BE PERFORMED WITH THE POSSIBILTY OF LOSING DATA** As the shard may be staled and 
we can't be sure which replica is the newest. 

### Program Arguments

* **-e/--endpoint** _http://<elastic_endpoint>:9200_ URL of ElasticSearch instance

```bash
python Main.py --environment http://<elastic_endpoint>:9200
```

### Getting dependencies

```bash
pipenv install
pipenv shell
```

And then run the Main.py file with arguments