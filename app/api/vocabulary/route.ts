import {getChatGPTUser} from '../../chatgpt-auth';
import {getDb} from '../../../db';
import {vocabularyProgress} from '../../../db/schema';
import {vocabulary} from '../../vocabulary';
import {eq} from 'drizzle-orm';
import {z} from 'zod';
const schema=z.object({wordId:z.string().refine(id=>vocabulary.some(w=>w.id===id)),status:z.enum(['review','mastered'])});
export async function GET(){
 const user=await getChatGPTUser();if(!user)return Response.json({error:'请先登录'},{status:401});
 const rows=await getDb().select({wordId:vocabularyProgress.wordId,status:vocabularyProgress.status}).from(vocabularyProgress).where(eq(vocabularyProgress.userId,user.userId));
 return Response.json({progress:rows});
}
export async function PUT(req:Request){
 const user=await getChatGPTUser();if(!user)return Response.json({error:'请先登录'},{status:401});
 const parsed=schema.safeParse(await req.json().catch(()=>null));if(!parsed.success)return Response.json({error:'单词记录不正确'},{status:400});
 const {wordId,status}=parsed.data,updated=new Date().toISOString(),id=user.userId+':'+wordId;
 await getDb().insert(vocabularyProgress).values({id,userId:user.userId,wordId,status,updated}).onConflictDoUpdate({target:vocabularyProgress.id,set:{status,updated}});
 return Response.json({ok:true});
}
