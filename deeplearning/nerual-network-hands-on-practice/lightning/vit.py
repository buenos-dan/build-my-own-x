import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import models, datasets, ops
from torchvision.transforms import v2 as transforms
import lightning as L

from models import Vit

# Use a pretrained Faster R-CNN model from torchvision and modify it
class VitModel(L.LightningModule):
    def __init__(self):
        super().__init__()
        self.model = Vit()
        self.criterion = nn.CrossEntropyLoss()

    def compute_loss(self, pred, target):
        loss = self.criterion(pred, target)
        return loss

    def forward(self, images, label=None):
        return self.model(images)

    def training_step(self, batch, batch_idx):
        images, labels = batch
        pred = self.model(images, labels)
        loss = self.criterion(pred, labels)
        self.log('train_loss', loss)
        return loss

    def configure_optimizers(self):
        return optim.SGD(self.parameters(), lr=0.001, momentum=0.9, weight_decay=0.0005)


class ImagenetData(L.LightningDataModule):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        transforms.Resize(size=(800,), max_size=1333),
    ])

    def train_dataloader(self):
        train_dataset = datasets.ImageNet(
                root="/mnt/bn/robotics-training-data-lf/danmingdi/datasets/imagenet",
                split="train"
                )


        return DataLoader(
            train_dataset, batch_size=8, shuffle=True, num_workers=4)


if __name__ == "__main__":
    data = ImagenetData()
    model = VitModel()
    trainer = L.Trainer(
        max_epochs=5, 
        log_every_n_steps=10
    )
    trainer.fit(model, data)
