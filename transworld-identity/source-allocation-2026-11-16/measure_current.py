from pathlib import Path
import json,re,hashlib,sys
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[2]
D=Path(sys.argv[3]).resolve() if len(sys.argv)>3 else Path(__file__).resolve().parent
assert len(sys.argv)>2, 'Usage: python3 measure_current.py REPOSITORY PERSONA_DISTILLER_SCRIPTS [OUTPUT_DIR]'
sys.path.insert(0,str(Path(sys.argv[2]).resolve()));import token_count
han=lambda s:len(re.findall(r'[\u3400-\u9fff]',s))
rows=[]
for cid in ['c02-1','c02-2','c05','c07-1','c07-2']:
 p=next((R/'references/clusters').glob(cid+'-*.md'));text=p.read_text();lines=text.splitlines(keepends=True)
 start=next(i for i,l in enumerate(lines) if l.startswith('## '));stop=next(i for i,l in enumerate(lines[start:],start) if re.match(r'## (來源定位|出處標記|書籍出處)',l))
 prose=[];bysection=[];name=None;section=[]
 def flush():
  if name is not None:bysection.append({'heading':name,'body_han':han(''.join(section))})
 for l in lines[start:stop]:
  if re.match(r'^#{1,6}\s',l):
   if l.startswith('## '):flush();name=l.strip()[3:];section=[]
   continue
  if re.match(r'^>\s*(?:本節承接|\*\*承接說明)',l):continue
  cleaned=re.sub(r'〔[^〕]*(?:CA\d|CA-L|NI\d|N0[45]|EA26)[^〕]*〕','',l)
  cleaned=re.sub(r'\]\([^)]*\)',']',cleaned)
  prose.append(cleaned);section.append(cleaned)
 flush()
 h=han(''.join(prose));counts=token_count.count(str(p),1/.6,1.3)
 rows.append({'module':cid,'path':p.relative_to(R).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'body_han':h,'metadata_han':han(text)-h,'whole_file_han':han(text),'whole_file_characters':len(text),'whole_file_heuristic_tokens':counts['tokens_est'],'section_counts':bysection})
standing=[token_count.count(str(R/p),1/.6,1.3) for p in ['SKILL.md','references/frameworks.md','references/voice.md']]
allclusters=[token_count.count(str(p),1/.6,1.3) for p in (R/'references/clusters').glob('*.md')]
base=sum(x['tokens_est'] for x in standing);largest=sorted(allclusters,key=lambda x:x['tokens_est'],reverse=True)[:2]
a={'unit':'正文漢字（U+3400..U+9FFF）','method':'從首個##實質章節到來源定位/出處標記/書籍出處之前；排除Markdown標題與CA/NI內嵌來源括註，保留實質引文及局部條件/時點說明；純舊來源承接標籤計入開銷。全文其餘漢字記為metadata_han。','not_quality_score':True,'rows':rows,'runtime_load':{'counter':'persona-distiller/scripts/token_count.py defaults; heuristic not model BPE','standing':{Path(x['file']).name:x['tokens_est'] for x in standing},'standing_total':round(base,2),'largest_two_current_topic_files':{Path(x['file']).name:x['tokens_est'] for x in largest},'standing_plus_two_largest':round(base+sum(x['tokens_est'] for x in largest),2),'scope':'當前完整檔案成本，只是最大兩模組同載情境；實際提問可能需更多/更少模組，這不是宿主context上限。'}}
(D/'measurements.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{k:v for k,v in x.items() if k!='section_counts'} for x in rows],ensure_ascii=False,indent=2));print(json.dumps(a['runtime_load'],ensure_ascii=False))
