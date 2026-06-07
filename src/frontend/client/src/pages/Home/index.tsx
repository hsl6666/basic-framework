import { useEffect, useRef } from 'react'
import { Button, Card, Space, Statistic, Tag, Typography } from 'antd'
import * as echarts from 'echarts'
import { useAppStore } from '@/store'

const { Paragraph, Title } = Typography

const chartOptions: echarts.EChartsOption = {
  tooltip: {},
  grid: {
    top: 24,
    right: 16,
    bottom: 32,
    left: 36,
  },
  xAxis: {
    type: 'category',
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
  },
  yAxis: {
    type: 'value',
  },
  series: [
    {
      name: 'Projects',
      type: 'bar',
      data: [12, 20, 15, 28, 22],
      itemStyle: {
        color: '#2563eb',
      },
    },
  ],
}

export function Home() {
  const chartRef = useRef<HTMLDivElement>(null)
  const { status, toggle } = useAppStore()
  const isRunning = status === 'running'

  useEffect(() => {
    if (!chartRef.current) return undefined

    const chart = echarts.init(chartRef.current)
    chart.setOption(chartOptions)

    const handleResize = () => chart.resize()
    window.addEventListener('resize', handleResize)

    return () => {
      window.removeEventListener('resize', handleResize)
      chart.dispose()
    }
  }, [])

  return (
    <div className="mx-auto flex w-full max-w-5xl flex-col gap-6">
      <Card>
        <Space orientation="vertical" size={12}>
          <Tag color="blue">Project Framework</Tag>
          <Title className="!mb-0" level={1}>
            Frontend scaffold
          </Title>
          <Paragraph className="!mb-0 max-w-2xl text-slate-600">
            Minimal demos for route layout, Ant Design, ECharts, Zustand, and
            Tailwind are kept here. Other directories are initialized with
            placeholders for future business code.
          </Paragraph>
        </Space>
      </Card>

      <section className="grid gap-6 md:grid-cols-[1fr_320px]">
        <Card title="ECharts demo">
          <div ref={chartRef} className="h-72 w-full" />
        </Card>

        <Card title="Zustand demo">
          <Space orientation="vertical" size={16}>
            <Statistic title="Current status" value={status} />
            <Button type="primary" onClick={toggle}>
              {isRunning ? 'Stop' : 'Start'}
            </Button>
          </Space>
        </Card>
      </section>

      <Card title="Ant Design demo">
        <Space wrap>
          <Button type="primary">Primary</Button>
          <Button>Default</Button>
          <Button danger>Danger</Button>
          <Tag color="success">Configured</Tag>
          <Tag color="processing">React 19</Tag>
        </Space>
      </Card>
    </div>
  )
}
