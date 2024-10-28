import pygame, sys
from pygame.locals import *
import random

chieu_dai = 800  # Chiều dài cửa sổ
chieu_rong = 500  # Chiều cao cửa sổ
pygame.init()  # Khởi tạo game
w = pygame.display.set_mode((chieu_dai, chieu_rong))  # Tạo 1 cửa sổ game tên là w
pygame.display.set_caption('Tiêu đề của game')

# ------------- tạo nền của game là 1 ảnh -----------------
anh_nen = pygame.image.load('package/bg2.png')  # Đường dẫn đến ảnh nền
anh_nen = pygame.transform.scale(anh_nen, (chieu_dai, chieu_rong))

# ------------ tạo ảnh các quả táo, cam, xoài ------------
tao = pygame.image.load('package/tao.png')  # Đường dẫn đến ảnh táo
tao = pygame.transform.scale(tao, (60, 70))

cam = pygame.image.load('package/cam.png')  # Đường dẫn đến ảnh cam
cam = pygame.transform.scale(cam, (60, 70))

xoai = pygame.image.load('package/xoai.png')  # Đường dẫn đến ảnh xoài
xoai = pygame.transform.scale(xoai, (60, 70))

# ----------- tạo ảnh con chim--------------
chim1 = pygame.image.load('package/chim1.png')  # Đường dẫn đến ảnh chim1
chim1 = pygame.transform.scale(chim1, (80, 70))

chim2 = pygame.image.load('package/chim2.png')  # Đường dẫn đến ảnh chim2
chim2 = pygame.transform.scale(chim2, (80, 70))

nui = pygame.image.load('package/nui.png')  # Đường dẫn đến ảnh núi
nui = pygame.transform.scale(nui, (250, 250))

# ---------- tạo vị trí ban đầu--------------
x_tao = 100
y_tao = 0
x_cam = 200
y_cam = 0
x_xoai = 300
y_xoai = 0

x1 = 0
y1 = 200
x2 = chieu_dai
y2 = 50

# ---------- Khởi tạo khung thời gian--------------
FPS = 60
fpsClock = pygame.time.Clock()

while True:  # tạo vòng lặp game
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                y1 = y1 - 5
            if event.key == K_DOWN:
                y1 = y1 + 5

    # -----vẽ ảnh nền ----------------
    w.blit(anh_nen, (0, 0))
    w.blit(nui, (300, 200))
    w.blit(chim1, (x1, y1))
    w.blit(chim2, (x2, y2))

    # Vẽ các quả trên màn hình
    w.blit(tao, (x_tao, y_tao))
    w.blit(cam, (x_cam, y_cam))
    w.blit(xoai, (x_xoai, y_xoai))

    # Cập nhật vị trí của các quả (nếu cần)
    y_tao += 1
    y_cam += 10
    y_xoai += 12

    if y_tao > chieu_rong:
        y_tao = 0
    if y_cam > chieu_rong:
        y_cam = 0
    if y_xoai > chieu_rong:
        y_xoai = 0

    # Cập nhật vị trí của chim
    x1 += 1
    x2 -= 5

    if x1 >= 350 and x1 < 400 and y1 >= 160:
        x1 = 350
        y1 += 5
    if x1 > chieu_dai:
        x1 = 0
    if x2 < 0:
        x2 = chieu_dai

    # Điền các thao tác game vào đây!
    pygame.display.update()
    fpsClock.tick(FPS)
