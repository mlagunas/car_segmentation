import gc

import datasets as dsets
import models
import torch
import torch.optim as optim
from torch.autograd import Variable
from torch.utils.data import DataLoader
from torchvision import transforms

import datasets.utils as data_utils

# parser = argparse.ArgumentParser(description='Car-segmentation kaggle competition')
#
# parser.add_argument('--workers', default=4, type=int, metavar='N', help='number of data loading workers (default: 4)')
# parser.add_argument('--epochs', default=90, type=int, metavar='N', help='number of total epochs to run')
# parser.add_argument('--start-epoch', default=0, type=int, metavar='N', help='manual epoch number (useful on restarts)')
# parser.add_argument('-b', '--batch-size', default=16, type=int, metavar='N', help='mini-batch size (default: 256)')
# parser.add_argument('--lr', '--learning-rate', default=1e-4, type=float, metavar='LR', help='initial learning rate')
# parser.add_argument('--momentum', default=0.9, type=float, metavar='M', help='momentum')
# parser.add_argument('--weight-decay', default=1e-4, type=float, metavar='W', help='weight decay')
# parser.add_argument('--print-freq', default=1, type=int, metavar='N', help='print frequency')
# parser.add_argument('--resume', default='', type=str, metavar='PATH', help='path to latest checkpoint')
# parser.add_argument('--evaluate', dest='evaluate', action='store_true', help='evaluate model on validation set')
# parser.add_argument('--test', dest='test', action='store_true', help='evaluate model on test set')
# parser.add_argument('--pretrained', dest='pretrained', action='store_true', help='use pre-trained model')
#
# global args, best_prec1
# args = parser.parse_args()

batch_size = 8
num_epochs = 100
lr = 0.001
momentum = 0.9
nesterov = True

train_dataset = dsets.CARVANA(root="./data/",
                              train=True,
                              transform=transforms.Compose([
                                  transforms.Scale(256),
                                  transforms.RandomCrop(256),
                                  transforms.ToTensor(),
                              ])
                              )
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                           batch_size=batch_size,
                                           shuffle=True,
                                           pin_memory=False,
                                           num_workers=1)
# unet = models.UNET_256().cuda()
# criterion = models.BCELoss2d().cuda()
# optimizer = optim.SGD(unet.parameters(),
#                       lr=lr,
                      # momentum=momentum,
                      # nesterov=nesterov)

for epoch in range(num_epochs):
    # pbar = tqdm()
    for i, (images, labels) in enumerate(train_loader):
        # Convert torch tensor to Variable
        data_utils.im_show([images[0], labels[0]])
        images = Variable(images.cuda())
        labels = Variable(labels.cuda())

        # # Forward + Backward + Optimize
        # optimizer.zero_grad()  # zero the gradient buffer
        # outputs = unet(images)
        # loss = criterion(outputs, labels)
        # loss.backward()
        # optimizer.step()
        # images, labels = None, None
        # gc.collect()

        # pbar.set_description('EPOCH %d/ %d || LOSS: %.4f || '
        #                      % (epoch+1, num_epochs, loss.data[0]))

