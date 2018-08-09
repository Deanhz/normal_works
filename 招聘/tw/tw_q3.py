# -*- coding: utf-8 -*-
"""
@author: 丁牟华
@email: 258796762@qq.com
"""
import sys
import unittest
import argparse

# 定义错误
INVALID_NUM = "Invalid number format."
OUT_OF_RANGE = "Number out of range."
FORMAT_ERROR = "Incorrect command format."
CONNECTION_ERROR = "Maze format error."


class TestMaze(unittest.TestCase):
    # 测试无效数字
    def test_InValidNum(self):
        commands = ["3 a\n0,1 0,2;0,0 1,0",
                    "3 3\n0,c 0,2;0,0 1,0"]
        for command in commands:
            MazeFacory = Mazefacotry()
            maze = MazeFacory.Create(command)
            mazeText = maze.Render()
            self.assertEqual(mazeText, INVALID_NUM)
        print("Test invalid number format success!")

    # 测试数字超出预定范围
    def test_OutOfRange(self):
        commands = ["3 -1\n0,1 0,2;0,0 1,0",
                    "3 3 \n0,1 0,2;0,0 1,3"]
        for command in commands:
            MazeFacory = Mazefacotry()
            maze = MazeFacory.Create(command)
            mazeText = maze.Render()
            self.assertEqual(mazeText, OUT_OF_RANGE)
        print("Test number out of range success!")

    # 测试输入命令格式错误
    def test_FormatError(self):
        commands = ["3 3\n0,1 0,2;0,0",
                    "3,3\n0,1 0,2;0,0 1,0",
                    "3 3\n0,1 0,2;0,0,1,0"]
        for command in commands:
            MazeFacory = Mazefacotry()
            maze = MazeFacory.Create(command)
            mazeText = maze.Render()
            self.assertEqual(mazeText, FORMAT_ERROR)
        print("Test incorrect command format success!")

    # 测试连通性错误
    def test_Connection_Error(self):
        commands = ["3 3\n0,1 0,2;0,0 0,2",
                    "3 3\n0,1 0,2;0,0 0,0"]

        for command in commands:
            MazeFacory = Mazefacotry()
            maze = MazeFacory.Create(command)
            mazeText = maze.Render()
            self.assertEqual(mazeText, CONNECTION_ERROR)
        print("Test maze format error success!")

    # 测试迷宫渲染为字符串
    def test_Render(self):
        commands = ["3 3\n\n",
                    "3 3\n0,1 0,2",
                    "3 3\n0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1"]
        labels = ["[W] [W] [W] [W] [W] [W] [W]\n" +
                  "[W] [R] [W] [R] [W] [R] [W]\n" +
                  "[W] [W] [W] [W] [W] [W] [W]\n" +
                  "[W] [R] [W] [R] [W] [R] [W]\n" +
                  "[W] [W] [W] [W] [W] [W] [W]\n" +
                  "[W] [R] [W] [R] [W] [R] [W]\n" +
                  "[W] [W] [W] [W] [W] [W] [W]\n",

                  "[W] [W] [W] [W] [W] [W] [W]\n" +
                  "[W] [R] [W] [R] [R] [R] [W]\n" +
                  "[W] [W] [W] [W] [W] [W] [W]\n" +
                  "[W] [R] [W] [R] [W] [R] [W]\n" +
                  "[W] [W] [W] [W] [W] [W] [W]\n" +
                  "[W] [R] [W] [R] [W] [R] [W]\n" +
                  "[W] [W] [W] [W] [W] [W] [W]\n",

                  "[W] [W] [W] [W] [W] [W] [W]\n" +
                  "[W] [R] [W] [R] [R] [R] [W]\n" +
                  "[W] [R] [W] [R] [W] [R] [W]\n" +
                  "[W] [R] [R] [R] [R] [R] [W]\n" +
                  "[W] [W] [W] [R] [W] [R] [W]\n" +
                  "[W] [R] [R] [R] [W] [R] [W]\n" +
                  "[W] [W] [W] [W] [W] [W] [W]\n",
                  ]
        for i, command in enumerate(commands):
            MazeFacory = Mazefacotry()
            maze = MazeFacory.Create(command)
            mazeText = maze.Render()
            self.assertEqual(mazeText, labels[i])
        print("Test maze render success!")
    
    #测试移动初始效果
    def test_Nomove(self):
        commands = ["3 3\n0,1 0,2\n1,0"]
        labels = ["[W] [W] [W] [W] [W] [W] [W]\n" +
                  "[W] [R] [W] [R] [R] [R] [W]\n" +
                  "[W] [W] [W] [W] [W] [W] [W]\n" +
                  "[W] [*] [W] [R] [W] [R] [W]\n" +
                  "[W] [W] [W] [W] [W] [W] [W]\n" +
                  "[W] [R] [W] [R] [W] [R] [W]\n" +
                  "[W] [W] [W] [W] [W] [W] [W]\n"
                ]
        for i, command in enumerate(commands):
            MazeFactory = Mazefacotry()
            maze = MazeFactory.Create(command)
            mazeText = maze.Render()
            self.assertEqual(mazeText, labels[i])
        print("Test no move render success!")

class Maze:
    def __init__(self, m=0, n=0, conn_cells=[], msg=None, start=None, moveStr=None):
#        print(m, n, conn_cells, msg, start)
        self.route_grid_m, self.route_grid_n = m, n
        self.render_grid_m, self.render_grid_n = 2*m + 1, 2*n + 1
        self.conn_cells = conn_cells
        self.maze = [["[W]" for j in range(self.render_grid_n)] for i in range(self.render_grid_m)]
        self.error_msg = msg
        self.start = start
        self.moveStr = moveStr
        if start:
            self.render_start = [i*2+1 for i in start]
        if moveStr:
            self.moveStr = moveStr

    def Render(self):
        if self.error_msg is not None:
            return self.error_msg

        for i in range(self.route_grid_m):
            for j in range(self.route_grid_n):
                self.maze[2*i+1][2*j+1] = "[R]"
        for c1, c2 in self.conn_cells:
            c1_i, c1_j = c1[0] * 2 + 1, c1[1] * 2 + 1
            c2_i, c2_j = c2[0] * 2 + 1, c2[1] * 2 + 1
            mid_cell_i = (c1_i + c2_i) // 2
            mid_cell_j = (c1_j + c2_j) // 2
            self.maze[mid_cell_i][mid_cell_j] = "[R]"
        if self.render_start:
            x, y = self.render_start
            if self.maze[x][y] == "[R]":
                self.maze[x][y] = "[*]"
        if self.render_start and self.moveStr:
            cur = self.render_start
            for c in self.moveStr:
                next_ = self.move(cur, c)
                if next_ == False:
                    break
                else:
                    cur = next_
        return self.display()
    
    def juageMove(self, x, y):
        if x > self.render_grid_m or x < 0:
            return False
        if y > self.render_grid_n or y < 0:
            return False
        if self.maze[x][y] != "[R]":
            return False
        return True
    
    def move(self, cur, c):
        next_x , next_y = 0, 0 
        if c == "A":
            next_x, next_y = cur[0], cur[1] - 1
        elif c == "D":
            next_x, next_y = cur[0], cur[1] + 1
        elif c == "W":
            next_x, next_y = cur[0] - 1, cur[1]
        elif c == "S":
            next_x, next_y = cur[0] + 1, cur[1]
        else:
            return False
        juage = self.juageMove(next_x, next_y)
        if juage:
            if self.maze[next_x][next_y] == "[R]":
                self.maze[next_x][next_y] = "[*]"
                return [next_x, next_y]
        return False
    
    def display(self):
        result = ""
        for i in range(self.render_grid_m):
            line = " ".join(self.maze[i]) + "\n"
            result += line
        return result


class Mazefacotry:
    route_grid_M, route_grid_N = 0, 0
    conn_cells = None
    error_msg = None

    def __init__(self):
        pass


    def Create(self, command):
        '''
        input: string of command
        return: instance of class Maze
        '''
        try:
            return self.check_create(command)
        except Exception:
            self.error_msg = FORMAT_ERROR
            return Maze(msg=self.error_msg)

    def check_create(self, command):
        '''
        input: string of command
        return: instance of Maze
        '''
        line1, line2, line3 = command.split("\n")
        size = line1.strip().split()
        connCell_list = line2.strip().split(";")
        start = []
        moveStr = ""
        line3_list = line3.split(" ")
        if len(line3_list) > 1:
            start, moveStr = line3_list
        else:
            start = line3_list[0]
        start = start.strip().split(",")
        # 检查command第一行
        if not self.checkSize(size):
            return Maze(msg=self.error_msg)
        else:
            self.route_grid_M, self.route_grid_N = size
        
        if not line2.strip():
            return Maze(self.route_grid_M, self.route_grid_N, [], start)
        self.conn_cells = []
        for s in connCell_list:
            s = s.split()
            cell1, cell2 = s
            cell1 = cell1.split(",")
            cell2 = cell2.split(",")
            # 检查连通性
            if not self.checkConnection(cell1, cell2):
                return Maze(msg=self.error_msg)
            self.conn_cells.append([cell1, cell2])
        # 检查command 第三行
        if not self.checkSize(start):
            return Maze(msg=self.error_msg)
        else:
            return Maze(self.route_grid_M, self.route_grid_N, self.conn_cells, start=start, moveStr = moveStr)

    def checkSize(self, cell):  # 检查网格输入的合法性
        '''
        input: (m,n)
        return: True or False
        '''
        m, n = cell
        try:
            m = int(m)
            n = int(n)
        except ValueError:  # 无效数字，无法转化为数字
            self.error_msg = INVALID_NUM
            return
        else:
            cell[::] = list(map(int, cell))
        # 判断数字是否为负数
        if cell[0] < 0 or cell[1] < 0:
            self.error_msg = OUT_OF_RANGE
            return False
        return True

    def checkConnection(self, cell1, cell2):  # 检查连通网格输入的合法性
        '''
        input: (i1, j2) (i2,j2)
        return: True or False
        '''
        # 判断网格输入的合法性
        if not self.checkSize(cell1) or not self.checkSize(cell2):
            return False
        # 判断网格输入是否超出最大范围
        if cell1[0] >= self.route_grid_M or cell1[1] >= self.route_grid_N \
            or cell2[0] >= self.route_grid_M or cell2[1] >= self.route_grid_N:
            self.error_msg = OUT_OF_RANGE
            return False
        # 判断连通性是否正确
        dist = abs(cell1[0]-cell2[0]) + abs(cell1[1]-cell2[1])
        if dist > 1 or dist == 0:
            self.error_msg = CONNECTION_ERROR
            return False
        return True



def main():
#    command = ""
    command = "3 3\n0,1 0,2;1,0 1,1;1,1 2,1;2,1 2,2\n1,0 DDSSDD"
    for i in range(3):
        command += sys.stdin.readline()
    MazeFacory = Mazefacotry()
    maze = MazeFacory.Create(command)
    mazeText = maze.Render()
    print(mazeText)


def suite():
    suite = unittest.TestSuite()
    tests = [TestMaze("test_InValidNum"), TestMaze("test_OutOfRange"),
             TestMaze("test_FormatError"), TestMaze("test_Connection_Error"),
             TestMaze("test_Render")]
#    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMaze))
    suite.addTests(tests)
    return suite


if __name__ == "__main__":
#    parser = argparse.ArgumentParser()
#    parser.add_argument("-t", dest="t", type=str, default="test", const="test", nargs="?")
#    args = parser.parse_args()
#    if args.t == "main":
#        main()
#    elif args.t == "test":
#        unittest.TextTestRunner().run(suite())
    main()
