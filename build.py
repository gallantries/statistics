import yaml

with open('kpis.yaml', 'r') as handle:
    kpis = yaml.safe_load(handle.read())

with open('template.html', 'r') as handle:
    tpl = handle.read()

for k in (1, 2, 3, 4):
    kpicount = kpis[f"KPI{k}"]['progress']
    kpipercent = kpis[f"KPI{k}"]['progress'] / kpis[f"KPI{k}"]['goal'] * 100
    success = kpipercent > 100
    print(k)

    tpl = tpl.replace(
        f'<!-- KPI{k}COUNT -->',
        f"{kpicount}"
    )
    tpl = tpl.replace(
        f'<!-- KPI{k}PERCENT -->',
        f"{kpipercent:0.0f}"
    )

    if success:
        tpl = tpl.replace(
            f'<!-- KPI{k}SUCCESS -->',
            f"success"
        )

for k in (6, 7, 8):
    kpicount = kpis[f"KPI{k}"]['progress']
    kpipercent = kpis[f"KPI{k}"]['progress'] / 9
    success = kpipercent > 1

    tpl = tpl.replace(
        f'<!-- KPI{k}COUNT -->',
        f"{kpicount:0.2f}"
    )
    tpl = tpl.replace(
        f'<!-- KPI{k}GOAL -->',
        f"{100 * kpipercent:0.0f}"
    )

    if success:
        tpl = tpl.replace(
            f'<!-- KPI{k}SUCCESS -->',
            f"success"
        )

with open('index.html', 'w') as handle:
    handle.write(tpl)
