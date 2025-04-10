"""
A basic training workflow.
"""

import torch
import random
from torch import nn
from torch.utils.data import Dataset, DataLoader
from torchvision.datasets import ImageNet, CIFAR10
from torchvision.transforms import Compose, ToTensor, Resize
from models.vit import Vit

device = 'cuda:0' if torch.cuda.is_available() else 'cpu'

def train():
    model = Vit(d_model=128, num_head=4, num_layer=4, patch_size=4, out_classes=10) 
    model = model.to(device)

    transform = Compose([
           ToTensor()
           ])
    # train_dataset = ImageNet(root='./data', split="train", transform=transform)
    # val_dataset = ImageNet(root='./data', split="val", transform=transform)

    train_dataset = CIFAR10(root='./data', train=True, transform=transform,
                            download=True)
    val_dataset = CIFAR10(root='./data', train=False, transform=transform,
                          download=True)

    train_dataloader = DataLoader(train_dataset, batch_size=2, shuffle=True)
    val_dataloader = DataLoader(val_dataset, batch_size=2, shuffle=False)

    optimizer = torch.optim.AdamW(
            params = model.parameters(), 
            lr = 1e-4,
            weight_decay=1e-3
            )
    criterion = nn.CrossEntropyLoss()

    epoch = 100
    log_every_n_step = 100
    for i in range(epoch):
        print(f"training {i+1}/{epoch} epochs...")
        model.train()
        step = 0
        for image, label in train_dataloader:
            image = image.to(device)
            label = label.to(device)

            # forward 
            cls = model(image)
            loss = criterion(cls, label)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            step += 1
            if step % log_every_n_step == log_every_n_step -1:
                print(f"loss: {loss.item()}")

        model.eval()
        with torch.no_grad():
            correctness_list = []
            correct_cnt = 0
            total_cnt = 0
            for image, label in val_dataloader:
                image = image.to(device)
                label = label.to(device)

                cls = model(image)
                cls = torch.argmax(cls)
                correct_cnt += torch.sum(cls == label)
                total_cnt += label.shape[0]

            correctness = correct_cnt / total_cnt * 100.0
            correctness_list.append(correctness)
            print(f"correctness: {correctness:.2f}%")

    # Output all correctness
    for c in correctness_list:
        print(f"correctness: {c:.2f}%")

if __name__=="__main__":
    train()
