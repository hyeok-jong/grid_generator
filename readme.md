

# Grid search is the best  
# beta version  


1. make your own `hyperparmeters.json`  


2. 
```
python generator.py
```  

3. Then run the generated bash file  
```
bash grid_searcher.sh
```



## Use for many combinations of hyperparamters searching.

Wandb sweep agent could be best option. However, the agent can only runs on one gpu.  

If each train have small memory but many experiments, allocate each train to all GPUs is better.  
Wandb agent cannot do this.  




## TO DO  
- add `wait` for multiple gpus  
- add `nohup` for background