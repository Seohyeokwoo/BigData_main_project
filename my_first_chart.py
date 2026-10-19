import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"

income = [150000, 156000, 94000, 207000, 47950]

fig, ax = plt.subplots(figsize=(7, 4))

ax.plot(income)
for i, p in enumerate(income):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points",
        xytext=(0, 8), ha="center")

ax.set_title("매주 알바 수입")
fig.savefig("my_first_chart.png")