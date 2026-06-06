import { Card, Empty, Typography } from 'antd'

const { Title } = Typography

export function Dashboard() {
  return (
    <Card>
      <Title level={2}>Dashboard</Title>
      <Empty description="Dashboard placeholder" />
    </Card>
  )
}
