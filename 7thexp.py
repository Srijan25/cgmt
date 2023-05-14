def sutherland_hodgman(subject_polygon, clip_polygon):
    def inside(p):
        return(cp2[0]-cp1[0])*(p[1]-cp1[1]) > (cp2[1]-cp1[1])*(p[0]-cp1[0])
    
    def compute_intersection():
        dc = [ cp1[0] - cp2[0], cp1[1] - cp2[1] ]
        dp = [ s[0] - e[0], s[1] - e[1] ]
        n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
        n2 = s[0] * e[1] - s[1] * e[0] 
        n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
        return [(n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3]
    
    output_list = subject_polygon
    cp1 = clip_polygon[-1]
    
    for clip_vertex in clip_polygon:
        cp2 = clip_vertex
        input_list = output_list
        output_list = []
        s = input_list[-1]
        
        for subject_vertex in input_list:
            e = subject_vertex
            if inside(e):
                if not inside(s):
                    output_list.append(compute_intersection())
                output_list.append(e)
            elif inside(s):
                output_list.append(compute_intersection())
            s = e
        cp1 = cp2
    return output_list
import numpy as np
import matplotlib.pyplot as plt

subject_polygon = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])
clip_polygon = np.array([[0.25, 0.25], [0.75, 0.25], [0.75, 0.75], [0.25, 0.75]])

clipped_polygon = sutherland_hodgman(subject_polygon, clip_polygon)

fig, ax = plt.subplots()

ax.plot(subject_polygon[:, 0], subject_polygon[:, 1], 'b', label='Subject Polygon')
ax.plot(clip_polygon[:, 0], clip_polygon[:, 1], 'g', label='Clip Polygon')
ax.plot([p[0] for p in clipped_polygon], [p[1] for p in clipped_polygon], 'r', label='Clipped Polygon')

ax.legend()
plt.show()
