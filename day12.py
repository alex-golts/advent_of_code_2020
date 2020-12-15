import numpy as np

f = open('input12.txt','r')
txt = f.read()
txt = txt.split('\n')
puzzle_input = txt

start_pos = [0,0] # [r,c]
start_direction = 90 # east. I define 0 degrees as north
cur_pos = start_pos.copy()
cur_direction = start_direction
for line in puzzle_input:
    d = line[0]
    num = int(line[1:])
    if d == 'N':
        cur_pos = [cur_pos[0] + num, cur_pos[1]]
    elif d == 'S':
        cur_pos = [cur_pos[0] - num, cur_pos[1]]
    elif d == 'E':
        cur_pos = [cur_pos[0], cur_pos[1] + num]
    elif d == 'W':
        cur_pos = [cur_pos[0], cur_pos[1] - num]
    elif d == 'L':
        cur_direction = (cur_direction - num)%360
    elif d == 'R':
        cur_direction = (cur_direction + num)%360
    elif d == 'F':
        cur_pos = [cur_pos[0] + num*np.cos(cur_direction*np.pi/180), cur_pos[1] + num*np.sin(cur_direction*np.pi/180)]

m_dist = np.abs(cur_pos[0]) + np.abs(cur_pos[1])
print(f'part 1 answer = {m_dist}')

# part 2
start_pos = [0,0] # [r,c]
wp_start_pos = [1, 10]
cur_pos = start_pos.copy()
wp_cur_pos = wp_start_pos.copy()
cur_dist = np.sqrt((wp_cur_pos[0]-cur_pos[0])**2 + (wp_cur_pos[1]-cur_pos[1])**2)
cur_direction = (180/np.pi)*np.arcsin((wp_cur_pos[1]-cur_pos[1])/cur_dist)


for line in puzzle_input:
    d = line[0]
    num = int(line[1:])
    if d == 'N':
        wp_cur_pos = [wp_cur_pos[0] + num, wp_cur_pos[1]]
    elif d == 'S':
        wp_cur_pos = [wp_cur_pos[0] - num, wp_cur_pos[1]]
    elif d == 'E':
        wp_cur_pos = [wp_cur_pos[0], wp_cur_pos[1] + num]
    elif d == 'W':
        wp_cur_pos = [wp_cur_pos[0], wp_cur_pos[1] - num]

    if d in ('N', 'S', 'E', 'W'):
        cur_dist = np.sqrt((wp_cur_pos[0]-cur_pos[0])**2 + (wp_cur_pos[1]-cur_pos[1])**2)
        cur_direction = (180/np.pi)*np.arcsin((wp_cur_pos[1]-cur_pos[1])/cur_dist)
    
    if d in ('L', 'R'):
        if d=='R':
            num = num*-1
        ang = num*np.pi/180
        rot_mat = np.array(([[np.cos(ang), -np.sin(ang)], [np.sin(ang), np.cos(ang)]]))

        ship_xy = np.array(([cur_pos[1], cur_pos[0]]))
        wp_xy = np.array(([wp_cur_pos[1], wp_cur_pos[0]]))
        new_wp_xy = ship_xy + rot_mat.dot(wp_xy-ship_xy)
        wp_cur_pos = [new_wp_xy[1], new_wp_xy[0]]

    elif d == 'F':
        cur_pos_old = cur_pos.copy()
        cur_pos = [cur_pos[0] + num*(wp_cur_pos[0]-cur_pos_old[0]), cur_pos[1] + num*(wp_cur_pos[1]-cur_pos_old[1])]
        wp_cur_pos = [wp_cur_pos[0] + num*(wp_cur_pos[0]-cur_pos_old[0]), wp_cur_pos[1] + num*(wp_cur_pos[1]-cur_pos_old[1])]

m_dist = np.abs(cur_pos[0]) + np.abs(cur_pos[1])
print(f'part 2 answer = {m_dist}')


