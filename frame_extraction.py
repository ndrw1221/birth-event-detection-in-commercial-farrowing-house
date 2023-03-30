import cv2
import argparse
import os, shutil


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to video that you want to extract frame from", type=str)
    args = parser.parse_args()

    path = args.path

    # check if input is a valid avi file
    if not os.path.isfile(path):
        raise FileNotFoundError(f"[ERROR] No such file or directory: '{path}'.")
    elif not path.endswith(".avi"):
        raise Exception("[EXCEPTION] Requires file in avi format as input.")
    else:
        print(f"[INFO] Avi file found at {path}")

    # start reading video
    cap = cv2.VideoCapture(path)
    count = 0

    if not cap.isOpened():
        raise Exception("[ERROR] Error opening video stream or file.")

    # check if directory "extracted_frames" exists
    if not os.path.isdir("extracted_frames"):
        os.mkdir("extracted_frames")
        print('[INFO] Directory "extracted_frames" NOT found and was created.')
    else:
        shutil.rmtree("extracted_frames")
        os.mkdir("extracted_frames")
        print('[INFO] Directory "extracted_frames" was FOUND and was removed and recreated.')

    print('[INFO] Start extracting')
    try:
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret:
                count += 1
                if not cv2.imwrite(f'./extracted_frames/frame_{count}.jpg', frame):
                    raise Exception('[ERROR] Fail to save frames.')
                print(f'[INFO] Frame {count} extracted')

            else:
                break

    except cv2.error as e:
        print("[ERROR]: ", e)

    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("[INFO] Total of %d frames extracted." % count)
        print("[INFO] Cap was realeased.")


if __name__ == '__main__':
    main()
