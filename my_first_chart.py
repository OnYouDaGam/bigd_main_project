import matplotlib.pyplot as plt


plt.rcParams["font.family"] = "Malgun Gothic"
nums = [73.6, 74.4, 72.6, 71.6, 72.1, 72.8, 74.3, 75.4, 74.4, 75.0, 74.3, 74.9, 74.8, 78 ]
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(nums)
for i, p in enumerate(nums):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points", 
                xytext=(0, 8), ha="center")
ax.set_title("나의 몸무게 변화")
fig.savefig("my_first_chart.png")