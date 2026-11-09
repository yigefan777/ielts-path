export const vocabulary = [
 {id:'sustainable',word:'sustainable',part:'adj.',meaning:'可持续的',topic:'环境',example:'Cities need sustainable transport systems that reduce pollution.',translation:'城市需要能够减少污染的可持续交通系统。'},
 {id:'emission',word:'emission',part:'n.',meaning:'排放；排放物',topic:'环境',example:'Better public transport can help reduce carbon emissions.',translation:'更好的公共交通有助于减少碳排放。'},
 {id:'biodiversity',word:'biodiversity',part:'n.',meaning:'生物多样性',topic:'环境',example:'Protecting forests is essential for maintaining biodiversity.',translation:'保护森林对维持生物多样性至关重要。'},
 {id:'accessible',word:'accessible',part:'adj.',meaning:'可进入的；可获得的',topic:'城市',example:'Public services should be accessible to everyone.',translation:'公共服务应当人人都能获得。'},
 {id:'congestion',word:'congestion',part:'n.',meaning:'拥堵',topic:'城市',example:'Cycling lanes may ease traffic congestion during rush hour.',translation:'自行车道可能缓解高峰时段的交通拥堵。'},
 {id:'infrastructure',word:'infrastructure',part:'n.',meaning:'基础设施',topic:'城市',example:'Investment in infrastructure can improve the quality of urban life.',translation:'基础设施投资可以改善城市生活质量。'},
 {id:'curriculum',word:'curriculum',part:'n.',meaning:'课程体系',topic:'教育',example:'The school has introduced practical skills into its curriculum.',translation:'这所学校在课程体系中加入了实用技能。'},
 {id:'acquire',word:'acquire',part:'v.',meaning:'获得；习得',topic:'教育',example:'Students acquire new vocabulary through regular reading.',translation:'学生通过经常阅读习得新词汇。'},
 {id:'critical',word:'critical',part:'adj.',meaning:'批判性的；至关重要的',topic:'教育',example:'Critical thinking helps students evaluate different arguments.',translation:'批判性思维帮助学生评估不同的论点。'},
 {id:'innovation',word:'innovation',part:'n.',meaning:'创新',topic:'科技',example:'Technological innovation has changed how people communicate.',translation:'技术创新改变了人们沟通的方式。'},
 {id:'privacy',word:'privacy',part:'n.',meaning:'隐私',topic:'科技',example:'Online platforms should take steps to protect user privacy.',translation:'网络平台应采取措施保护用户隐私。'},
 {id:'reliable',word:'reliable',part:'adj.',meaning:'可靠的',topic:'科技',example:'Researchers need reliable evidence to support their conclusions.',translation:'研究人员需要可靠的证据来支持结论。'}
];
export type WordStatus='review'|'mastered';
export type WordProgress={wordId:string;status:WordStatus};
