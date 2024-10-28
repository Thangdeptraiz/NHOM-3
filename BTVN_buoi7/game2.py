import pygame, sys
from pygame.locals import *
import random

# Kích thước cửa sổ game
chieu_dai = 800  # Chiều dài cửa sổ
chieu_rong = 500  # Chiều cao cửa sổ

pygame.init()  # Khởi tạo game
w = pygame.display.set_mode((chieu_dai, chieu_rong))  # Tạo cửa sổ game
pygame.display.set_caption('Tiêu đề của game')

# Tải ảnh nền
anh_nen = pygame.image.load('package/bg2.png')
anh_nen = pygame.transform.scale(anh_nen, (chieu_dai, chieu_rong))

# Tải ảnh con chim
chim1 = pygame.image.load('package/chim1.png')
chim1 = pygame.transform.scale(chim1, (80, 70))
chim2 = pygame.image.load('package/chim2.png')
chim2 = pygame.transform.scale(chim2, (80, 70))

# Tải ảnh núi
nui = pygame.image.load('package/nui.png')
nui = pygame.transform.scale(nui, (250, 250))

# Vị trí ban đầu của các đối tượng
x1, y1 = 0, 200  # Vị trí chim 1
x2, y2 = chieu_dai, 50  # Vị trí chim 2

# Khởi tạo tốc độ di chuyển
toc_do_chim1 = 1
toc_do_chim2 = -5

# Tốc độ di chuyển lên/xuống của chim 1 khi nhấn phím
toc_do_len_xuong = 5
chim_dang_len = False
chim_dang_xuong = False

# Khởi tạo tốc độ khung hình
FPS = 60
fpsClock = pygame.time.Clock()

while True:  # Vòng lặp game chính
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                chim_dang_len = True
            if event.key == K_DOWN:
                chim_dang_xuong = True
        if event.type == KEYUP:
            if event.key == K_UP:
                chim_dang_len = False
            if event.key == K_DOWN:
                chim_dang_xuong = False

    # Cập nhật vị trí con chim 1 dựa trên việc nhấn phím
    if chim_dang_len:
        y1 -= toc_do_len_xuong
    if chim_dang_xuong:
        y1 += toc_do_len_xuong

    # Vẽ ảnh nền
    w.blit(anh_nen, (0, 0))
    w.blit(nui, (300, 200))  # Vẽ núi
    w.blit(chim1, (x1, y1))  # Vẽ chim 1
    w.blit(chim2, (x2, y2))  # Vẽ chim 2

    # Cập nhật vị trí của chim 1 và chim 2
    x1 += toc_do_chim1
    x2 += toc_do_chim2

    # Nếu chim 1 đạt đến vị trí nhất định, nó sẽ hạ xuống
    if 350 <= x1 < 400 and y1 >= 160:
        x1 = 350
        y1 += toc_do_len_xuong

    # Đặt lại vị trí khi chim bay hết màn hình
    if x1 > chieu_dai:
        x1 = 0
    if x2 < 0:
        x2 = chieu_dai

    # Cập nhật màn hình
    pygame.display.update()
    fpsClock.tick(FPS)
