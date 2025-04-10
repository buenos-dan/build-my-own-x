"""
[An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929)
"""
import math
import torch
from torch import nn


class MultiHeadAttention(nn.Module):
    """
    [Attention is all you need](https://arxiv.org/pdf/1706.03762)
    """
    def __init__(self, d_model, num_head):
        super().__init__()
        assert d_model % num_head == 0, f"{d_model=} % {num_head=} must equals to 0."
        self.d_model = d_model
        self.num_head = num_head
        self.d_k = d_model//num_head

        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)


    def split_head(self, x):
        """split tokens.

        Args:
        x:tensor, x shape is  B x seq x d_model

        Returns:
        tensor, the return shape is B x num_head x seq x d_model//num_head
        """
        B, seq, _ = x.size()
        x = x.reshape(B, seq, self.num_head, -1).permute(0, 2, 1, 3)
        return x

    def combine_head(self, x):
        """merge tokens

        Args:
        x:tensor, x shape is B x num_head x seq x d_model//num_head

        Returns:
        tensor, return tensor shape is B x seq x d_model
        """
        B, _, seq, _ = x.shape
        x = x.permute(0, 2, 1, 3).reshape(B, seq, self.d_model)
        return x

    def scaled_dot_product_attention(self, Q, K, V):
        x = torch.matmul(Q, K.mT) / math.sqrt(self.d_k)
        x = torch.softmax(x, dim=-1)
        x = torch.matmul(x, V)

        return x

    def forward(self, x):
        Q=self.split_head(self.W_q(x))
        K=self.split_head(self.W_k(x))
        V=self.split_head(self.W_v(x))
        
        x = self.scaled_dot_product_attention(Q, K, V)
        x = self.W_o(self.combine_head(x))

        return x

class TransformerEncoder(nn.Module):
    def __init__(self, d_model=768, num_head=4):
        super().__init__()
        self.norm = nn.LayerNorm(d_model)
        self.multi_head_attention = MultiHeadAttention(d_model=d_model,
                                                       num_head=num_head)
        self.mlp = nn.Linear(d_model, d_model)

    def forward(self, x):
        x1 = self.norm(x)
        x1 = self.multi_head_attention(x1)
        x = x + x1
        x1 = self.norm(x)
        x1 = self.mlp(x1)
        x = x + x1

        return x

class SinusoidalPositionalEmbedding(nn.Module):
    def __init__(self, d_model, sequence=5000):
        super().__init__()
        self.d_model = d_model

        pe = torch.zeros(sequence, d_model)
        pos = torch.arange(0, sequence).unsqueeze(1)
        i = torch.arange(0, d_model, 2)
        pe[:, 0::2] = torch.sin(pos / ((10000) ** ( i / d_model)))
        pe[:, 1::2] = torch.cos(pos / ((10000) ** ( i / d_model)))
        self.register_buffer('pe', pe.unsqueeze(0))  # Save as buffer, not a parameter

    def forward(self, x):
        B, seq, d_model = x.shape
        return x + self.pe[:, :seq, :]

class Vit(nn.Module):
    def __init__(self, d_model=768, num_head=4, num_layer=6, patch_size=14, out_classes=1000):
        super().__init__()
        self.P = patch_size
        self.d_model = d_model
        self.encoders = nn.ModuleList([ TransformerEncoder(d_model, num_head) 
                       for i in range(num_layer)])
        self.cls_token = nn.Parameter(torch.randn(1, 1, d_model))
        self.image_embedding = nn.Linear(self.P ** 2 * 3, d_model)
        self.pos_embedding = SinusoidalPositionalEmbedding(d_model)

        self.mlp = nn.Sequential(
            nn.Linear(d_model, d_model),
            nn.Linear(d_model, out_classes),
            )

    def patchify(self, x):
        B, C, H, W = x.shape
        rows, cols = H // self.P, W // self.P
        x = x.reshape(B, C, rows, self.P, cols, self.P).permute(0, 1, 2, 4, 3, 5)
        x = x.permute(0, 2, 3, 1, 4, 5)
        x = x.reshape(B, rows * cols, -1)
        return x

    def forward(self, x):
        """Do image classification with transformer

        Args:
        x: tensor, images B x 3 x H x W

        Returns:
        tensor, labels B x 1000 (1k claasification)
        """
        B, C, H, W = x.shape
        cls_tokens = self.cls_token.expand(B, -1, -1)
        x = self.patchify(x) 
        x = self.image_embedding(x)
        x = torch.cat([cls_tokens, x], dim=1)
        x = self.pos_embedding(x)

        for layer in self.encoders:
            x = layer(x)

        x = x[:, 0, :]
        x = self.mlp(x)

        return x



if __name__=="__main__":
    x = torch.randn(4, 3, 224, 224)
    vit = Vit()
    x = vit(x)
    print(x)
    print(x.shape)

