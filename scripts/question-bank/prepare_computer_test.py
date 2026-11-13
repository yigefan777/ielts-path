"""Prepare the user-supplied C21 Academic Test 1 for the local computer-test preview."""
import json
import argparse
import re
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument('--pdf', type=Path, required=True)
parser.add_argument('--output', type=Path, default=ROOT / 'work/question-preview')
args = parser.parse_args()
OUT = args.output
OUT.mkdir(parents=True, exist_ok=True)
PDF = args.pdf
r = PdfReader(PDF)

def text(page):
    return r.pages[page-1].extract_text() or ''

def inline(title, instruction, html, ids):
    return dict(type='inline',title=title,instruction=instruction,html=html,ids=ids)

def choice(title,instruction,items,options=None):
    return dict(type='choice',title=title,instruction=instruction,items=[dict(id=n,text=t,options=o if options is None else options) for n,t,o in items])

def match(title,instruction,items,options):
    return dict(type='match',title=title,instruction=instruction,items=[dict(id=n,text=t) for n,t in items],options=options)

def multi(ids,title,question,options):
    return dict(type='multi',title=title,instruction='Choose TWO letters, A–E.',ids=ids,question=question,options=options)

L=[dict(name='Part 1',range=[1,10],audio='assets/part-1.mp3',groups=[
inline('Questions 1–6','Complete the table below. Write ONE WORD AND/OR A NUMBER for each answer.', '''<h3>Oyster Bay Sailing Club Courses</h3><div class="table-scroll"><table><thead><tr><th>Name of course</th><th>What you learn</th><th>Cost</th><th>Other information</th></tr></thead><tbody><tr><th>Taster day</th><td>introduction to sailing</td><td>£120 if booking one place</td><td>small groups (max {{1}} people)</td></tr><tr><th>Level 1</th><td>basic theory e.g. understanding the {{2}} and tides<br><br>basic sailing skills including {{3}} information</td><td>£200<br><br>{{4}} available for club members<br><br>all inclusive (plus a useful {{5}})</td><td>a {{6}} at the end of the course for all participants</td></tr></tbody></table></div>''',list(range(1,7))),
inline('Questions 7–10','Complete the notes below. Write ONE WORD ONLY for each answer.','''<h3>General information</h3><ul><li>Participants must be able to swim.</li><li>Bring suitable clothing, a {{7}} and toiletries (e.g. shampoo).</li><li>There is a {{8}} at the club.</li><li>Online training {{9}} are recommended.</li><li>{{10}} are available for course participants.</li></ul>''',list(range(7,11))) ]),
dict(name='Part 2',range=[11,20],audio='assets/part-2.mp3',groups=[
choice('Questions 11–16','Choose the correct letter, A, B or C.',[
(11,'What should trainees always expect to get when working on low budget short films?',['travel expenses','a minimum wage','meals']),
(12,'According to the speaker, on big budget films trainees may get experience of',['makeup for special effects.','working with different ethnicities.','creating a variety of hair styles.']),
(13,'The speaker says a problem for makeup artists is',['dealing with difficult directors.','being shouted at by their supervisor.','waiting around for hours doing nothing.']),
(14,'How did the speaker feel when she met famous actors for the first time?',['very shy','very proud','very disappointed']),
(15,'What advice does the speaker give about makeup kits?',['Always carry a basic kit with you.','Only buy the best products for a makeup kit.','Ask other makeup artists to check your kit.']),
(16,'What advice does the speaker give about creating a portfolio?',['Keep print and digital photos.','Only include a small selection of photos.','Get permission to use photos.'])]),
match('Questions 17–20','What ability is required for each of the following duties? Write the correct letter, A, B or C.',[(17,'Prepping an actor'),(18,'Continuity'),(19,'General'),(20,'Applying makeup')],['being well-organised','being flexible','working quickly'])]),
dict(name='Part 3',range=[21,30],audio='assets/part-3.mp3',groups=[
multi([21,22],'Questions 21 and 22','Which TWO features of the lecture on ocean biodiversity had the greatest impact on the students?',['the references to local problems','the broad focus of the examples','the practical suggestions for solutions','the type of issues discussed','the implications for government policy']),
multi([23,24],'Questions 23 and 24','Which TWO details about the research project particularly impressed the students?',["the team’s previous successes",'its wide geographical scale','the use of new technology','the extensive statistical evidence','the large range of specialists involved']),
match('Questions 25–30',"What is the students’ opinion of each of the following resources related to ocean biodiversity? Choose SIX answers from the box and write the correct letter, A–H.",[(25,'Article on invasive lionfish'),(26,'Documentary on microplastics'),(27,'Podcast on ocean pollution'),(28,'Book on coastal ecosystems'),(29,'Article on metal toxicity'),(30,'Podcast on floating marine cities')],['This is aimed at a very specialist audience.','This is now rather outdated.','This was an effective description of a new danger.','This suggests possible ways to improve the situation.','This does not give a balanced account.','This is too predictable to be useful.','This gives insufficient evidence for its claims.','This gives a clear explanation of the problems.'])]),
dict(name='Part 4',range=[31,40],audio='assets/part-4.mp3',groups=[inline('Questions 31–40','Complete the notes below. Write ONE WORD ONLY for each answer.','''<h3>Sources of rubber</h3><h4>Three resources which are essential for industrial civilisation</h4><ul><li>{{31}}</li><li>fossil fuels</li><li>rubber</li></ul><h4>Natural rubber</h4><p>This mainly comes from the Para rubber tree, now cultivated in South-East Asia.</p><p>The supply is limited because</p><ul><li>the growth of the tree is {{32}}</li><li>production cannot easily be adjusted because of increasing or decreasing {{33}}</li><li>the tree only grows near the {{34}}</li><li>extracting the latex (rubber) is labour-intensive</li><li>it is very difficult to {{35}} rubber after production.</li></ul><p>New threats include</p><ul><li>lack of genetic diversity, leading to danger of disease caused by a {{36}}</li><li>a shift to the cultivation of palm oil</li><li>extreme {{37}} events.</li></ul><h4>Synthetic rubber</h4><ul><li>may be used for engine parts and cooking utensils</li><li>is less {{38}} than natural rubber</li><li>is unsuitable for many purposes e.g. the tyres of aircraft.</li></ul><h4>An alternative source of natural rubber</h4><ul><li>A wild flower (a type of dandelion) has rubber in its {{39}}.</li><li>It can be grown in many locations and does not require good {{40}}.</li></ul>''',list(range(31,41)))])]

R=[dict(name='Passage 1',title='The Davies Sisters',range=[1,13],groups=[
inline('Questions 1–7','Complete the notes below. Choose ONE WORD ONLY from the passage for each answer.','''<h3>Gwendoline and Margaret Davies</h3><h4>Family and early life</h4><ul><li>their grandfather’s wealth came from {{1}} and transportation businesses</li><li>their upbringing gave them a sense of social responsibility</li><li>their {{2}} was designed to give them an interest in activities such as collecting art</li><li>their governess took them on trips to art galleries</li><li>they took lengthy {{3}} about the things they saw in art galleries</li></ul><h4>The sisters as art collectors</h4><ul><li>their {{4}} showed they liked Old Master paintings, but they were expensive to buy</li><li>their early purchases were safe, popular paintings</li><li>the first Impressionist paintings they bought showed places in {{5}}</li></ul><h4>Impact of First World War</h4><ul><li>they helped bring artists from Belgium to Wales</li><li>they worked in a {{6}} for soldiers in France</li></ul><h4>Opinions about the sisters as art collectors</h4><ul><li>were not considered typical collectors – they lived in isolation in the countryside and did not have any {{7}} who were artists</li></ul>''',list(range(1,8))),
choice('Questions 8–13','Do the following statements agree with the information given in Reading Passage 1? TRUE = agrees; FALSE = contradicts; NOT GIVEN = no information.',[(8,"The Davies sisters’ childhood influenced the way they decided to use their wealth.",None),(9,"The Jean-Baptiste-Camille Corot paintings in the Davies sisters’ collection were purchased from a gallery in France.",None),(10,"Hugh Blaker opposed the Davies sisters’ decision to buy art by French Impressionists.",None),(11,'The exhibition of Cezanne paintings at the Bath gallery was very popular with the public.',None),(12,'The impact of the First World War encouraged Gwendoline to reconsider her interest in collecting art.',None),(13,'The Davies sisters bought French Impressionist art during a period when very few people were doing so.',None)],['TRUE','FALSE','NOT GIVEN'])]),
dict(name='Passage 2',title='Why we need silence',range=[14,26],groups=[
match('Questions 14–17','Reading Passage 2 has seven sections, A–G. Which section contains the following information?',[(14,'examples of strategies to decrease the noise that the public are exposed to'),(15,'data indicating the extent of the problem of excessive noise'),(16,'a description of physiological changes in our bodies when we hear sudden noises'),(17,'evidence that a relatively quiet environment can be more beneficial than a totally silent one')],list('ABCDEFG')),
inline('Questions 18–21','Complete the summary below. Choose ONE WORD ONLY from the passage for each answer.','''<h3>Flotation Tanks</h3><p>According to Justin Feinstein, flotation tanks allow people to concentrate on their own {{18}}, which helps them relax and enables them to meditate.</p><p>Feinstein and his colleagues conducted an experiment in which 50 people, who were all suffering from stress and related issues, were given a {{19}} to complete before and after using a flotation tank. Participants reported a reduction in their symptoms after an hour in the tank, together with signs of relaxation and improved general {{20}}.</p><p>In another experiment, the researchers had 48 people spend periods of 90 minutes either lying back in a chair or floating in a tank. Brain scans then revealed that those people who had been in a tank had decreased activity in parts of the brain associated with {{21}}.</p>''',list(range(18,22))),
match('Questions 22–26','Match each statement with the correct person, A, B, C or D. You may use any letter more than once.',[(22,'It is unpleasant and upsetting for people to be placed in a silent environment against their will.'),(23,'The trend towards creating quieter urban locations is likely to increase in the coming years.'),(24,'When our body’s senses are completely deprived of input, our minds compensate for this by creating the illusion of images and sounds.'),(25,'Even a short amount of silent time can have a positive impact.'),(26,'External and internal quietness makes us more conscious of events occurring in our surroundings and helps us react appropriately to these events.')],['Nick Antonio','Justin Feinstein','Tai Dotan Ben-Soussan','Eric Pfeifer'])]),
dict(name='Passage 3',title='Book review: The World of Sugar by Ulbe Bosma',range=[27,40],groups=[
choice('Questions 27–30','Choose the correct letter, A, B, C or D.',[(27,'What does the reviewer suggest about the cultivation and trading of sugar in the first paragraph?',['Sugar has played a major role in international relations.','Beet sugar has been made more internationally competitive.','Cane sugar is thought to be of superior quality to beet sugar.','New locations for cultivating sugar have increased production.']),(28,'In the second paragraph, when discussing the sugar market in Britain, the reviewer stresses',['how the sources used changed over time.','how developments in agriculture affected trade.','the increased demand for sugar over the years.','the growing support for ethical methods of cultivation.']),(29,'What is the reviewer doing in the third paragraph?',['describing an efficient approach to sugar cultivation','explaining why the use of sugar plantations declined','addressing a misconception about the growing of sugar cane','evaluating different approaches to the cultivation of sugar cane']),(30,'In the final paragraph, what does the reviewer suggest is the overall message of Bosma’s book?',['Sugar is a harmful and unnecessary product.','Economic pressure is needed to control sugar production.','Conditions for workers in sugar production should be improved.','Intensive marketing of sugar has had disastrous consequences.'])]),
inline('Questions 31–36','Complete the summary using the list of words, A–I, below. Choose a letter for each gap.','''<h3>Sugar cultivation and production</h3><div class="option-bank"><span>A national governments</span><span>B agricultural developments</span><span>C less wealthy nations</span><span>D untrained workers</span><span>E small-scale cultivation</span><span>F outdated methods</span><span>G financial controls</span><span>H migrant workers</span><span>I powerful individuals and businesses</span></div><p>The book <em>The World of Sugar</em> points out the similarities in the way that sugar was cultivated around the world. In the big industries in both Germany and the US, sugar farming depended on {{31}}. However, in other parts of the world such as South Asia and Latin America, {{32}} continued.</p><p>Sugar production has also involved {{33}} who were eager to protect their markets. In countries such as Cuba the sugar industry therefore had a major influence on {{34}}.</p><p>To support the interests of sugar producers, {{35}} were established. As a result of this, {{36}} were penalised.</p>''',list(range(31,37))),
choice('Questions 37–40','Do the following statements agree with the views of the writer in Reading Passage 3? YES = agrees; NO = contradicts; NOT GIVEN = impossible to say.',[(37,'Sugar has now become available in large quantities due to a range of agricultural developments.',None),(38,'Advertisers initially marketed sugar as a luxury product.',None),(39,'The invention of high-fructose corn syrup was a positive development.',None),(40,'High-fructose corn syrup is an ingredient in many processed foods.',None)],['YES','NO','NOT GIVEN'])])]

# Preserve reading paragraphs; remove running headers/page numbers and fix obvious extraction artefacts.
def passage(pages, start):
    lines=[]
    for p in pages:
        for line in text(p).splitlines():
            line=line.strip()
            if not line or line in ['Reading','Test 1'] or re.fullmatch(r'\d+',line):continue
            lines.append(line)
    whole='\n'.join(lines)
    whole=whole[whole.index(start):]
    corrections={'lmow':'know','contemporaiy':'contemporary','well-lmown':'well-known','Provenc;al':'Provençal','Franc;ois':'François','I-hour':'1-hour','sugar­\ngrowing':'sugar-growing'}
    for a,b in corrections.items():whole=whole.replace(a,b)
    return whole
R[0]['passage']=passage([17,18],'The Davies Sisters')
# Correct a duplicated footer artefact after the Impressionist footnote.
R[0]['passage']=R[0]['passage'].split('*** Impressionist:')[0]+'*** Impressionist: an artist with a style of painting that developed in France in the late 1800s.'
R[0]['passage']=R[0]['passage'].replace('·while', 'While').replace('Jean- Baptiste-Camille', 'Jean-Baptiste-Camille')
footnotes=['• philanthropic: seeking to promote the welfare of others, often by charitable funding', '•• Old Master: a highly respected artist of great skill who worked in Europe before about 1800']
for note in footnotes:
    R[0]['passage']=R[0]['passage'].replace(note+'\n','')
R[0]['passage']+='\n'+'\n'.join(footnotes)
R[1]['passage']=passage([21,22],'Why we need silence')
R[2]['passage']=passage([26,27],'Book review:').replace('UlbeBosma','Ulbe Bosma')
W=[dict(name='Task 1',prompt='The graph below gives information about the number of jobs in four sectors of the economy in the US between 1960 and 2020.',instruction='Summarise the information by selecting and reporting the main features, and make comparisons where relevant.',minimum=150,chart='assets/writing-chart.jpg'),dict(name='Task 2',prompt='The best way to provide enough homes in large cities is to build tall apartment blocks.',instruction='To what extent do you agree or disagree with this statement? Give reasons for your answer and include any relevant examples from your own knowledge or experience.',minimum=250)]
S=[dict(name='Part 1',topic='Hairstyles',prompts=['Where do you go to get a haircut?','Have you changed your hairstyle recently?','Would you ever change the colour of your hair?','Do you enjoy going to the hairdresser/barber?']),dict(name='Part 2',topic='Describe a time when you used information for tourists, for example from a guidebook or online.',prompts=['where you got this information','what place this information was about','what information you got','and explain whether this information was very helpful for you.']),dict(name='Part 3',topic='Different types of holidays / Tourist attractions',prompts=['What are the most popular kinds of holidays for people from your country to go on?','Do you think most people prefer to have a holiday abroad rather than in their own country?','Why do some people want to do absolutely nothing when they go away on holiday?','What are the kinds of tourist attraction that visitors to your country like to see?','Do you think tourist attractions such as museums should be free for local people to visit?','What can make a tourist attraction disappointing for visitors?'])]
from PIL import Image
chart=Image.open(OUT/'assets/page-030.jpg')
chart.crop((185,760,985,1235)).save(OUT/'assets/writing-chart.jpg',quality=90)
keys=json.loads((Path(__file__).with_name('answer-keys.json')).read_text())
data=dict(id='cambridge-21-academic-test-1',listening=L,reading=R,writing=W,speaking=S,keys=keys,source='User supplied PDF; physical pages 11–32 and 118–119. Local preview only.')
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'computer-test.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
for skill in [L,R]:
    ids=[]
    for section in skill:
        for group in section['groups']:
            ids += group['ids'] if 'ids' in group else [i['id'] for i in group['items']]
    assert sorted(ids)==list(range(1,41)) and len(ids)==40
print('Prepared 80 structured questions, 3 reading passages, 2 writing tasks and 3 speaking parts.')
