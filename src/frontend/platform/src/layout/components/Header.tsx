import { Typography } from 'antd'

const { Title } = Typography

export function Header() {
  return (
    <header className="border-b border-slate-200 bg-white px-6 py-4">
      <Title className="!mb-0" level={4}>
        Frontend Framework
      </Title>
    </header>
  )
}
