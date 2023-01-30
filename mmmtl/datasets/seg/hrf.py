# Copyright (c) OpenMMLab. All rights reserved.

from .builder import SEG_DATASETS
from .custom import CustomDataset


@SEG_DATASETS.register_module()
class HRFDataset(CustomDataset):
    """HRF dataset.

    In segmentation map annotation for HRF, 0 stands for background, which is
    included in 2 categories. ``reduce_zero_label`` is fixed to False. The
    ``img_suffix`` is fixed to '.png' and ``seg_map_suffix`` is fixed to
    '.png'.
    """

    CLASSES = ('background', 'vessel')

    PALETTE = [[120, 120, 120], [6, 230, 230]]

    def __init__(self, **kwargs):
        super(HRFDataset, self).__init__(
            img_suffix='.png',
            seg_map_suffix='.png',
            reduce_zero_label=False,
            **kwargs)
        assert self.file_client.exists(self.img_dir)
