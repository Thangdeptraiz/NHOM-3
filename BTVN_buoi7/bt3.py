import pygame, sys
from pygame.locals import *
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ game
chieu_dai = 800
chieu_rong = 600
w = pygame.display.set_mode((chieu_dai, chieu_rong))
pygame.display.set_caption('Chuyển động 10 hình tròn')

# Màu sắc
colors = [
    (255, 0, 0),     # Đỏ
    (0, 255, 0),     # Xanh lá
    (0, 0, 255),     # Xanh dương
    (255, 255, 0),   # Vàng
    (255, 165, 0),   # Cam
    (128, 0, 128),   # Tím
    (0, 255, 255),   # Xanh lơ
    (255, 192, 203), # Hồng
    (0, 128, 128),   # Xanh biển sẫm
    (128, 128, 128)  # Xám
]

# Tạo danh sách tọa độ và tốc độ cho các hình tròn
circles = []
for i in range(10):
    x = random.randint(0, chieu_dai - 50)  # Tọa độ x ngẫu nhiên
    y = random.randint(-200, 0)            # Tọa độ y ban đầu (bên ngoài màn hình)
    radius = random.randint(20, 40)        # Bán kính ngẫu nhiên
    speed = random.randint(1, 5)           # Tốc độ ngẫu nhiên
    circles.append({'x': x, 'y': y, 'radius': radius, 'color': colors[i], 'speed': speed})

# Tạo Clock để kiểm soát FPS
FPS = 60
fpsClock = pygame.time.Clock()

while True:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Vẽ nền trắng
    w.fill((255, 255, 255))

    # Di chuyển và vẽ các hình tròn
    for circle in circles:
        pygame.draw.circle(w, circle['color'], (circle['x'], circle['y']), circle['radius'])
        circle['y'] += circle['speed']  # Di chuyển hình tròn xuống dưới

        # Nếu hình tròn ra khỏi màn hình, đưa nó lên trên lại
        if circle['y'] - circle['radius'] > chieu_rong:
            circle['y'] = random.randint(-200, 0)  # Đưa hình tròn về vị trí ngẫu nhiên ở trên

    # Cập nhật màn hình
    pygame.display.update()

    # Đồng bộ FPS
    fpsClock.tick(FPS)
