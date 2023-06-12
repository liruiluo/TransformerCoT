import torch.nn as nn
from fvcore.common.registry import Registry

MODEL_REGISTRY = Registry("model")

@MODEL_REGISTRY.register()
class BaseModel(nn.Module):
    def __init__(self, cfg):
        super().__init__()

    def get_opt_params(self):
        raise NotImplementedError("Function to obtain all default parameters for optimization")

def build_model(cfg):
	return MODEL_REGISTRY.get(cfg.model.name)(cfg)
