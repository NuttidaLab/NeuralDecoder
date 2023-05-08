from torch.utils.data import Dataset, DataLoader
from typing import List
import os

class RepKitDataset(Dataset):
    def __init__(self):
        super().__init__()

    def get_dataloader(self, batch_size: int = None, shuffle: bool = False, num_workers: int = 1):
        return DataLoader(self, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers)
    
    def _crawl_dir(self, data_dir: str, n: int) -> List[str]:
        
        path = sorted([os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.mat')])

        if n: return path[:n]
        else: return path