import torch

a = torch.randn([3, 5, 3, 8])
print(a.mean([-2, -1]))
