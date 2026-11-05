import type { Metadata } from 'next';
import './globals.css';
export const metadata:Metadata={title:'IELTS Path · 每一步，更接近目标',description:'面向雅思考生的学习工作台。目标规划、四科训练、错题复习与云端学习进度。'};
export default function Layout({children}:{children:React.ReactNode}){return <html lang="zh-CN"><body>{children}</body></html>}
