import { useEffect, useRef, useState } from 'react'
import * as echarts from 'echarts'

// Charts are canvas — they cannot inherit CSS, so they read the theme's
// semantic variables directly and re-read them when the theme changes.
// Without this a chart stays dark-styled on the light theme forever.
const readTheme = () => {
  const s = getComputedStyle(document.documentElement)
  const v = (name, fallback) => (s.getPropertyValue(name).trim() || fallback)
  return {
    text: v('--chart-text', '#94a3b8'),
    textStrong: v('--text-primary', '#f1f5f9'),
    axis: v('--chart-axis', '#232f45'),
    grid: v('--chart-grid', '#1a2333'),
    palette: [1, 2, 3, 4, 5, 6, 7, 8].map((n) => v(`--chart-${n}`, '#4f8ef7')),
  }
}

// Subscribes to the `data-theme` attribute the theme toggle stamps on <html>.
export function useChartTheme() {
  const [theme, setTheme] = useState(readTheme)
  useEffect(() => {
    const observer = new MutationObserver(() => setTheme(readTheme()))
    observer.observe(document.documentElement, {
      attributes: true, attributeFilter: ['data-theme'],
    })
    return () => observer.disconnect()
  }, [])
  return theme
}

// Force the current theme's colours onto one axis spec, keeping every other
// property the caller set (rotate, interval, formatter, fontSize...).
// Callers spread `axisStyle` when they build their option, which freezes
// whatever the theme was at that moment — so the colours are re-applied here,
// at draw time, where the current theme is known.
const themeAxis = (axis, theme) => {
  if (Array.isArray(axis)) return axis.map((a) => themeAxis(a, theme))
  if (!axis || typeof axis !== 'object') return axis
  return {
    ...axis,
    axisLine: {
      ...(axis.axisLine || {}),
      lineStyle: { ...(axis.axisLine?.lineStyle || {}), color: theme.axis },
    },
    splitLine: {
      ...(axis.splitLine || {}),
      lineStyle: { ...(axis.splitLine?.lineStyle || {}), color: theme.grid },
    },
    axisLabel: { ...(axis.axisLabel || {}), color: theme.text },
  }
}

export default function EChart({ option, height = 280, onClick }) {
  const ref = useRef(null)
  const chartRef = useRef(null)
  const theme = useChartTheme()

  useEffect(() => {
    const chart = echarts.init(ref.current, null, { renderer: 'canvas' })
    chartRef.current = chart
    const resize = () => chart.resize()
    window.addEventListener('resize', resize)
    return () => {
      window.removeEventListener('resize', resize)
      chart.dispose()
    }
  }, [])

  useEffect(() => {
    if (!chartRef.current) return
    const defaults = {
      backgroundColor: 'transparent',
      textStyle: { color: theme.text, fontFamily: 'Inter, system-ui, sans-serif' },
      grid: { left: 48, right: 20, top: 32, bottom: 32 },
      color: theme.palette,
    }
    const merged = { ...defaults, ...option }
    if (merged.xAxis) merged.xAxis = themeAxis(merged.xAxis, theme)
    if (merged.yAxis) merged.yAxis = themeAxis(merged.yAxis, theme)
    chartRef.current.setOption(merged, true)
    if (onClick) {
      chartRef.current.off('click')
      chartRef.current.on('click', onClick)
    }
  }, [option, onClick, theme])

  return <div ref={ref} style={{ height, width: '100%' }} />
}

// Structural axis defaults for callers building their own axes. The colours
// here are placeholders — EChart re-applies the live theme at draw time.
export const axisStyle = {
  axisLine: { lineStyle: {} },
  splitLine: { lineStyle: {} },
  axisLabel: {},
}

// Theme-aware series palette for callers that colour series explicitly.
export function useChartPalette() {
  return useChartTheme().palette
}

export const PALETTE = ['#4f8ef7', '#34d399', '#fbbf24', '#f87171', '#a78bfa', '#22d3ee', '#fb923c', '#e879f9']
