import type {Metadata} from 'next';
import {AppearanceProvider} from './appearance';
import './globals.css';
export const metadata:Metadata={title:'IELTS Path · 每一步，更接近目标',description:'雅思备考学习工作台：登录与注册、学习计划、单词库、题库、错题与复习。'};
export default function Layout({children}:{children:React.ReactNode}){return <html lang="zh-CN" suppressHydrationWarning><body><AppearanceProvider>{children}</AppearanceProvider></body></html>}
