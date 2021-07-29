import pygame
import math
import os
from settings import PATH

pygame.init()
ENEMY_IMAGE = pygame.image.load(os.path.join("images", "enemy.png"))


class Enemy:
    def __init__(self):
        self.width = 40
        self.height = 50
        self.image = pygame.transform.scale(ENEMY_IMAGE, (self.width, self.height))
        self.health = 20#調整了長寬
        self.max_health = 40
        self.path = PATH
        self.path_index = 0
        self.move_count = 0
        self.stride = 1
        self.x, self.y = self.path[self.path_index]

    def draw(self, win):
        # draw enemy
        win.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))
        # draw enemy health bar
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """
        Draw health bar on an enemy
        :param win: window
        :return: None
        """
        # ...(to be done)
        pygame.draw.rect(win,(255, 0, 0),[self.x-20,self.y-30,self.max_health,5])#讓血條跟著小怪走
        pygame.draw.rect(win,(0, 255, 0),[self.x-20,self.y-30,self.health,5])

    def move(self):#變數記得.self
        """
        Enemy move toward path points every frame
        :return: None
        """
        # ...(to be done)
        stride = 1 #步伐
        ax, ay =self.path[self.path_index]  # x, y position of point A
        bx, by =self.path[self.path_index+1]
        distance_A_B = math.sqrt((ax - bx)**2 + (ay - by)**2)
        max_count = int(distance_A_B / stride)  # total footsteps that needed from A to B

        if self.move_count < max_count:
            unit_vector_x = (bx - ax) / distance_A_B
            unit_vector_y = (by - ay) / distance_A_B
            delta_x = unit_vector_x * stride
            delta_y = unit_vector_y * stride
            # update the coordinate and the counter
            self.x += delta_x
            self.y += delta_y
            self.move_count += 1
        else:
            self.path_index+=1
            self.move_count=0



class EnemyGroup:
    def __init__(self):
        self.campaign_count = 0
        self.campaign_max_count = 120   # (unit: frame)
        self.reserved_members = []
        self.expedition = []  # don't change this line until you do the EX.3 

    def campaign(self):
        """
        Send an enemy to go on an expedition once 120 frame
        :return: None
        """
        # Hint: self.expedition.append(self.reserved_members.pop())

        if self.reserved_members and self.campaign_count>=self.campaign_max_count:#條件
            self.expedition.append(self.reserved_members.pop())#pop進expedition
            self.campaign_count=0#歸零
        else :
            self.campaign_count+=1#疊上去
            
    def generate(self, num):
        """
        Generate the enemies in this wave
        :param num: enemy number
        :return: None
        """
        # ...(to be done)
        for i in range(num):#迴圈
            self.reserved_members.append(Enemy())#append進去
    def get(self):
        """
        Get the enemy list
        """
        return self.expedition

    def is_empty(self):
        """
        Return whether the enemy is empty (so that we can move on to next wave)
        """
        return False if self.reserved_members else True

    def retreat(self, enemy):
        """
        Remove the enemy from the expedition
        :param enemy: class Enemy()
        :return: None
        """
        self.expedition.remove(enemy)





