import { useEffect, useRef } from 'react'
import * as echarts from 'echarts'

const DARK_DEFAULTS = {
  backgroundColor: 'transparent',
  textStyle: { color: '#94a3b8', fontFamily: 'Inter, system-ui, sans-serif' },
  grid: { left: 48, right: 20, top: 32, bottom: 32 },
}

export default function EChart({ option, height = 280, onClick }) {
  const ref = useRef(null)
  const chartRef = useRef(null)

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
    chartRef.current.setOption({ ...DARK_DEFAULTS, ...option }, true)
    if (onClick) {
      chartRef.current.off('click')
      chartRef.current.on('click', onClick)
    }
  }, [option, onClick])

  return <div ref={ref} style={{ height, width: '100%' }} />
}

export const axisStyle = {
  axisLine: { lineStyle: { color: '#232f45' } },
  splitLine: { lineStyle: { color: '#1a2333' } },
  axisLabel: { color: '#64748b' },
}

export const PALETTE = ['#4f8ef7', '#34d399', '#fbbf24', '#f87171', '#a78bfa', '#22d3ee', '#fb923c', '#e879f9']
