import { Card, Empty, Typography } from 'antd'

const { Title } = Typography

export function User() {
  return (
    <Card>
      <Title level={2}>User</Title>
      <Empty description="User module placeholder" />
    </Card>
  )
}
