import glob
import yaml

with open('kpis.yaml', 'r') as handle:
    kpis = yaml.safe_load(handle.read())

kpi2 = 0 # events
kpi3 = 0 # early
kpi4 = 0 # late
# kpi5 = 0 # external
kpi6 = {1:0, 2:0, 3:0, 4:0, 5:0} # quality
kpi7 = {1:0, 2:0, 3:0, 4:0, 5:0} # satisfaction
kpi8 = {'Yes':0, 'Maybe':0, 'No': 0} # recommendation

for event in glob.glob("events/*"):
    kpi2 += 1
    with open(event, 'r') as handle:
        data = yaml.safe_load(handle.read())
        print(event)

        if 'demographics' in data:
            if 'early' in data['demographics']['stage']:
                kpi3 += data['demographics']['stage']['early']
            else:
                kpi3 += data['demographics']['stage']['bsc'] + data['demographics']['stage']['msc'] + data['demographics']['stage']['phd']

            if 'late' in data['demographics']['stage']:
                kpi4 += data['demographics']['stage']['late']
            else:
                kpi4 += data['demographics']['stage']['faculty'] + data['demographics']['stage']['post-doc'] + data['demographics']['stage']['researcher']

        if 'results' in data:
            for k, v in data['results']['quality'].items():
                kpi6[k] += data['results']['quality'][k]
            for k, v in data['results']['satisfaction'].items():
                kpi7[k] += data['results']['satisfaction'][k]
            for k, v in data['results']['recommendation'].items():
                kpi8[k] += data['results']['recommendation'][k]

kpis['KPI2']['progress'] = kpi2
kpis['KPI3']['progress'] = kpi3
kpis['KPI4']['progress'] = kpi4

kpis['KPI6']['progress'] = 2 * sum([k * v for k, v in kpi6.items()]) / sum(kpi6.values())
kpis['KPI7']['progress'] = 2 * sum([k * v for k, v in kpi7.items()]) / sum(kpi7.values())
ynm = {'Yes': 5, 'Maybe': 3, 'No': 1}
kpis['KPI8']['progress'] = 2 * sum([ynm[k] * v for k, v in kpi8.items()]) / sum(kpi8.values())

# kpis['KPI2']['progress'] = kpi2

with open('kpis.yaml', 'w') as handle:
    yaml.dump(kpis, handle)
