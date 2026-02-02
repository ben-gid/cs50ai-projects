from fastcore.all import *
from fastai.vision.all import *


def main():
    path = Path("gtsrb")
    failed = verify_images(get_image_files(path))
    failed.map(Path.unlink)
    print(f"failed images: {len(failed)}")

    # define model
    dls = DataBlock(
        blocks=(ImageBlock, CategoryBlock),
        get_items=get_image_files,
        splitter=RandomSplitter(valid_pct=0.2, seed=42),
        get_y=parent_label,
        item_tfms=RandomResizedCrop(30, min_scale=0.5),
        batch_tfms=aug_transforms(mult=2)
    ).dataloaders(path, bs=32)

    # train model
    learn = vision_learner(dls, resnet18, metrics=error_rate)
    learn.fine_tune(10)

    learn.export("fastai_model.pkl")
    
if __name__ == "__main__":
    main()