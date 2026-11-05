import { getChatGPTUser } from '../../chatgpt-auth';
import { getDb } from '../../../db';
import { records } from '../../../db/schema';
import { eq } from 'drizzle-orm';
import { z } from 'zod';
const schema=z.object({id:z.string().min(1).max(160),skill:z.enum(['reading','listening','writing','speaking']),status:z.enum(['draft','review','mastered']),text:z.string().max(30000),answers:z.array(z.string().max(200)).max(20),checks:z.array(z.boolean()).max(8),score:z.number().min(0).max(5).nullable(),total:z.number().min(0).max(5).nullable()});
export async function GET() {
 const u=await getChatGPTUser(); if(!u) return Response.json({error:'请先登录'},{status:401});
 const rows=await getDb().select().from(records).where(eq(records.userId,u.userId));
 return Response.json({records:rows.map(r=>({...JSON.parse(r.data),id:r.id.slice(u.userId.length+1),updated:r.updated}))});
}
export async function PUT(req:Request) {
 const u=await getChatGPTUser(); if(!u) return Response.json({error:'请先登录'},{status:401});
 const parsed=schema.safeParse(await req.json().catch(()=>null));if(!parsed.success)return Response.json({error:'练习记录不正确'},{status:400});
 const r=parsed.data,id=u.userId+':'+r.id,data=JSON.stringify(r),updated=new Date().toISOString();
 await getDb().insert(records).values({id,userId:u.userId,data,updated}).onConflictDoUpdate({target:records.id,set:{data,updated}});
 return Response.json({ok:true,updated});
}
