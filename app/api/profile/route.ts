import { getChatGPTUser } from '../../chatgpt-auth';
import { getDb } from '../../../db';
import { profiles } from '../../../db/schema';
import { eq } from 'drizzle-orm';
import { z } from 'zod';
const schema=z.object({type:z.enum(['Academic','General Training']),target:z.number().min(5).max(9).multipleOf(.5),minutes:z.union([z.literal(15),z.literal(30),z.literal(60),z.literal(90),z.literal(120),z.literal(180)]),date:z.string().regex(/^(\d{4}-\d{2}-\d{2})?$/)});
export async function GET() {
 const u=await getChatGPTUser(); if(!u) return Response.json({error:'请先登录'},{status:401});
 const rows=await getDb().select().from(profiles).where(eq(profiles.userId,u.userId));
 return Response.json({profile:rows[0]?JSON.parse(rows[0].data):null,name:u.fullName||'同学'});
}
export async function PUT(req:Request) {
 const u=await getChatGPTUser(); if(!u) return Response.json({error:'请先登录'},{status:401});
 const parsed=schema.safeParse(await req.json().catch(()=>null));if(!parsed.success)return Response.json({error:'目标信息不正确'},{status:400});
 const data=JSON.stringify(parsed.data),updated=new Date().toISOString();
 await getDb().insert(profiles).values({userId:u.userId,data,updated}).onConflictDoUpdate({target:profiles.userId,set:{data,updated}});
 return Response.json({ok:true});
}
