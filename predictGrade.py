import numpy as np
import matplotlib.pyplot as plt
import scipy as sp 
import scipy.stats

plt.rcParams['figure.figsize'] = (10, 5)
plt.rcParams['font.size'] = 20
plt.rcParams['lines.linewidth'] = 3

mean1, sigma1 = 41.98, 22         #최대 점수 100점 
mean2, sigma2 = 26.94, 20.59      #최대 점수 90점
mean3, sigma3 = mean1+mean2 , np.sqrt(sigma1**2+sigma2**2) # 중간, 기말 합산 -> 최대 점수 190점
population = 100 #시험 응시자 

grade1_x , grade2_x = 35,48
grade3_x = grade1_x + grade2_x

x1 = np.linspace(0, 100, 1000)
x2 = np.linspace(0, 90 ,1000)
x3 = np.linspace(0,190,1000)
y1 = (1 / np.sqrt(2 * np.pi * sigma1**2)) * np.exp(-(x1-mean1)**2 / (2 * sigma1**2))
y2 = (1 / np.sqrt(2 * np.pi * sigma2**2)) * np.exp(-(x2-mean2)**2 / (2 * sigma2**2))
y3 = (1 / np.sqrt(2 * np.pi * sigma3**2)) * np.exp(-(x3-mean3)**2 / (2 * sigma3**2))

grade1_y = (1 / np.sqrt(2 * np.pi * sigma1**2)) * np.exp(-(grade1_x-mean1)**2 / (2 * sigma1**2))
grade2_y = (1 / np.sqrt(2 * np.pi * sigma2**2)) * np.exp(-(grade2_x-mean2)**2 / (2 * sigma2**2))
grade3_y = (1 / np.sqrt(2 * np.pi * sigma3**2)) * np.exp(-(grade3_x-mean3)**2 / (2 * sigma3**2))

rv_1 = sp.stats.norm(mean1, sigma1)
rv_2 = sp.stats.norm(mean2, sigma2)
rv_3 = sp.stats.norm(mean3, sigma3)

percent1 = 1-rv_1.cdf(grade1_x) # 상위 몇퍼?
percent2 = 1-rv_2.cdf(grade2_x) 
percent3 = 1-rv_3.cdf(grade3_x)

rank1 = round(percent1*population) # 퍼센트 * 응시자 수
rank2 = round(percent2*population)
rank3 = round(percent3*population)

plt.figure()
plt.plot(x1, y1, label=r'midterm ')
plt.plot(x2, y2, label=r'finalterm')
plt.plot(x3, y3, label=r'totalterm ')
plt.plot(grade1_x,grade1_y, '+', color='red', label=r'midterm grade')
plt.plot(grade2_x,grade2_y, '+', color = 'blue' ,label=r'finalterm grade')
plt.plot(grade3_x,grade3_y, '+',color='purple', label=r'total grade')
plt.xlabel('grade')
plt.grid()

plt.legend()
plt.show()

print("Midterm Rank : " + str(rank1)) 
print("Finalterm Rank : "+str(rank2)) 
print("total Rank : "+ str(rank3)) 

if rank3 < population*0.2:
    print("예상 학점은 A+ 입니다.")
elif rank3 < population*0.4:
    print("예상 학점은 A 입니다.")
elif rank3 < population*0.6:
    print("예상 학점은 B+ 입니다.")
elif rank3 < population*0.8:
    print ("에상 학점은 B 입니다.")