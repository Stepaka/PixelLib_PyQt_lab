import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import pixellib
from pixellib.instance import instance_segmentation
from pixellib.instance import custom_segmentation
from pixellib.tune_bg import alter_bg

def object_detection_on_an_image(path, List):
    print(path)
    segment_image = instance_segmentation()
    # segment_image.inferConfig(num_classes=2, class_names=["BG","butterfly", "squirrel"])
    segment_image.load_model("mask_rcnn_coco.h5")
    target_class = segment_image.select_target_classes(person=List[0], dog=List[1], car=List[2])
    try:
        result = segment_image.segmentImage(
            # image_path="1city.jpg",
            # image_path="C:/Users/Stepan/Desktop/игститут/СПБПУ/Графика/pix/img/3silicon_valley.jpg",
            image_path=path,
            show_bboxes=True,
            segment_target_classes=target_class,
            extract_segmented_objects=True,
            # save_extracted_objects=True,
            output_image_name="output.jpg"
        )


        print(result[0]["scores"])
        objects_count = len(result[0]["scores"])
        print(f"Найдено объектов: {objects_count}")

        return f"Найдено объектов: {objects_count}"
    except:
        return f"Найдено объектов: 0"

def obj_change_background(path1, path2, List):
    change_bg = alter_bg(model_type="pb")
    change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
    change_bg.change_bg_img(f_image_path=path1, b_image_path=path2, output_image_name="output.jpg", detect = "person")

    return f"Результат"



# def main():
#     object_detection_on_an_image()
#
#
# if __name__ == '__main__':
#     main()


# import pixellib
# from pixellib.torchbackend.instance import instanceSegmentation
#
# ins = instanceSegmentation()
# ins.load_model("pointrend_resnet50.pkl")
# ins.segmentImage("1city.jpg", show_bboxes=True, output_image_name="output_image.jpg")
#
#
# import pixellib
# from pixellib.semantic import semantic_segmentation
# import cv2
#
# capture = cv2.VideoCapture(0)
#
# segment_video = semantic_segmentation()
# segment_video.load_ade20k_model("deeplabv3_xception65_ade20k.h5")
# segment_video.process_camera_ade20k(capture, overlay=True, frames_per_second= 15, output_video_name="output_video.mp4", show_frames= True,
# frame_name= "frame")


# import pixellib
# from pixellib.custom_train import instance_custom_training
#
# train_maskrcnn = instance_custom_training()
# train_maskrcnn.modelConfig(network_backbone = "resnet101", num_classes= 2, batch_size = 1)
# train_maskrcnn.load_pretrained_model("mask_rcnn_coco.h5")
# train_maskrcnn.load_dataset("Nature")
# train_maskrcnn.train_model(num_epochs = 2, augmentation=True, path_trained_models = "mask_rcnn_models")

# import pixellib
# from pixellib.instance import custom_segmentation
#
# segment_image = custom_segmentation()
# segment_image.inferConfig(num_classes=2, class_names=["BG", "butterfly", "squirrel"])
# segment_image.load_model("mask_rcnn_models/mask_rcnn_model.002-1.381244.h5")
# segment_image.segmentImage("Nature/train/butterfly (4).png", show_bboxes=True, output_image_name="sample_out.jpg")