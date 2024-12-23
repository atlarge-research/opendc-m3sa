# analysis.py

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from migrator import MetaModel, SCALE_TO_MARCONI
from plotter import colorblind_friendly_colors

# Requirements (if needed):

# Gather metamodel data
all_metamodels = []
countries_metamodels = []
migration_metamodels = []

for file in os.listdir("./results/experiment3/metamodels/"):
    country_code = file[:2]
    if country_code == "EU":
        country_code = file[:6]

    # print(f"!!!!!!!!!!!!24\n\n\n\n")
    # # the content of this folder is
    # for file in os.listdir("./experiment3/metamodels/"):
    #     print(file)

    metamodel = MetaModel(
        country_code=country_code,
        co2_emissions=pd.read_parquet(f"./results/experiment3/metamodels/{file}")["carbon_emission"].values
    )
    if "." in country_code:
        country_code = country_code.replace(".", "")

    metamodel.total_emissions *= SCALE_TO_MARCONI
    all_metamodels.append((country_code, metamodel.total_emissions))

    if len(country_code) > 2:
        migration_metamodels.append((country_code, metamodel.total_emissions))
    else:
        countries_metamodels.append((country_code, metamodel.total_emissions))

# Average emissions across countries
average_emissions = sum([x[1] for x in countries_metamodels]) / len(countries_metamodels)
print("Average emissions among countries:", average_emissions)

# Print all countries and their total emissions
print("\nCountry \t Total kgCO2")
for country, total in all_metamodels:
    print(f"{country:<15}{total:>0.2f}")

# Violin plot
violin_data = pd.DataFrame({
    'Country': [x[0] for x in countries_metamodels],
    'Total CO2': [x[1] / 1e3 for x in countries_metamodels]
})

plt.figure(figsize=(10, 3))
sns.violinplot(
    data=violin_data,
    x='Total CO2',
    inner_kws=dict(box_width=20, whis_width=5, color='#C8642B'),
    color='#00649D',
    cut=0
)
plt.grid(False)
plt.xlabel('Total Emissions [tCO2]', fontsize=22)
plt.xlim(0, None)
plt.xticks(fontsize=32, ticks=[0, 4, 8, 12])
plt.tight_layout()
plt.savefig('./results/figure-exports/figure-14.pdf')
plt.close()

# 10 lowest CO2 emissions
all_metamodels.sort(key=lambda x: x[1])
lowest_10_models = all_metamodels[:10]
lowest_10_emissions = [x[1] for x in lowest_10_models]
lowest_10_countries = [x[0] for x in lowest_10_models]

plt.figure(figsize=(10, 5))
bars = plt.barh(
    lowest_10_countries,
    lowest_10_emissions,
    color=[
        'green' if emission in [x[1] for x in migration_metamodels]
        else colorblind_friendly_colors[i]
        for i, emission in enumerate(lowest_10_emissions)
    ]
)
plt.xlabel('Total Emissions [kgCO2]', fontsize=22)
plt.xlim(0, max(lowest_10_emissions) * 1.2)
plt.yticks(fontsize=22)
plt.xticks(fontsize=0)

for bar, emission in zip(bars, lowest_10_emissions):
    if emission in [x[1] for x in migration_metamodels]:
        bar.set_hatch('///')
    plt.text(
        bar.get_width(),
        bar.get_y() + bar.get_height() / 2,
        f'{emission:.2f}',
        va='center',
        ha='left',
        fontsize=22,
        color='black'
    )

plt.grid(False)
plt.tight_layout()
plt.savefig('./results/figure-exports/figure-15.pdf')
plt.close()

# All CO2 emissions (linear scale)
all_emissions = [x[1] for x in all_metamodels]
all_countries = [x[0] for x in all_metamodels]

plt.figure(figsize=(8, 20))
bars = plt.barh(
    all_countries,
    all_emissions,
    color=[
        'green' if emission in [x[1] for x in migration_metamodels]
        else colorblind_friendly_colors[i]
        for i, emission in enumerate(all_emissions)
    ]
)
plt.xticks(fontsize=22, ticks=[0, 5000, 10000, 15000])
plt.xlabel('Total Emissions [kgCO2]', fontsize=22)
plt.yticks(fontsize=22)
plt.xlim(0, max(all_emissions) * 1.3)

for bar, emission in zip(bars, all_emissions):
    if emission in [x[1] for x in migration_metamodels]:
        bar.set_hatch('///')
    plt.text(
        bar.get_width(),
        bar.get_y() + bar.get_height() / 2,
        f'{emission:.2f}',
        va='center',
        ha='left',
        fontsize=22,
        color='black'
    )

plt.grid(False)
plt.tight_layout()
plt.savefig('./results/figure-exports/figure-16.pdf')
plt.close()

# All CO2 emissions (log scale)
plt.figure(figsize=(8, 20))
bars = plt.barh(
    all_countries,
    all_emissions,
    color=[
        'green' if emission in [x[1] for x in migration_metamodels]
        else colorblind_friendly_colors[i]
        for i, emission in enumerate(all_emissions)
    ]
)
plt.xlabel('Total Emissions [kgCO2]', fontsize=22)
plt.yticks(fontsize=22)
plt.xscale('log')
plt.xlim(1, 200000)

for bar, emission in zip(bars, all_emissions):
    if emission in [x[1] for x in migration_metamodels]:
        bar.set_hatch('///')
    plt.text(
        bar.get_width(),
        bar.get_y() + bar.get_height() / 2,
        f'{emission:.2f}',
        va='center',
        ha='left',
        fontsize=22,
        color='black'
    )

plt.grid(False)
plt.tight_layout()
plt.savefig('./results/figure-exports/figure-17.pdf')
plt.close()
