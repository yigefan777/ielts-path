'use client';
import {ThemeProvider,useTheme} from 'next-themes';
import {Sun,Moon} from 'lucide-react';
import {useEffect,useState} from 'react';
export function AppearanceProvider({children}:{children:React.ReactNode}){return <ThemeProvider attribute="data-theme" defaultTheme="light" enableSystem={false} disableTransitionOnChange>{children}</ThemeProvider>}
export function ThemeChoice(){const {theme,setTheme}=useTheme();const [ready,setReady]=useState(false);useEffect(()=>setReady(true),[]);return <div className="theme-choice" role="group" aria-label="界面模式"><button aria-pressed={ready&&theme==='light'} onClick={()=>setTheme('light')} title="白色浅色模式"><Sun size={14}/><span>浅色</span></button><button aria-pressed={ready&&theme==='dark'} onClick={()=>setTheme('dark')} title="深灰色深色模式"><Moon size={14}/><span>深色</span></button></div>}
