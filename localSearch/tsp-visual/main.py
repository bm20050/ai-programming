import pygame
from algo_info import ALGO_INFO, DIVIDERS
from gfx import *
from util import *
import threading


# 0. 알고리즘을 어떻게 되었든 먼자 만들어야 되는거 아닌가
# 1. 좌표를 찍어야 됨
# 2. Loop를 만들어야 됨


def loop():
    # 1. 알고리즘 정보를 가져온다.
    # 2. 무한반복
    # 2-1. 알고리즘을 배치한다.
    # 2-2. 그린다.
    # 점, 선, 텍스트
    # draw_point(x, y) => 값 반환하지 않음
    # draw_line(x, y) => 값 반환하지 않음
    # draw_text(x, y) => 값 반환하지 않음

    for i in range(len(ALGO_INFO)):
        print(ALGO_INFO[i])
    while True:
        check_events()
        draw_text_center(surface, "Hello", font, 50, 50)
        draw_dividers(surface, DIVIDERS)

        for i in range(len(ALGO_INFO)):
            if i < len(sim):
                draw_text_top_left(surface,
                                   ALGO_INFO[i]['name'],
                                   GREEN,
                                   font,
                                   *ALGO_INFO[i]['name_coords'],
                                   )
                draw_path(surface, list_of_cities_list[i], sim[i].best_order)
            elif len(sim[ALGO_INFO[i]['depends']].best_order) != 0:
                pass
        pygame.display.update()
        surface.fill(BLACK)

    # 1. 애니메이션 나오게 하고 싶음.
    # - P를 내가 만들어야 됨(랜덤으로) => 답이 있는 랜덤
    # 1-2. 포팅
    #


pygame.init()
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
font = pygame.font.SysFont("Consolas", FONT_HEIGHT)
cities = make_cities(20)
list_of_cities_list = []
sim = []
threads = []

for i in range(len(ALGO_INFO)):
    list_of_cities_list.append(displace(cities, *ALGO_INFO[i]['displacement']))


# 스레드에서 에러(계산이 동기적으로 이뤄지지 않음)
for i in range(len(ALGO_INFO)):
    if ALGO_INFO[i]['depends'] == -1:
        sim.append(ALGO_INFO[i]['sim'](list_of_cities_list[i]))
        threads.append(threading.Thread(target=sim[i].find()))
        threads[i].daemon = True
# graph = make_graph_from_city_list(cities)
if __name__ == "__main__":
    pygame.display.set_caption('TSP - Visualizer')

    # print(ALGO_INFO[i]['displacement'])
    # loop()
    # 첫 번째 시작 위치
    # 두 번째 시작 위치
