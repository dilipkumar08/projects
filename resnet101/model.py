import torch
from torchvision import transforms
import torchvision.models as models


def process(img):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    model=models.resnet101(pretrained=True)
    model.eval()
    preprocess=transforms.Compose([transforms.Resize(240),
                                transforms.CenterCrop(224),
                                transforms.ToTensor(),
                                transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])])
    img_t=preprocess(img)
    batch_t=torch.unsqueeze(img_t,0)
    
    with open('imagenet_classes.txt','rb') as f:
        labels=[line.strip() for line in f.readlines()]
    
    out=model(batch_t)

    index=torch.max(out,1)[1]

    
    probablities=torch.nn.functional.softmax(out,dim=1)[0]
    percentage=probablities*100
    return (labels[index[0]],percentage[index[0]].item())


