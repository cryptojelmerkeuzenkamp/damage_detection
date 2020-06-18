import os
import json
import numpy as np
import skimage.draw
from mrcnn import utils


class CustomDataset(utils.Dataset):

    def load_custom(self, dataset_dir, subset):
        """

        :param dataset_dir:
        :param subset:
        :return:
        """

        self.add_class("scratch", 1, "scratch")

        # Train or validation images?
        assert subset in ["train", "val"]
        dataset_dir = os.path.join(dataset_dir + subset)
        annotations1 = json.load(open(os.path.join(dataset_dir + '/' + "via_region_data.json"),'r',encoding="utf8",errors='ignore'))
        annotations = list(annotations1.values())
        annotations = [a for a in annotations if a['regions']]

        # Add images
        for a in annotations:

            polygons = [r['shape_attributes'] for r in a['regions'].values()]
            image_path = os.path.join(dataset_dir, a['filename'])
            image = skimage.io.imread(image_path)
            height, width = image.shape[:2]

            self.add_image(
                "scratch",
                image_id=a['filename'],
                path=image_path,
                width=width, height=height,
                polygons=polygons)

    def load_mask(self, image_id):

        image_info = self.image_info[image_id]
        if image_info["source"] != "scratch":
            return super(self.__class__, self).load_mask(image_id)

        # Convert polygons to a bitmap mask of shape
        # [height, width, instance_count]
        info = self.image_info[image_id]
        mask = np.zeros([info["height"], info["width"], len(info["polygons"])],
                        dtype=np.uint8)
        for i, p in enumerate(info["polygons"]):
            # Get indexes of pixels inside the polygon and set them to 1
            rr, cc = skimage.draw.polygon(p['all_points_y'], p['all_points_x'])
            mask[rr, cc, i] = 1

        return mask.astype(np.bool), np.ones([mask.shape[-1]], dtype=np.int32)

    def image_reference(self, image_id):
        """Return the path of the image."""
        info = self.image_info[image_id]
        if info["source"] == "scratch":
            return info["path"]
        else:
            super(self.__class__, self).image_reference(image_id)
