import { Card, Empty, Typography } from 'antd'

const { Title } = Typography

export function Login() {
  return (
    <Card className="w-full max-w-md">
      <Title className="text-center" level={3}>
        Login
      </Title>
      <Empty description="Login placeholder" />
    </Card>
  )
}
