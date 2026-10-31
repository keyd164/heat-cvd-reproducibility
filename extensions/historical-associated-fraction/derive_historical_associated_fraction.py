"""Historical zero-ACH associated fractions from the GBD2023 annual-data release.

Usage: python derive_historical_associated_fraction.py --root EXTRACTED_PACKAGES
Uses the Python standard library; does not fit models or modify input files.
"""
import argparse,csv,gzip,math
from pathlib import Path
from collections import defaultdict

def read(path):
    with (gzip.open(path,'rt',encoding='utf-8-sig',newline='') if path.suffix=='.gz' else path.open(encoding='utf-8-sig',newline='')) as stream:
        return list(csv.DictReader(stream))

def derive(root):
    panel=read(root/'data/input/historical_panel.csv.gz')
    groups={int(float(r['fid'])):r['group'] for r in read(root/'data/input/country_SDI_groups.csv')}
    candidates=[root/'results/models/four_models.csv',root/'data/GBD2023_results/models__four_models.csv']
    model_path=next((p for p in candidates if p.exists()),None)
    if model_path is None:raise FileNotFoundError('GBD2023 four-model result table not found')
    model=next(r for r in read(model_path) if r['model']=='country_year_FE')
    beta,lower,upper=(float(model[k]) for k in ['beta','ci_low','ci_high'])
    assert math.isclose(beta,1.26618081258455,rel_tol=0,abs_tol=1e-12),'Use the GBD2023 outcome release'
    data=[];keys=set()
    for r in panel:
        if int(float(r['measure_id']))!=2 or not r['fid'] or r['fid'].lower()=='nan':continue
        fid=int(float(r['fid']));year=int(float(r['year']));region=r['GBDregion'].strip()
        if fid==95 and not region:region='Western Sub-Saharan Africa'
        ach,y=float(r['absolute_cumulative_heat']),float(r['val'])
        assert region and y>0 and math.isfinite(ach) and math.isfinite(y)
        assert (fid,year) not in keys
        keys.add((fid,year));data.append((fid,year,region,groups[fid],ach,y))
    ids={r[0] for r in data};assert len(data)==6293 and len(ids)==203
    counts=defaultdict(int)
    for r in data:counts[r[0]]+=1
    assert set(counts.values())=={31} and {r[1] for r in data}==set(range(1990,2021))
    regions=sorted({r[2] for r in data});assert len(regions)==21
    specs=[('Overall','Overall',data)]
    specs += [('SDI',g,[r for r in data if r[3]==g]) for g in ['Low','Middle','High']]
    specs += [('GBD region',g,[r for r in data if r[2]==g]) for g in regions]
    result=[]
    for scope,label,rows in specs:
        n=len(rows);ach=math.fsum(r[4] for r in rows)/n;y=math.fsum(r[5] for r in rows)/n
        lo,hi=sorted((100*lower*ach/y,100*upper*ach/y))
        minima={}
        for r in rows:minima[r[0]]=min(minima.get(r[0],math.inf),r[4])
        result.append(dict(scope=scope,label=label,n_countries=len(minima),n_country_years=n,mean_ACH=ach,observed_DALYs_rate=y,conditional_rate_difference=beta*ach,AF_percent=100*beta*ach/y,coefficient_only_ci_low=lo,coefficient_only_ci_high=hi,countries_zero_outside_range=sum(v>0 for v in minima.values())))
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,required=True,help='Directory containing the extracted GBD2023 code and data ZIPs')
    parser.add_argument('--out',type=Path,default=Path('Table_S17_historical_AF.csv'))
    args=parser.parse_args();rows=derive(args.root)
    with args.out.open('w',encoding='utf-8',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    print('Wrote 25 summaries. AF = 100 * beta * mean(ACH) / mean(observed DALYs rate).')
    print('Intervals are coefficient-only; the observed-rate denominator is fixed. AF is not a causal attributable fraction or a share of DALYs counts.')

