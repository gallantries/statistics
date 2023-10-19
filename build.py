import yaml

with open('kpis.yaml', 'r') as handle:
    kpis = yaml.safe_load(handle.read())

with open('template.html', 'r') as handle:
    tpl = handle.read()

for k in (1, 2, 3, 4):
    kpicount = kpis[f"KPI{k}"]['progress']
    kpipercent = kpis[f"KPI{k}"]['progress'] / kpis[f"KPI{k}"]['goal'] * 100
    success = kpipercent >= 100
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
    success = kpipercent >= 0.99

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

# Open the events and pull their data?
rows = []
# <th>Title</th>
# <th>Dates</th>
# <th>Participants</th>
# <th>Gender</th>
# <th>Stage</th>
# <th>Quality</th>
# <th>Satisfaction</th>
# <th>Recommendation</th>
import glob
import yaml
for event in sorted(glob.glob("events/*")):
    with open(event, 'r') as handle:
        d = yaml.safe_load(handle)
        quality = "not reported"
        if 'results' in d and 'quality' in d['results']:
            quality = 0
            for k, v in d['results']['quality'].items():
                quality += v * k * 2
            quality_denom = sum(d.get('results', {}).get('quality', {}).values())
            if quality_denom:
                quality = round(quality / quality_denom, 1)

        satisfaction = "not reported"
        if 'results' in d and 'satisfaction' in d['results']:
            satisfaction = 0
            for k, v in d['results']['satisfaction'].items():
                satisfaction += v * k * 2
            satisfaction_denom = sum(d.get('results', {}).get('satisfaction', {}).values())
            if satisfaction_denom:
                satisfaction = round(satisfaction / satisfaction_denom, 1)

        recommendation = "not reported"
        if 'results' in d and 'recommendation' in d['results']:
            recommendation = 0
            for k, v in d['results']['recommendation'].items():
                recommendation += v if k == "Maybe" or k == "Yes" else 0
            recommendation_denom = sum(d.get('results', {}).get('recommendation', {}).values())
            if recommendation_denom:
                recommendation = round(recommendation * 100 / recommendation_denom, 2)

        q = [
            d['title'],
            f"{d['start']} - {d['end']}",
            sum(d['demographics']['gender'].values()),
            d.get('demographics', {}).get('gender', {}),
            d.get('demographics', {}).get('stage', {}),
            quality,
            satisfaction,
            recommendation,
        ]
        rows.append(
                "<tr>" + "".join([f"<td>{x}</td>" for x in q]) + "</tr>")
tpl = tpl.replace(
    f'<!-- EVENT_FEEDBACK -->',
    "\n".join(rows)
)

with open('index.html', 'w') as handle:
    handle.write(tpl)
