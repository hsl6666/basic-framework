import { Table as AntTable, type TableProps } from 'antd'

export function Table<T extends object>(props: TableProps<T>) {
  return <AntTable<T> {...props} />
}
