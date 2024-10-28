import pygame, sys
from pygame.locals import *

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ game
chieu_dai = 800
chieu_rong = 600
w = pygame.display.set_mode((chieu_dai, chieu_rong))
pygame.display.set_caption('Chuyển động 2 ô tô')

# Tải ảnh nền
anh_nen = pygame.image.load('package/bg3.png')
anh_nen = pygame.transform.scale(anh_nen, (chieu_dai, chieu_rong))

# Tải ảnh ô tô
oto1 = pygame.image.load('package/oto1.png')
oto1 = pygame.transform.scale(oto1, (100, 50))  # Thay đổi kích thước ô tô 1
oto2 = pygame.image.load('package/oto2.png')
oto2 = pygame.transform.scale(oto2, (100, 50))  # Thay đổi kích thước ô tô 2

# Tọa độ ban đầu của các ô tô
x_oto1 = 100 #duoi cung , trai qua phai
y_oto1 = 450 #tren cung , tren xuong duoi
x_oto2 = 100
y_oto2 = 480

# Tốc độ của các ô tô
toc_do_oto1 = 2
toc_do_oto2 = 5

# Tạo Clock để kiểm soát FPS
FPS = 60
fpsClock = pygame.time.Clock()

while True:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Di chuyển ô tô
    x_oto1 += toc_do_oto1
    x_oto2 += toc_do_oto2

    # Nếu ô tô đi quá chiều dài màn hình thì quay lại từ đầu
    if x_oto1 > chieu_dai:
        x_oto1 = -100  # Quay lại từ trái màn hình
    if x_oto2 > chieu_dai:
        x_oto2 = -100

    # Vẽ nền
    w.blit(anh_nen, (0, 0))

    # Vẽ ô tô
    w.blit(oto1, (x_oto1, y_oto1))  # Vẽ ô tô 1
    w.blit(oto2, (x_oto2, y_oto2))  # Vẽ ô tô 2

    # Cập nhật màn hình
    pygame.display.update()

    # Đồng bộ FPS
    fpsClock.tick(FPS)
