import cv2

def compare_videos(video_path1, video_path2):
    # Buka dua video
    cap1 = cv2.VideoCapture(video_path1)
    cap2 = cv2.VideoCapture(video_path2)

    while cap1.isOpened() and cap2.isOpened():
        # Baca frame dari dua video
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if not ret1 or not ret2:
            break

        # Ubah frame ke skala abu-abu untuk memudahkan perbandingan
        gray_frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray_frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        # Bandingkan dua frame menggunakan perbedaan absolut
        difference = cv2.absdiff(gray_frame1, gray_frame2)

        # Tampilkan perbedaan pada layar
        cv2.imshow('Perbedaan', difference)

        # Tekan tombol 'q' untuk keluar dari tampilan video
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Keluar
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # Sesuaikan video path
    video_path1 = 'Ari Lasso - Hampa - Rollback.mp4'
    video_path2 = 'Ari Lasso - Hampa.mp4'

    compare_videos(video_path1, video_path2)
