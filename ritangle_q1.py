x = [17, 19, 23, 29, 31, 37]
y = [2, 3, 5, 7, 11, 13]
total = 0

all_grid_points = []
for xi in range(len(x)):
    for yi in range(len(y)):
        all_grid_points.append((xi, yi))

given_points = [(0, 3), (2, 1), (4, 0)]

available_spots = []
for point in all_grid_points:
    if point not in given_points:
        available_spots.append(point)


for i in range(len(available_spots)):
    for j in range(i + 1, len(available_spots)):
        for k in range(j + 1, len(available_spots)):
            
            p4 = available_spots[i]
            p5 = available_spots[j]
            p6 = available_spots[k]
            
            six_points = given_points + [p4, p5, p6]
            

            distances = []

            for m in range(len(six_points)):
                for n in range(m + 1, len(six_points)):
                    p1 = six_points[m]
                    p2 = six_points[n]
        
                    dx = p2[0] - p1[0]
                    dy = p2[1] - p1[1]
   
                    listd = (dx**2 + dy**2)
        
                    distances.append(listd)

            unique_d = []
            for dist in distances:
                if dist not in unique_d:
                    unique_d.append(dist)

            if len(unique_d) == 15:
                print("found")
                
                val4 = x[p4[0]] * y[p4[1]]
                val5 = x[p5[0]] * y[p5[1]]
                val6 = x[p6[0]] * y[p6[1]]
                
                total = val4 + val5 + val6
                print(total)
                break
