import random
import time
import csv

from src.linear_search import linear_search
from src.bidirectional_search import bidirectional_search
from src.tem_search import tem_search

sizes=[100,1000,10000,100000]

with open("results/benchmark_results.csv","w",newline="") as file:

    writer=csv.writer(file)

    writer.writerow([
        "Size",
        "Algorithm",
        "Found",
        "Comparisons",
        "Time(ms)"
    ])

    for n in sizes:

        arr=list(range(n))

        target=random.choice(arr)

        algorithms=[
            ("Linear",linear_search),
            ("Bidirectional",bidirectional_search),
            ("TEM",tem_search)
        ]

        for name,algo in algorithms:

            start=time.perf_counter()

            found,comparisons=algo(arr,target)

            end=time.perf_counter()

            elapsed=(end-start)*1000

            writer.writerow([
                n,
                name,
                found,
                comparisons,
                round(elapsed,6)
            ])

            print(
                n,
                name,
                comparisons,
                round(elapsed,6)
            )

print("Finished")